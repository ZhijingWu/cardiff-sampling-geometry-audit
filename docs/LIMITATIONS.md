# Limits of the pilot and this package

- Ordered first 64 valid attributes, three seeds, one hardware/software setting and 192 trajectories per arm. Attribute split/held-out provenance is unknown.
- The 2.503015x estimator is a median of paired-batch ratios, not a ratio of total times and not end-to-end acceleration.
- Timing intervals resample eight batch positions retaining all seeds; geometric intervals resample attribute IDs retaining all seeds. Both are conditional descriptive intervals, not population equivalence or broad seed-robustness tests.
- Passing frozen point-estimate margins does not establish geometric equivalence. Individual paths can differ; the turning-tail change was exploratory, without a frozen quality threshold.
- Effective eta=1. Restored states share Gaussian draws by draw index, not common diffusion timestep; initial schedule indices and coefficients differ. Noise assignment and schedule effects are not separated.
- Original clean inference conditioning is intentional. The auxiliary noise-time convention remains a clarification item, not a demonstrated defect. This was not a conditioning-noise ablation.
- No original road graph, segment-route decoding, checkpoint-matched held-out real control, map matching, physical time model, privacy evaluation or paper benchmark scores were tested.
- Region containment and coordinate geometry are not road-validity metrics. No physical realism, road-validity or privacy improvement is claimed.
- Original checkpoint loads and one exact same-environment repeatability control succeeded. This package's verification script does not repeat those model operations.
- Python/PyTorch differ from the author recipe. The pilot used an isolated project environment with a read-only shared runtime dependency; that environment and its original infrastructure assumptions are not shipped.
- Raw outputs and third-party assets are withheld pending permissions. The curated package supports summary replay, not independent rederivation of all geometric statistics or new inference.
- Road-alignment work is proposed only; compatible decoding/mapping/reference assets and rights still require author clarification.
