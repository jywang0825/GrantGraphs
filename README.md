# Ego4D Benchmark Visualization

This repository contains Python scripts to generate bar charts for Ego4D benchmark results comparing different language models.

## Files

- `grouped_metrics_chart.py` - Generates a chart comparing BLEU-1, ROUGE-L, and METEOR scores across 4 models against GPT generated captions
- `before_after_comparison_chart.py` - Generates a before/after finetuning comparison chart
- `ground_truth_captions_chart.py` - Generates a chart for Ego4d ground truth captions benchmark results

## Models

The charts compare the following models:
- InternVL3-Uniform
- InternVL2.5
- Qwen-Omni
- LLaVA-Video-7B-Qwen2

