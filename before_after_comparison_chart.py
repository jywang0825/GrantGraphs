import matplotlib.pyplot as plt
import numpy as np

# Data for InternVL3-Uniform before and after finetuning
# Before finetuning (from previous data)
bleu1_before = 15.88
meteor_before = 16.08
rouge_l_before = 14.15

# After finetuning (from new data)
bleu1_after = 20.92
meteor_after = 17.22
rouge_l_after = 21.63

# Create a chart with metrics grouped together
fig, ax = plt.subplots(figsize=(12, 8))

# Create positions for the bars - comparing before vs after finetuning
# Group 1: BLEU-1 comparison (positions 0-1)
# Group 2: ROUGE-L comparison (positions 3-4) 
# Group 3: METEOR comparison (positions 6-7)
x_bleu1 = np.arange(0, 2)
x_rouge_l = np.arange(3, 5)
x_meteor = np.arange(6, 8)

# Create bars for each metric group - before vs after
bars_bleu1_before = ax.bar(x_bleu1[0], bleu1_before, label='Before', color='#2E86AB', alpha=0.8, edgecolor='black', linewidth=0.5)
bars_bleu1_after = ax.bar(x_bleu1[1], bleu1_after, label='After', color='#DC143C', alpha=0.8, edgecolor='black', linewidth=0.5)

bars_rouge_l_before = ax.bar(x_rouge_l[0], rouge_l_before, color='#2E86AB', alpha=0.8, edgecolor='black', linewidth=0.5)
bars_rouge_l_after = ax.bar(x_rouge_l[1], rouge_l_after, color='#DC143C', alpha=0.8, edgecolor='black', linewidth=0.5)

bars_meteor_before = ax.bar(x_meteor[0], meteor_before, color='#2E86AB', alpha=0.8, edgecolor='black', linewidth=0.5)
bars_meteor_after = ax.bar(x_meteor[1], meteor_after, color='#DC143C', alpha=0.8, edgecolor='black', linewidth=0.5)

# Customize the chart
ax.set_xlabel('Metrics', fontsize=12, fontweight='bold')
ax.set_ylabel('Scores', fontsize=12, fontweight='bold')
ax.set_title('Ego4D Ground Truth Captions Finetuned Benchmark', fontsize=16, fontweight='bold', pad=20)

# Set x-axis ticks and labels
all_x_positions = list(x_bleu1) + list(x_rouge_l) + list(x_meteor)
all_labels = ['BLEU-1\nBefore', 'BLEU-1\nAfter', 'ROUGE-L\nBefore', 'ROUGE-L\nAfter', 'METEOR\nBefore', 'METEOR\nAfter']
ax.set_xticks(all_x_positions)
ax.set_xticklabels(all_labels, rotation=0, ha='center', fontsize=10)

ax.legend(fontsize=11, bbox_to_anchor=(1.05, 1), loc='upper left')
ax.grid(axis='y', alpha=0.3)

# Add value labels on bars
def add_value_labels(bar_container, value):
    height = value
    bar = bar_container[0]  # Get the first (and only) bar from the container
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
            f'{height:.1f}', ha='center', va='bottom', fontsize=18, fontweight='bold')

add_value_labels(bars_bleu1_before, bleu1_before)
add_value_labels(bars_bleu1_after, bleu1_after)
add_value_labels(bars_rouge_l_before, rouge_l_before)
add_value_labels(bars_rouge_l_after, rouge_l_after)
add_value_labels(bars_meteor_before, meteor_before)
add_value_labels(bars_meteor_after, meteor_after)

# Adjust layout and display
plt.tight_layout()
plt.show()

print("Before/After comparison chart generated successfully!")
print("\nSummary of the data:")
print(f"{'Model':<30} {'BLEU-1':<8} {'METEOR':<8} {'ROUGE-L':<8}")
print("-" * 60)
print(f"{'InternVL3-Uniform (Before)':<30} {bleu1_before:<8.2f} {meteor_before:<8.2f} {rouge_l_before:<8.2f}")
print(f"{'InternVL3-Finetuned-Uniform':<30} {bleu1_after:<8.2f} {meteor_after:<8.2f} {rouge_l_after:<8.2f}") 