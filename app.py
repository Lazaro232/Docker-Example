from Database.crud import DatabaseCrud

from flask import Flask, request, Response
# Database object
database = DatabaseCrud()
# Flask object
app = Flask(__name__)


@app.route('/user/<int:user_id>')
def get_user(user_id: int) -> dict:
    # Fetching user informations
    user_info = database.fetch_user_by_id(user_id)
    # User not found
    if user_info is None:
        return Response(
            "User not found",
            status=404,
        )
    # Tuple to dict
    user_info_dict = {
        'name': user_info[1],
        'age': user_info[2]
    }

    return user_info_dict


@app.route('/user/create', methods=['POST'])
def create_user() -> str:
    # User informations
    json_content = request.get_json()
    user_name = json_content['name']
    user_age = json_content['age']
    # Creating user
    database.create_user(user_name, user_age)

    return f'User with name "{user_name}" and age {user_age} created!'


@app.route('/user/update/<int:user_id>', methods=['POST'])
def update_user(user_id: int) -> str:
    # User informations
    json_content = request.get_json()
    user_new_name = json_content['name']
    user_new_age = json_content['age']
    # Updating user
    database.update_user(user_id, user_new_name, user_new_age)

    return f'Name and age of user with {user_id} updated to "{user_new_name}" and {user_new_age}'


@app.route('/user/delete/<int:user_id>')
def delete_user(user_id: int) -> str:
    # Fetching user informations
    user_info = database.fetch_user_by_id(user_id)
    # User not found
    if user_info is None:
        return Response(
            "User not found",
            status=404,
        )
    # Deleting user
    database.delete_user(user_id)

    return f'User {user_id} deleted!'


if __name__ == '__main__':
    app.run()
