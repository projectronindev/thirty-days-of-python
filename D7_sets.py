# Creating a Set

st = set()
print('Sample Set:', st)

sample_set = {'Item1', 'Item2', 'Item3', 'Item4', 'Item1'}
print('Sample Set:', sample_set) # {'Item1', 'Item2', 'Item3', 'Item4'}

# Length of a Set

length = len(sample_set)
print('Length of Sample Set:', length) # 4

# Checking an Item in a Set

does_exist = 'Item1' in sample_set
print('Does Item1 exist in Sample Set?', does_exist) # True

# Adding Items to a Set

sample_set.add('Item5')
print('Sample Set after adding Item5:', sample_set) # {'Item1', 'Item

# Adding multiple Items to a Set

fruits_set = {'banana', 'orange', 'mango', 'lemon'}
print('Fruits Set:', fruits_set) # {'banana', 'orange', 'mango'}

fruits_set.update(['lime', 'watermelon'])
print('Updated Fruits Set: ', fruits_set)

# Removing items from a Set

countries_set = {'Philippines', 'USA', 'Norway', 'Australia'}
print('Countries Set:', countries_set)

countries_set.remove('USA'); # using remove method
print('Updated Countries Set:', countries_set)

# countries_set.remove('USA'); # Will result an error if you try to remove USA again even if it's already removed
# print('Updated Countries Set:', countries_set)

countries_set.discard('USA'); # Will not result to an error if you use discard.
print('Updated Countries Set:', countries_set)

countries_set.pop(); # using pop method
print('Updated Countries Set:', countries_set)

removed_item = countries_set.pop(); # storing the removed item
print('Updated Countries Set:', countries_set)
print('Removed Country:', removed_item)

# Clearing Items in a Set

sample_set = {'item 1', 'item 2', 'item 3'}
print('Sample Set:', sample_set)
sample_set.clear()
print('Cleared Set:',sample_set)

# Deleting a Set

sample_set = {'item 1', 'item 2', 'item 3'}
print('Sample Set:', sample_set)
del sample_set
# print('Deleted Set:',sample_set) # Will cause an error

# Converting List to SEt

sample_list = ['item1', 'item2', 'item3', 'item4', 'item1']
print('Sample list:', sample_list)

sample_set = set(sample_list)  # the order is random, because sets in general are unordered
print('List to Set:', sample_set)

# Joining Sets

# Using union

st1 = {'item 1', 'item 2'}
print('Set 1:', st1)

st2 = {'item 3', 'item 4'}
print('Set 2:', st2)

st3 = st1.union(st2)
print('Joined Set Using Union Method:', st3)

# Using update

st1 = {'item 5', 'item 6'}
print('Set 1:', st1)

st2 = {'item 7', 'item 8'}
print('Set 2:', st2)

st1.update(st2)
print('Updated Set 1:', st1)

# Using | 

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('Fruits Set:', fruits)

vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print('Vegetables Set:', vegetables)

print('Foods:', fruits | vegetables)

# Check if disjoint set

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print('Whole Numbers:', whole_numbers)

even_numbers = {1, 2, 3, 4, 5}
print('Even Numbers:', even_numbers)

even_numbers2 = {11, 12, 13, 14, 15}
print('Even Numbers (Set 2):', even_numbers2)

is_disjoint = even_numbers.isdisjoint(whole_numbers)
print('Is the Whole and Even Numbers Disjoint?', is_disjoint) # False, because there are common items

is_disjoint = even_numbers2.isdisjoint(whole_numbers)
print('Is the Whole and Even Numbers (Set 2) Disjoint?', is_disjoint) # False, because there are common items


# Finding Intesection in sets

st1 = {'item1', 'item2', 'item3', 'item4'}
print('Set 1:', st1)

st2 = {'item3', 'item2'}
print('Set 2:', st2)

st3 = st1.intersection(st2) # {'item3', 'item2'}
print('Intersection 3:', st3)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print('Whole Numbers:', whole_numbers)

even_numbers = {0, 2, 4, 6, 8, 10}
print('Even Numbers:', even_numbers)

print('Interesection Numbers:', whole_numbers & even_numbers)

# Checking Subset and Superset

st1 = {'Item1', 'Item2', 'Item3', 'Item4'}
print('Set 1:', st1)

st2 = {'Item1', 'Item3'}
print('Set 2:', st2)

print('Is Set 2 subset of Set 1?', st2.issubset(st1)) #True
print('Is Set 1 superset of Set 2?', st1.issuperset(st2)) # True

# Check Difference Between Two Sets

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print('Whole Numbers:', whole_numbers)

even_numbers = {0, 2, 4, 6, 8, 10}
print('Even Numbers:', even_numbers)

# usign difference method
number_difference = whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}
print('Difference between Whole and Even Numbers:', number_difference)

# usign - symbol
number_difference = whole_numbers - even_numbers # {1, 3, 5, 7, 9}
print('Difference between Whole and Even Numbers:', number_difference)

# Finding Symmetric Difference Between Two Setts

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print('Whole Numbers:', whole_numbers)

even_numbers = {1, 2, 3, 4, 5}
print('Even Numbers:', even_numbers)

# usign symmetric_difference method
number_difference = whole_numbers.symmetric_difference(even_numbers) # {1, 3, 5, 7, 9}
print('Symmetric Difference between Whole and Even Numbers:', number_difference)

# usign ^ symbol
number_difference = whole_numbers ^ even_numbers # {1, 3, 5, 7, 9}
print('Symmetric Difference between Whole and Even Numbers:', number_difference)

