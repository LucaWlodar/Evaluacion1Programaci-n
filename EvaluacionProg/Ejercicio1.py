def intersect(lista1, lista2):
    listafinal = []
    for i in range(len(lista1)):
        moment = lista1[i]
        print(moment)
        moment2 = lista2[i]
        if moment == moment2:
            listafinal.append(moment)
    return listafinal

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
resultado = intersect(lista1, lista2)
print(resultado)
