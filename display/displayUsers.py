def individual_user(user)->dict :
    return {
        "id" : str(user["_id"]),
        "name" : user["name"],
        "email" : user["email"]
    }

def all_users(users) -> list :
    return [individual_user(user) for user in users]