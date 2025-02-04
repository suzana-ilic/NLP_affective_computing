

This thesis aims to contribute to research efforts in the field of affective computing and to provide a holistic analysis of text-based emotion recognition from the perspective of Applied and Computational  Linguistics. We will examine linguistic features, annotation schemes, categorical and dimensional emotion models, as well as commonly used research datasets with different linguistic styles, and focus on deep neural network architectures as the main prediction systems, since deep learning has achieved major breakthroughs and state-of-the-art results for a large number of tasks in the field of Natural Language Processing (Young  et  al. 2018). Schematic thesis overview that spans analyses, tasks and implications for (1) datasets, (2) emotion models and (3) algorithms:

<p align="center"><img src="https://github.com/suzana-ilic/EDA_nlp_emotion_datasets/blob/master/images/overview.png" width="600"></p>

# Overview

## Emotion Models

- Categorical emotion models – emotions are represented as distinct, mutually exclusive categories (e.g. the basic emotions anger, fear, joy, ...)
- Dimensional emotion models – emotions are represented in a two- or multidimensional space (e.g. valence and arousal)

<p align="center"><img src="https://github.com/suzana-ilic/EDA_nlp_emotion_datasets/blob/master/images/em_models.png" width="600"></p>


### Model demo: Predicting basic emotions

In this demo you can try out directly in the browser [a fine-tuned checkpoint of DistilRoBERTa-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) by Jochen Hartmann. The model was trained on 6 diverse datasets (see Appendix below) and predicts Ekman's 6 basic emotions, plus a neutral class:

- anger 🤬
- disgust 🤢
- fear 😨
- joy 😀
- neutral 😐
- sadness 😭
- surprise 😲

[Demo](https://huggingface.co/spaces/Suzana/text_basic_emotions) by Suzana Ilic

Model reference: Jochen Hartmann, "Emotion English DistilRoBERTa-base". https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/, 2022.

### Datasets

- Dataset I – Facebook posts
- Dataset II – Media headlines (SemEval 2007)

### Notebooks

- EDA
- Transformers

# Exploratory data analysis for emotion datasets (text)

The goal of exploratory data analyses for emotion datasets is to get an understanding of the corpus, the linguistic style, lexical elements, syntax as well as the annotation scheme, distribution and imbalance check of classes (or analyses of scores).

## Contents

## Dataset I

- **Dataset:** 2,894 Facebook posts annotated with scores for valence and arousal on an integer scale from 1-9 repsectively
- [EDA](https://github.com/suzana-ilic/EDA_nlp_emotion_datasets/blob/master/notebooks/)
- Model (BERT, RoBERTa) using [Simple Transformers](https://simpletransformers.ai/)

**Task:** Regression\
**Paper:** [Modelling valence and arousal in facebook posts (2016)](https://www.semanticscholar.org/paper/Modelling-Valence-and-Arousal-in-Facebook-posts-Preotiuc-Pietro-Schwartz/5b9f7b419766a35c9ee4a37d5338fa557bbbea47)\
**References:**\
Preoţiuc-Pietro, D., Schwartz, H. A., Park, G., Eichstaedt, J., Kern, M., Ungar, L., & Shulman, E. (2016): Modelling valence and arousal in facebook posts. In Proceedings of the 7th workshop on computational approaches to subjectivity, sentiment and social media analysis (pp. 9-15).

Dimensonal Emotion model based on the circumplex model (valence and arousal) by James A. Russell (1980): A Circumplex Model of Affect. Journal of Personality and Social Psychology (39,6:1161–1178).

## Dataset II


