# Review-driven system reruns

These commands regenerate reports through the full research system. They do not edit downloaded report/source files. The original preset topic remains the metadata topic; reviewer feedback is appended to the initial research prompt.

## Video attempt 3

Independent source checks of attempt 2 found that VideoGPT was cited to Video Diffusion Models, and DreamFoley to WorldSonus. The wrong named methods were absent from the reopened excerpts. Original artifacts are preserved under `video-attempt2/artifacts/`.

```powershell
.\.venv\Scripts\python.exe -u research.py "survey about video and multimodal generation" --review-feedback "Previous run cited Video Diffusion Models for a VideoGPT primary-paper claim and WorldSonus for a DreamFoley claim. Retrieve and retain the correct primary source for each named method, or omit that method. Do not reuse old citation numbers. Checker must inspect every named method in Background, all numbers, and these audio-video claims against actual finalized URLs. Avoid unsupported method names in synthesis and TL;DR."
```

## World model final rerun (attempt 4 completed)

Attempt 3 passed the sampled claim audit, but repeated method descriptions between themes and used surveys for foundational context. Rerun with the final runner and a more explicit foundational-source requirement. Its original artifacts and audit remain under `world-model-attempt3/`.

```powershell
.\.venv\Scripts\python.exe -u research.py "survey about world model" --review-feedback "The previous report repeated FLIP and AdaWorld descriptions across themes and used recent surveys for foundational context. Retrieve and cite at least one seminal primary world-model paper in Background. A verified starting URL is https://arxiv.org/abs/1803.10122; fetch its actual text through source tools, or retrieve another seminal primary paper. Give each theme a distinct analytical purpose; avoid duplicated method descriptions. Verify every named foundational method and quantitative result against its actual finalized citation URL."
```
