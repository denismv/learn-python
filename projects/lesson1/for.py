school=[
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '5', 'scores': [5,4,2,5,2]},
    {'school_class': '6', 'scores': [3,2,2,5,2]},
    {'school_class': '7b', 'scores': [5,2,4,5,5]}
]

def midle_score(school):
    sum_class=0
    sum_school=0
    score_num=0
    for sclass in school:
        #print(sclass)
        for score in sclass['scores']:
            #print(score)
            sum_class+=score
            sum_school+=score
            score_num+=1
        midle_class=sum_class/len(sclass['scores']) 
        print (sclass['school_class'], midle_class)
    midle_school=sum_school/score_num
    print ('school',midle_school)


if __name__ == '__main__':
    midle_score(school)

