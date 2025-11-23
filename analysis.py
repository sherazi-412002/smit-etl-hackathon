import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit page setup
st.set_page_config(
    page_title="Product Insights Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title and intro
st.title("📊 Product Analytics Dashboard")
st.write("Here you can explore insights about product pricing, ratings, reviews and value. Enjoy the visuals and get a quick understanding of the dataset.")

# Load Data
df = pd.read_csv("cleaned_products_data.csv")

# Precomputations
df['value_score'] = df['rating'] / np.log1p(df['price'])

df['stock_proxy'] = np.where(
    (df['reviews'] > df['reviews'].quantile(0.75)) & (df['rating'] >= 4.8),
    'High Availability',
    np.where(df['reviews'] > df['reviews'].median(), 'Medium', 'Low')
)


# ------------------------------------
# 1. Best Value Score per Price Tier
# ------------------------------------
st.subheader("💰 Best Value Score per Price Tier")
st.write("Value score helps estimate how much value a product gives based on its rating relative to price.")

tier_value = df.groupby('price_tier')['value_score'].mean().sort_values(ascending=False)

fig1, ax1 = plt.subplots(figsize=(10, 5))
tier_value.plot(kind='bar', color=['#2ecc71', '#3498db', '#e74c3c'], ax=ax1)
ax1.set_title("Average Value Score per Price Tier")
ax1.set_xlabel("Price Tier")
ax1.set_ylabel("Average Value Score")
st.pyplot(fig1)


# ------------------------------------
# 2. Estimated Stock Availability
# ------------------------------------
st.subheader("📦 Estimated Stock Availability")
st.write("This estimation uses review volume and rating to guess likely availability.")

stock_counts = df['stock_proxy'].value_counts()

fig2, ax2 = plt.subplots(figsize=(8, 6))
stock_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    colors=['#27ae60', '#f39c12', '#e74c3c'],
    explode=(0.05, 0.05, 0.05),
    ax=ax2
)
ax2.set_ylabel("")
ax2.set_title("Estimated Stock Availability")
st.pyplot(fig2)


# ------------------------------------
# 3. Price Distribution
# ------------------------------------
st.subheader("💲 Price Distribution (Log Scaled)")
st.write("Because price data is usually skewed, a log scaled histogram gives clearer insight.")

fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.hist(df['price'], bins=50, color='skyblue', edgecolor='black', log=True)
ax3.set_title("Price Distribution (Log Scale)")
ax3.set_xlabel("Price")
ax3.set_ylabel("Frequency")
st.pyplot(fig3)


# ------------------------------------
# 4. Rating vs Price
# ------------------------------------
st.subheader("⭐ Rating vs Price")
st.write("This scatter plot shows the relationship between product rating and price. The trend line shows how rating shifts across prices.")

fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x="price", y="rating", hue="price_tier", alpha=0.7, s=60, ax=ax4)
sns.regplot(data=df, x="price", y="rating", scatter=False, color="red", lowess=True, ax=ax4)
ax4.set_title("Rating vs Price")
ax4.set_xlabel("Price")
ax4.set_ylabel("Rating")
st.pyplot(fig4)


# ------------------------------------
# 5. Top Reviewed Products
# ------------------------------------
st.subheader("🔥 Top Reviewed Products")
st.write("These products have the highest number of reviews and usually represent what users engage with the most.")

top_reviewed = df.nlargest(10, 'reviews')[['product_name', 'reviews', 'rating', 'price', 'price_tier']]

fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_reviewed, x='reviews', y='product_name', hue='price_tier', dodge=False, ax=ax5)
ax5.set_title("Top 10 Most Reviewed Products")
ax5.set_xlabel("Reviews")
ax5.set_ylabel("Product Name")
st.pyplot(fig5)

st.write("Here are the top reviewed products:")
st.dataframe(top_reviewed)

