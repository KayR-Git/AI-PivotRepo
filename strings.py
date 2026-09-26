name = input('Enter your email ID: ')
domain = name[name.find("@") + 1:]
l_date = "2026-09-26"
l_slice = domain[1:4]
l_split = name.split('.')

l_dateslice = l_date[5:7]
l_fruits = "apple, Banana, Cherry".split(', ')[1]

print(domain)
print(l_slice)
print(l_split)
print(l_dateslice)
print(l_fruits)