from langchain.agents import initialize_agent, AgentType
from rag import load_llm_model
from menu_tool import get_menu_tool
from rag import rag_tool

# Create a LangChain agent
def create_agent():
    """
    Initializes and returns a LangChain agent with the specified tools.
    """
    tools = [get_menu_tool, rag_tool]
    
    # Initialize the agent with the LLM and tools
    agent = initialize_agent(
        tools=tools,
        llm=load_llm_model(),
        agent_type=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True
    )
    
    return agent

# Example usage of the agent
if __name__ == "__main__":
    agent = create_agent()
    print(agent.invoke("Show me the full menu."))