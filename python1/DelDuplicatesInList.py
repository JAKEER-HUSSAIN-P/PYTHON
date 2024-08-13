word_list = input("Enter list elements (comma-separated): ").split(',')
unique_list = []
for word in word_list:
    if word not in unique_list:
        unique_list.append(word)
print("List after removing duplicates:", unique_list)
