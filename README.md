- # Advanced Software Engineering 2022/23  
- ### BHT with Prof. Dr. Edlich  
- # mentalHealth_Chatbot  
<h3> an AI therapist, based on GPT3, fine-tuned with custom data. </h3>
- ## Table of content  
	* [About the App](#About-the-app)
	* [Checklist](#Checklist)
	* [Technology](#Technology)
	* [local Setup](#Setup)

- ## About the app  
- The [application](https://huggingface.co/spaces/lsacy/mentalChat) is a chatbot, acting as a mental health therapist.  
- The chatbot is powered by GPT3, a powerful large language model by [openai](https://www.openai.com). The GUI was realized with the [streamlit](https://www.streamlit.io) package.  
- Fine-tuning had to be done In order to achieve good results for therapeutic purpose. Various sources of data have been accumulated for this task:  
	- scrapping of 28 youtube videos conversations between therapist and client on behaviour therapy, using [whisper AI](openai.com/blog/whisper/) to transcribe the conversations.  
	- https://dl.acm.org/doi/10.1145/3488560.3498509 A manually annotated dataset of approximately 300 therapeutic conversation between patient and therapist  
	- [kaggle dataset](https://www.kaggle.com/datasets/narendrageek/mental-health-faq-for-chatbot) of 29 prompt and detailed answer on mental health and related topic  
- the datasets are cleaned, merged and transformed to JSONL format, then pushed via API to the OpenAI server to train a custom model (fine-tuning). Due to cost reasons, fine-tuning was done only on the medium-sized model (curie).  
- The result can be previewed at [huggingface.co/spaces/lsacy/mentalChat](https://huggingface.co/spaces/lsacy/mentalChat)  
- Besides the ability to have a conversation. With the help of two more additional models (Bert based), each conversation can be summarised and evaluated on three sentiment categories (positive, negative, neutral). These information could then be stored in a database and tracked for further analysis.  
- ## Checklist  
-  
<b>1. Git</b>
- For an already exiting project, clone -> add file for example add . for all files or add certain file --> always pull before commit/push -> stash if needed -> push in the end  
-  
  ```
	  git clone https://www.Github(anyHostingSerivce).com/User/Repo
	  git add .
	  git pull 
	  git stash
	  git commit -m 'commit message'
	  git push
  ```
- For a new project, one could use git init to initialize a local git repository then on the preferred Git hosting service create a repository and then add the remote origin  
-  
  ```
	  git init 
	  git remote add origin <remote-repository-url>
	  git push -u origin master/main
	  
  ```
- My way of creating a new repo with existing code: create a new empty repository on the host, git clone the empty repository and put all codes into the cloned folder.  
- use .gitignore to add files to be ignored, so git would not push them (personal api etc)  
-  
  ```
	  touch .gitignore #create .ignore file
	  vim .gitignore #i 
  ```
- if more than one people working on the same repository, branches are useful to coordinate the work.  
-  
  ```
	  git branch #list all branches
	  git checkout -b <newBranch> #create a new branch named newBranch
	  git push --set-upstream origin <newBranch> #pushing the first time
	  git switch/checkout <main> #switch back to main branch
	  git merge <newBranch> #to merge main with files from branch <newBranch>
	  git branch -d <newBranch> #to delete the branch <newBranch>
  ```
-  
-  
<b>2. UML</b>
  Using PlantUML and LucidChart:  
- [UseCase](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/uml/UseCase.png)  
- [flowDiagram](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/uml/flowDiagram.png)  
- [sequenceDiagrame](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/uml/sequence.png)  
-  
-  
<b>3. DDD</b>
  [DDD](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/ddd/ddd.png) - Dividing the into 3 domains: Core, Support and Miscellaneous. Core Domain are the core functionality perceived by the user. Support domains contains the functions which enable the core functionalities and miscellaneous domain made of subjects, which are required for an operating company.  
-  
-  
<b>4. Metrics</b>
- Two different metrics tools have been applied to this project. The first one is universal and cloud enabled: SonarQube. The second one is a python specific cli tool: PyLint.  
- For Sonarcube the .vscode extension [SonarLint](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/metrics/sonarLint.png) was installed and it was checking for inconsistencies while coding. With SonarLint it was very easy to connect to the Sonarqube Cloud, which did a [deep dive](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/metrics/sonarQubeCloud.png) into my code and checked for additional reliability, security, maintainability and duplications.  
- Additionally PyLint was used to further checking up the code. Even though Sonarcube didn't find any inconsistencies, PyLint was able to find [small issues](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/metrics/pylint1.png), which got solved after a [few iterations](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/metrics/pylint2.png).  
-  
-  
<b>5. Clean Code Development</b>
-  
-  
-  
<b>6. Build Management</b>
- Python is an interpreter language, nothing needs to be compiled so a build management tool seems unnecessary. Nonetheless for this project I have installed pyBuilder, unfortunately after a successful installation I was [not able](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/buildManagement/pyBuild.png) to properly build something.  
- So instead of relying on on pyBuilder, I choose to use github Action for continuously integrated [building and testing](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/buildManagement/actionYAML.png).  
-  
-  
<b>7. Unit-Test</b>
- Pytest was used for unit testing purpose. I have build a [simple test](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/test_sample.py) to test two different functions. Both test [have passed](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/unitTest/unitTest.png) locally without any issue.  
- Testing in the Github Action pipeline was [unsuccessful](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/unitTest/testFailed.png), but this was to be expect, since I didn't want to upload my openAI API key.  
-  
-  
<b>8. Continuous Delivery</b>
- Github Action is used for this project. Compared to Jenkins there is no need to setup for a local server, which saves resources and it has many template pipelines to choose from. Since I already extensively use Github, using Github Action for CI/CD was the reasonable thing to do.  
- For demonstration purpose, a test branch with a pull request was created and [successfully merged](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/CICD/githubActionPullRequest.png).  
- Next, a [YAML file](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/buildManagement/actionYAML.png) was created for the continuous delivery pipeline. The file states that on push or pull_request each time the jobs of running on a ubuntu-latest server with python 3.8, all dependencies will be installed, Lint test with flake8 will be executed and testing with pytest will be done.  
- The entire [chain of events](https://github.com/Lsacy/mentalHealth_Chatbot/blob/main/CICD/BUILD_TEST.png) are successful with the only exception of testing with the reasons stated above. (no API key because its an open repository)  
-  
-  
<b>9. IDE-shortcut</b>
- My IDE is vsCode. It is lightweight, fast. It has available many plugin and a very functional terminal. Besides, it integrates Jupyter Notebook very well, which is a must have tool for data scientists.  
- Some of my favorite shortcuts are:  
	- CTRL + O: open a folder / file  
	- F5: open debug mode  
	- CTRL + SHIFT + P: open the command palette to access all available commands based on the current context.  
	- while in Jupyter Notebook mode:  
		- a/b: add a new block above/below current block  
		- SHIFT + ENTER: Run current block, jump to the next block  
		- dd: delete current block  
	-  
-  
<b>10. DSL Demo</b>
-  
-  
-  
<b>11. Functional Programming</b>
-  
-  
-  
- ## Technology  
- Python 3.8  
- Jupyter Notebook for data gathering, data wrangling and fine-tuning upload  
	- PyTube for video scrapping, OpenAI Whisper for transcribing  
- large language models  
	- Language generation(decoder based model): OpenAI GPT3  
	- Language summarization and sentiment analysis(encoder based model): Huggingface Transformers, bert based models  
- StreamLit as a web app interface  
-  
- ## Setup  
- access the demo version at https://huggingface.co/spaces/lsacy/mentalChat  
- Running the code on a local machine:  
	- register and load a custom [OpenAI](www.openai.com) api key, insert the key at line 7 in streamlit_app.py -> openai.api_key = 'your-api-key'  
	- install dependencies:  
	-  
	  ```
	  		  (yourEnv) ~/dir_to_the_chatbot pip install -r requirements.txt
	  ```
	- start the program in terminal with:  
	-  
	  ```
	  		  (yourEnv) ~/dir_to_the_chatbot streamlit run streamlit_app.py
	  ```
	-  
-  
