# Ego4D Benchmark Visualization

This repository contains Python scripts to generate bar charts for Ego4D benchmark results comparing different language models.

## Files

- `grouped_metrics_chart.py` - Generates a chart comparing BLEU-1, ROUGE-L, and METEOR scores across 4 models
- `before_after_comparison_chart.py` - Generates a before/after finetuning comparison chart
- `ground_truth_captions_chart.py` - Generates a chart for ground truth captions benchmark results

## Models

The charts compare the following models:
- InternVL3-Uniform
- InternVL2.5
- Qwen-Omni
- LLaVA-Video-7B-Qwen2

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install matplotlib numpy
```

## Usage

Run any of the chart scripts:
```bash
python grouped_metrics_chart.py
python before_after_comparison_chart.py
python ground_truth_captions_chart.py
```

Each script will generate a matplotlib chart and display it, along with printing a summary of the data.

## Data Sources

- GPT Captions benchmark results
- Ground Truth Captions benchmark results
- Before/After finetuning comparison for InternVL3-Uniform 