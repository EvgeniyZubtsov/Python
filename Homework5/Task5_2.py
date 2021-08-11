def name_serial(shows_dic,show_janr):
    list_janr = []
    for key,value in shows.items():
        if value == show_janr:
            list_janr.append(key)
    return list_janr

def avg_rait(raiting_dic,list_janr):
    sum_raiting = 0
    count = 0
    for i in list_janr:
        sum_raiting += raiting_dic[i]
        count+= 1
    avg_raiting = sum_raiting/count
    return avg_raiting