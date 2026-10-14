# Cardiff sampling and geometry audit

Independent, inference-only Porto pilot by Zhijing Wu, Sichuan University. Publication package for ZhijingWu/cardiff-sampling-geometry-audit. Public availability is verified separately after upload.

With 64 conditions and seeds 0/1/2, Stage 1 latents were fixed per seed while GPS sampling intervals 20 and 50 were compared. The median of 24 paired-batch speedups was **2.503015x**, conditional 95% bootstrap interval **[2.431523, 2.692350]x**. Median length and pooled p95 step-distance point estimates passed frozen ±10% margins. Turning-tail and individual-path sensitivity remain; road validity was not evaluated.

Read the two-page Technical Note PDF/source at the repository root, docs/LIMITATIONS.md and docs/REPRODUCIBILITY.md before interpreting the result. All eight frozen point-estimate criteria passed in the preserved pilot. This is neither a new sampling algorithm nor a full Cardiff benchmark reproduction.

## Safe summary replay

Requires Python 3.11+ standard library only. From this repository:

    python3 scripts/verify_package.py
    python3 scripts/replay_summaries.py

These commands verify curated files and replay timing arithmetic from retained summaries. They do not regenerate trajectories, re-evaluate raw coordinates, rerun bootstrap intervals or independently reproduce model execution.

Optional PDF build (TeX Live with pdfLaTeX/Latin Modern, geometry, microtype, booktabs and fancyhdr; no model environment required):

    bash scripts/build_note.sh

The result goes to _build/ and does not replace the curated PDF.

## Original Cardiff

Baoshen Guo, Zhiqing Hong, Junyi Li, Shenhao Wang and Jinhua Zhao.
*Leveraging the Spatial Hierarchy: Coarse-to-fine Trajectory Generation via Cascaded Hybrid Diffusion.*
https://arxiv.org/abs/2507.13366v1

Official code pinned to 1138b1ef0646c18e878608a848dafca018b8a888:
https://github.com/urban-mobility-generation/Cardiff/tree/1138b1ef0646c18e878608a848dafca018b8a888

The paper already studies sampling intervals; this pilot asks a narrower fixed-Stage-1 Porto question. Clean inference conditioning is intentional (paper §3.5.2). The original stochastic sampler was preserved.

## Scope and rights

Only applicant-authored analysis/note, aggregate numerical facts, a latency figure, frozen settings, safe scripts and notices are included. Third-party checkpoints, raw GPS, latents, attribute arrays, full datasets and internal logs are excluded. No model/data redistribution permission is implied by Cardiff's software MIT license. Original project code: MIT. Original authored prose/figures: CC BY 4.0. Third-party files retain their terms. See LICENSE, NOTICE and notices/THIRD_PARTY.md.

This study is independent and is not affiliated with or endorsed by the Cardiff authors.
