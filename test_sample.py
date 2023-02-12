import pytest
from streamlit_app import ask, clean_chat_log

def test_ask():
    question = "What's your name?"
    chat_log = ""
    model = 'text-davinci-003'
    temp = 0.9

    answer, log = ask(question, chat_log, model, temp)

    assert isinstance(answer, str)
    assert isinstance(log, str)

def test_clean_chat_log():
    # Test case 1
    input_chat_log = ['hello', 'world\n', 'how', 'are', 'you\n']
    expected_output = '  how are you '
    assert clean_chat_log(input_chat_log) == expected_output

    # Test case 2
    input_chat_log = ['\n', 'this', 'is', 'a', 'new', 'line\n', '\n']
    expected_output = '  this is a new line   '
    output = clean_chat_log(input_chat_log)
    assert output == expected_output
    assert isinstance(output, str)

