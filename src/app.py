import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage


#logic to get user input 
def get_responce(user_input):
    return "I don't know"


#app config 
st.set_page_config(page_title="Chat with websites", page_icon="🤖")
st.title("Chat with websites")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
    #add langchain schemas
    AIMessage(content='Hello, I am bot, how can i help uou?'),
]

# sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

#user input
user_query = st.chat_input("type your message here...")
if user_query is not None and user_query != "":
    responce = get_responce(user_query)
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.chat_history.append(AIMessage(content=responce))

with st.sidebar:
    st.write( st.session_state.chat_history)


 # conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

