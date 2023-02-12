# Advanced Software Engineering 2022/23
### BHT with Prof. Dr. Edlich
# mentalHealth_Chatbot
<h3> an AI therapist, based on GPT3, fine-tuned with custom data. </h3>

## Table of content
* [About the App]
* [Checklist]
* [Technology]
* [local Setup]

## About the app
The [application](https://huggingface.co/spaces/lsacy/mentalChat) is a chatbot, acting as a mental health therapist.
The chatbot is powered by GPT3, a powerful large language model by [openai](https://www.openai.com). The GUI was realized with the [streamlit](https://www.streamlit.io) package.

Fine-tuning had to be done In order to achieve good results for therapeutic purpose. Various sources of data have been accumulated for this task:
* scrapping of 28 youtube videos conversations between therapist and client on behaviour therapy, using [whisper AI](https://openai.com/blog/whisper/) to transcribe the conversations.
* https://dl.acm.org/doi/10.1145/3488560.3498509 A manually annotated dataset of approximately 300 therapeutic conversation between patient and therapist
* [kaggle dataset](https://www.kaggle.com/datasets/narendrageek/mental-health-faq-for-chatbot) of 29 prompt and detailed answer on mental health and related topic

the datasets are cleaned, merged and transformed to JSONL format, then pushed via API to the OpenAI server to train a custom model (fine-tuning). Due to cost reasons, fine-tuning was done only on the medium-sized model (curie).

The result can be previewed at [huggingface.co/spaces/lsacy/mentalChat](https://huggingface.co/spaces/lsacy/mentalChat)

Besides the ability to have a conversation. With the help of two more additional models (Bert based), each conversation can be summarised and evaluated on three sentiment categories (positive, negative, neutral). These information could then be stored in a database and tracked for further analysis.

## Checklist
<b>1. Git</b>
For an already exiting project, clone -> add file for example add . for all files or add certain file --> always pull before commit/push -> stash if needed -> push in the end
```
	  git clone https://www.Github(anyHostingSerivce).com/User/Repo
	  git add .
	  git pull 
	  git stash
	  git commit -m 'commit message'
	  git push
```
For a new project, one could use git init to initialize a local git repository then on the preferred Git hosting service create a repository and then add the remote origin
```
	  git init 
	  git remote add origin <remote-repository-url>
	  git push -u origin master/main
	  
```
My way of creating a new repo with existing code: create a new empty repository on the host, git clone the empty repository and put all codes into the cloned folder.
use .gitignore to add files to be ignored, so git would not push them (personal api etc)
```
	  touch .gitignore #create .ignore file
	  vim .gitignore #i 
```
if more than one people working on the same repository, branches are useful to coordinate the work.
```
	  git branch #list all branches
	  git checkout -b <newBranch> #create a new branch named newBranch
	  git push --set-upstream origin <newBranch> #pushing the first time
	  git switch/checkout <main> #switch back to main branch
	  git merge <newBranch> #to merge main with files from branch <newBranch>
	  git branch -d <newBranch> #to delete the branch <newBranch>
``` 
<br/>
<b>2. UML</b>

Using PlantUML and LucidChart:  
* [UseCase](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/uml/UseCase.png)
* [flowDiagram](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/uml/flowDiagram.png)
* [sequenceDiagrame](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/uml/sequence.png)

<br/>

<b>3. DDD</b>

[DDD](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/ddd/ddd.png) - Dividing the into 3 domains: Core, Support and Miscellaneous. Core Domain are the core functionality perceived by the user. Support domains contains the functions which enable the core functionalities and miscellaneous domain made of subjects, which are required for an operating company.  
<br/>

<b>4. Metrics</b>

Two different metrics tools have been applied to this project. The first one is universal and cloud enabled: SonarQube. The second one is a python specific cli tool: PyLint. 

For Sonarcube the .vscode extension [SonarLint](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/metrics/sonarLint.png) was installed and it was checking for inconsistencies while coding. With SonarLint it was very easy to connect to the Sonarqube Cloud, which did a [deep dive](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/metrics/sonarQubeCloud.png) into my code and checked for additional reliability, security, maintainability and duplications. \
When integrated with SonarCloud, automatic quality testing was also done when [merging two branches](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/CICD/githubActionPullRequest.png)

Additionally PyLint was used to further checking up the code. Even though Sonarcube didn't find any inconsistencies, PyLint was able to find [small issues](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/metrics/pylint1.png), which got solved after a [few iterations](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/metrics/pylint2.png). 
<br/>

<b>5. Clean Code Development</b>

please check out [CCC.md](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/CCC.md) for details.
<br/>

<b>6. Build Management</b>

Python is an interpreted language, nothing needs to be compiled so a build management tool seems rather unnecessary. The most used build tool 'setuptools' is used for packaging and publishing on pypi, which is not the intend of this application. \
Nonetheless for this project pyBuilder was installed. Unfortunately after a successful installation the build process [failed](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/buildManagement/pyBuilder.png). It seems to be stuck in some sort of directory creation loop, and with a rather small community and the last update more than 3 months ago, I was not able to find a solution. 

So instead of relying on on pyBuilder, I choose to use Github Action for continuously integrated [building and testing](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/buildManagement/actionYAML.png) management. 
<br/>

<b>7. Unit-Test</b>

Pytest was used for unit testing purpose. I have build a [simple test](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/test_sample.py) to test two different functions. / Both test [have passed](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/unitTest/unitTest.png) locally without any issue. 

After setting up secrets in Github Action as a environment variable, testing in the Github Action pipeline was also [successful](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/unitTest/ActionTest.png). 
<br/>

<b>8. Continuous Delivery</b>
Github Action is used for this project. Compared to Jenkins there is no need to setup for a local server, which saves resources. Besides, Github Action has a big community with many pipeline templates to choose from. Since I already extensively use Github, using Github Action for CI/CD was the reasonable thing to do. 

For demonstration purpose, a test branch with a pull request was created and [successfully merged](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/CICD/githubActionPullRequest.png). 

Next, a [YAML file](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/buildManagement/actionYAML.png) was created for the continuous delivery pipeline. The file states that each time on push or pull_request the pipeline will be restarted. First a ubuntu-latest server with python 3.8 got setup, then all dependencies will be installed, Lint test with flake8 will be executed and finally testing with pytest (with the openAI api key as a secret)will be conducted. The entire [pipeline](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/CICD/BUILD_TEST.png) was successful.
<br/>

<b>9. IDE-shortcut</b>

My IDE is vsCode. It is lightweight, fast. It has available many plugin and a very functional terminal. Besides, it integrates Jupyter Notebook very well, which is a must have tool for data scientists. \
Some of my favorite shortcuts are:

* `CTRL + O`: open a folder / file
* `F5`: open debug mode
* `CTRL + SHIFT + P`: open the command palette to access all available commands based on the current context.

while in Jupyter Notebook mode:
* `a/b`: add a new block above/below current block
* `SHIFT + ENTER`: Run current block, jump to the next block
* `dd`: delete current block 
<br/>

<b>10. DSL Demo</b>

For this project apart from a few basic functions for cleaning and aggregating data, I have heavily on domain specific language patterns to get the job done. 

* For example the usage of hugginface.co transformers library greatly reduced the amount of coding working and made it possible to use strong performing language models. [example](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/streamlit_app.py#L10-L13) 
* The same applies to the openai package for text generation. [example](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/streamlit_app.py#L32-L43) 
* Additionally, the entire interface for the chatbot was also based a domain specific package (Streamlit), which is heavily used by data scientists. Code example can be found [here](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/streamlit_app.py#L87-L130) 
<br/>

<b>11. Functional Programming</b>

* [`summarize()`](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/streamlit_app.py#L10-L13) is a final data structured fucntion because it does not modify or mutate the input 'chat_log' in anyway. The output is solely dependent on the input parameters.

* [`remove_backslash()`](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/streamlit_app.py#L76-L80) is a side effect free function because it also does not modify any state outside of its scope and does not produce any observable effects other than its return value.

* [`analyze_sentiment()`](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/streamlit_app.py#L69-L74) is a higher order function since it takes two other functions function(`clean_chat_log, sentiment_task`) as parameters and returns the function `sentiment_task` as return value.

* [`remove_backslash()`](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/streamlit_app.py#L76-L80) uses an anonymous lambda function.

## Technology
* Python 3.8
* Jupyter Notebook for data gathering, data wrangling and fine-tuning upload 
* PyTube for video scrapping, OpenAI Whisper for transcribing 
* LLM - Large Language Models: 
- Language generation(decoder based model): OpenAI GPT3 
- Language summarization and sentiment analysis(encoder based model): Huggingface Transformers, bert based models\
* StreamLit as a web app interface 

## Setup
* access the demo version at https://huggingface.co/spaces/lsacy/mentalChat 
* Running the code on a local machine: 
register and load a custom [OpenAI](www.openai.com) api key, insert the key at line 7 in streamlit_app.py -> openai.api_key = 'your-api-key'

	install dependencies:
	```
			  (yourEnv) ~/dir_to_the_chatbot pip install -r requirements.txt
	```
	start the program in terminal with:
	```
			  (yourEnv) ~/dir_to_the_chatbot streamlit run streamlit_app.py
	```
