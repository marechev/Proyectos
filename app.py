import json
import csv
import problog

from flask import request
import flask
from flask import Flask, render_template
from flask_cors import CORS
from problog.program import PrologFile
from problog import get_evaluatable
import re


app = Flask(__name__)
CORS(app)

#@app.route('/')
#def index():
# return render_template('docprueba2.html')

@app.route('/test', methods=['GET','POST'])
def test():
    if request.method == "POST":
        output = request.get_json()
        edad = output['data']['edad']
        localiz = '" '+ output['data']['localizacion']+'"'
        listlibros = output['data']['librosSeleccionados']
        
        for libro in listlibros:
            # Acceder a los valores de cada diccionario
            isbn = libro['ISBN']
            titulo = '"'+ libro['Titulo']+'"'
            autor = '"'+ libro['Autor']+'"'
            idioma ='"'+  libro['Idioma']+'"'
            genero1 ='"'+  libro['Generos1']+'"'
            genero2 ='"'+  libro['Generos2']+'"'
            genero3 ='"'+  libro['Generos3']+'"'
            genero4 = '"'+ libro['Generos4']+'"'
            genero5 = '"'+ libro['Generos5']+'"'
            genero6 = '"'+ libro['Generos6']+'"'
            genero7 ='"'+  libro['Generos7']+'"'
            genero8 ='"'+  libro['Generos8']+'"'
            genero9 ='"'+  libro['Generos9']+'"'
            genero10 ='"'+  libro['Generos10']+'"'
            paginas = libro['Paginas']
            fecha_publicacion = libro['FechaPublicacion']

            nuevafila = [0,localiz,edad,isbn,10,titulo,autor,idioma,genero1,genero2,genero3,genero4,genero5,genero6,genero7,genero8, genero9,genero10,paginas,fecha_publicacion]
            with open('./tfgprueba.csv', 'a', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                escritor_csv.writerow(nuevafila)
       # isbntotales = [1576737330, 1551667010, 886774004]
       # return flask.Response(response=json.dumps(isbntotales), status=201)

        
        p = PrologFile("prueba3.pl")
        result = get_evaluatable().create_from(p).evaluate()
        print(result)
        similitudlibros = []
        similitudusuarios=[]
        for (res1,res2) in result.items():
            if str(res1).find('similitudLibros')!=-1:
                similitudlibros.append((str(res1),res2))
            else: 
                similitudusuarios.append((str(res1),res2))
        print(similitudlibros)
        print(similitudusuarios)
        max_similitud_libros = sorted(similitudlibros, key=lambda x:x[1])[:2]
        max_similitud_usuarios = sorted(similitudusuarios, key=lambda x:x[1])[:2]
        print(max_similitud_libros)
        print(max_similitud_usuarios)
        #SE TIENEN EN CUENTA LOS USUARIOS ANTES QUE LOS LIBROS
        isbntotales = []
        if len(listlibros)>1:
            isbn1 = max_similitud_libros[0][0].split('(')[1].split(',')[1][:-1]
            print(isbn1)
            usu1 = max_similitud_usuarios[0][0].split('(')[1].split(',')[1][:-1]
            usu2 = max_similitud_usuarios[1][0].split('(')[1].split(',')[1][:-1]
            print(usu1,usu2,isbn1)
            isbntotales.append(isbn1)
            with open('./tfgprueba.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(isbntotales)==3:
                        break
                    if row[0] == str(usu1) and row[3] not in isbntotales:
                        isbntotales.append(row[3])
                    if row[0] == str(usu2) and row[3] not in isbntotales:
                        isbntotales.append(row[3])    
            
        else:
            isbn1 = max_similitud_libros[0][0].split('(')[1].split(',')[1][:-1]
            isbn2 = max_similitud_libros[1][0].split('(')[1].split(',')[1][:-1]
            isbntotales.append(isbn1)
            isbntotales.append(isbn2)
            usu1 = max_similitud_usuarios[0][0].split('(')[1].split(',')[1][:-1]
            print(isbn1,isbn2,usu1)
            with open('./tfgprueba.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(isbntotales)==3:
                        break
                    if row[0] == str(usu1) and row[3] not in isbntotales:
                        isbntotales.append(row[3])
        print(isbntotales)
        return flask.Response(response=json.dumps(isbntotales), status=201)
        

if __name__ == '__main__':
    app.run("localhost", 8001)


"""        for clave, valor in result.items():
            if 'six' in str(clave):
                print("Algo")
        print(result.items())
        print(result.keys())
        lista = []
        for (res,res2) in result.items():
            if str(res).find('six')!=-1:
                print("porfin")
                lista.append((res,res2))
        
        print(lista)
        max_similitud_libros = sorted(result.items(), key=lambda x:x[1])[:2]
        print(max_similitud_libros)
        print(result)       
        return flask.Response(response=json.dumps(output), status=201)

"""