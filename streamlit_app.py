"""OpenAI GPT-3 Chatbot with Streamlit"""
import openai
import streamlit as st
from streamlit_chat import message
from transformers import pipeline


summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")
sentiment_task = pipeline("sentiment-analysis",
                            model='cardiffnlp/twitter-roberta-base-sentiment-latest',
                            tokenizer='cardiffnlp/twitter-roberta-base-sentiment-latest')

openai.api_key = st.secrets["openai_api_key"]

completion = openai.Completion()

START_PROMPT = '[Instruction] Act as a friendly, compasionate, insightful, and empathetic AI \
                therapist named Joy. Joy listens and offers advices. \
                End the conversation when the patient wishes to.'
START_MESSAGE = 'I am Joy, your AI therapist. How are you feeling today?'
START_SEQUENCE = "\nJoy:"
RESTART_SEQUENCE = "\n\nPatient:"

def ask(question: str, chat_log: str, model='text-davinci-003', temp=0.9) -> (str, str):
    ''' funtion takes a input string and the preview chat_log, 
        returns the model's repsonse/answer and the dialog
        by using the preview chat_log, gold fish memory effect can be prevented,
        the chat_log is used to summarize and analyze the sentiment of the user's input '''

    prompt = f'{chat_log}{RESTART_SEQUENCE} {question}{START_SEQUENCE}'
    response = completion.create(
        prompt = prompt,
        model = model,
        stop = ["Patient:",'Joy:'],
        temperature = temp, #the higher the more creative
        frequency_penalty = 0.9, #prevents word repetition, larger -> higher penalty
        presence_penalty = 1, #prevents topic repetition, larger -> higher penalty
        top_p =1,
        best_of=1,
        max_tokens=170,
        )

    answer = response.choices[0].text.strip()
    log = f'{RESTART_SEQUENCE}{question}{START_SEQUENCE}{answer}'
    return str(answer), str(log)

def clean_chat_log(chat_log: list) -> str:
    ''' cleans the chat log to be used for summarization and sentiment analysis '''

    chat_log = ' '.join(chat_log)
    # find the first /n
    first_newline = chat_log.find('\n')
    chat_log = chat_log[first_newline:]
    # remove all \n
    chat_log = chat_log.replace('\n', ' ')
    return chat_log

def summarize(chat_log: list) -> str:
    ''' returns a summary of the chat log '''

    chat_log = clean_chat_log(chat_log)
    summary = summarizer(chat_log, do_sample=False)[0]['summary_text']
    return summary

def analyze_sentiment(user_input: list) -> str:
    ''' returns user sentiment based on the users input'''

    user_input = clean_chat_log(user_input)
    summary = summarizer(user_input, do_sample=False)[0]['summary_text']
    sentiment = sentiment_task(summary)
    return sentiment

def remove_backslash(chat_log: list) -> list:
    ''' removes the backslash from the chat log '''

    chat_log = [i.replace('\n', ' ') for i in chat_log]
    return chat_log



def main():
    ''' main function '''

    st.title("Chat with Joy - the AI therapist!")
    col1, col2 = st.columns(2)
    temp = col1.slider("Bot-Creativeness", 0.0, 1.0, 0.9, 0.1)
    model = col2.selectbox("Model", ["text-davinci-003",
    "text-curie-001", "curie:ft-personal-2023-02-03-17-06-53"])

    if 'generated' not in st.session_state:
        st.session_state['generated'] = [START_MESSAGE]

    if 'past' not in st.session_state:
        st.session_state['past'] = []

    if 'summary' not in st.session_state:
        st.session_state['summary'] = []

    if 'chat_log' not in st.session_state:
        st.session_state['chat_log'] = [START_PROMPT+START_SEQUENCE+START_MESSAGE]


    if len(st.session_state['generated']) > 2:
        if st.button("Clear and summerize", key='clear'):
            chat_log = clean_chat_log(st.session_state['chat_log'])
            summary = summarizer(chat_log, max_length=100, min_length=30, do_sample=False)
            st.write(summary)
            user_sentiment = st.session_state['past']
            user_sentiment = remove_backslash(user_sentiment)
            st.write(analyze_sentiment(user_sentiment))
            st.session_state['generated'] = [START_MESSAGE]
            st.session_state['past'] = []
            st.session_state['chat_log'] = [START_PROMPT+START_SEQUENCE+START_MESSAGE]
            st.session_state['summary'] = []

    user_input=st.text_input("You:",key='input')

    if user_input:
        output, chat_log = ask(user_input, st.session_state['chat_log'], model=model, temp=temp)
        st.session_state['chat_log'].append(chat_log)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            if i < len(st.session_state['past']):
                message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))



if __name__ == "__main__":
    main()
