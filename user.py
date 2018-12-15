from database import connect


class User:
    def __init__(self, first_name, last_name, email, id, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.id = id
        self.password = password

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        with connect() as connection:
            with connection.cursor() as cursor:
                if not self.user_exist(self.email):
                    cursor.execute("INSERT INTO users(first_name, last_name, email, password) VALUES(%s, %s, %s, %s)",
                                   (self.first_name, self.last_name, self.email, self.password))
                    return True

            return False

    def user_exist(self, email):
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT email FROM users WHERE email=%s", (email,))
                user_email = cursor.fetchone()
                if user_email is None:
                    return False

        return True


my_user = User('Frank', 'Sinatra', 'nancy@sinatra', None, '12345')
print(my_user)
# my_user.save_to_db()
result = my_user.user_exist(my_user.email)
print(result)
