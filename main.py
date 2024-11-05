# Create good script to create new list, which only contains users from Poland. Try to do it with List Comprehension. =====================================================
print("Create good script to create new list, which only contains users from Poland. Try to do it with List Comprehension.")

users = [{"name": "Kamil", "country":"Poland"}, {"name":"John", "country": "USA"}, {"name": "Yeti"}]

polish_users = [ user for user in users if user.get("country") == "Poland" ]

print(polish_users)



# Display sum of first ten elements starting from element 5: numbers = [1,5,2,3,1,4,1,23,12,2,3,1,2,31,23,1,2,3,1,23,1,2,3,123] ============================================
print("Display sum of first ten elements starting from element 5: numbers = [1,5,2,3,1,4,1,23,12,2,3,1,2,31,23,1,2,3,1,23,1,2,3,123]")
# !!! "starting from element 5" as 5th element in list NOT index 5"
numbers = [1,5,2,3,1,4,1,23,12,2,3,1,2,31,23,1,2,3,1,23,1,2,3,123]

start_index = 5
n = 10

print(sum(numbers[start_index-1 : n + start_index-1]))

# !!! "starting from element 5" as starting from element 5 from the list
# start_element = 5
# try:
#     start_index = numbers.index(start_element)
# except ValueError:
#     start_index = None 

# if start_index:
#     print(sum(numbers[start_index : n + start_index]))



# Fill list with powers of 2, n [1..20] ====================================================================================================================================
print("Fill list with powers of 2, n [1..20]")

data = [number ** 2 for number in range(1,21)]

print(data)




# ============================== OUTPUT ===============================

# Create good script to create new list, which only contains users from Poland. Try to do it with List Comprehension.
# [{'name': 'Kamil', 'country': 'Poland'}]
# Display sum of first ten elements starting from element 5: numbers = [1,5,2,3,1,4,1,23,12,2,3,1,2,31,23,1,2,3,1,23,1,2,3,123]
# 80
# Fill list with powers of 2, n [1..20]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]