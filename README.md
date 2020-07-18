

This thesis aims to contribute to research efforts in the field of affective computing and to provide a holistic analysis of text-based emotion recognition from the perspective of Applied and Computational  Linguistics. We will examine linguistic features, annotation schemes, categorical and dimensional emotion models, as well as commonly used research datasets with different linguistic styles, and focus on deep neural network architectures as the main prediction systems, since deep learning has achieved major breakthroughs and state-of-the-art results for a large number of tasks in the field of Natural Language Processing (Young  et  al. 2018). Schematic thesis overview that spans analyses, tasks and implications for (1) datasets, (2) emotion models and (3) algorithms:

<p align="center"><img src="https://github.com/suzana-ilic/EDA_nlp_emotion_datasets/blob/master/images/overview.png" width="500"></p>

# Overview

### Datasets

- Dataset I – Facebook posts
- Dataset II – Media headlines (SemEval 2007)
- Dataset III – Dialogue (SemEval 2019)

### Notebooks

- EDA
- Transformers

# Exploratory data analysis for emotion datasets (text)

The goal of exploratory data analyses for emotion datasets is to get an understanding of the corpus, the linguistic style, lexical elements, syntax as well as the annotation scheme, distribution and imbalance check of classes (or analyses of scores).

## Contents
- [Dataset I](#dataset-i)

## Dataset I

[Jupyter notebook](https://github.com/suzana-ilic/EDA_nlp_emotion_datasets/blob/master/notebooks/)

Dataset: 2,894 Facebook posts annotated with scores for valence and arousal

Preoţiuc-Pietro, D., Schwartz, H. A., Park, G., Eichstaedt, J., Kern, M., Ungar, L., & Shulman, E. (2016): Modelling valence and arousal in facebook posts. In Proceedings of the 7th workshop on computational approaches to subjectivity, sentiment and social media analysis (pp. 9-15).

Dimensonal Emotion model based on the circumplex model (valence and arousal) by James A. Russell (1980): A Circumplex Model of Affect. Journal of Personality and Social Psychology (39,6:1161–1178).

<p align="center"><img src="https://github.com/suzana-ilic/EDA_nlp_emotion_datasets/blob/master/images/spacy_ner.png" width="500"></p>

<p align="center"><img src="https://github.com/suzana-ilic/EDA_nlp_emotion_datasets/blob/master/images/lda.png" width="400"></p>
