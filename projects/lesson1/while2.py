
names_list=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person(person_name):
    i=0
    for name in names_list:
        i+=1
        if name == person_name:
            print("Нашелся: ",name,i)

if __name__ == '__main__':
    find_person("Валера")

