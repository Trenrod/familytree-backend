# FamilyTree Backend

This application is the backend of the family tree app. Offers user authentication, stores family tree data as family members, their relations as well as other user informations.

## How to develop

### IDE

As an IDE im using VSCode with Python plugin from MS. 

### Develop

Its required to have Python3 with pip and venv support installed.

- Install python >= 3.5
- Create virtual environment (venv) `python3 -m venv .venv`
- Activate virtual environment
    * Windows: `.venv\Script\activate.bat`
    * Linux: `source .venv/bin/activate`
- Install libs `pip install -r requirements.txt` 
- Create tables and setup db `python3 manage.py migrate`
- Start in developer mode `python3 manage.py runserver`

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