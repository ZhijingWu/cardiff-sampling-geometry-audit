# What can be reproduced from this package

## Summary and document replay

Python scripts in scripts/ use the standard library and have no networking, pickle loading or model execution. verify_package.py verifies the curated SHA-256 entries. replay_summaries.py checks the median of 24 batch ratios, total GPS times and time per trajectory against data/metrics_summary.json. It prints already-recorded uncertainty, explicitly without recomputing it. Configuration is in config/frozen_settings.json and the three pinned upstream parameter JSONs.

The note can be rebuilt with scripts/build_note.sh. The included aggregate figure is an unchanged original pilot export, not a road trace. Its provenance hash is recorded in docs/provenance.json. PDF bytes need not match after rebuilding because of TeX metadata/toolchain variation.

## Historical inference protocol (documented, not a runnable command here)

Original Porto diffusion checkpoints were inspected and loaded with weights_only=True and strict=True; their sizes/hashes and official relative paths are in docs/provenance.json. All 231 original hashed artifacts were verified preserved during preparation.

Use original revision and Porto parameters; first 64 valid attributes in row order; seeds 0,1,2; cache interval-20 Stage 1 latents shaped (64,32,128). Pair GPS intervals20/50 with the same latents/attributes; each output has shape (64,2,64). Use eight-row batches, alternate order, restore complete CPU/CUDA Torch, NumPy and Python RNG states per pair, then advance by interval20's post-call state. Preserve effective eta=1, auxiliary noise time200, cond_scale3.0 as passed by the original code, FP32/no autocast/disabled TF32. Use CUDA synchronization; exclude setup/writes/Stage1 from GPS timing. Preserve every output and perform a repeatability control.

The released code contains no visible classifier-free-guidance blend in this measured path despite the cond_scale name; the pilot preserved that behavior rather than reinterpreting the parameter. Clean inference conditioning is intentional. Do not remove unused/terminal noise draws, which would change RNG consumption.

New inference additionally requires separately obtained official checkpoints/attributes and a reviewed environment/configuration adapter. No portable one-command inference runner is claimed here. The private pilot runner's infrastructure-specific assumptions were intentionally not copied. No command here downloads or executes models.

Original run: RTX3090 24GB, Python3.11.2, Torch2.5.1+cu124/CUDA12.4, driver570.133.07; dependency versions differ from author recipe. That disclosure is not a claim of portability.

## Historical verification boundaries

Strict loading, smoke and repeatability are recorded execution evidence, not actions repeated by these scripts. Full raw-array metrics and bootstrap rederivation require withheld original arrays and the preserved analysis. The source manifest hash authenticates an inventory, not publicly available underlying files. No individual path figure or raw trajectory is redistributed.
