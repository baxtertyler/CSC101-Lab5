# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Tyler Baxter
# Section: 03

# This function returns a list with all the even nums
# list -> list
# List comprehension
def are_even(list1):
    list2 = [num for num in list1 if num % 2 == 0]
    return list2


# This function returns a new list without the duplicates
# list -> list
# For loop
def remove_duplicates(list1):
    list2 = []
    for i in list1:
        new_val = True
        for j in list2:
            if i == j:
                new_val = False
        if new_val:
            list2.append(i)
    return list2


# This function returns a new list with all the values that are divisible by n
# list, int -> list
# While loop
def are_divisible_by_n(list1, n):
    list2 = []
    idx = 0
    while idx < len(list1):
        if list1[idx] % n == 0:
            list2.append(list1[idx])
        idx += 1
    return list2
