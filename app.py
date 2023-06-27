import streamlit as st
import openai

st.sidebar.image("ali-removebg-preview.png", width=150)
openai.api_key = st.secrets['pass']

# st.sidebar.header("Summaries text to understand easily 5 years old.")
# artical_text = st.sidebar.text_area("Enter you text")

# if len(artical_text) > 20:
#     if st.sidebar.button("Generate Summary"):
#         response = openai.Completion.create(
#             engine="text-davinci-003",
#             prompt="Please summaries this sentence in a simple way that can easily understand 5 years old :" + artical_text,
#             temperature=0.5,
#             max_tokens=2000,
#         )
#         res = response['choices'][0]['text']
#         st.info(res)

@st.cache_data()
def generate_summary(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Please summaries this sentence in detail way that can understand easily 5 years old :" + text,
        max_tokens=3000,
        temperature=0.5,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=None,
        n=1
    )
    summary = response.choices[0].text.strip()
    return summary

def main():
    st.sidebar.title("Text Summarizer for 5-Year-Olds")
    st.sidebar.title("Text Summarizer")
    st.sidebar.write("Enter a piece of text and I'll generate a simplified summary!")

    user_input = st.sidebar.text_area("Enter your text here")

    if st.sidebar.button("Generate explanation detail"):
        if user_input:
            summary = generate_summary(user_input)
            st.sidebar.subheader("Explanation:")
            st.sidebar.write(summary)
        else:
            st.write("Please enter some text.")

if __name__ == "__main__":
    main()

import streamlit as st
from PyPDF2 import PdfReader

def read_pdf(file):
    pdf_reader = PdfReader(file)
    num_pages = len(pdf_reader.pages)
    text = ""
    for page in range(num_pages):
        text += pdf_reader.pages[page].extract_text()
    return text

def main():
    st.title("PDF Viewer")

    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        pdf_text = read_pdf(uploaded_file)

        # CSS styling to change font size and font family
        st.markdown(
            """
            <style>
            .pdf-text {
                font-size: 16px;
                font-family: Times New Roman;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Display PDF text with font size and font family
        st.subheader("PDF Text:")
        st.markdown(f"<div class='pdf-text'>{pdf_text}</div>", unsafe_allow_html=True)

        st.subheader("PDF Viewer:")
        st.write(uploaded_file)

if __name__ == "__main__":
    main()


