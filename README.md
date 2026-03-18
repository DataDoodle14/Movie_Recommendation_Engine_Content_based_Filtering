# Smart Movie Recommender System

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)


A content-based movie recommender system built with NLP and Streamlit.  
Recommends movies similar to a selected title using **TF-IDF vectorization** and **cosine similarity**.

> [Live Demo](https://your-streamlit-app-link.streamlit.app) ← replace with your deployed link

---

## Screenshots

| Home | Recommendations |
|------|-----------------|
| ![Home](screenshots/app_preview_1.png) | ![Results](screenshots/app_preview_2.png) |

---

## Features

- Content-Based Filtering using movie metadata
- TF-IDF Vectorization over combined features (overview, genres, keywords, cast, director)
- Cosine Similarity for ranking recommendations
- O(1) lookup with optimized dictionary indexing
- Movie posters fetched via TMDB API
- Clean and responsive Streamlit UI

---

## How It Works

1. Movie metadata (overview, genres, keywords, cast, director) is merged and preprocessed.
2. Weighted feature engineering boosts recommendation quality.
3. Text is vectorized using TF-IDF.
4. A cosine similarity matrix is computed across all movies.
5. Top 5 most similar movies are returned with posters.

---

## Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3.10 |
| Data Processing | Pandas, NLTK |
| ML / Similarity | Scikit-learn |
| Frontend | Streamlit |
| External API | TMDB API |

---

## Setup & Installation

### Prerequisites
- Python 3.10+
- A [TMDB API key](https://www.themoviedb.org/settings/api)

### Steps
```bash
# 1. Clone the repo
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API key
echo "API_KEY=your_api_key_here" > .env

# 4. Generate model files (run notebook or script)
jupyter notebook notebook/content_based_filtering.ipynb

# 5. Launch the app
streamlit run app.py
```

### Run with Docker
```bash
docker-compose up --build
```
Then open `http://localhost:8501` in your browser.

---

## Project Structure
```
movie_recommender/
├── data/
│   ├── tmdb_5000_credits.csv
│   └── tmdb_5000_movies.csv
├── model/
│   ├── movies.pkl
│   └── similarity.pkl
├── notebook/
│   └── content_based_filtering.ipynb
├── screenshots/
│   ├── smart_movie_recommender_sys_1.png
│   └── smart_movie_recommender_sys_2.png
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env 
├── .gitignore
└── README.md
```

---

## Future Improvements

- [ ] Hybrid recommendation (content + collaborative filtering)
- [ ] User rating-based filtering
- [ ] Trending movies section using TMDB's trending API

---

## Dataset

[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) — via Kaggle

---

##  License

MIT © Krutika Malli