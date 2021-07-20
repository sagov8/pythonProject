names = ['Santiago', 'Emma', 'Jane', 'Tatiana']

def imprimir():
    print('La lista tiene', len(names), 'personas')
    for name in names:
        print(name)
    else:
        print('No existen más nombres\n')

imprimir()
names.append('Duberney')
imprimir()

