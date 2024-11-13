#исход.дан.
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#изм.типа дан.и сортир.по алф.
students1=list(students)
sorted_list=sorted(students1)
ключи_словаря=sorted_list
#расчет ср.ариф.
a=grades[0]
b=grades[1]
c=grades[2]
d=grades[3]
e=grades[4]
a1=sum(a)/len(a)
b1=sum(b)/len(b)
c1=sum(c)/len(c)
d1=sum(d)/len(d)
e1=sum(e)/len(e)
значения_словаря=[a1, b1, c1, d1, e1]
#вывод
result=dict(zip(ключи_словаря, значения_словаря))
print(result)