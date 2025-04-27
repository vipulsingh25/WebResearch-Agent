import streamlit as st
from app.agent import run_research_pipeline

st.set_page_config(page_title="Web Research Agent", layout="wide")
st.title("🌐 Web Research Agent")

query = st.text_input("Enter your research query:", "Latest AI hiring trends in 2025")

if st.button("Run Research"):
    with st.spinner("Processing your query... please wait."):
        summary = run_research_pipeline(query)

    st.markdown("## 🔍 Research Summary")
    st.write(summary)
