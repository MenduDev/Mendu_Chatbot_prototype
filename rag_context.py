import pandas as pd
import faiss
import numpy as np
from numpy.linalg import norm
from transformers import AutoModel

user_name = 'Jill'
guideline_path = './data/Mental_Health_FAQ.csv'
past_conversation_path = "./data/transcript2"
embedding_model_name = 'jinaai/jina-embeddings-v2-small-en'
embedding_model = AutoModel.from_pretrained(embedding_model_name, trust_remote_code=True)

def save_embeddings(data, embedding_model):
    '''Save the embeddings to disk'''
    # cos_sim = lambda a,b: (a @ b.T) / (norm(a)*norm(b))
    # tokenizer = AutoTokenizer.from_pretrained(embedding_model)
    model = AutoModel.from_pretrained(embedding_model, trust_remote_code=True) # trust_remote_code is needed to use the encode method
    embeddings = model.encode(data)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    # save the embeddings to disk
    return faiss.write_index(index, "embeddings.index") 

def load_data(guideline_path, past_conversation_path, user_name):
    '''Load the guideline and past conversation'''
    ## Load the general guideline from a.csv file
    qa_df = pd.read_csv(guideline_path)

    # Select the question and answer columns
    df = qa_df
    selected_columns = df.iloc[:, [1, 2]]
    combined_columns = selected_columns.apply(lambda x: ''.join(x), axis=1)
    row_list = combined_columns.tolist()

    ## load client information, past conversation, and process the conversation
    with open(past_conversation_path, "r") as file:
        file_content = file.read()

    # Replace client with Jill
    updated_content = file_content.replace('client', user_name).replace('\n', ' ').replace('\t', ' ')

    # Split the content into general information and dialogues
    dialogues = updated_content.split('Therapist:')
    user_background, dialogues = [dialogues[0]], dialogues[1:]

    # Process each dialogue
    processed_dialogues = []
    for dialogue in dialogues:
        parts = dialogue.split('Jill:')
        for part in parts:
            processed_dialogues.append('Therapist:' + part if part.startswith(' ') else 'Jill:' + part)

    ## concatenate all contents 
    combined_infos = row_list + processed_dialogues
    return user_background, combined_infos

def retrieve_similar_sentences(query, index, k=3, filter_distance=41, model = embedding_model):
    query_embedding = model.encode(f'{query}')
    if len(query_embedding.shape) == 1:
        query_embedding = query_embedding.reshape(1, -1)
    D, I = index.search(query_embedding, k)
    
    # Filter out indices with distance greater than 41
    filtered_indices = [I[0][i] for i in range(len(D[0])) if D[0][i] < filter_distance]
    filtered_distances = [D[0][i] for i in range(len(D[0])) if D[0][i] < filter_distance]
    return filtered_distances, filtered_indices

if __name__ == '__main__':
    # Load the data
    user_background, combined_infos = load_data(guideline_path, past_conversation_path, user_name)

    # Save the embeddings
    save_embeddings(combined_infos, embedding_model)
