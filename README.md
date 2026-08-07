# Movie Recommendation System

A Content-Based Movie Recommendation System built using Machine Learning and Streamlit. The application recommends the top 5 movies similar to a selected movie based on movie metadata and displays their posters using the TMDB API.

---

## Preview

### Recommendation Example 1

![Recommendation Example 1](images/homepage1.png)

### Recommendation Example 2

![Recommendation Example 2](images/homepage2.png)

---

## Features

- Recommend Top 5 Similar Movies
- Display Movie Posters using TMDB API
- Content-Based Recommendation System
- Interactive Streamlit Interface
- Fast Recommendations using Cosine Similarity

---

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Requests
- TMDB API

---

## Dataset

- TMDB 5000 Movies Dataset
- TMDB 5000 Credits Dataset

---

## Project Workflow

1. Load the movie and credits datasets.
2. Merge both datasets.
3. Perform data cleaning and preprocessing.
4. Create tags using genres, keywords, cast, crew, and overview.
5. Apply Porter Stemming.
6. Convert text into vectors using CountVectorizer.
7. Compute Cosine Similarity.
8. Save processed data as `movies.pkl` and `similarity.pkl`.
9. Display movie recommendations using Streamlit.

---

## Project Structure

```text
MovieRecommendationProject/
│
├── app.py
├── main.py
├── movies.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
└── images/
    ├── homepage1.png
    └── homepage2.png
```

> **Note:** `similarity.pkl` is not included in this repository because it exceeds GitHub's 100 MB file size limit. Generate it locally by running `main.py`.

---

## Installation

Clone the repository

```bash
git clone https://github.com/riteshmishra16/MovieRecommendationSystem.git
```

Move into the project directory

```bash
cd MovieRecommendationSystem
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment (Windows)

```bash
.venv\Scripts\activate
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root directory.

```env
TMDB_API_KEY=YOUR_TMDB_API_KEY
```

You can refer to the `.env.example` file for the required format.

---

## Generate Recommendation Files

Run the preprocessing script to generate the required pickle files.

```bash
python main.py
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Future Improvements

- Hybrid Recommendation System
- Collaborative Filtering
- User Authentication
- Movie Ratings & Reviews
- Search Suggestions

---

## Author

**Ritesh Kumar Mishra**

GitHub: https://github.com/riteshmishra16

LinkedIn: https://www.linkedin.com/in/ritesh-kumar-mishra-234252349/
