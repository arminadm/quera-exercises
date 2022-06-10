# 150/150
#Armin Darabi Mahboub

def main():
    m = input()
    detail = []
    detail = give_detail(m, detail)
    answer = ''
    for eachDetail in detail:
        which_number = eachDetail[0]
        repeated_time = eachDetail[1]
        answer = answer + f'{repeated_time}{which_number}'
    print(answer)


def give_detail(m, detail):
    number_repeatation_counter = 0  
    if len(m) == 1:
        number_repeatation_counter = 1
        which_number = m[0]
        detail.append([which_number, number_repeatation_counter])
        return detail
    if len(m) < 1:
        return detail
    for i in range(len(m)):  
        if i == 0:
            which_number = m[i]
            number_repeatation_counter += 1
        elif m[i] == m[i - 1]:
            try:
                test = m[i + 1]
                number_repeatation_counter += 1
            except:
                number_repeatation_counter += 1
                detail.append([which_number, number_repeatation_counter])
                return detail

        else:
            detail.append([which_number, number_repeatation_counter])
            m = m[number_repeatation_counter:]
            number_repeatation_counter = 0
            which_number = None
            return give_detail(m, detail)

if __name__ == '__main__':
    main()