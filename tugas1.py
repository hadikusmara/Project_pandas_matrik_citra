nama = input("Nama  : ")
email = input("Email    : ")
jabatan = input("Jabatan    : ")
umur = input("Umur  : ")
print("Nama : ", nama)
print("Email : ", email)
print("Jabatan : ", jabatan)
print("Umur : ", umur)

print("Bilangan Terurut")
i = 0
x = int(input("Masukkan bilangan x = "))

while i < 18:
    i=i+3
    print(i)

print("Bilangan Terurut")
i = 19
x = int(input("Masukkan bilangan x = "))

while i > 3:
    i=i-2
    print(i)
    
# ordonya  harus sama 2x2
mat1 = [
    [1, 2],
    [3, 1],
]

mat2 = [
    [1, 4],
    [6, 7],
]

mat3 = []

for x in range(0, len(mat1)):
    row = []
    for y in range(0, len(mat1[0])):
        total = 0
        for z in range(0, len(mat1)):
            total = total + (mat1[x][z] * mat2[z][y])
        row.append(total)
    mat3.append(row)


for x in range(0, len(mat3)):
    for y in range(0, len(mat3[0])):
        print (mat3[x][y], end=' ')
    print ()
