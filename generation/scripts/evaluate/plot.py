import os
import re
import matplotlib.pyplot as plt
import numpy as np

# Define methods
mask_methods = ["Random", "Purpose"]
split_methods = ["Random", "RandomFull", "Cascade", "CascadeFull", "Window", "MixBasic", "MixSuper", "Full"]

# Create dictionary to store results
results = {mask: {train: {test: 0.0 for test in split_methods} for train in split_methods} for mask in mask_methods}

# Read log files and extract acc values
log_dir = "logs/evaluate"
for mask in mask_methods:
    for train in split_methods:
        for test in split_methods:
            filename = f"MAEGIN_{train}_{mask}_on_{test}_{mask}.log"
            filepath = os.path.join(log_dir, filename)
            
            try:
                with open(filepath, 'r') as f:
                    content = f.read()
                    # Extract acc value using regex
                    match = re.search(r'\[acc\]=(\d+\.\d+)', content)
                    if match:
                        acc = float(match.group(1))
                        results[mask][train][test] = acc
            except FileNotFoundError:
                print(f"Warning: File {filepath} not found")

fig_dir = "figs/evaluate"

# Create plots
# plt.style.use('seaborn')
colors = plt.cm.Set2(np.linspace(0, 1, len(split_methods)))

for mask in mask_methods:
    plt.figure(figsize=(12, 8))
    
    for i, train in enumerate(split_methods):
        acc_values = [results[mask][train][test] for test in split_methods]
        plt.plot(split_methods, acc_values, '-o', label=f'Train: {train}', color=colors[i])
    
    plt.title(f'Accuracy for {mask} Mask Method')
    plt.xlabel('Test Split Method')
    plt.ylabel('Accuracy')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(f'{fig_dir}/acc_plot_{mask}.pdf', dpi=300, bbox_inches='tight')
    plt.close()