# Mendu mental health CBD Chatbot with 'memory' function.

## Features
The chatbot is able to answer user specific questions using RAG (retrieval augmented generator) by pulling and retrieving user specific data, general mental health guideline and past user conversations.
It has a contexual windows of 4090 tokens (gpt3.5-turbo). Thats roughly 200 sentences. Assuming a single therapy conversation lasts around 60-100 sentences, this contexual windows should be okay for most cases. 

## Underlying technology
- Uses Openai gpt3.5 for natural language ability. 
- Pull user/patient information for .csv or txt files, clean and merges them,
- uses the Jinai embedding to embedd the textual information (jinaai/jina-embedding-s-en-v1)
- uses FAISS to index and retrieval

## Installation
1. install python / conda
2. recommended: create a new conda environment
3. go to the folder of the chatbot where requirement.txt is located. Inside terminal, pip install -r requirements.txt
4. python main.py to start 




to do:
- implement a vector datbase for storage of all textual content (user data, conversations, guidelines)
- implement conversation summary tool to work around the 4090 token limitation
- implemenation of 'Demi Flow' for a more hardcoded responses from the chatbot




