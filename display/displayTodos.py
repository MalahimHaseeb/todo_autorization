def individual_todo(todo)-> dict :
    return {
        "id" : str(todo["_id"]),
        "title" : todo["title"],
        "description" : todo["description"],
        "complete" : todo["complete"],
        "created_at" : todo["created_at"]
    }

def all_todos(todos) -> list :
    return [individual_todo(todo) for todo in todos]