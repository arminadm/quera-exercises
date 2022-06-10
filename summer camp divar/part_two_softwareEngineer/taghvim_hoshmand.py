#FAIELD
#Armin Darabi Mahboub

def main():
    n = int(input())
    # 'worker_id':[index][day][start_epoch][end_epoch]
    worker_info = [[[None], [None], [None], [None]] for x in range(number_of_meetings)]
    for worker_id in range(n):
        #worker_id is a selector index for showing which worker you're talking about
        user_id = input() #useless
        busy_day = input().upper()
        number_of_meetings = int(input())
        for i in range(number_of_meetings):
            given_data_for_meeting = input()
            start_epoch = given_data_for_meeting.split(' ')[2]
            end_epoch = given_data_for_meeting.split(' ')[3]
            worker_info[worker_id][i][busy_day][start_epoch][end_epoch]
    
    print(worker_info)

if __name__ == '__main__':
    main()