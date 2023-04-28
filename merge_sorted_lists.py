list_1 = list(input("liste 1 için veri giriniz:"))

list_2 = list(input("liste 2 için veri giriniz:"))


total_list = []

for i in list_1:
    total_list.append(i)

for j in list_2:
    total_list.append(j)
        

print(total_list)
total_list.sort(reverse=False)

print(total_list)


