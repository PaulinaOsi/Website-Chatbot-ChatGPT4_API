import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


#logic to get user input 
def get_responce(user_input):
    return "I don't know"

def get_vectorstore_from_url(url):
    loader = WebBaseLoader(url)
    document = loader.load()
    #split document into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)
    return document_chunks


#app config 
st.set_page_config(page_title="Chat with websites", page_icon="🤖")
st.title("Chat with websites")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
    #add langchain schemas
    AIMessage(content='Hello, I am bot, how can i help you?'),
]

# sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("WebsitURL")

if website_url is None or website_url == "":
    st.info("Please enter a website URL")
else:
    document_chunks = get_vectorstore_from_url(website_url)
    with st.sidebar:
        st.write(document_chunks)  

#user input
user_query = st.chat_input("type your message here...")
if user_query is not None and user_query != "":
    responce = get_responce(user_query)
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.chat_history.append(AIMessage(content=responce))


 # conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

