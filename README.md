# Langchain Chatbot with OpenAI

<p>
This code is an implementation of a chatbot using OpenAI's language model GPT-3.5. The chatbot is trained on a given PDF file and can answer questions related to the contents of the PDF.
</p>

![Screenshot](pdf_bot.png)

## Requirements

<p>
To run this code, you need the following libraries:
</p>
* langchain
* PyPDF2
* gradio
* pickle

You also need to have an OpenAI API key to access the GPT-3.5 model.

## Usage
1. Install the required libraries.
2. Set your OpenAI API key in the code by replacing `enter your openai api key here` with your actual key.
3. Add the path to the PDF file you want to train the chatbot on by setting the `PdfReader` path to the file's location.
4. Run the code and wait for the chatbot to initialize.
5. Enter your questions or prompts into the text box and hit enter to receive a response from the chatbot.

## Explaination
<p>
This code initializes a chatbot using OpenAI's GPT-3.5 language model to answer questions related to a PDF file. It first extracts the text from the PDF file and splits it into smaller chunks using a **CharacterTextSplitter** object. It then uses the **OpenAIEmbeddings** class to generate embeddings for each chunk of text and stores them using the FAISS library. This allows for efficient similarity searches to be performed when a user inputs a question.
</p>

<p>
The **predict** function is the main function that is called when the user inputs a question. It first performs a similarity search on the text chunks using the FAISS index and returns the top 6 most similar chunks. It then concatenates the input question with the text from the top 6 chunks and sends the resulting string to the chatbot. The chatbot generates a response, which is then returned to the user.
</p>

<p>
The **gradio** library is used to create a simple user interface where the user can input questions and receive responses from the chatbot.
</p>

