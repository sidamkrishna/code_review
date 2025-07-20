import streamlit as st
import tempfile
import subprocess
import os
from utils import run_flake8, run_black, run_radon

st.set_page_config(page_title="AI Code Reviewer", layout="wide")
st.title("🧠 AI Code Reviewer")

# Input code
code_input = st.text_area("Paste your Python code here:", height=300)

uploaded_file = st.file_uploader("Or upload a .py file", type=["py"])
if uploaded_file is not None:
    code_input = uploaded_file.read().decode("utf-8")

if st.button("Analyze Code"):
    if not code_input.strip():
        st.warning("Please provide code input.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode='w+') as tmp_file:
            tmp_file.write(code_input)
            tmp_file_path = tmp_file.name

        st.subheader("🔍 Flake8 Style Issues")
        st.code(run_flake8(tmp_file_path), language="text")

        st.subheader("🎨 Black Formatting Suggestions")
        formatted_code, diff = run_black(tmp_file_path)
        st.text("Before:")
        st.code(code_input, language="python")
        st.text("After (Black-formatted):")
        st.code(formatted_code, language="python")

        st.subheader("📊 Radon Complexity Analysis")
        st.code(run_radon(tmp_file_path), language="text")

        os.unlink(tmp_file_path)  # Cleanup temp file
