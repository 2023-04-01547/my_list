my_list=[]
i=[10,20,30,40]
for x in i:
  my_list.append(x)
my_list.insert(1,15)
new_list=[50,60,70]
my_list.extend(new_list)
my_list.remove(70)
my_list.sort()
print(my_list)