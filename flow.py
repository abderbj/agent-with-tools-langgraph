# 1. Bring in dependencies 
from typing import Annotated 
from langgraph.graph import START, END, StateGraph
from langgraph.graph.message import add_messages 
from langgraph.checkpoint.memory import InMemorySaver 
from langchain_ollama import ChatOllama
from colorama import Fore
import sys 

# 2. Create LLM
try:
    llm = ChatOllama(model='llama3.2')
except Exception as e:
    print(f"Error connecting to Ollama: {e}")
    print("Make sure Ollama is running with: ollama serve")
    print("And the model is available with: ollama pull llama3.2")
    sys.exit(1)


# 3. Create state
class State(dict): 
    messages: Annotated[list, add_messages]
# 4. Build LLM node 
def chatbot(state:State): 
    print(state['messages'])
    return {"messages":[llm.invoke(state['messages'])]}

# 5. Assemble Graph 
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
# 12. Update graph for Tools
graph_builder.add_edge("chatbot", END)
# 6. Add Memory and Compile Graph 
memory = InMemorySaver() 
graph = graph_builder.compile(checkpointer=memory)
# 7. Build call loop and run it
if __name__ == '__main__': 
    print("🤖 Customer Support Bot is ready! Type 'quit' to exit.")
    while True: 
        try:
            prompt = input("🤖 Pass your prompt here: ")
            if prompt.lower() in ['quit', 'exit', 'bye']:
                print("👋 Goodbye!")
                break
            result = graph.invoke({"messages":[{"role":"user", "content":prompt}]}, config={"configurable":{"thread_id":1234}})
            print(Fore.LIGHTYELLOW_EX + result['messages'][-1].content + Fore.RESET)
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Make sure Ollama is running and the model is available.") 

