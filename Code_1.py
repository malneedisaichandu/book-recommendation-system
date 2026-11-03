
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
fav_book = input("Enter your favourite book name: ")

# Find book index
if fav_book in book_names:

    book_index = df[df["Book_Name"] == fav_book].index[0]

    # Get similarity scores
    scores = list(enumerate(similarity[book_index]))

    # Sort by similarity
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nBooks recommended for you:\n")

    count = 0

    for index, score in scores:

        if index != book_index:
            print(df.iloc[index]["Book_Name"])
            count += 1

        if count == 5:
            break

else:
    print("Book not found in dataset.")
