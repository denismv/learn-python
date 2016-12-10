import string

dict_dialog=dict()
dict_dialog={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
symbols ='.<>?/*&^%)(-='

def get_answer(dict_key, dict_words):
    dict_key=str.lower(dict_key)
    dict_key=dict_key.strip()

    for char in dict_key:
        if char in string.punctuation:
            dict_key = dict_key.replace(char,'')
#   dict_key=dict_key.replace(',', '').replace("!", '').replace("?", '').replace(".", '')

    return dict_words.get(dict_key, "Я не понял вопрос")

def ask_user(dict_dialog):
    while True:
        try:
            user_input=input("Скажи что-нибудь: ")

            answer=get_answer(user_input, dict_dialog)    

            print(answer)

            if user_input == 'пока':
                break

        except (KeyboardInterrupt):
            print('\nПока')
            break

if __name__ == '__main__':
    ask_user(dict_dialog)

