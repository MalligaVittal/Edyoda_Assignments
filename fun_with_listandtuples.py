'''Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''


def Sort(tup):
    n = len(tup)
    for i in range(1, n):
        key = tup[i]
        j = i - 1
        while j >= 0 and key[1] < tup[j][1]:
            tup[j + 1] = tup[j]
            j -= 1
        tup[j + 1] = key
    return tup
print(Sort([(1,5), (5,2), (12,0), (9,100), (12,90)]))
