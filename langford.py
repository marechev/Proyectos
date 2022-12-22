# -*- coding: utf-8 -*-

# AUTORES: Maria del Mar Porras Echeverria
# (poner aquí el nombre o 2 nombres del equipo de prácticas

import sys

def langford(N):
    N2   = 2*N
    seq  = [0]*N2
    def backtracking(num):
        if num<=0 :
            yield "-".join(map(str, seq))
        else:
           i = 0
           while i <= N2:
            if  i+num+1 < N2 and seq[i] == 0 and seq[i+num+1] == 0:
                seq[i] =num
                seq[i+num+1] = num

                yield from backtracking(num-1)
                seq[i] = 0
                seq[i+num+1] = 0
            i+=1

    if N%4 in (0,3):
        yield from backtracking(N)

if __name__ == "__main__":
    if len(sys.argv) not in (2,3):
        print('\nUsage: %s N [maxsoluciones]\n' % (sys.argv[0],))
        sys.exit()
    try:
        N = int(sys.argv[1])
    except ValueError:
        print('First argument must be an integer')
        sys.exit()
    numSolutions = None
    if len(sys.argv) == 3:
        try:
            numSolutions = int(sys.argv[2])
        except ValueError:
            print('Second (optional) argument must be an integer')
            sys.exit()

    i = 0
    for sol in langford(N):
        if numSolutions is not None and i>=numSolutions:
            break
        i += 1
        print(f'sol {i:4} ->',sol)
