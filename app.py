import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import pickle

# Sample DataFrame
data = {
    'Title': [
        'Fundamentals of Wavelets', 'Data Smart', 'God Created the Integers',
        'Superfreakonomics', 'Orientalism', 'Structure and Randomness',
        'Image Processing with MATLAB', 'Animal Farm', 'Idiot, The', 'Christmas Carol, A'
    ],
    'Author': [
        'Goswami, Jaideva', 'Foreman, John', 'Hawking, Stephen',
        'Dubner, Stephen', 'Said, Edward', 'Tao, Terence',
        'Eddins, Steve', 'Orwell, George', 'Dostoevsky, Fyodor', 'Dickens, Charles'
    ],
    'Genre': [
        'signal_processing', 'data_science', 'mathematics',
        'economics', 'history', 'mathematics',
        'signal_processing', 'fiction', 'fiction', 'fiction'
    ],
    'Height': [
        228, 235, 197, 179, 197, 252, 241, 180, 197, 196
    ],
    'Publisher': [
        'Wiley', 'Wiley', 'Penguin', 'HarperCollins', 'Penguin', 'NaN', 'NaN', 'NaN', 'NaN', 'NaN'
    ]
}

df = pd.DataFrame(data)

# Combine features
df['combined_features'] = df['Title'] + ' ' + df['Author'] + ' ' + df['Genre'] + ' ' + df['Publisher'].fillna('') + ' ' + df['Height'].astype(str)

# Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['combined_features'])

# Similarity calculation
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Save the vectorizer and similarity matrix
with open('cosine_sim.pkl', 'wb') as file:
    pickle.dump(cosine_sim, file)

with open('vectorizer.pkl', 'wb') as file:
    pickle.dump(vectorizer, file)

# Streamlit app
st.title('Book Recommendation System')

selected_book = st.selectbox('Select a book:', df['Title'])

if st.button('Show Recommendations'):
    # Load the models
    with open('cosine_sim.pkl', 'rb') as file:
        cosine_sim = pickle.load(file)

    with open('vectorizer.pkl', 'rb') as file:
        vectorizer = pickle.load(file)

    def get_recommendations(title, cosine_sim=cosine_sim):
        idx = df.index[df['Title'] == title][0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        book_indices = [i[0] for i in sim_scores]
        return df['Title'].iloc[book_indices]

    recommendations = get_recommendations(selected_book)
    st.write('Recommended Books:')
    for book in recommendations:
        st.write(book)
