import streamlit as st
import requests

st.set_page_config(page_title="LLM Email/Resume Rewriter", layout="centered")

st.title("📝 Email or Resume Rewriter")
st.markdown("Rewrite your content in a chosen tone using an LLM.")

input_text = st.text_area("Enter your text:", height=200)
doc_type = st.selectbox("Select type:", ["email", "resume"])
tone = st.selectbox("Select tone:", ["formal", "friendly", "persuasive", "apologetic", "brutal"])

if st.button("Rewrite"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Rewriting..."):
            response = requests.post(
                "http://localhost:8000/rewrite",
                json={"text": input_text, "tone": tone, "type": doc_type}
            )
            if response.status_code == 200:
                st.subheader("🔁 Rewritten Text:")
                st.success(response.json()["rewritten"]["content"])
            else:
                st.error("Error: Could not reach the backend.")
