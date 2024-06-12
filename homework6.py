my_dict = {'Yulia': 1995, 'Olia': 1973, 'Mania': 1993}
print(my_dict)
print(my_dict.get('Olia'))
print(my_dict.get('Katia'))
my_dict.update({'Verka': 1994, 'Dima': 1992})
print(my_dict)
a = my_dict.pop('Yulia')
print(a)
print(my_dict)

my_set = {2, 2, 3, 5, 6, 5, 3}
print(my_set)
my_set.update({8, 9})
my_set.remove(3)
print(my_set)
