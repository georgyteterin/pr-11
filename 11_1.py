def bubble_sort(listt):
    l = len(listt)
    for i in range(l-1):
        for j in range(l-1):
            if (listt[j] > listt[j + 1]): 
                a = listt[j] 
                listt[j] = listt[j + 1] 
                listt[j + 1] = a
    return lis
#2 n^2