import streamlit as st
import cohere

# Initialize Cohere API key
cohere_api_key = '9cXeu16WbLhcKXpfCjJspMsN9WLQY5zEIIaw77BB'  # Replace with your Cohere API key
co = cohere.Client(cohere_api_key)

## Function To get response from Cohere model
def get_cohere_response(input_text, no_words, blog_style):
    # Define the prompt template
    prompt = f"""
        Write a blog for {blog_style} job profile for a topic '{input_text}' within {no_words} words.
    """
    
    # Generate response using Cohere API with command-xlarge model
    response = co.generate(
        model='command-xlarge',  # Use a valid model like 'command-xlarge'
        prompt=prompt,
        max_tokens=500,  # You can adjust the number of tokens based on your required word count
        temperature=0.7  # Controls the creativity of the response
    )
    
    # Extract and return the generated text
    generated_text = response.generations[0].text.strip()
    return generated_text

# Streamlit UI setup
st.set_page_config(page_title="Generate Blogs", page_icon='🤖', layout='centered', initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

# Creating two columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")

# Final response
if submit:
    if input_text and no_words.isdigit():
        st.write(get_cohere_response(input_text, no_words, blog_style))
    else:
        st.write("Please enter valid input values.")