# DS24_project
Analyzing NPF discourse in Swedish news – a semantic and sentiment approach

This project explores how neuropsychiatric disorders (NPF) are portrayed in Swedish news media. Using topic modeling and sentiment analysis, the goal is to identify recurring themes and emotional tone across a large set of articles.

## Contents
- `url_scraper.py`: Script for collecting news articles from Swedish media sources.
- `data_exploration.ipynb`: Initial data overview and cleaning.
- `npf_analysis.ipynb`: Topic modeling with BERTopic and sentiment analysis.
- `Result_example/`: Example outputs and visualizations.
- `README.md`: Project overview.

## Methods
- Topic modeling using BERTopic
- Sentiment analysis based on word lists
- Visualization of theme and tone distribution

## Language
Most code and comments are in Swedish, as the analysis focuses on Swedish-language media.

## How to Run
This project was developed and tested in Google Colab. To run the analysis:

1. Open `npf_analysis.ipynb` in Google Colab.
2. Make sure the following Python packages are installed:
   - `bertopic`
   - `pandas`
   - `matplotlib`
   - `scikit-learn`
   - `nltk`
   - `numpy`
   - `seaborn`
3. If needed, install missing packages using:
   ```python
   !pip install bertopic pandas matplotlib scikit-learn nltk numpy seaborn

## Author
Lisa Påhlsson

