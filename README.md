# Fake News Detection

A simple machine learning project to classify news as fake or real using Python and scikit-learn.

## Project Structure

```
fake-news-detection/
├── data/                  # Place your CSV dataset here (e.g., fake_or_real_news.csv)
├── models/                # Saved models and vectorizers
├── requirements.txt
├── README.md
├── fake_news_detector.py  # Main script for training and evaluation
├── utils.py               # Utility functions for loading model and prediction
└── notebook.ipynb         # Jupyter notebook for experiments
```

## Usage

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare your data**  
   Place your dataset (e.g., `fake_or_real_news.csv`) in the `data/` folder.  
   The CSV should have at least two columns: `text` (news content) and `label` (`FAKE` or `REAL`).

3. **Train the model**  
   ```bash
   python fake_news_detector.py
   ```

4. **Predict on new text**  
   Use functions in `utils.py` to load the model and predict.

5. **Jupyter Notebook**  
   Open `notebook.ipynb` for interactive exploration.

## Dataset

You can use datasets like:
- [Kaggle: Fake and real news dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)
- [LIAR dataset](https://www.cs.ucsb.edu/~william/data/liar_dataset.zip)

## Example

```python
from utils import load_model_and_vectorizer, predict_news
model, vectorizer = load_model_and_vectorizer()
result = predict_news("The moon landing was faked.", model, vectorizer)
print(result)  # Outputs: FAKE or REAL
```
