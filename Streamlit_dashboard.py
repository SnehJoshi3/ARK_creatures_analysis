import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="ARK Creature Dashboard", layout="wide")
st.title("🦕 ARK: Survival Evolved - Creature Analytics")

@st.cache_data
def load_data():
    return pd.read_csv("ARK_dino.csv")

df = load_data()

st.sidebar.header("Filter Data")

rideable_filter = st.sidebar.multiselect(
    "Rideable Status:",
    options=df["RideableRide"].unique(),
    default=df["RideableRide"].unique()
)

diet_filter = st.sidebar.multiselect(
    "Select Diet:",
    options=df["Diet"].unique(),
    default=df["Diet"].unique()
)


filtered_df = df[
    (df["RideableRide"].isin(rideable_filter)) & 
    (df["Diet"].isin(diet_filter))
]


col1, col2, col3 = st.columns(3)
col1.metric("Total Creatures Displayed", len(filtered_df))
col2.metric("Most Common Diet", filtered_df["Diet"].mode()[0] if not filtered_df.empty else "N/A")
col3.metric("Most Common Temperament", filtered_df["Temperament"].mode()[0] if not filtered_df.empty else "N/A")

st.subheader("⭐ Personal Hall of Fame (and Shame)")
fav_col1, fav_col2, fav_col3, fav_col4 = st.columns(4)

fav_col1.metric(label="🌿 Favorite Herbivore", value="Stegosaurus")
fav_col2.metric(label="🥩 Favorite Carnivore", value="Sabertooth")
fav_col3.metric(label="🏔️ Special Mention", value="Titanosaur")
fav_col4.metric(label="🦟 I Hate This Thing", value="Rhyniognatha")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Diet Distribution")
    fig_diet = px.pie(
        filtered_df, 
        names="Diet", 
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_diet, use_container_width=True)

with chart_col2:
    st.subheader("Temperament Breakdown")
    temp_counts = filtered_df["Temperament"].value_counts().reset_index()
    temp_counts.columns = ["Temperament", "Count"]
    fig_temp = px.bar(
        temp_counts.head(10), 
        x="Count", 
        y="Temperament", 
        orientation="h",
        color="Count",
        color_continuous_scale="Reds"
    )
    fig_temp.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig_temp, use_container_width=True)


st.subheader("Filtered Creature Data")
st.dataframe(df, hide_index=True, use_container_width=True)
