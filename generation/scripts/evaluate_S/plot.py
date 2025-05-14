import os
import re
import matplotlib.pyplot as plt
import numpy as np

# Define parameters
number_of_levels_list = [0, 1, 2, 3, 4, 5]  # 0-5
generation_steps_list = [1, 2, 3, 4, 5, 6]  # 1-6

# Create 2D array to store results
results = np.zeros((len(number_of_levels_list), len(generation_steps_list)))

# Read log files and extract acc values
log_dir = "logs/evaluate_S"
for i, level in enumerate(number_of_levels_list):
    for j, step in enumerate(generation_steps_list):
        filename = f"MAEGIN_MixSuper_Purpose_S{level}_on_G{step}.log"
        filepath = os.path.join(log_dir, filename)
        
        try:
            with open(filepath, 'r') as f:
                content = f.read()
                # Extract acc value using regex
                match = re.search(r'\[acc\]=(\d+\.\d+)', content)
                if match:
                    acc = float(match.group(1))
                    results[i][j] = acc
        except FileNotFoundError:
            print(f"Warning: File {filepath} not found")

# Create plot
plt.figure(figsize=(10, 8))
colors = plt.cm.Set2(np.linspace(0, 1, len(number_of_levels_list)))

for i, level in enumerate(number_of_levels_list):
    acc_values = results[i]
    plt.plot(generation_steps_list, acc_values, '-o', 
             label=f'Sampling Levels {level}', 
             color=colors[i])

plt.title('Accuracy for Different Sampling Levels and Max Generation Steps')
plt.xlabel('Max Generation Steps')
plt.ylabel('Accuracy')
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('figs/evaluate_S/acc_plot_S.pdf', dpi=300, bbox_inches='tight')
plt.close()