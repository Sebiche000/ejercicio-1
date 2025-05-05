total= float (input("ingrese el total de su compra"))
if total >=100 and total<199:
    descuento= total*(10/100)
    print ("su descuento es:", descuento)
elif total>=200:
        descuento= total *(20/100)
        print("su descuento es:",descuento)
elif total<99:
    print ("no aplica descuento")

        
        