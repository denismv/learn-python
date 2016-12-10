
names_list=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person(person_name):
#    i=0
    while names_list:
#        i+=1
        name=names_list.pop()
        if name == person_name:
            print("Нашелся: ",name)
            break
    else:
        print(person_name, "не найден")

if __name__ == '__main__':
    find_person("Валера")

