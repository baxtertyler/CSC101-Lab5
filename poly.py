# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Tyler Baxter
# Section: 03

# This function adds two strings together
# list, list -> list
def poly_add2(list1, list2):
    list3 = [list1[0] + list2[0],
             list1[1] + list2[1],
             list1[2] + list2[2]]
    return list3


# This function multiplies two binomials
# list, list -> list
def poly_mult2(list1, list2):
    list3 = [list1[0] * list2[0],
             (list1[1] * list2[0]) + (list1[0] * list2[1]),
             list1[1] * list2[1]]
    return list3
