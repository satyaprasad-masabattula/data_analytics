# Expense Tracking System
This project is related to expense usage based

## Project Structue
-** frontend/**: contains all front streaamlit functionality
-** backend/**: contains all backned structure
-** tests/**: using pytest performed unit testing
-** requirement.txt : All dependant packages are listed here
-** README.md : Documentation of project

## Setup execution
1. ** clone the repo: **
2. ** install dependancies:**
    '''commandline
     pip install -r requirement.txt
    '''
3. ** Run FASTAPI server: **
    '''commandline
     unicorn server:app --reload
    '''
4. ** Run Streamlit app:**
    '''commandline
     streamlit run frontend.app.py
    '''