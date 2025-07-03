import tkinter as tk
from textblob import TextBlob
import webbrowser

mood_links = {
    "positive": "https://www.youtube.com/watch?v=ZbZSe6N_BXs&list=RDZbZSe6N_BXs&start_radio=1",
    "negative": "https://www.youtube.com/watch?v=24u3NoPvgMw&list=RD24u3NoPvgMw&start_radio=1",  
    "neutral":  "https://www.youtube.com/watch?v=SAWzXkV3hHo&list=RDSAWzXkV3hHo&start_radio=1",  
}

def analyze_mood():
    user_input = entry.get()
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        mood = "positive"
    elif polarity < -0.1:
        mood = "negative"
    else:
        mood = "neutral"

    result_label.config(text=f"Detected Mood: {mood.capitalize()}")
    webbrowser.open(mood_links[mood])

root = tk.Tk()
root.title("Moodify 🎧")
root.geometry("400x250")
root.configure(bg="#f7f7f7")

title = tk.Label(root, text="How do you feel? 🧠", font=("Arial", 16), bg="#f7f7f7")
title.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)
entry.bind("<Return>", lambda event: analyze_mood()) 


button = tk.Button(root, text="🎶 Reccomend a music!", command=analyze_mood, bg="#4CAF50", fg="white", font=("Arial", 12))
button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f7f7f7")
result_label.pack(pady=10)

root.mainloop()
