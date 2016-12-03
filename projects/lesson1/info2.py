user_name=dict()

def get_data_from_user():
    user_name['first_name']= input('Input your first name: ')
    print ('Your first name: ' + user_name['first_name'])
    user_name['last_name'] = input('Input your last name: ')
    print ('Your last name: ' + user_name['last_name'])

if __name__ == '__main__':
#   user_name={'first_name':'Denis','last_name':'Maximov'}
    get_data_from_user()
    print(user_name)
