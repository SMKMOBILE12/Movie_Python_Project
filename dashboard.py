import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Movie Ratings & Revenue Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("movies.csv")
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
    df["Metascore"] = pd.to_numeric(df["Metascore"], errors="coerce")
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Options")
selected_genre = st.sidebar.multiselect("Select Genre(s):", options=df["Genre"].unique(), default=df["Genre"].unique())
selected_year = st.sidebar.slider("Select Year Range:", int(df["Year"].min()), int(df["Year"].max()), (2000, 2016))

# Filter data
filtered_df = df[
    (df["Genre"].isin(selected_genre)) &
    (df["Year"].between(*selected_year))
]

# Title
st.title("🎬 Movie Ratings & Revenue Analysis")
st.markdown("An interactive dashboard to explore movie data, ratings, and revenue trends.")

# KPIs
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Movies", filtered_df.shape[0])
with col2:
    st.metric("Average Rating", f"{filtered_df['Rating'].mean():.2f}")
with col3:
    st.metric("Total Revenue (M)", f"${filtered_df['revenue'].sum():,.2f}")

st.markdown("---")

# Ratings Distribution
st.subheader("📊 Distribution of Ratings")
fig, ax = plt.subplots()
sns.histplot(filtered_df["Rating"], kde=True, bins=20, ax=ax)
st.pyplot(fig)

# Revenue by Genre
st.subheader("💰 Average Revenue by Genre")
genre_revenue = filtered_df.groupby("Genre")["revenue"].mean().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10, 5))
genre_revenue.plot(kind='bar', ax=ax)
plt.ylabel("Revenue (Millions)")
st.pyplot(fig)

# Top 10 Movies by Revenue
st.subheader("🏆 Top 10 Movies by Revenue")
top_movies = filtered_df.sort_values("revenue", ascending=False)[["Title", "revenue", "Rating", "Year"]].head(10)
st.dataframe(top_movies)

# Scatter Plot - Revenue vs Rating
st.subheader("🔍 Revenue vs Rating")
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_df, x="Rating", y="revenue", ax=ax)
st.pyplot(fig)

# Correlation Heatmap
st.subheader("🧠 Correlation Heatmap")
numeric_cols = ["Year", "runtime", "Rating", "Votes", "revenue", "Metascore"]
corr = filtered_df[numeric_cols].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Footer
st.markdown("[GitHub Repo](https://github.com/SMKMOBILE12/Movie_Python_Project)")
