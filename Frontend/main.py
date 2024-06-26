import pandas as pd
import numpy as np
import pickle
import streamlit as st


# Load the saved pickle files
pt = pd.read_pickle('pt.pkl')
similarity_scores = pd.read_pickle('similarity_scores.pkl')
books = pd.read_pickle('books.pkl')
adjusted_similarity_scores = similarity_scores.copy()

# Function to load similarity scores from pickle file
def load_similarity_scores(file_path):
    with open(file_path, 'rb') as f:
        similarity_scores = pickle.load(f)
    return similarity_scores

# Function to save similarity scores to pickle file
def save_similarity_scores(similarity_scores, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(similarity_scores, f)

# Modify recommend_through_cs function with error handling
def recommend_through_cs(book_name, similarity_scores=similarity_scores):
    try:
        # Get the index of the Book Name
        index = np.where(pt.index == book_name)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:11]

        data = []
        for idx, score in similar_items:
            temp_df = books[books['Book-Title'] == pt.index[idx]]
            item = [temp_df['Book-Title'].values[0], temp_df['Book-Author'].values[0], temp_df['Image-URL-M'].values[0]]
            data.append(item)

        # Creating a DataFrame 'df' using 'data' with columns labeled as 'Book-Title', 'Book-Author', and 'Image-URL-M'
        df = pd.DataFrame(data, columns=['Book-Title', 'Book-Author', 'Image-URL-M'])

        return df
    except:
        # If the book is not found in the database, return empty DataFrame
        return pd.DataFrame(columns=['Book-Title', 'Book-Author', 'Image-URL-M'])

def get_books_list():
    return pt.index.tolist()

books_list = get_books_list()

# UI configurations
st.set_page_config(page_title="Book Recommendation System",
                   page_icon=":books:",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.markdown("# :books: Book Recommendation System")

# Add sidebar
selected_book = st.sidebar.selectbox('**Select a Book**', books_list)
st.sidebar.write('**Selected Book Details:**')

# Display the selected book image in the sidebar with gallery placeholder
sidebar_placeholder = st.sidebar.empty()
sidebar_placeholder.image(books[books['Book-Title'] == selected_book]['Image-URL-M'].values[0], width=200)  # Adjust width here
# Display the selected books details in the sidebar
st.sidebar.write('**Title:**', selected_book)
st.sidebar.write('**Author:**', books[books['Book-Title'] == selected_book]['Book-Author'].values[0])
st.sidebar.write('**Year of Publication:**', books[books['Book-Title'] == selected_book]['Year-Of-Publication'].values[0])
st.sidebar.write('**Publisher:**', books[books['Book-Title'] == selected_book]['Publisher'].values[0])

recommended_books=pd.DataFrame(columns=['Book-Title', 'Book-Author', 'Image-URL-M'])
# Interactive recommendation loop
# Initialize session state
if 'recommend_btnClicked' not in st.session_state:
    st.session_state['recommend_btnClicked'] = False

# Interactive recommendation loop
if st.sidebar.button('Recommend'):
    st.session_state['recommend_btnClicked'] = True
if st.session_state['recommend_btnClicked']:
    recommended_books = recommend_through_cs(selected_book,adjusted_similarity_scores)
    if recommended_books.empty:
        st.write('Book not found in the database')
    else:
        st.header('**Recommended Books:**')
        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                st.markdown(
                    f"""
                    <div style="border: 2px solid #ccc; padding: 10px; margin-bottom: 20px; text-align: center; width: 250px; height: 600px; ">
                        <img src="{recommended_books['Image-URL-M'][i]}" style="width: 200px; height: 350px; border-radius: 10px;">
                        <p><strong>Title:</strong> {recommended_books['Book-Title'][i]}</p>
                        <p><strong>Author:</strong> {recommended_books['Book-Author'][i]}</p>
                        <p><strong>Year of Publication:</strong> {books[books['Book-Title'] == recommended_books['Book-Title'][i]]['Year-Of-Publication'].values[0]}</p>
                        <p><strong>Publisher:</strong> {books[books['Book-Title'] == recommended_books['Book-Title'][i]]['Publisher'].values[0]}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        # Allow user to provide feedback
        feedback = st.selectbox('Provide feedback:', ('Select', 'Yes', 'No'))
        if feedback == 'Yes':
            # toast
            st.success('Please provide feedback for the recommended books')
            st.write('Feedback:')
            feedback_data = []
            for i, book_title in enumerate(recommended_books['Book-Title']):
                st.write(f"Book: {book_title}")
                rating = st.slider(f"Rate book {book_title}", 1, 5, 3,step=1)
                feedback_data.append({'Book-Title': book_title, 'Rating': rating})
            feedback_df = pd.DataFrame(feedback_data)
            if(st.button('Submit Feedback')):
                # Update similarity scores based on feedback
                print("Updating similarity scores...")
            
                for _, row in feedback_df.iterrows():
                    
                    book_title = row['Book-Title']
                    rating = row['Rating']
                    # Get the index of the book in the similarity scores matrix
                    index = np.where(pt.index == book_title)[0]
                    if len(index) > 0:
                        index = index[0]
                        # Adjust similarity scores based on the user rating
                        if rating == 1:
                            # Decrease similarity scores
                            adjusted_similarity_scores[index, :] *= 0.8  # Update the entire row
                            adjusted_similarity_scores[:, index] *= 0.8 # Update the entire column

                        elif rating == 2:
                            # Decrease similarity scores
                            adjusted_similarity_scores[index, :] *= 0.9
                            adjusted_similarity_scores[:, index] *= 0.9
                            
                        elif rating==4:
                            # Increase similarity scores
                            adjusted_similarity_scores[index, :] *= 1.1 # Update the entire row
                            adjusted_similarity_scores[:, index] *= 1.1 # Update the entire column
                            
                        elif rating==5:
                            # Increase similarity scores
                            adjusted_similarity_scores[index, :] *= 1.2 # Update the entire row
                            adjusted_similarity_scores[:, index] *= 1.2 # Update the entire column

                        # Re-normalize similarity scores
                        adjusted_similarity_scores[index] = (adjusted_similarity_scores[index] - min(adjusted_similarity_scores[index])) / (max(adjusted_similarity_scores[index]) - min(adjusted_similarity_scores[index]))
                        # Ensure scores are between 0 and 1
                # Get new recommendations with updated similarity scores
                # Save the updated similarity scores
                save_similarity_scores(adjusted_similarity_scores, 'similarity_scores.pkl')
                # Reload the similarity scores
                similarity_scores = load_similarity_scores('similarity_scores.pkl')
                updated_recommendations = recommend_through_cs(selected_book,adjusted_similarity_scores)
                if not updated_recommendations.empty:
                    st.header('**Updated Recommended Books:**')
                    cols = st.columns(5)
                    for i, col in enumerate(cols):
                        with col:
                            st.markdown(
                                f"""
                                <div style="border: 2px solid #ccc; padding: 10px; margin-bottom: 20px; text-align: center; width: 250px; height: 600px; ">
                                    <img src="{updated_recommendations['Image-URL-M'][i]}" style="width: 200px; height: 350px; border-radius: 10px;">
                                    <p><strong>Title:</strong> {updated_recommendations['Book-Title'][i]}</p>
                                    <p><strong>Author:</strong> {updated_recommendations['Book-Author'][i]}</p>
                                    <p><strong>Year of Publication:</strong> {books[books['Book-Title'] == updated_recommendations['Book-Title'][i]]['Year-Of-Publication'].values[0]}</p>
                                    <p><strong>Publisher:</strong> {books[books['Book-Title'] == updated_recommendations['Book-Title'][i]]['Publisher'].values[0]}</p>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )