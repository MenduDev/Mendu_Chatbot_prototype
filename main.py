print('System Loading...')

from dotenv import load_dotenv
import os
from openai import OpenAI
import faiss
from rag_context import retrieve_similar_sentences, load_data

gpt3 = 'gpt-3.5-turbo-0301'
gpt4 = 'gpt-4-1106-preview'
def ask(question: str, chat_log: list, model=gpt3, temp=0.9):

    if not chat_log:
        messages = [{'role': 'system', 'content': system_updated},
                    {'role': 'assistant', 'content': start_message}]
    else:
        # chat_log.append({'role': 'user', 'content': question})
        messages = chat_log    

    # Retrieve similar sentences
    _, similar_indices = retrieve_similar_sentences(question, index)
    if similar_indices:
        retrieval_content = ' '.join(
            [f'{combined_infos[idx]}' for idx in similar_indices]
        )
        messages.append({'role': 'system', 'content': retrieval_content})
    
    messages.append({'role': 'user', 'content': question})

    response = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temp,
    )
        
    answer = response.choices[0].message.content

    # remove the role system content from retrieval
    if similar_indices:
        messages.pop(-2)
    
    messages.append({'role': 'assistant', 'content': answer})

    # print(sum(len(message['content']) for message in messages))

    return str(answer), messages


if __name__ == '__main__':
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    load_dotenv()
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    client = OpenAI(api_key=openai_api_key)

    index_path = './embeddings.index'

    # load the guideline and past conversation
    user_name = 'Jill'
    guideline_path = './data/Mental_Health_FAQ.csv'
    past_conversation_path = "./data/transcript2"
    # Load the data
    index = faiss.read_index(index_path)
    user_background, combined_infos = load_data(guideline_path, past_conversation_path, user_name)
    print('User data has been loaded successfully!')
    print('Mendu Chat is ready to chat with you! Type "quit" to exit.')
    print('----------------------------------------------')
    # system definition and start message
    system = 'You are a skillful and empathetic AI \
            therapist named Mendu Chat who practices Cognitive Behavioral Therapy (CBT) to help her clients. \
            You help your clients identify and change \
            the irrational thoughts and beliefs that are causing them to suffer. \
            You also help them learn and practice coping skills to help them \
            better manage their stress and anxiety.'

    system_updated = f'{system} Information of your patient: {user_background[0]}'

    start_message = 'This is the Mendu Chat. How are you feeling today?'

    chat_log = []  # Initialize the chat_log
    print(start_message)

    while True:
        question = input("You: ")
        if question.lower() == 'quit':
            break

        answer, chat_log = ask(question, chat_log)
        print("Mendu Chat:", answer)
