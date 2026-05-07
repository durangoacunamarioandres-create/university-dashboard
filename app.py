import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="University Dashboard", layout="wide")
st.title("University Student Data Dashboard")

df = pd.read_csv("university_student_data.csv")

st.sidebar.header("Filters")

year = st.sidebar.selectbox("Select Year", df["Year"].unique())
term = st.sidebar.selectbox("Select Term", df["Term"].unique())

filtered_df = df[(df["Year"] == year) & (df["Term"] == term)]

col1, col2, col3 = st.columns(3)

retention = filtered_df["Retention Rate (%)"].mean()
satisfaction = filtered_df["Student Satisfaction (%)"].mean()
enrolled = filtered_df["Enrolled"].sum()

col1.metric("Retention Rate", f"{retention:.2f}%")
col2.metric("Satisfaction", f"{satisfaction:.2f}%")
col3.metric("Enrolled Students", enrolled)

st.subheader("Retention Rate Trend Over Time")
retention_trend = df.groupby("Year")["Retention Rate (%)"].mean().reset_index()
fig1, ax1 = plt.subplots()
sns.lineplot(data=retention_trend, x="Year", y="Retention Rate (%)", marker='o', ax=ax1)
st.pyplot(fig1)

st.subheader("Student Satisfaction by Year")
satisfaction_trend = df.groupby("Year")["Student Satisfaction (%)"].mean().reset_index()
fig2, ax2 = plt.subplots()
sns.barplot(data=satisfaction_trend, x="Year", y="Student Satisfaction (%)", ax=ax2)
st.pyplot(fig2)

st.subheader("Retention Rate: Spring vs Fall")
term_data = df.groupby("Term")["Retention Rate (%)"].mean().reset_index()
fig3, ax3 = plt.subplots()
sns.barplot(data=term_data, x="Term", y="Retention Rate (%)", ax=ax3)
st.pyplot(fig3)

st.subheader("Filtered Data")
st.dataframe(filtered_df)