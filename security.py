from Users import users

users_list = [
    users(1, 'Bob', 'Jose')]

user_mapping = {u.username: u for u in users_list}
userid_mapping = {u.id: u for u in users_list}


def authenticate(username, password):
    user = user_mapping.get(username, None)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
