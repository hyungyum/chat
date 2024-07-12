import streamlit as st
from utils import print_messages
from langchain_core.messages import ChatMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
# Load environment variables
load_dotenv()

st.set_page_config(page_title="chatgpt", page_icon="O")
st.title("chatgpt")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 이전 대화 출력력
print_messages()


if user_input:= st.chat_input("메시지를 입력해 주세요"):
    st.chat_message("user").write(f"{user_input}")
    st.session_state["messages"].append(ChatMessage(role="user", content=user_input))

    # 답변 생성
    prompt = ChatPromptTemplate.from_template(
        """ 질문에 대하여 간결하게 답변해주세요.
        {question}
        """
    )

    chain = prompt | ChatOpenAI()
    response = chain.invoke({"question": user_input}) 
    msg = response.content

    with st.chat_message("assistant"):
        st.write(msg)
        st.session_state["messages"].append(ChatMessage(role="assisant", content=msg))

