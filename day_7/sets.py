#day 7 set Exercises 

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print('it companies set length: ', len(it_companies))
it_companies.add('twitter') #adding one item to a set
it_companies.update(['Netflix', 'Firefox']) #addint multiple items to a set
it_companies.remove('Apple')
print('it companies: ', it_companies)
#discard and remove both delete an item but discard doesnt give an error if it fails

#Exercise 2
joined_set = A.union(B)
print('Intersections between A and B set: ', A.intersection(B))
print('is A subset of B?', A.issubset(B))
print('are A and B disjoint sets?', A.isdisjoint(B))

join_AwithB = A.union(B)
join_BwithA = B.union(A)
print('symmetric difference between A and B', A.symmetric_difference(B))

del A
del B

#Exercise 3

ages_set = set(age)
print(ages_set)
age_lst_len = str(len(age))
age_set_len = str(len(ages_set))
print(f'Age set length: ', age_set_len, '\nAge List length: ', age_lst_len)

#a string is an ordered unchangeable 'string' of letters or text 
#a list is ordered changeable collection of items
#a tuple is an ordered but unchangeable set of data or items 
#a set is unordered changeable set of unique items it doesnt allow duplicates

sentence = "I am a teacher and I love to inspire and teach people."
unique_words = len(set(sentence.split()))
print('unique words: ', unique_words)