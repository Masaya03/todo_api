import requests
import json

def main():
    get_ToDo_all()

def url(fn :CRUD) :
    return
    def func():   
        url = "http://127.0.0.1:8000/ToDo/create_ToDo"
        CRUD()
        res = requests.post(url,json.dumps(body))
        print(res.json()) 
    

def post_todo(user_id:int , description:str):
    url = "http://127.0.0.1:8000/ToDo/create_ToDo"
    
    #jsonに変換する必要がある
    body = {
        "description":description,
        "user_id": user_id
    }

    res = requests.post(url,json.dumps(body))
    print(res.json()) 

def post_user(username:str):
    url = "http://127.0.0.1:8000/ToDo/create_user"
    
    #jsonに変換する必要がある
    body = {
        "username":username
    }

    res = requests.post(url,json.dumps(body))
    print(res.json()) 

def get_users_all():
    url = "http://127.0.0.1:8000/ToDo/get_users_all"
    
    res = requests.get(url)
    print(res.json())

def get_ToDo_all():
    url = "http://127.0.0.1:8000/ToDo/get_ToDo_all"
    
    res = requests.get(url)
    print(res.json())

def get():
    url = "http://127.0.0.1:8000/ToDo/get"
    
    body = {
        "ToDo_id": 1
    }
    res = requests.post(url, json.dumps(body))
    print(res.json())

def delete():
    url = "http://127.0.0.1:8000/ToDo/delete"
    
    #jsonに変換する必要がある
    body = {
        "ToDo_id": 1
    }

    res = requests.post(url,json.dumps(body))
    print(res.json())

def update():
    url = "http://127.0.0.1:8000/ToDo/update"
    
    body = {
        "ToDo_id": 1,
        "description": "update_1"
    }
    res = requests.post(url, json.dumps(body))
    print(res.json())




if __name__ == "__main__":
    main()