
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page configuration
st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚"
)

st.title("📚 Book Recommendation System")

st.write("Find books similar to your favourite book!")

# Read dataset
df = pd.read_csv("Book_Recommendation_Dataset.csv")

# Apply TF-IDF on Genre
vectorizer = TfidfVectorizer(stop_words="english")
feature_vectors = vectorizer.fit_transform(df["Genre"])

# Calculate cosine similarity
similarity = cosine_similarity(feature_vectors)

# Get book names
book_names = df["Book_Name"].tolist()

# Get user input
fav_book = st.text_input(
    "Enter your favourite book name:"
)

# Recommendation button
if st.button("Get Recommendations"):

    # Find book index
    if fav_book in book_names:

        book_index = df[df["Book_Name"] == fav_book].index[0]

        # Get similarity scores
        scores = list(enumerate(similarity[book_index]))

        # Sort by similarity
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        st.subheader("Recommended Books:")

        count = 0

        for index, score in scores:

            if index != book_index:
                st.write("📖", df.iloc[index]["Book_Name"])
                count += 1

            if count == 5:
                break

    else:
        st.error("Book not found in dataset.")
