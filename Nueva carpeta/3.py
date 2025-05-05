calificacion = float (input("ingrese su calificacion"))
if calificacion>=4.5:
    print("nota: Superior")
elif calificacion>=3.9 and calificacion<4.5:
    print ("nota: Alto")
elif calificacion>=3.0:
    print("nota: Basico")
elif calificacion<2.9:
    print("nota: Bajo")
