# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Tyler Baxter
# Section: 03

# This function creates a list with each value ** 3
# list -> list
# List comprehension
def cube_all(list1):
    list2 = [num ** 3 for num in list1]
    return list2


# This function adds n to every value and adds the value to a list new
# list, int -> list
# For loop
def add_n_to_all(list1, n):
    list2 = []
    for idx in range(0, len(list1), 1):
        list2.append(list1[idx] + n)
    return list2


# This function returns true/false if each value is divisible by 5
# list -> list
# While loop
def div_by_5_all(list1):
    idx = 0
    list2 = []
    while idx < len(list1):
        if list1[idx] % 5 == 0:
            list2.append(True)
        else:
            list2.append(False)
        idx += 1
    return list2
