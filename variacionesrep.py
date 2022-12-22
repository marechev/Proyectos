# AUTORES: Maria del Mar Porras Echeverría
# (poner aquí el nombre o 2 nombres del equipo de prácticas

def variacionesRepeticion(elementos, cantidad):
    sol = [None]*cantidad
    def backtracking(longSol):
        if longSol == cantidad:
            yield sol.copy()
        else:
            for child in elementos:
                sol[longSol] = child
                yield from backtracking(longSol+1)
    yield from backtracking(0)

def permutaciones(elementos):
    cantidad = len(elementos)
    sol = [None]*cantidad
    def backtracking(longSol):
        if longSol == cantidad:
            yield sol.copy()
        else:
            for child in elementos:
                if child not in sol[:longSol]:
                    sol[longSol] = child
                    yield from backtracking(longSol+1)
    yield from backtracking(0)

def combinaciones(elementos,cantidad):
    sol = [None]*cantidad
    def backtracking(longSol,cont):
        if longSol == cantidad:
            yield sol.copy()
        else:
            for child in elementos:
                
                if child in elementos[cont:] and child not in sol[:longSol]:
                    #print(elementos[longSol:],child)
                    sol[longSol] = child
                    cont = elementos.index(child)
                    yield from backtracking(longSol+1,cont)
                
    yield from backtracking(0,0)

if __name__ == "__main__":  
    #[’tomate’, ’queso’, ’anchoas’]
    #[’tomate’, ’queso’, ’aceitunas’]
    #[’tomate’, ’anchoas’, ’aceitunas’]
    #[’queso’, ’anchoas’, ’aceitunas’]

    for x in permutaciones(['tomate','queso','anchoas']):
        print(x)
    print("Combinaciones:")
    for x in combinaciones(['tomate','queso','anchoas','aceitunas'],3):
        print(x)
    elem = ['tomate','queso','anchoas','aceitunas']
    