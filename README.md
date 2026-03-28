<div align="center">

[![Contributors](https://img.shields.io/github/contributors/oyyPoodles/ToxiClass-Multi-Label-NLP-Based-Moderation-Engine?style=for-the-badge)](https://github.com/oyyPoodles/ToxiClass-Multi-Label-NLP-Based-Moderation-Engine/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/oyyPoodles/ToxiClass-Multi-Label-NLP-Based-Moderation-Engine?style=for-the-badge)](https://github.com/oyyPoodles/ToxiClass-Multi-Label-NLP-Based-Moderation-Engine/network/members)
[![Stars](https://img.shields.io/github/stars/oyyPoodles/ToxiClass-Multi-Label-NLP-Based-Moderation-Engine?style=for-the-badge)](https://github.com/oyyPoodles/ToxiClass-Multi-Label-NLP-Based-Moderation-Engine/stargazers)
[![Issues](https://img.shields.io/github/issues/oyyPoodles/ToxiClass-Multi-Label-NLP-Based-Moderation-Engine?style=for-the-badge)](https://github.com/oyyPoodles/ToxiClass-Multi-Label-NLP-Based-Moderation-Engine/issues)
[![License](https://img.shields.io/github/license/oyyPoodles/ToxiClass-Multi-Label-NLP-Based-Moderation-Engine?style=for-the-badge)](https://github.com/oyyPoodles/ToxiClass-Multi-Label-NLP-Based-Moderation-Engine/blob/main/LICENSE)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/)

# ToxiClass: Multi-Label NLP-Based Moderation Engine

</div>

> **Author**: Ujjwal Chaudhary

## 📌 1. Project Overview
The **Hate Speech Detection System** is an advanced NLP-powered text classification framework designed to identify and categorize abusive language in online conversational platforms. Operating as a **multi-label classification** problem, the system determines the probability of a text exhibiting specific types of toxicity. By leveraging both traditional machine learning models and deep learning architectures like LSTMs, this project aims to foster safer digital environments by automating the moderation of harmful content.

## 🚨 2. Problem Statement
The exponential growth of online communities has inadvertently led to a rise in toxic behavior, harassment, and hate speech. This hostile environment not only degrades user experience but can also drive users away from platforms. Manual moderation is unscalable, subjective, and emotionally taxing for human reviewers. Therefore, an automated, robust, and highly accurate detection system is critical to analyzing vast streams of textual data in real time, ensuring platforms remain safe, inclusive, and welcoming.

## ✨ 3. Key Features
- **Multi-Label Classification**: Simultaneously flags content across distinct toxicity categories (Toxic, Severe Toxic, Obscene, Threat, Insult, Identity Hate).
- **Multiple ML & DL Models**: Implements and thoughtfully compares cutting-edge traditional algorithms (SVM, Logistic Regression, XGBoost, Extra Trees, Naive Bayes, Apriori) and Deep Learning models (LSTMs).
- **Pretrained Embeddings**: Integrates world-class NLP embeddings including FastText, GloVe, and Word2Vec to capture deep semantic and contextual associations.
- **Performance Evaluation**: Comprehensive robust evaluation using AUC-ROC scores uniquely suited for highly imbalanced dataset topologies.
- **Scalability Potential**: Built with optimization in mind, allowing the architecture to securely scale for real-world APIs and continuous automated content moderation pipelines.

## 🏗️ 4. System Architecture
The system architecture follows a structured NLP pipeline, translating raw text ingestion to final multi-label inference. The text undergoes rigorous cleaning and tokenization before being transformed by feature extraction techniques or dense word embeddings. These numerical representations are then classified by parallel predictive models for final aggregated toxicity flags.

```mermaid
flowchart TD
    A[User Input Text] --> B[Text Preprocessing]
    B --> C[Tokenization & Cleaning]
    C --> D[Feature Extraction]

    D --> E1[TF-IDF / Bag of Words]
    D --> E2[Word Embeddings<br>(FastText / GloVe / Word2Vec)]

    E1 --> F1[Traditional ML Models<br>(SVM, Logistic Regression, XGBoost)]
    E2 --> F2[Deep Learning Models<br>(LSTM)]

    F1 --> G[Prediction Layer]
    F2 --> G

    G --> H[Multi-label Classification Output]
    H --> I[Toxicity Categories<br>(Toxic, Obscene, Threat, Insult, Hate)]
```

## 📊 5. Dataset Statistics
The dataset, originally sourced from [Conversation AI](https://conversationai.github.io/), consists of a vast array of labeled conversational records. 

### Data Dimensions
- **Total Training Records**: 159,571
- **Total Testing Records**: 153,164
- **Total Records in Dataset**: 312,735

### Class Support (Positive Labels in Training Data)
| Category | Support |
| :--- | :--- |
| **Toxic** | 15,294 |
| **Obscene** | 8,449 |
| **Insult** | 7,877 |
| **Severe Toxic** | 1,595 |
| **Identity Hate**| 1,405 |
| **Threat** | 478 |

> **Note on Apriori**: In mining frequent patterns via the Apriori algorithm, a minimum support threshold of `0.01` (1%) and a minimum confidence threshold of `0.1` (10%) were utilized.

## 🧠 6. Pretrained Embeddings
The models utilize state-of-the-art context vectors. The download links for the pretrained embeddings used are attached below:
- [FastText Embeddings](https://www.kaggle.com/vsmolyakov/fasttext/download)
- [GloVe Embeddings](https://www.kaggle.com/joshkyh/glove-twitter/download)
- [Word2Vec Embeddings](http://vectors.nlpl.eu/repository/20/2.zip)

## 📁 7. File Structure & Notebooks
The codebase is structured into self-contained Jupyter notebooks (`.ipynb`), combining the execution code with direct outputs for maximum reproducibility.

- **Data Visualization & Analysis**: [`Visualisation.ipynb`](Visualisation.ipynb)
- **Extra Trees**: [`ExtraTrees.ipynb`](ExtraTrees.ipynb)
- **Naive Bayes**: [`NaiveBayes.ipynb`](NaiveBayes.ipynb)
- **Logistic Regression** - Binary Relevance & Classifier Chains: [`LogisticRegression.ipynb`](LogisticRegression.ipynb)
- **Support Vector Machine (SVM)** - Binary Relevance & Classifier Chains: [`SupportVectorMachine.ipynb`](SupportVectorMachine.ipynb)
- **XGBoost**: [`XGBoost.ipynb`](XGBoost.ipynb)
- **LSTM (No Pretrained Embeddings)**: [`LSTM_without.ipynb`](LSTM_without.ipynb)
- **LSTM (FastText Embeddings)**: [`LSTM_fasttext.ipynb`](LSTM_fasttext.ipynb)
- **LSTM (GloVe Embeddings)**: [`LSTM_glove.ipynb`](LSTM_glove.ipynb)
- **LSTM (Word2Vec Embeddings)**: [`LSTM_word2vec.ipynb`](LSTM_word2vec.ipynb)

*Included documentation artifacts:*
- `Project_Description.pdf`
- `Presentation.pdf`
- `Report.pdf`
- `Report.md` (Markdown version of the detailed technical report)

## 🏆 8. Algorithms and Results
Due to the highly imbalanced nature of the dataset, models are primarily evaluated based on the computationally solid **Mean AUC-ROC Score**, serving as the final verdict metric for overall predictive reliability.

| Algorithm (Model) | Accuracy (Mean AUC-ROC Score) |
| :--- | :--- |
| Support Vector Machines (Binary Relevance) | 0.66 |
| Support Vector Machines (Classifier Chains) | 0.67 |
| Logistic Regression (Binary Relevance) | 0.73 |
| Logistic Regression (Classifier Chains) | 0.76 |
| Apriori (Association Rules) | 0.50 |
| LSTM with Word2Vec embedding | 0.85 |
| LSTM with Glove embedding | 0.88 |
| Extra Trees | 0.93 |
| XGBoost | 0.96 |
| LSTM with FastText embedding | 0.96 |
| Naive Bayes | 0.97 |
| **LSTM without pretrained embeddings** | **0.97** |
