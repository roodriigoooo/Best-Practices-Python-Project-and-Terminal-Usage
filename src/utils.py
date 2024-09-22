import logging
import plotly.express as px
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob

logger = logging.getLogger(__name__)

def interactive_visualization(numbers, chart_type="scatter"):
    """
    Creates an interactive chart from a list of numbers.
    """
    if not numbers:
        logger.error("No data provided to visualize.")
        raise ValueError("The list of numbers is empty.")
    if chart_type not in ["scatter", "line"]:
        logger.error(f"Unsupported chart type {chart_type}")
        raise ValueError(f"Unsupported chart type {chart_type}")

    df = pd.DataFrame({"Index": range(len(numbers)), "Value": numbers})
    if chart_type == "scatter":
        fig = px.scatter(df, x="Index", y="Value", title="Interactive Scatter Plot")
    elif chart_type == "line":
        fig = px.line(df, x="Index", y="Value", title="Interactive Line Chart")

    fig.write_html("interactive_chart.html")
    logger.info("Interactive chart saved as 'interactive_chart.html'.")

def advanced_text_analysis(text):
    """
    Performs advanced text analysis including keyword extraction and sentiment analysis.
    """
    if not text:
        logger.error("No text provided for analysis.")
        raise ValueError("The text is empty.")

    blob = TextBlob(text)
    sentiment = blob.sentiment

    # Keyword Extraction using TF-IDF
    vectorizer = TfidfVectorizer(stop_words = "english")
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_array = vectorizer.get_feature_names_out()
    tfidf_sorting = tfidf_matrix.toarray().flatten().argsort()[::-1]

    top_n = 5
    top_n_keywords = feature_array[tfidf_sorting][:top_n]
    logger.info(f"Advanced text analysis: "
                f"Polarity={sentiment.polarity}, "
                f"Subjectivity={sentiment.subjectivity}, "
                f"Keywords={top_n_keywords}")
    return {
        "polarity": sentiment.polarity,
        "subjectivity": sentiment.subjectivity,
        "keywords": top_n_keywords.tolist()
    }

