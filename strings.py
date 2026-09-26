name = input('Enter your email ID: ')
domain = name[name.find("@") + 1:]
l_slice = domain[1:4]
l_split = name.split('.')

print(domain)
print(l_slice)
print(l_split)