amount = int(input())
sum_faces = 0
for i in range(amount):
    shape = input().lower()
    if  shape == "tetrahedron":
        sum_faces += 4
    elif shape == "cube":
        sum_faces += 6
    elif shape == "octahedron":
        sum_faces += 8
    elif shape == "dodecahedron":
        sum_faces += 12
    elif shape == "icosahedron":
        sum_faces += 20
print(sum_faces)
