import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import pickle
import gradio as gr


os.environ["OPENAI_API_KEY"] = "enter your openai api key here"
chat = ChatOpenAI(temperature=0)

'''Add the path to pickle file containing embedding '''
with open("/Users/shashankvats/projects_openai/Langchain/langchain/gpt-4.pkl", 'rb') as f: 
    faiss_index = pickle.load(f)

message_history = []

def predict(input):
    '''Find the k best matched chunks to the queried test. 
    These will be the context over which our bot will try to answer the question.
    The value of k can be adjusted so as to get the embeddings for the best n chunks.'''

    docs = faiss_index.similarity_search(input, K = 6)

    main_content = input + "\n\n"
    for doc in docs:
        main_content += doc.page_content + "\n\n"

    message_history.append({"role": "user", "content": f"{input}"})

    messages.append(HumanMessage(content=main_content))
    ai_response = chat(messages).content
    messages.pop()
    messages.append(HumanMessage(content=input))
    messages.append(AIMessage(content=ai_response))

    message_history.append({"role": "assistant", "content": f"{ai_response}"}) 
    
    # get pairs of msg["content"] from message history, skipping the pre-prompt: here.
    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(0, len(message_history)-1, 2)]  # convert to tuples of list
    return response

# creates a new Blocks app and assigns it to the variable demo.
with gr.Blocks() as demo: 

    messages = [
        SystemMessage(
            content="You are a Q&A bot and you will answer all the questions that the user has. If you dont know the answer, output 'Sorry, I dont know' .")
    ]

    # creates a new Chatbot instance and assigns it to the variable chatbot.
    chatbot = gr.Chatbot() 

    # creates a new Row component, which is a container for other components.
    with gr.Row(): 
        '''creates a new Textbox component, which is used to collect user input. 
        The show_label parameter is set to False to hide the label, 
        and the placeholder parameter is set'''
        query = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)
    '''
    sets the submit action of the Textbox to the predict function, 
    which takes the input from the Textbox, the chatbot instance, 
    and the state instance as arguments. 
    This function processes the input and generates a response from the chatbot, 
    which is displayed in the output area.'''
    query.submit(predict, query, chatbot) # submit(function, input, output)
    #txt.submit(lambda :"", None, txt)  #Sets submit action to lambda function that returns empty string 

    '''
    sets the submit action of the Textbox to a JavaScript function that returns an empty string. 
    This line is equivalent to the commented out line above, but uses a different implementation. 
    The _js parameter is used to pass a JavaScript function to the submit method.'''
    query.submit(None, None, query, _js="() => {''}") # No function, no input to that function, submit action to textbox is a js function that returns empty string, so it clears immediately.
         
demo.launch()
