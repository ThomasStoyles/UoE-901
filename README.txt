README 

Within this GitLab you will find all experiments conducted for the MSc project conducted. Before we begin, please make sure you have python3 installed and have downloaded the requirements.txt. 
You will also need to have Ollama installed you can do this by going to: https://ollama.com

Once Ollama is installed you will need to pull the required models from the ollama library. These models are...
- Llama3
- Solar
- Phi3
- Mistral

To do this you can use the following code in the terminal of your IED: ollama pull MODELNAMEHERE 

If you get stuck, then please see the models page on the ollama website here: https://ollama.com/library which will explain further.

For Experiment1.ipynb you will need to have the llama3 bin files downloaded. These are attached to the GitLab however if you cannot pull them then you can download them from this website:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

The models used are:
- llama-2-7b-chat.ggmlv3.q4_K_S.bin
- llama-2-7b-chat.ggmlv3.q3_K_S.bin
- llama-2-7b-chat.ggmlv3.q5_K_S.bin
- llama-2-7b-chat.ggmlv3.q8_0.bin


Experiment1.ipynb 

Experiment1.ipynb is the first Jupyter Notebook that was designed. It demonstrates a pipeline for loading text documents, processing them,
and querying a language model, in this case LLaMA-2 to generate responses based on the content of those documents using RAG. The questions/queries will 
be asked by the user on mental health.

Structure

Library Imports
Essential libraries for document processing, embedding creation, and language modelling are imported, please ensure that you have installed the requiremetns.txt file

Data Loading
Text documents are loaded from a specified directory using a custom UTF8TextLoader. The documents are then split into chunks for easier processing and embedding.

Model and Embedding Setup:
Text embeddings are created using the HuggingFaceEmbeddings model.
A FAISS vector store is employed to store and retrieve these embeddings.
A language model is initialized and configured to handle the retrieval of relevant documents and answer questions.

Query Function:
The query function is designed to input a question from the user and process it with the model. This will return a response along with the source document. 

Editing the model 
To edit the model, you will first need to change the model type in the third cell in the notebook. This experiment only works with llama2 bin files so you will need the bin file downloaded
and in the same place as the Experiment1.ipynb file. If you wish to add addition text files to the infomation that the model can read, then you can add the text file you wish to add to the same 
place as all the other text files, you will need to rerun the whole notebook to make sure that the new text file is processed. You will also need to change the loader variable in the second cell 
of the notebook, currently it is reading from the default loading area of the notebook however if you run into any issues you will need to change the location of the variable to where you have stored
the text files. 

Experiment1 was the baseline for all other experiment files therefore unless stated otherwise assume that the structure is the same for all experiments


Experiment2.ipynb 

Overview
Experiment2.ipynb builds upon the functionality demonstrated in Experiment1.ipynb, with key modifications in the language model used, stated in the report as well as additional preprocessing 
steps. The notebook is tailored for users interested in experimenting with different Ollama models and parameter-tuning prompt structures for improved performance in RAG question-answering tasks.

Differences

Model and Embedding Setup:
Embeddings are created with the HuggingFaceEmbeddings model.
FAISS vector store is used for storing and querying embeddings.
The Ollama language model is employed with a specific configuration.

Prompt Template:
A prompt template is defined to structure the input to the language model, enhancing the quality of the generated responses.

Query Function:
A token truncation function is introduced to ensure that inputs to the language model are within the allowed token limit.

Editing the model 
To edit the model, you will first need to install the Ollama model you wish to use. You can do this by using the Ollama pull function as stated above. You will also need to change the loader 
variable of the notebook, currently it is reading from the default loading area of the notebook however if you run into any issues you will need to change the location of the variable to were 
you have stored the text files. You will also need to change the directory_path variable to your directory.


Experiment3_AllDocsPrint.ipynb

Experiment3_AllDocsPrint.ipynb is used to print all the documents that the models read to make sure that the program is correctly reading information from multiple text files. This allows us 
to test questions that will have information in more than one text file and ensure the model is reading these documents to present an answer.


Experiment3_chunkTest.ipynb

Experiment3_chunkTest.ipynb like Experiment3_AllDocsPrint.ipynb is used to print all the chunks that the models read to make sure that the program is correctly following the RAG system 
implemented and that the chunks are loading correctly to the model.


Experiment3_Tokens.ipynb

Experiment3_Tokens.ipynb is used to test the model under different token amounts. This allowed me to experiment with the token amount that the model had access to, checking if 
the token amount would change the response given to the model. This also allowed me to find the most optimal token count for the model.


Experiment3_Comparision.ipynb

Experiment3_Comparision.ipynb is used to test llama3 and llama3.1, this notebook shows the user 2 responses without knowing which model is what. You then choose the best response to the
question to reveal the model which has given the better response. This prevents any bias from the user and allows for the best model to be the one that gives advice.
