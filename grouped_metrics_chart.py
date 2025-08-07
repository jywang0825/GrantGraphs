import matplotlib.pyplot as plt
import numpy as np

# Data from the table
models = ['InternVL3-Uniform', 'InternVL2.5', 
          'Qwen-Omni', 'LLaVA-Video-7B-Qwen2']

bleu1_scores = [26.23, 26.62, 26.12, 16.79]
bleu2_scores = [10.68, 12.71, 12.89, 8.29]
bleu3_scores = [5.07, 5.85, 6.12, 3.17]
bleu4_scores = [2.94, 3.22, 3.56, 1.34]
meteor_scores = [20.49, 20.45, 20.45, 27.67]
rouge1_scores = [29.51, 30.40, 30.40, 22.87]
rouge2_scores = [5.19, 7.56, 7.56, 5.64]
rouge_l_scores = [20.92, 22.94, 22.94, 15.43]

# Create a chart with metrics grouped together
fig, ax = plt.subplots(figsize=(16, 8))

# Create positions for the bars
# Group 1: All BLEU-1 scores (positions 0-3)
# Group 2: All ROUGE-L scores (positions 5-8) 
# Group 3: All METEOR scores (positions 10-13)
x_bleu1 = np.arange(0, 4)
x_rouge_l = np.arange(5, 9)
x_meteor = np.arange(10, 14)

# Create bars for each metric group
bars_bleu1 = ax.bar(x_bleu1, bleu1_scores, label='BLEU-1', color='#2E86AB', alpha=0.8, edgecolor='black', linewidth=0.5)
bars_rouge_l = ax.bar(x_rouge_l, rouge_l_scores, label='ROUGE-L', color='#A23B72', alpha=0.8, edgecolor='black', linewidth=0.5)
bars_meteor = ax.bar(x_meteor, meteor_scores, label='METEOR', color='#F18F01', alpha=0.8, edgecolor='black', linewidth=0.5)

# Customize the chart
ax.set_xlabel('Models', fontsize=12, fontweight='bold')
ax.set_ylabel('Scores', fontsize=12, fontweight='bold')
ax.set_title('Ego4D GPT Captions Benchmark', fontsize=16, fontweight='bold', pad=20)

# Set x-axis ticks and labels
all_x_positions = list(x_bleu1) + list(x_rouge_l) + list(x_meteor)
all_labels = models + models + models
ax.set_xticks(all_x_positions)
ax.set_xticklabels(all_labels, rotation=45, ha='right', fontsize=10)

ax.legend(fontsize=11, bbox_to_anchor=(1.05, 1), loc='upper left')
ax.grid(axis='y', alpha=0.3)

# Add value labels on bars
def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{height:.1f}', ha='center', va='bottom', fontsize=18, fontweight='bold')

add_value_labels(bars_bleu1)
add_value_labels(bars_rouge_l)
add_value_labels(bars_meteor)

# Adjust layout and display
plt.tight_layout()
plt.show()

print("Grouped metrics chart generated successfully!")
print("\nSummary of the data:")
print(f"{'Model':<30} {'BLEU-1':<8} {'BLEU-2':<8} {'BLEU-3':<8} {'BLEU-4':<8} {'METEOR':<8} {'ROUGE-1':<8} {'ROUGE-2':<8} {'ROUGE-L':<8}")
print("-" * 100)
for i, model in enumerate(models):
    print(f"{model:<30} {bleu1_scores[i]:<8.2f} {bleu2_scores[i]:<8.2f} {bleu3_scores[i]:<8.2f} {bleu4_scores[i]:<8.2f} {meteor_scores[i]:<8.2f} {rouge1_scores[i]:<8.2f} {rouge2_scores[i]:<8.2f} {rouge_l_scores[i]:<8.2f}") 