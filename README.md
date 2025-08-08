# Movie_Python_Project


## Movie Ratings & Revenue Analysis

An interactive data analytics project exploring trends in movie ratings, genres, revenues, and release years. Built using **Python**, **Pandas**, **Matplotlib**, and **Streamlit**, this project provides both an in-depth Jupyter Notebook and a live dashboard for intuitive exploration.


### Project Overview

The **Movie Ratings & Revenue Analysis** project is a data-driven exploration of the movie industry, offering both analytical insights and an interactive dashboard for users to:

* Understand how revenue and ratings have changed over time.
* Identify top-performing genres and production countries.
* Explore the relationship between budget, rating, and revenue.

The project is ideal for **data analysis learners**, **portfolio builders**, and **dashboard developers** who want to understand full-stack data workflows—from data cleaning to visual storytelling.



### Features

#### Jupyter Notebook:

* Data cleaning and preprocessing of a raw movie dataset.
* Exploratory Data Analysis (EDA) using pandas and matplotlib.
* Revenue distribution analysis.
* Genre trends over time.
* Rating vs. Revenue correlation.
* Budget vs. Revenue scatter plots.

#### Streamlit Dashboard:

* Filterable by year, rating, and genre.
* Key metrics: total revenue, average rating, total number of movies.
* Visual charts:

  * Line chart of average rating per year.
  * Bar chart of total revenue by genre.
  * Pie chart of movie count by country.
  * Scatter plot: Budget vs Revenue.
  * Heatmap or boxplots on demand.



### Tech Stack

| Tool             | Purpose                        |
| ---------------- | ------------------------------ |
| Python           | Core programming language      |
| Pandas           | Data manipulation and analysis |
| Matplotlib       | Visualizations in the notebook |
| Streamlit        | Interactive dashboard web app  |
| Jupyter Notebook | EDA and analysis notebook      |



### Project Structure
```
movie_project/
├── data/
│   └── movies.csv
├── dashboard.py
├── analysis_notebook.ipynb
├── requirements.txt
├── README.md
```



### Getting Started

#### ✅ Clone this repository:

```bash
git clone https://github.com/yourusername/movie-ratings-revenue-analysis.git
cd movie-ratings-revenue-analysis
```

#### ✅ Install dependencies:

```bash
pip install -r requirements.txt
```

#### ✅ Run the dashboard locally:

```bash
streamlit run dashboard.py
```



### Sample Data Fields (CSV Schema)

| Column Name   | Description                       |
| ------------- | --------------------------------- |
| Title         | Name of the movie                 |
| Genre         | Movie genre (e.g., Action, Drama) |
| Rating        | Viewer rating (e.g., IMDb score)  |
| Revenue       | Global revenue in USD             |
| Budget        | Production budget in USD          |
| Release\_Year | Year of release                   |
| Country       | Primary production country        |
| Runtime       | Duration in minutes               |


### Checkout the streamlit dashboard:





