# 1
users = [{"name": "Kamil", "country":"Poland"}, {"name":"John", "country": "USA"}, {"name": "Yeti", "country":"Unknown"}]
polish_users = [user for user in users if user.get("country") == "Poland"]
print(polish_users)

# 2
numbers = [1,5,2,3,1,4,1,23,12,2,3,1,2,31,23,1,2,3,1,23,1,2,3,123]
sum_selected_elements = sum(numbers[4:14])
print(sum_selected_elements)

# 3
powers_of_two = [2**n for n in range(1, 21)]
print(powers_of_two)


