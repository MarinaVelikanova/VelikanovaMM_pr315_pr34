z = input()
m = 1
x = 1
j = z[x:x+1]
for i in z:
    if i in j:
       m += 1
else:
   print(i, end='')
   print(m, end='')
m = 1
x += 1
j = z[x:x+1]
