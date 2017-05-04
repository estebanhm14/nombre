
def promedio(listaNotas):
  """
  Entra una lista de de notas [4,3,2,1] donde
  cada nota tenga un porcentaje del 25%
  y tiene como salida el resultado del promedio 
  """
  resultado = 0
  acumulador = 0

  v = 10

##  for x in listaNotas:
##    acumulador = acumulador + x
##
##    resultado = acumulador/len(listaNotas)
##
##  return resultado

#para sacar el promedio con un porcentaje en cada nota
def prom(notalista,porcentaje):
  """
  """
  r = 0
  a = 0
  posicion = range(len(notalista))

  for x in posicion:
    a = notalista[x]*porcentaje[x]
    r = r + a

  return resultado 
#==========================================================================

"""def max(lista):
  
  Saca el maximo de una lista

  resultado = 0
  posicion = range(lend(lista))

  for alguien in posicion:
    if(resultado < lista[alguien]

  return resultado """
