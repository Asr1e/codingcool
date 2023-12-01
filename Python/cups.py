cup4L = 0
cup7L = 0

cup4L = 4
cup7L = cup7L + cup4L
cup4L = 0
cup4L = 4
cup7L = cup7L + (cup4L - 1)
cup4L = cup4L - 3
cup7L = 0
cup7L = cup7L + cup4L
cup4L = 0
cup4L = 4
cup7L = cup7L + cup4L

print("there is now ", cup7L, "L in the 7L cup")

cup4L = 0
cup7L = 0

cup4L = 4
cup7L += cup4L
cup4L = 0
cup4L = 4
cup7L += (cup4L - 1)
cup4L -= 3
cup7L = 0
cup7L += cup4L
cup4L = 0
cup4L = 4
cup7L += cup4L

print(cup7L, "L")
