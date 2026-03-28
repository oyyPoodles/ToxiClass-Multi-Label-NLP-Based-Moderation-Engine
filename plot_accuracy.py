import matplotlib.pyplot as plt

algorithms = [
    'SVM (Binary Rel.)',
    'SVM (Classifier Chains)',
    'Logistic Reg. (Binary Rel.)',
    'Logistic Reg. (Classifier Chains)',
    'Extra Trees',
    'XGBoost',
    'LSTM (No Pretrained)',
    'LSTM (FastText)',
    'LSTM (GloVe)',
    'LSTM (Word2Vec)',
    'Naive Bayes',
    'Apriori'
]

# Using the AUC_ROC parameters for consistency apart from Naive Bayes where val accuracy was generated 
accuracies = [0.66, 0.67, 0.73, 0.76, 0.93, 0.96, 0.97, 0.96, 0.88, 0.85, 0.97, 0.50]

plt.figure(figsize=(14, 7))
cmap = plt.get_cmap('tab20')
bars = plt.bar(algorithms, accuracies, color=cmap.colors[:len(algorithms)])

plt.xlabel('Algorithm', fontsize=12, fontweight='bold')
plt.ylabel('Score (Accuracy / Mean AUC-ROC)', fontsize=12, fontweight='bold')
plt.title('Performance Comparison of Classification Algorithms', fontsize=15, fontweight='bold')
plt.ylim(0, 1.1)

plt.xticks(rotation=35, ha='right')

# Adding precision labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02, f"{yval:.2f}", ha='center', va='bottom', fontsize=11)

plt.tight_layout()
plt.savefig('accuracy_plot.png', dpi=300)
print("Plot successfully generated and saved as accuracy_plot.png")
