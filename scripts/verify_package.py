# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Zhijing Wu
"""Verify the curated package's SHA-256 manifest, without network or model calls."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'package_sha256.json').read_text())
bad=[]
for rel,expected in manifest.items():
 candidate=root/rel
 p=candidate.resolve()
 if candidate.is_symlink() or not p.is_relative_to(root) or not p.is_file():
  bad.append(rel);continue
 if hashlib.sha256(p.read_bytes()).hexdigest()!=expected:bad.append(rel)
print(json.dumps({'files_checked':len(manifest),'all_match':not bad,'failures':bad},indent=2))
raise SystemExit(1 if bad else 0)
