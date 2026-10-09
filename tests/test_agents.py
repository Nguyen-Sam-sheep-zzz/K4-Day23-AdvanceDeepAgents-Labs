"""Agent assembly checks; no network or model calls."""

import asyncio
import unittest
from unittest.mock import patch

from langchain.agents.middleware import (
    ModelCallLimitMiddleware,
    TodoListMiddleware,
    ToolCallLimitMiddleware,
)
from langchain.agents.middleware.types import ToolCallRequest
from langchain_core.messages import AIMessage, ToolMessage

import agents
from tools import SOURCE_TOOLS, web_fetch


def limits(middleware):
    model = [item for item in middleware if isinstance(item, ModelCallLimitMiddleware)]
    tool = [item for item in middleware if isinstance(item, ToolCallLimitMiddleware)]
    assert len(model) == len(tool) == 1
    return model[0], tool[0]


class AgentAssemblyTests(unittest.TestCase):
    def test_first_researcher_dispatch_requires_three_calls_in_one_model_batch(self):
        middleware_type = getattr(agents, "InitialResearchBatchMiddleware", None)
        self.assertIsNotNone(middleware_type)
        middleware = middleware_type()
        call = {"name": "task", "args": {"subagent_type": "researcher", "description": "Question A"}, "id": "research-1"}
        message = AIMessage(content="", tool_calls=[call])
        request = ToolCallRequest(tool_call=call, tool=None, state={"messages": [message]}, runtime=None)
        handled = []

        def handler(tool_request):
            handled.append(tool_request.tool_call["id"])
            return ToolMessage(content="ran", tool_call_id=tool_request.tool_call["id"])

        result = middleware.wrap_tool_call(request, handler)
        self.assertIsInstance(result, ToolMessage)
        self.assertEqual(result.tool_call_id, "research-1")
        self.assertEqual(result.status, "error")
        self.assertIn("three", str(result.content).lower())
        self.assertEqual(handled, [])

    def test_valid_batch_then_focused_followup_and_checker_run_unchanged(self):
        middleware_type = getattr(agents, "InitialResearchBatchMiddleware", None)
        self.assertIsNotNone(middleware_type)
        middleware = middleware_type()
        initial = [
            {"name": "task", "args": {"subagent_type": "researcher", "description": f"Question {n}"}, "id": f"research-{n}"}
            for n in range(1, 4)
        ]
        first = AIMessage(content="", tool_calls=initial)
        followup = {"name": "task", "args": {"subagent_type": "researcher", "description": "Fill gap"}, "id": "research-4"}
        checker = {"name": "task", "args": {"subagent_type": "citation-checker"}, "id": "check-1"}
        called = []

        def handler(request):
            called.append(request.tool_call["id"])
            return ToolMessage(content="ran", tool_call_id=request.tool_call["id"])

        for call, history in [
            (initial[0], [first]),
            (initial[1], [first]),
            (initial[2], [first]),
            (followup, [first, AIMessage(content="", tool_calls=[followup])]),
            (checker, [AIMessage(content="", tool_calls=[checker])]),
        ]:
            request = ToolCallRequest(tool_call=call, tool=None, state={"messages": history}, runtime=None)
            result = middleware.wrap_tool_call(request, handler)
            self.assertEqual(result.content, "ran")
        self.assertEqual(called, ["research-1", "research-2", "research-3", "research-4", "check-1"])

    def test_async_researcher_dispatch_has_same_batch_guard(self):
        middleware_type = getattr(agents, "InitialResearchBatchMiddleware", None)
        self.assertIsNotNone(middleware_type)
        call = {"name": "task", "args": {"subagent_type": "researcher"}, "id": "research-1"}
        request = ToolCallRequest(tool_call=call, tool=None,
                                  state={"messages": [AIMessage(content="", tool_calls=[call])]}, runtime=None)
        called = []

        async def handler(tool_request):
            called.append(tool_request.tool_call["id"])
            return ToolMessage(content="ran", tool_call_id=tool_request.tool_call["id"])

        result = asyncio.run(middleware_type().awrap_tool_call(request, handler))
        self.assertEqual(result.status, "error")
        self.assertEqual(called, [])

    def test_subagents_have_restricted_tools_and_independent_limits(self):
        first = agents.build_subagents()
        second = agents.build_subagents()
        self.assertEqual({spec["name"] for spec in first}, {"researcher", "citation-checker"})
        by_name = {spec["name"]: spec for spec in first}
        self.assertEqual(by_name["researcher"]["tools"], SOURCE_TOOLS)
        self.assertEqual(by_name["citation-checker"]["tools"], [web_fetch])
        for spec in first:
            self.assertTrue(spec["description"])
            self.assertTrue(spec["system_prompt"])
            model, tool = limits(spec["middleware"])
            self.assertEqual((model.run_limit, model.exit_behavior), (40, "end"))
            self.assertEqual(tool.run_limit, 60)
        self.assertIsNot(limits(first[0]["middleware"])[0], limits(first[1]["middleware"])[0])
        self.assertIsNot(limits(first[0]["middleware"])[0], limits(second[0]["middleware"])[0])

    def test_lead_passes_model_backend_subagents_and_own_limits(self):
        backend = object()
        model = object()
        sentinel = object()
        with patch.object(agents, "create_deep_agent", return_value=sentinel) as create:
            self.assertIs(agents.build_lead_agent(backend, model), sentinel)
        kwargs = create.call_args.kwargs
        self.assertIs(kwargs["backend"], backend)
        self.assertIs(kwargs["model"], model)
        self.assertEqual(kwargs["system_prompt"], agents.LEAD_PROMPT)
        self.assertEqual({spec["name"] for spec in kwargs["subagents"]}, {"researcher", "citation-checker"})
        self.assertEqual(sum(isinstance(item, TodoListMiddleware) for item in kwargs["middleware"]), 1)
        self.assertEqual(sum(isinstance(item, agents.InitialResearchBatchMiddleware) for item in kwargs["middleware"]), 1)
        lead_model, lead_tool = limits(kwargs["middleware"])
        self.assertEqual((lead_model.run_limit, lead_model.exit_behavior), (150, "end"))
        self.assertEqual(lead_tool.run_limit, 300)
        for spec in kwargs["subagents"]:
            sub_model, sub_tool = limits(spec["middleware"])
            self.assertIsNot(sub_model, lead_model)
            self.assertIsNot(sub_tool, lead_tool)

    def test_real_graph_compiles_with_pinned_dependencies(self):
        from deepagents.backends import StateBackend
        from langchain_openai import ChatOpenAI

        model = ChatOpenAI(model="compile-only", api_key="test", base_url="https://example.invalid")
        graph = agents.build_lead_agent(StateBackend(), model)
        self.assertTrue(hasattr(graph, "invoke"))
        self.assertIn("model", graph.nodes)


if __name__ == "__main__":
    unittest.main()
