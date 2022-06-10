# 210/300
#Armin Darabi Mahboub

def main():
    n = int(input())
    # [index][start_epoch][end_epoch]
    first_worker_epoches = [[[None], [None], [None]] for x in range(n)]
    for i in range(n):
        epoches = input()
        first_worker_epoches[i][0] = int(epoches.split()[0])
        first_worker_epoches[i][1] = int(epoches.split()[1])
        first_worker_epoches[i][2] = int(epoches.split()[2])
    
    m = int(input())
    # [index][start_epoch][end_epoch]
    second_worker_epoches = [[[None], [None], [None]] for x in range(m)]
    for i in range(m):
        epoches = input()
        second_worker_epoches[i][0] = int(epoches.split()[0])
        second_worker_epoches[i][1] = int(epoches.split()[1])
        second_worker_epoches[i][2] = int(epoches.split()[2])
    
    
    in_common_epoches = 0
    for range1 in range(n): #about first worker
        for range2 in range(m): #about second worker
            w1_start_range = first_worker_epoches[range1][1]
            w1_end_range = first_worker_epoches[range1][2]
            w2_start_range = second_worker_epoches[range2][1]
            w2_end_range = second_worker_epoches[range2][2]

            # first: ====
            # second:      ==
            if w1_start_range > w2_end_range or w1_end_range < w2_start_range:
                pass #nothing in common
            
            # first:   =====
            # second:     ====
            elif w2_start_range >= w1_start_range and w2_start_range <= w1_end_range:
                in_common_epoches += (w1_end_range - w2_start_range)

            # first:      ====
            # second:  =====
            elif w2_end_range >= w1_start_range and w2_end_range <= w1_end_range:
                in_common_epoches += (w2_end_range - w1_start_range)

            # first:   ===
            # second:  ======
            elif w1_start_range >= w2_start_range and w1_start_range <= w2_end_range and w1_end_range >= w2_start_range and w1_end_range <= w2_end_range:
                in_common_epoches += (w1_end_range - w1_start_range)

            # first:   =====
            # second:   ===
            elif w2_start_range >= w1_start_range and w2_start_range <= w1_end_range and w2_end_range >= w1_start_range and w2_end_range <= w1_end_range:
                in_common_epoches += (w2_end_range - w2_start_range)
            
    print(in_common_epoches)  



if __name__ == '__main__':
    main()