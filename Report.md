# Project Report: Hate Speech Detection

**Author**: Ujjwal CHaudhary
**Date**: March 2026

## 1. Introduction and Objective

The project aims at improving the user experience of using any website for online chats, conversations, and posts by flagging and removing textual material containing hate and toxicity.

Given any text or paragraph containing a few lines in natural language (such as English), the objective is to classify it as belonging to one of the following categories: normal, obscene, threatening, insulting, toxic, severely toxic, and hate.

This is a multi-class and multi-label classification problem, since a single post can be abusive in multiple ways. The model outputs the probability of the post belonging to each category, and based on a threshold, a comment is classified into a set of categories.

---

## 2. Dataset Overview

The dataset consists of comments extracted and labeled for toxic behavior. It is split into training data (with assigned label probabilities) and test data for evaluating our classifications.

### Dataset Size Statistics:
- **Total Training Records**: 159,571
- **Total Testing Records**: 153,164
- **Total Records in Dataset**: 312,735

---

## 3. Methodology

Embeddings were utilized to give context and weight to the texts processed by some models. Specifically:
- **Fasttext Embeddings**
- **GloVe Embeddings**
- **Word2Vec Embeddings**

Several machine learning models and neural network architectures were tested to compare effectiveness and execution efficiency.

---

## 4. Algorithms and Results

We evaluated the distinct machine learning and deep learning models based on the AUC_ROC Score. This score serves as the primary metric indicating the performance and accuracy of our models over the highly imbalanced classification datasets.

| Algorithm (Model) | Accuracy (Mean AUC_ROC Score) |
| :--- | :--- |
| Support Vector Machines (Binary Relevance) | 0.66 |
| Support Vector Machines (Classifier Chains) | 0.67 |
| Logistic Regression (Binary Relevance) | 0.73 |
| Logistic Regression (Classifier Chains) | 0.76 |
| Extra Trees | 0.93 |
| XGBoost | 0.96 |
| **LSTM without pretrained embeddings** | **0.97** |
| LSTM with FastText embedding | 0.96 |
| Naive Bayes | 0.97 |
| LSTM with Glove embedding | 0.88 |
| LSTM with Word2Vec embedding | 0.85 |
| Apriori (Association Rules) | 0.50 |

## 5. Conclusion

The Recurrent Neural Network architectural setup via **LSTM (Long Short-Term Memory) without pretrained embeddings** performed the best on our training distributions, achieving the highest Mean AUC_ROC accuracy score of **0.97**.
