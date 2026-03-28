import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from mlxtend.frequent_patterns import apriori, association_rules
from sklearn.metrics import roc_auc_score, accuracy_score
import time

print("Loading data...")
# Load a smaller subset of the dataset because Apriori is computationally expensive
train = pd.read_csv('dataset/train.csv').sample(n=10000, random_state=42)

def clean(comment):
    comment = comment.lower()
    comment = re.sub('[^a-zA-Z]', ' ', comment)
    comment = comment.strip()
    return comment

print("Cleaning text...")
train['clean_text'] = train['comment_text'].apply(clean)

print("Vectorizing...")
# Using a small vocabulary size for Apriori
vectorizer = CountVectorizer(max_features=100, stop_words='english', binary=True)
X = vectorizer.fit_transform(train['clean_text']).toarray()
words = vectorizer.get_feature_names_out()
X_df = pd.DataFrame(X, columns=words)

labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

print("Running Apriori for Association Rules based Classification...")
# Combine features and labels
X_train, X_val, y_train, y_val = train_test_split(X_df, train[labels], test_size=0.2, random_state=42)

y_train_df = y_train.reset_index(drop=True)
X_train_df = X_train.reset_index(drop=True)

df_apriori = pd.concat([X_train_df, y_train_df], axis=1)

start_time = time.time()
# Applying Apriori algorithm to discover frequent itemsets
# Min support set to a reasonable value
frequent_itemsets = apriori(df_apriori, min_support=0.01, use_colnames=True)

# Generate rules
print("Generating rules...")
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)

print(f"Apriori finished in {time.time() - start_time:.2f} seconds.")

# Very naive Rule-Based Classifier
# For each label, if a comment contains the antecedents of a rule that implies the label, predict 1.
val_acc = []
val_auc = []

X_val_df = X_val.reset_index(drop=True).copy()
y_val_df = y_val.reset_index(drop=True)

for label in labels:
    # Filter rules for the current label
    label_rules = rules[rules['consequents'] == {label}]
    
    preds = np.zeros(len(X_val_df))
    
    # If a row has all items in any antecedent, predict 1
    for idx, row in label_rules.iterrows():
        antecedents = list(row['antecedents'])
        # Check matching
        # taking the product of the boolean values across the antecedents
        if all(item in X_val_df.columns for item in antecedents):
            match = X_val_df[antecedents].all(axis=1)
            preds[match] = 1
            
    try:
        auc = roc_auc_score(y_val_df[label], preds)
    except:
        auc = 0.5
    acc = accuracy_score(y_val_df[label], preds)
    
    val_acc.append(acc)
    val_auc.append(auc)
    
    print(f"Class: {label} | Val Acc: {acc:.4f} | Val AUC: {auc:.4f}")

mean_auc = np.mean(val_auc)
print(f"\nMean AUC_ROC Score: {mean_auc:.4f}")

with open('apriori_results.txt', 'w') as f:
    f.write(str(mean_auc))
