print("Hello from my project!")
mass = [ "def2", "def1", "def3"]
mass.append("def4")
mass.remove("def1")
mass.sort()
len(mass)
print(mass)

for mas in mass:
    print(mas)


for i in range(5):
    print(i)

zv = 0

while(zv<5):
    zv+=1
    print("ZV")


for i in range(5):
    if i == 5:
        break
    elif i % 2==0:
        print("пойдет")

    else:
        print("еще")


def zv_dan (n):
    return n**2

print(zv_dan(5))
