def prvociselny_rozklad(number = 2):
    number_list = []
    delitel= 2
    while number >=2:
        if number % delitel ==0:
            number_list.append(delitel)
            number /= delitel
        else:
            delitel += 1
    return(number_list)

