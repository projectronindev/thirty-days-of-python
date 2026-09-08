# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print('IT Companies:', it_companies)
print('A:', A)
print('B:', B)
print('Ages:',age)

# 1
len_companies = len(it_companies)
print('Number of IT Companies:', len_companies)

# 2

it_companies.add('Twitter')
print('Updated IT Companies:', it_companies)

# 3

it_companies.discard('Amazon')
print('Updated IT Companies:', it_companies)

# 4 
# it_companies.remove('DXC') # will cause an error
it_companies.discard('DXC') # will not cause an error

# Level 2

# 1

joined_sets = A.union(B) # or A | B
print('Combination of A and B:', joined_sets)

# 2

intersection_sets = A.intersection(B) # or A & B
print('Intersection of A and B:', intersection_sets)

# 3

is_subset = A.issubset(B)
print('Is A subset of B?', is_subset)

# 4

is_disjoint = A.isdisjoint(B)
print('Are A and B disjoint sets?', is_disjoint)

# 5

join_AB = A | B
print('Join A with B:', join_AB)

join_BA = B | A
print('Join B with A:', join_BA)

# 6

symm_diff = A.symmetric_difference(B) # or A ^ B
print('Symmetric Difference between A and B:', symm_diff)

# 7 

del it_companies
del A
del B

# Error
# print('IT Companies:', it_companies)
# print('A:', A)
# print('B:', B)

# Level 3

# 1

age_set = set(age)
print('Length of Age List:', len(age))
print('Length of Age Set:', len(age_set))

# 3 

sentence = 'I am a teacher and I love to inspire and teach people'
print('Sample Sentence:', sentence)

split_sentence = sentence.split()
print('Sentence Split:', split_sentence)

set_sentence = set(split_sentence)
print('Sentence Set:', set_sentence)

print('Unique words in the sentence:', len(set_sentence))