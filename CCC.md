Personal Clean Code Cheat Sheet (Leonhard Liu):

1. Use descriptive and meaningful variable and function names.
2. Avoid using global variables as much as possible.
3. Keep your functions short and focused on doing one thing.
4. Use docstrings to describe your functions and modules.
5. Use comments to explain any complicated code or edge cases.
6. Avoid deeply nested loops and conditionals.
7. Use list comprehensions and generator expressions instead of loops where possible.
8. Write unit tests for your functions.
9. Use meaningful and consistent formatting to improve readability.
10. Follow PEP 8 style guidelines.

Demonstration of usage with my own code:

1. meaningful variable names: [api_key](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/streamlit_app.py#L15), [START_PROMPT](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/streamlit_app.py#L19) etc. 
2. short function which do one thing: the [`remove_backslash()`](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/streamlit_app.py#L76) function is short.
   It only removes backslash in a list of strings.
3. Use doctrings: Every function has its own docstring. [example](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/streamlit_app.py#L27-L30)
4. Avoid deeply nested loops and conditionals: There is no deeply nested loops. Maximum 2 layers.
   [list comprehensions](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/streamlit_app.py#L79) are also used.
5. write unit test: [unit testing](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/test_sample.py) has been written and executed.
