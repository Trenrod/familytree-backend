# FamilyTree Backend

This application is the backend of the family tree app. Offers user authentication, stores family tree data as family members, their relations as well as other user informations.

## How to develop

### IDE

As an IDE im using VSCode with Python plugin from MS. 

### Develop

Its required to have Python3 with pip and venv support installed.

1. Create virtual environment (venv) `python3 -m venv .venv`
2. Activate virtual environment
    * Windows: `.venv\Script\activate.bat`
    * Linux: `source .venv/bin/activate`
3. Install libs `pip install -r requirements.txt` 
4. Create tables and setup db `python3 manage.py migrate`
5. Start in developer mode ` python3 manage.py runserver`

```plantuml

entity Person {
    * marriages
    * parents
    * children
    * places
}
entity Place

Person }|--|{ Person
Person }|--|{ Place


```