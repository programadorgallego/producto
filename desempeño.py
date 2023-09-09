from os import system
system('cls')

def continuar():
  while True:
    try:
      rta=int(input('Continuar ?\n1.Sí\n2.No\n'))
      if rta==1 or rta==2:
        return rta
        break
      else:
        print('Valor no válido')
    except ValueError:
      print('valor no aceptado')

def validarOpcMenu():
  while True:
    try:
      rta=int(input('Elija la opción deseada:\n1.Registrar\n2.Consultar\n3.Actualizar\n4.Borrar\n'))
      if rta>=1 and rta<=4:
        return rta
        break
      else:
        print('Valor inválido')
    except ValueError:
      print('Valor no permitido')

productos = {}

while True:
  opc=validarOpcMenu()
  codigo=input('Código: ')
  if opc==1:
    if codigo not in productos:
      nombre=input('Nombre: ')
      productos[codigo]=nombre
      print('Producto agregado con éxito')
    else:
      print('Producto existente')
  elif opc==2:
    if codigo in productos:
      print(productos[codigo])
    else:
      print('Producto no registrado')
  elif opc==3:
    if codigo in productos:
      nombre=input('Nombre: ')
      productos[codigo]=nombre
    else:
      print('Producto no registrado')
  else:
    if codigo in productos:
      productos.pop(codigo)
      print('Producto borrado con éxito')
  
  continuacion=continuar()
  if continuacion==1:
    break

