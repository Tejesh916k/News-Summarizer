import streamlit as st
from newspaper import Article
from textblob import TextBlob
import nltk


nltk.download('punkt')

def summarize_article(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    blob = TextBlob(article.text)
    sentiment = blob.sentiment

    return {
        "title": article.title,
        "authors": ", ".join(article.authors),
        "publish_date": article.publish_date,
        "summary": article.summary,
        "sentiment": f"Polarity: {sentiment.polarity:.2f}, Subjectivity: {sentiment.subjectivity:.2f}"
    }

st.set_page_config(page_title="News Summarizer", layout="centered")
st.title("📰 News Summarizer & Sentiment Analyzer")
st.markdown("Enter a news article URL and get its title, author, summary, and sentiment analysis.")

url = st.text_input("🔗 Enter the URL of a news article")

if st.button("Summarize"):
    if url:
        with st.spinner("Analyzing..."):
            try:
                data = summarize_article(url)

                st.subheader("📌 Title")
                st.write(data["title"])

                st.subheader("✍️ Author(s)")
                st.write(data["authors"] or "Not Available")

                st.subheader("🗓️ Published Date")
                st.write(data["publish_date"] or "Not Available")

                st.subheader("📄 Summary")
                st.write(data["summary"])

                st.subheader("📊 Sentiment Analysis")
                st.success(data["sentiment"])

            except Exception as e:
                st.error(f"⚠️ Failed to summarize article. Error: {e}")
    else:
        st.warning("Please enter a valid URL.")
