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
flowchart TB

%% ================= CLIENT LAYER =================
subgraph CL["🌐 Client Layer"]
    A1[Web App<br/>React / TypeScript]
    A2[Mobile App / Extension<br/>Android / Chrome]
end

%% ================= API LAYER =================
subgraph API["⚙️ API Gateway Layer"]
    B1[/api/detect<br/>Text Input/]
    B2[/api/auth<br/>JWT Authentication/]
    B3[/api/history<br/>User Logs/]
    B4[Rate Limiter<br/>60 req/min]
end

%% ================= PROCESSING =================
subgraph PROC["🧹 Preprocessing Layer"]
    C1[Text Cleaning<br/>Lowercase, Stopwords]
    C2[Tokenization<br/>Lemmatization]
end

%% ================= FEATURE ENGINEERING =================
subgraph FE["🧠 Feature Engineering"]
    D1[TF-IDF / Bag of Words]
    D2[Word Embeddings<br/>FastText / GloVe]
end

%% ================= ML ENGINE =================
subgraph ML["🤖 ML / DL Engine"]
    E1[Traditional Models<br/>SVM / Logistic Regression / XGBoost]
    E2[Deep Learning Models<br/>LSTM / BiLSTM]
end

%% ================= PREDICTION =================
subgraph PRED["📊 Prediction Layer"]
    F1[Sigmoid Activation]
    F2[Multi-label Output]
end

%% ================= DATA LAYER =================
subgraph DB["🗄️ Data Layer"]
    G1[(Dataset<br/>Jigsaw Toxic Comments)]
    G2[(User Data & Logs)]
    G3[(Trained Models<br/>.pkl / .h5)]
end

%% ================= FLOW =================

%% Client → API
A1 --> B1
A2 --> B1

A1 --> B2
A2 --> B2

%% API Routing
B1 --> C1
B2 --> G2
B3 --> G2
B4 --> B1

%% Processing
C1 --> C2
C2 --> D1
C2 --> D2

%% Feature → Models
D1 --> E1
D2 --> E2

%% Model Fusion
E1 --> F1
E2 --> F1

%% Output
F1 --> F2
F2 --> B1

%% Storage
E1 --> G3
E2 --> G3
G1 --> E1
G1 --> E2

%% ================= STYLING =================
classDef client fill:#0d47a1,color:#fff;
classDef api fill:#1b5e20,color:#fff;
classDef process fill:#4a148c,color:#fff;
classDef model fill:#e65100,color:#fff;
classDef data fill:#263238,color:#fff;
classDef pred fill:#880e4f,color:#fff;

class A1,A2 client;
class B1,B2,B3,B4 api;
class C1,C2,D1,D2 process;
class E1,E2 model;
class G1,G2,G3 data;
class F1,F2 pred;
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
