d = {'sakib': 845165161, 'test': 1351651651, 'joe': 1611784151}
print(d)
print(d["sakib"])
d['copa']=51651981
print(d["copa"])
del d["test"]
# print(d["test"])

for key in d:
    print("Key:",key, "Value", d[key])