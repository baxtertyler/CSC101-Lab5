# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Tyler Baxter
# Section: 03

# This function returns a new list with the nested list values multiplied
# list[][] -> list
def product(list1):
    list2 = []
    for i in list1:
        sum_list = 1
        for j in i:
            sum_list *= j
        list2.append(sum_list)
    return list2
