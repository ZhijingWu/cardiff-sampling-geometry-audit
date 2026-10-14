# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Zhijing Wu
"""Replay published timing arithmetic; no inference or raw-trajectory analysis."""
from pathlib import Path
import csv,json,math,statistics
root=Path(__file__).resolve().parents[1]
summary=json.loads((root/'data/metrics_summary.json').read_text())
rows=list(csv.DictReader((root/'data/paired_batch_timings.csv').open()))
assert len(rows)==24
ratios=[float(r['interval20_seconds'])/float(r['interval50_seconds']) for r in rows]
speed=statistics.median(ratios)
assert math.isclose(speed,summary['median_paired_batch_speedup'],rel_tol=1e-12)
totals={str(i):sum(float(r[f'interval{i}_seconds']) for r in rows) for i in [20,50]}
for i in totals:
 assert math.isclose(totals[i],summary['intervals'][i]['gps_seconds_total'],rel_tol=1e-12)
 assert math.isclose(totals[i]/192,summary['intervals'][i]['seconds_per_trajectory'],rel_tol=1e-12)
assert len(summary['frozen_criteria'])==8 and all(summary['frozen_criteria'].values())
result={
 'scope':'summary arithmetic only; no model execution, bootstrap rerun or raw GPS access',
 'median_paired_batch_speedup':speed,'gps_wall_seconds':totals,
 'conditional_ci95_as_recorded':summary['timing_uncertainty']['ci95'],
 'all_eight_frozen_criteria_recorded_pass':True,
 'geometry_and_ci_status':'quoted from preserved analysis; not independently rederived from trajectories by this script'}
print(json.dumps(result,indent=2))
