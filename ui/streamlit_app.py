import streamlit as st
from search.semantic_search import SemanticSearch

st.title("Semantic Document Search")

query = st.text_input("Search")

if query:

    results = ["Document result example"]

    for r in results:
        st.write(r)
