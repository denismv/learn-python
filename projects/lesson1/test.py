some_dict=dict()

some_dict=[{'name':'Denis','city':'Moscow','age':30},
    {'name':'Ivan','city':'Samara','age':32}]

if __name__ == '__main__':

    if some_dict[0]['age'] == 30:
        print(some_dict[0]['name']);
    else:
        print('Not found');

