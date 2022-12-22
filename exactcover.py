# AUTORES: Maria del Mar Porras Echeverria
# (poner aquí el nombre o 2 nombres del equipo de prácticas

def exact_cover(listaConjuntos,U=None):
    if U is None:
        U = set().union(*listaConjuntos) # para saber qué universo tenemos
    N = len(listaConjuntos)
    solucion = []
    
    def backtracking(longSol, cjtAcumulado):
        if longSol >= N:
            if len(U) == len(set().union(cjtAcumulado)):
                yield solucion.copy()
        else:
            cjt = listaConjuntos[longSol]
            if cjt.isdisjoint(cjtAcumulado):
                solucion.append(cjt)
                
                yield from backtracking(longSol+1,cjtAcumulado|cjt)
                solucion.pop()
            yield from backtracking(longSol+1,cjtAcumulado)
        # COMPLETAR
        # consulta los métodos isdisjoint y union de la clase set,
        # podrías necesitarlos
        #isdisjoint es para saber si dos {}{} no tienen ningun elemento en comun
    yield from backtracking(0, set())

if __name__ == "__main__":
    cjtdcjts = [{"casa","coche","gato"},
                {"casa","bici"},
                {"bici","perro"},
                {"boli","gato"},
                {"coche","gato","bici"},
                {"casa", "moto"},
                {"perro", "boli"},
                {"coche","moto"},
                {"casa"}]
    for solucion in exact_cover(cjtdcjts):
        print(solucion)
