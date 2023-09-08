from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


load_dotenv()

chat_llm = ChatOpenAI(model="gpt-4")
chat_memory = ConversationBufferMemory()
chat = ConversationChain(llm=chat_llm, memory=chat_memory)

def get_ai_response(user_query):
    ai_response = chat(user_query)
    return ai_response["response"]