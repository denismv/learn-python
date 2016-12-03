dict_dialog=dict()
dict_dialog={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

def get_answer(dict_key, dict_words):
    dict_key=str.lower(dict_key)
    dict_key=dict_key.strip()
    dict_key=dict_key.replace(',', '').replace("!", '').replace("?", '').replace(".", '')

    return dict_words[dict_key]

if __name__ == '__main__':
    
    print (get_answer(' как Дела,?',dict_dialog))

