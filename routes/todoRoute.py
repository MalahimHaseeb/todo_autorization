from fastapi import APIRouter ,Depends  ,HTTPException
from object.todoObject import TodoItem
from datetime import datetime
from config.db import todocl
from display.displayTodos import all_todos , individual_todo
from bson import ObjectId
from middleware.checkUser import get_current_user
todor = APIRouter()

#create todo
@todor.post("/add-todo" , tags=["todo-routes"])
def add_todo(todo: TodoItem, current_user: dict = Depends(get_current_user)):
    todo_dict = {
        "title": todo.title,
        "description": todo.description,
        "complete" : False ,
        "user_id": current_user["_id"],
        "created_at": datetime.utcnow()
    }
    todocl.insert_one(todo_dict)
    return {"success": True, "message": "Todo item added successfully"} 

#Get todos
@todor.get("/get_todos" , tags=["todo-routes"] )
def get_todos(id : dict = Depends(get_current_user)):
    user_todo = todocl.find({"user_id" : id["_id"]})
    return {"success" : True , "todos" : all_todos(user_todo)} 

#Get one todo
@todor.get("/get_todo/{id}", tags=["todo-routes"])
def get_todo(id: str, current_user: dict = Depends(get_current_user)):
    try:
        todo_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Todo ID")

    user_todo = todocl.find_one({"_id": todo_id, "user_id": current_user["_id"]})
    if user_todo is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return {"success": True, "todo": individual_todo(user_todo)} 

#update todos   
@todor.put("/update-todo/{id}", tags=["todo-routes"])
def update_todo(id: str, todo: TodoItem, current_user: dict = Depends(get_current_user)):
    try:
        todo_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Todo ID")
    old_data = todocl.find_one({"_id" : todo_id})
    update_data = {
        "title": todo.title,
        "description": todo.description,
        "complete": old_data["complete"],
        "updated_at": datetime.utcnow()  # Optional: Track when it was last updated
    }

    result = todocl.update_one({"_id": todo_id, "user_id": current_user["_id"]}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Todo item not found")

    return {"success": True, "message": "Todo item updated successfully"}

#update complete status
@todor.patch("/update-complete/{id}", tags=["todo-routes"])
def update_complete_status(id: str, complete: bool, current_user: dict = Depends(get_current_user)):
    try:
        todo_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Todo ID")

    result = todocl.update_one(
        {"_id": todo_id, "user_id": current_user["_id"]},
        {"$set": {"complete": complete}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Todo item not found")

    return {"success": True, "message": "Todo item status updated successfully"}

#delete todo
@todor.delete("/delete-todo/{id}", tags=["todo-routes"])
def delete_todo(id: str, current_user: dict = Depends(get_current_user)):
    try:
        todo_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Todo ID")

    result = todocl.delete_one({"_id": todo_id, "user_id": current_user["_id"]})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return {"success": True, "message": "Todo item deleted successfully"}
