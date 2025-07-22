import streamlit as st
import requests
import time


st.set_page_config(page_title="Persona-Driven Document Intelligence", layout="wide")

st.markdown("""
    <style>
        body {
            background-color: #282c34; /* Darker background */
            color: #abb2bf; /* Lighter, less harsh text */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Modern font */
        }
        .stTextInput>div>div>input {
            font-size: 16px;
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #61afef; /* Softer blue */
            background-color: #3e4451; /* Darker input background */
            color: #d1d5db; /* Light gray input text */
        }
        .stButton>button {
            background-color: #61afef; /* Softer blue button */
            color: #ffffff;
            font-size: 18px;
            font-weight: bold;
            padding: 12px 28px;
            border-radius: 8px;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background-color: #569cd6; /* Slightly darker on hover */
            transform: translateY(-2px);
        }
        .stMarkdown, .stSubheader {
            color: #e06c75; /* Soft red for headers */
            font-weight: bold;
        }
        .summary-section {
            background-color: #3e4451;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            border-left: 5px solid #61afef;
        }
        .section-title {
            color: #61afef;
            font-size: 24px;
            margin-bottom: 15px;
        }
        .section-content {
            color: #d1d5db;
            font-size: 16px;
            line-height: 1.6;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Persona-Driven Document Intelligence")
st.markdown("Connecting What Matters - For The User Who Matters")

status_placeholder = st.empty()

def format_section(title, content):
    """Format a section of the summary with consistent styling"""
    return f"""
    <div class="summary-section">
        <div class="section-title">{title}</div>
        <div class="section-content">{content}</div>
    </div>
    """


uploaded_file = st.file_uploader("Upload a local PDF", type="pdf")

if st.button("Analyze PDF"):
    if uploaded_file:
        with st.spinner("Processing..."):
            status_placeholder.info("Uploading and analyzing the document...")

            try:
                response = requests.post(
                    "http://localhost:8000/summarize_local/",
                    files={"file": uploaded_file.getvalue()},
                    timeout=3600
                )

                if response.status_code == 200:
                    data = response.json()
                    if "error" in data:
                        status_placeholder.error(f"{data['error']}")
                    else:
                        summary = data.get("analysis", "No analysis generated.")
                        status_placeholder.success("Analysis Ready!")
                        st.text_area("📜 Analysis", summary, height=400)
                        st.download_button("⬇️ Download Analysis", summary, "summary.md")
                else:
                    status_placeholder.error("Server error.")
            except Exception as e:
                status_placeholder.error(f"Error: {str(e)}")
    else:
        status_placeholder.warning("Please upload a PDF file.")


st.markdown("---")
st.markdown("""
###
- Processing typically takes 3-5 minutes depending on pdf size
- The analysis is structured into key sections for better readability
- You can download the analysis as a markdown file
""")
