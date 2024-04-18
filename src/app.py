import streamlit as st


#logic to get user input 
def get_responce(user_input):
    return "I don't know"


#app config 
st.set_page_config(page_title="Chat with websites", page_icon="🤖")
st.title("Chat with websites")
chat_history = [
    {
        #add langchain schemas
    }
]

# sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

#user input
user_query = st.chat_input("type your message here...")
if user_query is not None and user_query != "":
    responce = get_responce(user_query)
    with st.chat_message("Human"):
        st.write(user_query)
    with st.chat_message("AI"):
        st.write(responce)

