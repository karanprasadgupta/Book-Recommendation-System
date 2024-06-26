# Book Recommendation System
## Problem Statement
We aim to develop an advanced book recommendation system to address the challenge users face in finding personalized book suggestions amidst a vast array of options. Existing systems often fail to provide accurate recommendations, resulting in user dissatisfaction and reduced engagement. We propose a novel approach leveraging sophisticated algorithms and user-centric design to deliver tailored book suggestions that enhance user satisfaction and engagement.

## Table of Contents

- [Project Overview](#project-overview)
- [Literature Review](#literature-review)
- [Data](#data)
- [Demo](#demo)
- [Frontend Implementation](#frontend-implementation)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Contributors](#contributors)
- [License](#license)

## Project Overview
The Book Recommendation System is a comprehensive platform developed to address the challenge users encounter when seeking personalized book recommendations in a vast sea of options. Traditional recommendation systems often provide generic suggestions that fail to resonate with individual preferences, leading to user dissatisfaction and reduced engagement. To overcome these limitations, our project leverages sophisticated algorithms and user-centric design principles to deliver tailored book suggestions that enhance user satisfaction and engagement. By integrating elements from collaborative filtering, content-based filtering, and hybrid recommendation methods, we aim to provide accurate, diverse, and personalized recommendations that cater to the unique tastes and interests of each user. The system features a user-friendly web interface that allows users to explore books seamlessly, receive recommendations, and provide feedback, fostering a dynamic and engaging reading experience. With future enhancements focusing on advanced machine learning techniques, real-time updates, community engagement, and inclusivity, our project aims to revolutionize the way users discover and engage with books.

## Literature Review
1. [**IEEE Xplore: Book Recommendation System Based on Machine Learning Techniques**](https://ieeexplore.ieee.org/document/9579647)
   - The authors explore machine learning methods, including K-nearest neighbors, Pearson’s R Correlation Coefficient, and Cosine Similarity, for collaborative filtering.

2. [**Carleton College: Book Recommendation System Using Machine Learning Classifiers and Collaborative Filtering**](https://cs.carleton.edu/cs_comps/1617/book_rec/final-results/paper.pdf)
   - This project utilizes data gathered from various sources and employs machine learning classifiers such as Naive Bayes and Maximum Entropy, along with collaborative filtering methods, for book recommendations.

3. [**Book Recommendation System using Association Rule Mining & Collaborative Filtering**](https://www.academia.edu/38859595/ONLINE_BOOK_RECOMMENDATION_SYSTEM_USING_ASSOCIATION_RULE_MINING_AND_COLLABORATIVE_FILTERING_)
   - This research paper discusses collaborative filtering algorithms like Jaccard Distance and Pearson’s Coefficient, alongside a novel technique called Association Mining, for book recommendations.
  
## Data
The dataset used in this project is sourced from [Kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) and comprises three main tables:

- **Users:** Contains information about users, including unique User-IDs and demographic details.
- **Ratings:** Stores user ratings for various books, identified by their ISBN. Each rating is associated with a specific user and book combination.
- **Books:** Provides comprehensive details about each book, such as title, author, publication year, and genre. Additionally, it includes attributes like book cover images and URLs.

The dataset has been preprocessed to handle missing values, inconsistencies, and outliers, ensuring data quality for model training and evaluation. Data merging and transformation have been done to create unified representations to facilitate recommendation model development.

## Demo
[Youtube Demo Video](https://youtu.be/HXynlfPxUM8)
### Recommendation System in Action
1. *Users exploring personalized book recommendations.*
   ![Demo Image 1](https://github.com/sarthak20574/Book_Recommendation_System/blob/main/Frontend/Demo%20Images/Img1.png)

2. *User Providing feedback on different books recommended*
   ![Demo Image 2](https://github.com/sarthak20574/Book_Recommendation_System/blob/main/Frontend/Demo%20Images/Img2.png)

3. *Updated Recommendations being shown to the user based on feedback*
   ![Demo Image 3](https://github.com/sarthak20574/Book_Recommendation_System/blob/main/Frontend/Demo%20Images/Img3.png)


## Frontend Implementation
The front end of the Book Recommendation System consists of an interactive `python streamlit`web application designed to provide users with a seamless recommendation experience. Key features include:

- **User-Friendly Interface:** An intuitive and user-friendly interface that allows users to navigate the system and access personalized recommendations easily.
- **Book Selection:** Enables users to search for books by title.
- **Recommendation Display:** Presents recommended books to users in a visually appealing format, including book covers, titles, authors, and additional details.
- **Feedback Mechanism:** Incorporates mechanisms for user feedback and ratings, allowing users to provide input on recommended books and improve future recommendations.
### Tools Used:

- **Streamlit:** A Python framework for building interactive web applications.
- **HTML/CSS:** Used with Streamlit markdown to customize the appearance and layout of the web application.

## Directory Structure

### Baseline Directory
- [38_Baseline.zip](path/to/38_Baseline.zip): Contains the baseline version of the project.
- [38_BaselineReport_IR.pdf](path/to/38_BaselineReport_IR.pdf): Baseline report for the IR project.
- [IR_Project_Baseline (2).ipynb](path/to/IR_Project_Baseline.ipynb): Jupyter Notebook for the baseline version of the IR project.

### Frontend Directory
- **Demo Images/**
  - Added Website Images: Images demonstrating the Book Recommendation System.
- [main.py](path/to/main.py): Contains the code for the streamlit app for web application

### Proposal Directory
- [38_Proposal_IR.pdf](path/to/38_Proposal_IR.pdf): Proposal for the IR project.
- [38_UpdatedBaselineReport_IR.pdf](path/to/38_UpdatedBaselineReport_IR.pdf): Updated baseline report for the Information Retrieval project.

### [IR_Project_Final.ipynb](IR_Project_Final.ipynb)
- Jupyter Notebook for the final version of the IR project.

### [Project Report](https://github.com/sarthak20574/Book_Recommendation_System/blob/main/38__FinalReport_IR.pdf)
- Final project report that includes Problem Statement, Motivation, Literature Review, Novelty, Methodology, Code, and Evaluation.

### [Project Presentation](https://github.com/sarthak20574/Book_Recommendation_System/blob/main/38_IR-Final-PPT.pptx)
- Final Presentation for the project.

## Installation
To get a local copy of this project up and running, follow these steps:

1. Clone this repository to your local machine using the following command:

   ```shell
   git clone https://github.com/sarthak20574/Book_Recommendation_System.git
   ```
2. Navigate to the project directory:
   ``` shell
   cd .\Book_Recommendation_System\Frontend\
   ```
3. Install the required dependencies (streamlit, pandas and numpy, etc.):
   ``` shell
   pip install streamlit
   ```
4. Running the App:
   ``` shell
   streamlit run main.py
   ```
   This will start the app in the local environment.
   > Note: Before running the app place `books.pkl`, `similarity_scores.pkl` and `pt.pkl` in the same folder. The files can be obtained directly by running the code in [`IR_Project_Final.ipynb`](IR_Project_Final.ipynb)


## Contributors
- [Karan Prasad Gupta](https://github.com/karanprasadgupta)
- [Sarthak Dixit](https://github.com/sarthak20574)
- [Shivanshu Kumar](https://github.com/shivanshu07)
- [D Likhith](https://github.com/sherlock1108)
- [Rishav](https://github.com/rishav197)
- Harsh Kashyap

## License
This project is licensed under the [MIT License](LICENSE).

>This project was developed for learning purposes as part of the CSE508-Information Retrieval, Winter 2024 semester, Project at IIITD under the supervision of [Prof. Rajiv Ratn Shah](https://faculty.iiitd.ac.in/~rajivratn/).
