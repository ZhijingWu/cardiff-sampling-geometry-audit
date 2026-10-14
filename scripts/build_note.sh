#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Zhijing Wu
# Build an optional local PDF; the curated published PDF is not overwritten.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p _build
for pass in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error -output-directory=_build Zhijing_Wu_Cardiff_Technical_Note.tex
done
