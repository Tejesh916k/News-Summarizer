import tkinter as tk
import tkinter.ttk as ttk
import nltk
from textblob import TextBlob
from newspaper import Article


def summarize():
    url = utext.get('1.0', "end").strip()
    article = Article(url)

    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state="normal")
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state="normal")

    title.delete('1.0', "end")
    title.insert("1.0", article.title)

    author.delete('1.0', "end")
    author.insert("1.0", ', '.join(article.authors))

    publication.delete('1.0', "end")
    publication.insert("1.0", article.publish_date)

    summary.delete('1.0', "end")
    summary.insert("1.0", article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f"Polarity: {analysis.polarity}, Sentiment: {'Positive' if analysis.polarity > 0.06 else 'Negative' }")

    title.config(state='disabled')
    author.config(state="disabled")
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state="disabled")


root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')
root.configure(bg="#f0f0f0")

header = tk.Label(root, text="News Summarizer 📰", font=("Arial", 18, "bold"), bg="orange", fg="white")
header.pack(fill="x", pady=5)

frame_top = tk.Frame(root, bg="lightblue", padx=10, pady=10)
frame_top.pack(fill="x")

frame_bottom = tk.Frame(root, bg="white", padx=10, pady=10)
frame_bottom.pack(fill="both", expand=True)

ulabel = tk.Label(frame_top, text="Enter News URL:", font=("Arial", 12, "bold"), bg="lightblue")
ulabel.pack(side="left", padx=5)

utext = tk.Text(frame_top, height=1, width=100)
utext.pack(side="left", padx=5)

btn = tk.Button(frame_top, text="Summarize", command=summarize, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")
btn.pack(side="left", padx=10)

title_label = tk.Label(frame_bottom, text="Title", font=("Arial", 12, "bold"))
title_label.pack(anchor="w")

title = tk.Text(frame_bottom, height=1, width=140)
title.config(state='disabled', bg="#dddddd")
title.pack()

author_label = tk.Label(frame_bottom, text="Author", font=("Arial", 12, "bold"))
author_label.pack(anchor="w")

author = tk.Text(frame_bottom, height=1, width=140)
author.config(state='disabled', bg="#dddddd")
author.pack()

publication_label = tk.Label(frame_bottom, text="Publishing Date", font=("Arial", 12, "bold"))
publication_label.pack(anchor="w")

publication = tk.Text(frame_bottom, height=1, width=140)
publication.config(state='disabled', bg="#dddddd")
publication.pack()

summary_label = tk.Label(frame_bottom, text="Summary", font=("Arial", 12, "bold"))
summary_label.pack(anchor="w")

summary = tk.Text(frame_bottom, height=10, width=140)
summary.config(state='disabled', bg="#dddddd")
summary.pack()

sentiment_label = tk.Label(frame_bottom, text="Sentiment Analysis", font=("Arial", 12, "bold"))
sentiment_label.pack(anchor="w")

sentiment = tk.Text(frame_bottom, height=1, width=140)
sentiment.config(state='disabled', bg="#dddddd")
sentiment.pack()

summary_scroll = tk.Scrollbar(frame_bottom)
summary_scroll.pack(side="right", fill="y")
summary.config(yscrollcommand=summary_scroll.set)
summary_scroll.config(command=summary.yview)

root.mainloop()