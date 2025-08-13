from langchain.agents import initialize_agent, AgentType
from langchain_ollama import ChatOllama
from menu_tool import get_menu_tool
from rag import rag_tool

model = ChatOllama(
    model="llama3.2",
    temperature=0.0,   # avoid hallucinations
    max_tokens=300,    # concise responses
    top_p=0.9,
)

tools=[get_menu_tool, rag_tool]

def create_agent():
    """
    Create a LangChain agent for restaurant assistance.
    """
    agent = initialize_agent(
    llm=model,
    tools=tools,
    agent_type=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=3,
    early_stopping_method='generate',
    #return_intermediate_steps=False,
    prompt="""
    You are a helpful restaurant assistant designed to answer questions about food and the menu.  

    **Tools Available:**  
    1. **Menu Tool** – Provides details about the restaurant's menu (items, ingredients, prices, etc.).  
    2. **RAG Tool** – Answers general food-related questions. If the answer isn't in its database, it searches the web.  

    **Rules:**  
    - Use the **Menu Tool** for questions about the restaurant's menu (e.g., "What desserts do you offer?").  
    - Use the **RAG Tool** only for general food-related queries (e.g., "Is sushi healthy?").  
    - If the RAG Tool detects an **out-of-scope question** (non-food-related), politely respond:  
    *"I can only assist with food-related or menu-related questions. Could you ask about food or our menu instead?"*  
    - **Do NOT answer** non-food questions, take orders, or make reservations.  
    - If a tool lacks information, say: *"I couldn't find that information. Could you clarify or ask something else?"*
    """  
    )

    return agent

# Example usage of the agent
if __name__ == "__main__":

    agent = create_agent()

    input_text = "Show me the full menu."
    response = agent.invoke(input_text, return_final_answer=True)
    print(response.get("output") if response else "No response received.")

