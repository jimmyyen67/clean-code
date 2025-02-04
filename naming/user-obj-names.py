class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

# user dictionary
user_data = {
    'entered_name': {
        'value': 'Jim',
        'is_valid': True
    },
    'entered_age': {
        'value': 34,
        'is_valid': True
    },
    'entered_email': {
        'value': 'jimmy.yen@test.com',
        'is_valid': True
    }
}

# user object
user = User('Jim', 34, 'jimmy.yen@test.com')