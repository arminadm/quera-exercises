# 160/200
#Armin Darabi Mahboub

def main():
    n = int(input())
    workers_epoches = [[[None], [None], [None]] for x in range(n)]
    for i in range(n):
        epoches = input()
        workers_epoches[i][0] = int(epoches.split()[0])
        workers_epoches[i][1] = int(epoches.split()[1])
        workers_epoches[i][2] = int(epoches.split()[2])
    # print(workers_epoches)
    looking_for = input()
    answer_duration = int(looking_for.split(' ')[1])
    # print(start, end)

    in_order_data = set_data_in_order(workers_epoches)
    # print(in_order_data)

    for i in range(len((in_order_data))):
        # print(f"i[0]: {i[0]}, i[1]: {i[1]}, i[2]: {i[2]} \n answer_duration: {answer_duration}, anwser_start: {answer_start}, answer_end: {answer_end}")
        if in_order_data[i][2] >= answer_duration and in_order_data[i][0] + answer_duration != in_order_data[i + 1][0]:
            start_range = in_order_data[i][0]
            end_range = in_order_data[i][0] + answer_duration
            # print(end_range)
            if start_range != 0 and end_range != 32400000:
                start_range += 1
                end_range += 1
            print(f'{start_range} {end_range}')
            break

def set_data_in_order(workers_epoches):
    start = 0
    end = 32400000
    time_frame = []
    time_frame.append([
        start,
        workers_epoches[0][1],
        workers_epoches[0][1] - start,
    ])
    for i in range(len(workers_epoches) - 1):
        time_frame.append([
            workers_epoches[i][2],
            workers_epoches[i + 1][1],
            workers_epoches[i + 1][1] - workers_epoches[i][2],
        ])
    time_frame.append([
        workers_epoches[len(workers_epoches) - 1][1],
        end,
        end - workers_epoches[len(workers_epoches) - 1][1],
    ])
    return time_frame

if __name__ == '__main__':
    main()