# TO START THE APPLICATION

You must install Python 3.11 or another currently version, after that you must install all the libs used in this project. To do it copy the commands bellow:

    python -m venv venv    # creating a new virtual enviroment
    
    venv\Scripts\activate  # activating the scripts and this virtual enviroment
    
    pip install -r requirements.txt    # installing all requirements and libs to run this app

# SETTING YOUR 'CREDENTIALS_PATH'

1 - Open the Google Cloud API and start a new project.

2 - After that, click on API's and Services.

3 - Then, initialize the Google Sheet API.

4 - Register a new creadential and download the .json file.

5 - Rename the value of the variable 'credentials_path' on the code and pass the location of the .json file into your computer.

    credentials_path = 'path.json'   # the location of the file containing Google Cloud API credentials

# RUNNING THE APP

    python challenge.py


    
