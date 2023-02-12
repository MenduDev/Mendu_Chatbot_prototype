Skip to main content
ase_readme
Advanced Software Engineering 2022/23 
BHT with Prof. Dr. Edlich
mentalHealth_Chatbot
 an AI therapist, based on GPT3, fine-tuned with custom data. 
Table of content
About-the-app

Checklist

Technology

Setup

About the app
The application is a chatbot, acting as a mental health therapist.
The chatbot is powered by GPT3, a powerful large language model by openai. The GUI was realized with the streamlit package.
Fine-tuning had to be done In order to achieve good results for therapeutic purpose. Various sources of data have been accumulated for this task:
scrapping of 28 youtube videos conversations between therapist and client on behaviour therapy, using whisper AI to transcribe the conversations.
https://dl.acm.org/doi/10.1145/3488560.3498509 A manually annotated dataset of approximately 300 therapeutic conversation between patient and therapist
kaggle dataset of 29 prompt and detailed answer on mental health and related topic
the datasets are cleaned, merged and transformed to JSONL format, then pushed via API to the OpenAI server to train a custom model (fine-tuning). Due to cost reasons, fine-tuning was done only on the medium-sized model (curie).
The result can be previewed at huggingface.co/spaces/lsacy/mentalChat
Besides the ability to have a conversation. With the help of two more additional models (Bert based), each conversation can be summarised and evaluated on three sentiment categories (positive, negative, neutral). These information could then be stored in a database and tracked for further analysis.
Checklist
1. Git
For an already exiting project, clone -> add file for example add . for all files or add certain file --> always pull before commit/push -> stash if needed -> push in the end
1
git clone https://www.Github(anyHostingSerivce).com/User/Repo
2
git add .
3
git pull 
4
git stash
5
git commit -m 'commit message'
6
git push
For a new project, one could use git init to initialize a local git repository then on the preferred Git hosting service create a repository and then add the remote origin
1
git init 
2
git remote add origin <remote-repository-url>
3
git push -u origin master/main
4
​
My way of creating a new repo with existing code: create a new empty repository on the host, git clone the empty repository and put all codes into the cloned folder.
use .gitignore to add files to be ignored, so git would not push them (personal api etc)
1
touch .gitignore #create .ignore file
2
vim .gitignore #i 
if more than one people working on the same repository, branches are useful to coordinate the work.
1
git branch #list all branches
2
git checkout -b <newBranch> #create a new branch named newBranch
3
git push --set-upstream origin <newBranch> #pushing the first time
4
git switch/checkout <main> #switch back to main branch
5
git merge <newBranch> #to merge main with files from branch <newBranch>
6
git branch -d <newBranch> #to delete the branch <newBranch>
2. UML
Using PlantUML and LucidChart:
UseCase
flowDiagram
sequenceDiagrame
3. DDD
DDD - Dividing the into 3 domains: Core, Support and Miscellaneous. Core Domain are the core functionality perceived by the user. Support domains contains the functions which enable the core functionalities and miscellaneous domain made of subjects, which are required for an operating company.
4. Metrics
Two different metrics tools have been applied to this project. The first one is universal and cloud enabled: SonarQube. The second one is a python specific cli tool: PyLint.
For Sonarcube the .vscode extension SonarLint was installed and it was checking for inconsistencies while coding. With SonarLint it was very easy to connect to the Sonarqube Cloud, which did a deep dive into my code and checked for additional reliability, security, maintainability and duplications.
Additionally PyLint was used to further checking up the code. Even though Sonarcube didn't find any inconsistencies, PyLint was able to find small issues, which got solved after a few iterations.
5. Clean Code Development
6. Build Management
Python is an interpreter language, nothing needs to be compiled so a build management tool seems unnecessary. Nonetheless for this project I have installed pyBuilder, unfortunately after a successful installation I was not able to properly build something.
So instead of relying on on pyBuilder, I choose to use github Action for continuously integrated building and testing.
7. Unit-Test
Pytest was used for unit testing purpose. I have build a simple test to test two different functions. Both test have passed locally without any issue.
Testing in the Github Action pipeline was unsuccessful, but this was to be expect, since I didn't want to upload my openAI API key.
8. Continuous Delivery
Github Action is used for this project. Compared to Jenkins there is no need to setup for a local server, which saves resources and it has many template pipelines to choose from. Since I already extensively use Github, using Github Action for CI/CD was the reasonable thing to do.
For demonstration purpose, a test branch with a pull request was created and successfully merged.
Next, a YAML file was created for the continuous delivery pipeline. The file states that on push or pull_request each time the jobs of running on a ubuntu-latest server with python 3.8, all dependencies will be installed, Lint test with flake8 will be executed and testing with pytest will be done.
The entire chain of events are successful with the only exception of testing with the reasons stated above. (no API key because its an open repository)
9. IDE-shortcut
My IDE is vsCode. It is lightweight, fast. It has available many plugin and a very functional terminal. Besides, it integrates Jupyter Notebook very well, which is a must have tool for data scientists.
Some of my favorite shortcuts are:
CTRL + O: open a folder / file
F5: open debug mode
CTRL + SHIFT + P: open the command palette to access all available commands based on the current context.
while in Jupyter Notebook mode:
a/b: add a new block above/below current block
SHIFT + ENTER: Run current block, jump to the next block
dd: delete current block
10. DSL Demo
11. Functional Programming
Technology
Python 3.8
Jupyter Notebook for data gathering, data wrangling and fine-tuning upload
PyTube for video scrapping, OpenAI Whisper for transcribing
large language models
Language generation(decoder based model): OpenAI GPT3
Language summarization and sentiment analysis(encoder based model): Huggingface Transformers, bert based models
StreamLit as a web app interface
Setup
access the demo version at https://huggingface.co/spaces/lsacy/mentalChat
Running the code on a local machine:
register and load a custom OpenAI api key, insert the key at line 7 in streamlit_app.py -> openai.api_key = 'your-api-key'
install dependencies:
1
(yourEnv) ~/dir_to_the_chatbot pip install -r requirements.txt
start the program in terminal with:
1
(yourEnv) ~/dir_to_the_chatbot streamlit run streamlit_app.py
Unlinked References

