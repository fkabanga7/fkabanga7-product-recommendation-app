import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load the dataset
data = pd.read_excel('AllITBooks_DataSet.xlsx')  # Adjust the path to your .xlsx file

# Preprocess the descriptions (clean the text)
data['Description'] = data['Description'].str.replace(r'\nBook Description:', '', regex=True)
data['Description'] = data['Description'].str.strip()  # Remove any extra spaces

# Vectorize the descriptions using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=500)
X = vectorizer.fit_transform(data['Description'])

# Apply KMeans clustering (you can change the number of clusters)
num_clusters = 5  # Adjust the number of clusters as needed
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
data['Category_Predicted'] = kmeans.fit_predict(X)

# Streamlit Title
st.title("IT Book Categorizer")

# User Input - Search for a book by name
book_name = st.text_input("Enter Book Name:")

if book_name:
    # Filter book based on user input (ignore case)
    book = data[data['Book_name'].str.contains(book_name, case=False, na=False)].iloc[0]
    
    st.subheader(f"Book: {book['Book_name']}")
    st.write(f"Predicted Category: {book['Category_Predicted']}")
    st.write(f"Description: {book['Description']}")
    
    # Display most related books (bonus part)
    related_books = data[data['Category_Predicted'] == book['Category_Predicted']].sort_values(by='Description')
    st.write("Related Books:")
    st.write(related_books[['Book_name', 'Description']].head(2))  # Show top 2 related books

