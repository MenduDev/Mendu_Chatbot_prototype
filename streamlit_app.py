import openai
import streamlit as st
from streamlit_chat import message
from transformers import pipeline
summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")
sentiment_task = pipeline("sentiment-analysis", model='cardiffnlp/twitter-roberta-base-sentiment-latest', tokenizer='cardiffnlp/twitter-roberta-base-sentiment-latest')
openai.api_key = st.secrets["openai_api_key"]

from math import log

completion = openai.Completion()


start_prompt = '[Instruction] Act as a friendly, compasionate, insightful, and empathetic AI therapist named Joy. Joy listens and offers advices. End the conversation when the patient wishes to.'
start_message = 'I am Joy, your AI therapist. How are you feeling today?'
start_sequence = "\nJoy:"
restart_sequence = "\n\nPatient:"
  
def ask(question: str, chat_log: str, model='text-davinci-003', temp=0.9) -> (str, str):

  prompt = f'{chat_log}{restart_sequence} {question}{start_sequence}'

  response = completion.create(
      prompt = prompt,
      model = model,
      stop = ["Patient:",'Joy:'],
      temperature = temp, #the higher the more creative
      frequency_penalty = 0.9, #prevents word repetition, larger -> higher penalty
      presence_penalty = 1, #prevents topic repetition, larger -> higher penalty
      top_p =1, 
      best_of=1,
      max_tokens=170
  )
  
  answer = response.choices[0].text.strip()
  log = f'{restart_sequence}{question}{start_sequence}{answer}'
  return str(answer), str(log)

def clean_chat_log(chat_log):
    chat_log = ' '.join(chat_log)
    # find the first /n
    first_newline = chat_log.find('\n')
    chat_log = chat_log[first_newline:]
    # remove all \n
    chat_log = chat_log.replace('\n', ' ')
    return chat_log

def summarize(chat_log):
    chat_log = clean_chat_log(chat_log)
    summary = summarizer(chat_log, max_length=150, do_sample=False)[0]['summary_text']
    return summary

def analyze_sentiment(chat_log):
    # split chat_log into smaller chunks

    # analyze each chunk

    # return the average sentiment


    chat_log = clean_chat_log(chat_log)
    sentiment = sentiment_task(chat_log)
    return sentiment

def remove_backslashN(chat_log: list) -> list:
    chat_log = [i.replace('\n', ' ') for i in chat_log]
    return chat_log



def main():
    st.title("Chat with Joy - the AI therapist!")
    col1, col2 = st.columns(2)
    temp = col1.slider("Bot-Creativeness", 0.0, 1.0, 0.9, 0.1)
    model = col2.selectbox("Model", ["text-davinci-003", "text-curie-001", "curie:ft-personal-2023-02-03-17-06-53"])

    if 'generated' not in st.session_state:
        st.session_state['generated'] = [start_message]
        
    if 'past' not in st.session_state:
        st.session_state['past'] = []

    if 'summary' not in st.session_state:
        st.session_state['summary'] = []

    if 'chat_log' not in st.session_state:
        st.session_state['chat_log'] = [start_prompt+start_sequence+start_message]
        

    if len(st.session_state['generated']) > 2:
        if st.button("Clear and summerize", key='clear'):
            chat_log = clean_chat_log(st.session_state['chat_log'])
            summary = summarizer(chat_log, max_length=100, min_length=30, do_sample=False)
            st.write(summary)
            user_sentiment = st.session_state['past']
            user_sentiment = remove_backslashN(user_sentiment)
            st.write(sentiment_task(user_sentiment))
            st.session_state['generated'] = [start_message]
            st.session_state['past'] = []
            st.session_state['chat_log'] = [start_prompt+start_sequence+start_message]
            st.session_state['summary'] = []

    user_input=st.text_input("You:",key='input')

    if user_input:
        output, chat_log = ask(user_input, st.session_state['chat_log'], model=model, temp=temp)
        st.session_state['chat_log'].append(chat_log)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)
        print(model)
        print(temp)
        print(st.session_state['chat_log'])
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            if i < len(st.session_state['past']):
                message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))



if __name__ == "__main__":
    main()
    # save the user's input and the model's output to the database and analyze the user's input and the model's output

    # if len(st.seesion_state['generated'])  :
        # save the user's input and the model's output to the database
        # analyze the user's input and the model's output
        


        