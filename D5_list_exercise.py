# # 1
# empty_list = []

# # 2
# sample_list = ['item1', 'item2', 'item3', 'item4', 'item5']

# # 3
# print(len(sample_list)) # 5

# # 4
# first_item = sample_list[0]
# middle_item = sample_list[2]
# last_item = sample_list[4]

# print('First Item:', first_item) # item1
# print('Middle Item:', middle_item) # item3
# print('Last Item:', last_item) # item5

# # 5
# mixed_data_types = ['Ron Vincent P. San Juan', 26, 5.2, 'Single', 'Philippines']

# # 6 
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# # 7
# print('IT Companies:', it_companies)

# # 8
# print('Number of IT Companies:', len(it_companies))

# # 9
# print('First IT Company:', it_companies[0])
# print('Middle IT Company:', it_companies[3])
# print('Last IT Company:', it_companies[6])


# # 10
# print('IT Companies:', it_companies)

# # 11
# it_companies.append('Twitter')
# print('IT Companies after adding Twitter:', it_companies)

# # 12
# first_it_company = it_companies[0]
# print('First IT Company:', first_it_company)
# uppercase_first_it_company = first_it_company.upper()
# print('Uppercase First IT Company:', uppercase_first_it_company)

# # 13
# it_companies.insert(3, 'Tesla')
# print('IT Companies after inserting Tesla at index 3:', it_companies)

# # 14 
# joined_it_companies = '#; '.join(it_companies)
# print('Joined IT Companies:', joined_it_companies)

# # 15
# does_company_exist = 'Apple' in it_companies
# print('Does Apple exist in IT Companies?', does_company_exist)

# # 16
# it_companies.sort()
# print('Sorted IT Companies:', it_companies)

# # 17
# it_companies.reverse()
# print('Reversed IT Companies:', it_companies)

# # 18
# first_three_companies = it_companies[0:3]
# print('First Three IT Companies:', first_three_companies)

# # 19
# last_three_companies = it_companies[-3:]
# print('Last Three IT Companies:', last_three_companies)

# # 20
# middle_three_companies = it_companies[2:5]
# print('Middle Three IT Companies:', middle_three_companies)

# # 21
# it_companies.pop(0)
# print('IT Companies after removing the first company:', it_companies)

# # 22
# it_companies.pop(len(it_companies) // 2)
# print('IT Companies after removing the middle company:', it_companies)

# # 23
# it_companies.pop(-1)
# print('IT Companies after removing the last company:', it_companies)

# # 24
# it_companies.clear()
# print('IT Companies after clearing the list:', it_companies)

# # 25
# del it_companies
# # print(it_companies) # This will raise an error because the list has been deleted
# print('IT Companies list has been deleted.') # This will raise an error if you try to print it after deletion

# # 26
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

# full_stack = front_end + back_end
# print('Full Stack:', full_stack)

# # 27
# full_stack.insert(5, 'Python')
# print('Full Stack after inserting Python:', full_stack)

# full_stack.insert(6, 'SQL')
# print('Full Stack after inserting SQL:', full_stack)

# full_stack.insert(7, 'Redux')
# print('Full Stack after inserting Redux:', full_stack)

# # Level 2

# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ages.sort()
# print('Sorted Ages:', ages)
# print('Minimum Age:', ages[0])
# print('Maximum Age:', ages[-1])
# print('Average Age:', sum(ages) / len(ages))
# print('Range of Ages:', ages[-1] - ages[0])
