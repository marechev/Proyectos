import json
from nltk.stem.snowball import SnowballStemmer
import os
import re
import math


class SAR_Project:
    """
    Prototipo de la clase para realizar la indexacion y la recuperacion de noticias
        
        Preparada para todas las ampliaciones:
          parentesis + multiples indices + posicionales + stemming + permuterm + ranking de resultado

    Se deben completar los metodos que se indica.
    Se pueden añadir nuevas variables y nuevos metodos
    Los metodos que se añadan se deberan documentar en el codigo y explicar en la memoria
    """

    # lista de campos, el booleano indica si se debe tokenizar el campo
    # NECESARIO PARA LA AMPLIACION MULTIFIELD
    fields = [("title", True), ("date", False),
              ("keywords", True), ("article", True),
              ("summary", True)]
    
    
    # numero maximo de documento a mostrar cuando self.show_all es False
    SHOW_MAX = 10

    #TESTCOMMENT FELIX
    def __init__(self):
        """
        Constructor de la classe SAR_Indexer.
        NECESARIO PARA LA VERSION MINIMA

        Incluye todas las variables necesaria para todas las ampliaciones.
        Puedes añadir más variables si las necesitas 

        """
        self.index = {
            'article': {},
            'title':{},
            'summary':{},
            'keywords':{},
            'date':{}
        } # hash para el indice invertido de terminos --> clave: termino, valor: posting list.
                        # Si se hace la implementacion multifield, se pude hacer un segundo nivel de hashing de tal forma que:
                        # self.index['title'] seria el indice invertido del campo 'title'.
        self.index2 = {
            'article': {},
            'title':{},
            'summary':{},
            'keywords':{},
            'date':{}
        }
        self.sindex = {
            'article': {},
            'title':{},
            'summary':{},
            'keywords':{},
            'date':{}
        } # hash para el indice invertido de stems --> clave: stem, valor: lista con los terminos que tienen ese stem
        self.ptindex = {
            'article': {},
            'title':{},
            'summary':{},
            'keywords':{},
            'date':{}
        } # hash para el indice permuterm.
        self.docs = {} # diccionario de documentos --> clave: entero(docid),  valor: ruta del fichero.
        self.score = {}
        self.weight = {
            'article': {
                'ntokens': 0,
                'npermu':0,
                'nstem':0
            },
            'title':{
                'ntokens': 0,
                'npermu':0,
                'nstem':0
            },
            'summary':{
                'ntokens': 0,
                'npermu':0,
                'nstem':0
            },
            'keywords':{
                'ntokens': 0,
                'npermu':0,
                'nstem':0
            },
            'date':{
                'ntokens': 0,
                'npermu':0,
                'nstem':0
            }
        } # hash de terminos para el pesado, ranking de resultados. puede no utilizarse
        self.news = {} # hash de noticias --> clave entero (newid), valor: la info necesaria para diferenciar la noticia dentro de su fichero (doc_id y posición dentro del documento)
        self.tokenizer = re.compile("\W+") # expresion regular para hacer la tokenizacion
        self.stemmer = SnowballStemmer('spanish') # stemmer en castellano
        self.show_all = False # valor por defecto, se cambia con self.set_showall()
        self.show_snippet = False # valor por defecto, se cambia con self.set_snippet()
        self.use_stemming = True # valor por defecto, se cambia con self.set_stemming()
        self.use_ranking = False  # valor por defecto, se cambia con self.set_ranking()
        
        self.docid = 0 # identificador del documento
        self.newid = 0 # identificador de la noticia
        self.ntokens = 0 
        self.npermuterms = 0 
        self.nstems = 0
        self.contadornoticias = 0 # contador de noticias indexadas

    ###############################
    ###                         ###
    ###      CONFIGURACION      ###
    ###                         ###
    ###############################


    def set_showall(self, v):
        """

        Cambia el modo de mostrar los resultados.
        
        input: "v" booleano.

        UTIL PARA TODAS LAS VERSIONES

        si self.show_all es True se mostraran todos los resultados el lugar de un maximo de self.SHOW_MAX, no aplicable a la opcion -C

        """
        self.show_all = v


    def set_snippet(self, v):
        """

        Cambia el modo de mostrar snippet.
        
        input: "v" booleano.

        UTIL PARA TODAS LAS VERSIONES

        si self.show_snippet es True se mostrara un snippet de cada noticia, no aplicable a la opcion -C

        """
        self.show_snippet = v


    def set_stemming(self, v):
        """

        Cambia el modo de stemming por defecto.
        
        input: "v" booleano.

        UTIL PARA LA VERSION CON STEMMING

        si self.use_stemming es True las consultas se resolveran aplicando stemming por defecto.

        """
        self.use_stemming = v


    def set_ranking(self, v):
        """

        Cambia el modo de ranking por defecto.
        
        input: "v" booleano.

        UTIL PARA LA VERSION CON RANKING DE NOTICIAS

        si self.use_ranking es True las consultas se mostraran ordenadas, no aplicable a la opcion -C

        """
        self.use_ranking = v




    ###############################
    ###                         ###
    ###   PARTE 1: INDEXACION   ###
    ###                         ###
    ###############################


    def index_dir(self, root, **args):
        """
        NECESARIO PARA TODAS LAS VERSIONES
        
        Recorre recursivamente el directorio "root" e indexa su contenido
        los argumentos adicionales "**args" solo son necesarios para las funcionalidades ampliadas

        """

        self.multifield = args['multifield']
        self.positional = args['positional']
        self.stemming = args['stem']
        self.permuterm = args['permuterm']

        for dir, subdirs, files in os.walk(root):
            for filename in files:
                if filename.endswith('.json'):
                    fullname = os.path.join(dir, filename)
                    self.index_file(fullname)

        ##########################################
        ## COMPLETAR PARA FUNCIONALIDADES EXTRA ##
        ##########################################
        if self.stemming:
            self.make_stemming()
        if self.permuterm:
            self.make_permuterm()


    def index_file(self, filename):
        """
        NECESARIO PARA TODAS LAS VERSIONES

        Indexa el contenido de un fichero.

        Para tokenizar la noticia se debe llamar a "self.tokenize"

        Dependiendo del valor de "self.multifield" y "self.positional" se debe ampliar el indexado.
        En estos casos, se recomienda crear nuevos metodos para hacer mas sencilla la implementacion

        input: "filename" es el nombre de un fichero en formato JSON Arrays (https://www.w3schools.com/js/js_json_arrays.asp).
                Una vez parseado con json.load tendremos una lista de diccionarios, cada diccionario se corresponde a una noticia

        """

        with open(filename) as fh:
            jlist = json.load(fh)

        #
        # "jlist" es una lista con tantos elementos como noticias hay en el fichero,
        # cada noticia es un diccionario con los campos:
        #      "title", "date", "keywords", "article", "summary"
        #
        # En la version basica solo se debe indexar el contenido "article"
        #
        #
        #
        #################
        ### COMPLETAR ###
        #################
        self.docid += 1
        posicion = 0
        numtokdate = 0
       
        for noticia in jlist:
            posicion += 1
            self.newid += 1
            
            if self.multifield:
                fie = noticia.keys()
                for field in fie:
                    for f,b in self.fields:
                        if f == field and b == True:
                            self.crearindex(noticia,filename,field,posicion)
                        elif field == 'date':
                            if self.index[field].get(noticia['date']) == None:
                                self.index[field][noticia['date']] = []
                                numtokdate+= 1
                            if self.newid not in self.index[field][noticia['date']]:
                                self.index[field][noticia['date']].append((self.newid))
            else:
                self.crearindex(noticia,filename,'article',posicion) 

            self.contadornoticias+=1
        if self.multifield:    
            self.weight['date']['ntokens'] += numtokdate


    def crearindex(self,noticia,filename,field,posicion):
        
        postoken = 0
        numTokens = 0
        contenido = noticia[field]
        tokens = self.tokenize(contenido)                        
        self.docs[self.docid] = filename
        for token in tokens:
            if self.index[field].get(token) == None:
                self.index[field][token] = []
                if self.positional:
                    self.index2[field][token] = []
                numTokens += 1
            if self.newid not in self.index[field][token]:
                self.index[field][token].append((self.newid))
            if self.positional:
                self.index2[field][token].append((self.newid,postoken))
                postoken += 1
        self.news[self.newid] = (self.docid,posicion)
        self.weight[field]['ntokens'] += numTokens

    def tokenize(self, text):
        """
        NECESARIO PARA TODAS LAS VERSIONES

        Tokeniza la cadena "texto" eliminando simbolos no alfanumericos y dividientola por espacios.
        Puedes utilizar la expresion regular 'self.tokenizer'.

        params: 'text': texto a tokenizar

        return: lista de tokens

        """
        return self.tokenizer.sub(' ', text.lower()).split()



    def make_stemming(self):
        
        fields = self.index.keys()
        for field in fields:
            claves = self.index[field].keys()
            contador=0
            for clave in claves:
                stem = self.stemmer.stem(clave)
                if stem in self.sindex[field].keys():
                    self.sindex[field][stem].append(clave)
                else:
                    self.sindex[field][stem] = [clave]
                    contador+=1
            self.weight[field]['nstems']=contador

    
    def make_permuterm(self):

        fields = self.index.keys()
        for field in fields:
            claves = self.index[field].keys()
            contador = 0
            for clave in claves:
                term = clave + "$"
                for x in range(len(term)):
                    cadena = term[x:]+term[:x]
                    if cadena in self.ptindex[field].keys():
                        self.ptindex[field][cadena].append(clave)
                    else:
                        self.ptindex[field][cadena] = [clave]
                        contador+=1
            self.weight[field]['npermu']=contador


    def show_stats(self):
        """
        NECESARIO PARA TODAS LAS VERSIONES
        
        Muestra estadisticas de los indices
        
        """
        #pass
        ########################################
        ## COMPLETAR PARA TODAS LAS VERSIONES ##
        ########################################
        print("========================================")
        print("Number of indexed days:",self.docid)
        print("----------------------------------------")
        print('Number of indexed news:',self.contadornoticias)
        print("----------------------------------------")
        print("TOKENS:")
        if self.multifield:
            print("     # of tokens in 'title':", self.weight['title']['ntokens'])
            print("     # of tokens in 'date':", self.weight['date']['ntokens'])
            print("     # of tokens in 'keywords':", self.weight['keywords']['ntokens'])
            print("     # of tokens in 'article':", self.weight['article']['ntokens'])
            print("     # of tokens in 'summary':", self.weight['summary']['ntokens'])
        else:
            print("     # of tokens in 'article':", self.weight['article']['ntokens'])
        print("----------------------------------------")
        if self.permuterm:
            print("PERMUTERMS:")
            if self.multifield:
                print("     # of permuterms in 'title':", self.weight['title']['npermu'])
                print("     # of permuterms in 'date':", self.weight['date']['npermu'])
                print("     # of permuterms in 'keywords':", self.weight['keywords']['npermu'])
                print("     # of permuterms in 'article':", self.weight['article']['npermu'])
                print("     # of permuterms in 'summary':", self.weight['summary']['npermu'])
            else:
                print("     # of permuterms in 'article':",self.weight['article']['npermu'])
            print("----------------------------------------")
        if self.stemming:
            print("STEMS:")
            if self.multifield:
                print("     # of stems in 'title':", self.weight['title']['nstems'])
                print("     # of stems in 'date':", self.weight['date']['nstems'])
                print("     # of stems in 'keywords':", self.weight['keywords']['nstems'])
                print("     # of stems in 'article':", self.weight['article']['nstems'])
                print("     # of stems in 'summary':", self.weight['summary']['nstems'])
            else:
                print("     # of stems in 'article':",self.weight['article']['nstems'])
            print("----------------------------------------")
        if self.positional: 
            print("Positional queries are allowed.")
        else:
            print("Positional queries are NOT allowed.")
        print("========================================")





    ###################################
    ###                             ###
    ###   PARTE 2.1: RECUPERACION   ###
    ###                             ###
    ###################################


    def solve_query(self, query, prev={}):
        """
        NECESARIO PARA TODAS LAS VERSIONES

        Resuelve una query.
        Debe realizar el parsing de consulta que sera mas o menos complicado en funcion de la ampliacion que se implementen


        param:  "query": cadena con la query
                "prev": incluido por si se quiere hacer una version recursiva. No es necesario utilizarlo.


        return: posting list con el resultado de la query

        """

        if query is None or len(query) == 0:
            return []

        ########################################
        ## COMPLETAR PARA TODAS LAS VERSIONES ##
        ########################################
        query = query.replace("(", "( ")
        query = query.replace(")", " )")
        query = query.replace("'"," ' ")
        query = query.replace('"', ' " ')
        consulta = query.split()

        listas = []
        aux=[]
        i = 0
        while i<len(consulta):
            if (consulta[i].startswith('date:') or consulta[i].startswith('keywords:') or 
            consulta[i].startswith('title:') or consulta[i].startswith('summary:')):
                if i+1<len(consulta):
                    if consulta[i+1] == "'":
                        pos = consulta[i+2:].index("'")
                        pos = pos + i + 1
                        aux.append(" ".join(consulta[i:pos+2]))
                        i = pos+1
                    elif consulta[i+1] == '"':
                        pos = consulta[i+2:].index('"')
                        pos = pos + i + 1
                        aux.append(" ".join(consulta[i:pos+2]))
                        i = pos+1
                    else:
                        aux.append(consulta[i])
                else:
                    aux.append(consulta[i])
            elif consulta[i] not in {'"',"'"}:
                aux.append(consulta[i])
            else:
                if consulta[i] == "'":
                    pos = consulta[i+1:].index("'")
                    pos = pos + i + 1
                    aux.append(" ".join(consulta[i:pos+1]))
                else:
                    pos = consulta[i+1:].index('"')
                    pos = pos + i + 1
                    aux.append(" ".join(consulta[i:pos+1]))
                i = pos
            i = i + 1
        consulta = aux
        #Creamos una lista que guarda la consulta tokenizada sustituyendo los términos por sus posting list 
        for i in range(0, len(consulta)):
            if consulta[i] not in {'OR', 'AND', 'NOT', '(', ')'}:
                listas.append(self.get_posting(consulta[i]))
            else:
                listas.append(consulta[i])
        i = 0
        #Bucle para resolver las subconsultas que están entre paréntesis 
        while(i<len(listas)):
            if listas[i] == "(":
                pabrir = 1
                pcerrar = 0            
                pospabrir = [] #para guardar la posición de los paréntesis que abren 
                pospcerrar = [] #para guardar la posición de los paréntesis que cierran
                pospabrir.append(i)
                pospcerrar.append(0)
                j = i + 1
                cierro = True
                while cierro: #bucle para encontrar el paréntesis que cierra la subconsulta 
                    if listas[j] == ")":
                        pcerrar = pcerrar + 1 
                        k = len(pospcerrar) - 1
                        seguir = True
                        while k>=0 and seguir:
                            if pospcerrar[k] == 0:
                                pospcerrar[k] = j
                                seguir = False
                            k = k - 1
                        if pabrir == pcerrar:
                            #i = j + 1
                            cierro = False
                    else:
                        if listas[j] == "(":
                            pospabrir.append(j)
                            pospcerrar.append(0)
                            pabrir = pabrir + 1 
                    j = j + 1   
                t = pabrir - 1
                while t>=0: #bucle para resolver las subconsultas que están entre paréntesis
                    x = pospabrir[t] + 1
                    y = pospcerrar[t] 
                    z = x
                    while z<y:
                        if listas[z] == "NOT":
                            del listas[z] 
                            listas[z] = self.reverse_posting(listas[z]) 
                            y = y - 1
                            #actualizamos las posiciones de los paréntesis
                            for d in range(0,len(pospabrir)): 
                                if pospabrir[d] > z:
                                    pospabrir[d] = pospabrir[d] - 1
                            for d in range(0,len(pospcerrar)):
                                if pospcerrar[d] > z:
                                    pospcerrar[d] = pospcerrar[d] - 1
                        z = z + 1
                    x = pospabrir[t] + 1
                    y = pospcerrar[t] 
                    z = x
                    while z<y:
                        if listas[z] == "AND":
                            aux = self.and_posting(listas[z-1], listas[z+1])
                            del listas[z]
                            del listas[z]
                            listas[z-1] = aux
                            y = y - 2
                            for d in range(0,len(pospabrir)):
                                if pospabrir[d] > z:
                                    pospabrir[d] = pospabrir[d] - 2
                            for d in range(0,len(pospcerrar)):
                                if pospcerrar[d] > z:
                                    pospcerrar[d] = pospcerrar[d] - 2
                        else:
                            if listas[z] == "OR":
                                aux = self.or_posting(listas[z-1], listas[z+1])
                                del listas[z]
                                del listas[z]
                                listas[z-1] = aux
                                y = y - 2
                                for d in range(0,len(pospabrir)):
                                    if pospabrir[d] > z:
                                        pospabrir[d] = pospabrir[d] - 2
                                for d in range(0,len(pospcerrar)):
                                    if pospcerrar[d] > z:
                                        pospcerrar[d] = pospcerrar[d] - 2
                            else:
                                z = z + 1
                    del listas[pospabrir[t]]
                    for d in range(0,len(pospcerrar)):
                        if pospcerrar[d] > pospabrir[t]:
                            pospcerrar[d] = pospcerrar[d] - 1
                    del pospabrir[t]
                    del listas[pospcerrar[t]]
                    for d in range(0,len(pospcerrar)):
                        if pospcerrar[d] > pospcerrar[t]:
                            pospcerrar[d] = pospcerrar[d] - 1
                    del pospcerrar[t]
                    t = t - 1
            else:
                i = i + 1
        i = 0
        while(i<len(listas)):
            if listas[i] == "NOT":
                del listas[i]
                listas[i] = self.reverse_posting(listas[i])
            i = i + 1
        i = 0
        while (i<len(listas)):
            if listas[i] == "OR":
                aux = self.or_posting(listas[i-1],listas[i+1])
                del listas[i-1]
                del listas[i]
                listas[i-1] = aux
            elif listas[i] == "AND":
                aux = self.and_posting(listas[i-1],listas[i+1])
                del listas[i-1]
                del listas[i]
                listas[i-1] = aux
            else:
                i = i + 1
        
        return(listas[0])


    def get_posting(self, term, field='article'):
        """
        NECESARIO PARA TODAS LAS VERSIONES

        Devuelve la posting list asociada a un termino. 
        Dependiendo de las ampliaciones implementadas "get_posting" puede llamar a:
            - self.get_positionals: para la ampliacion de posicionales
            - self.get_permuterm: para la ampliacion de permuterms
            - self.get_stemming: para la amplaicion de stemming


        param:  "term": termino del que se debe recuperar la posting list.
                "field": campo sobre el que se debe recuperar la posting list, solo necesario se se hace la ampliacion de multiples indices

        return: posting list

        """
        #pass
        ########################################
        ## COMPLETAR PARA TODAS LAS VERSIONES ##
        ########################################
        
        if term.startswith('date:'):
            field = 'date'
            term = term[5:]
        elif term.startswith('keywords:'):
            field = 'keywords'
            term = term[9:]
        elif term.startswith('title:'):
            field = 'title'
            term = term[6:]
        elif term.startswith('summary:'):
            field = 'summary'  
            term = term[8:]
        
        if (term.find("*") != -1) or (term.find("?") != -1):
            res = self.get_permuterm(term,field)
            
        elif  term.startswith("'"):
            term = term[:len(term)]
            res = self.get_positionals(term,field)
        
        elif term.startswith('"'):
            term = term[:len(term)]
            res = self.get_positionals(term,field) 
        
        elif self.use_stemming:
            res = self.get_stemming(term.lower(),field)
            

        else:
            res = self.index[field].get(term.lower(), [])
        
        res.sort()
        return res



    def get_positionals(self, terms, field):
        """
        NECESARIO PARA LA AMPLIACION DE POSICIONALES

        Devuelve la posting list asociada a una secuencia de terminos consecutivos.

        param:  "terms": lista con los terminos consecutivos para recuperar la posting list.
                "field": campo sobre el que se debe recuperar la posting list, solo necesario se se hace la ampliacion de multiples indices

        return: posting list

        """
        res = []
        if terms.startswith("'"):
            terms = terms[2:len(terms)-2]
            term = terms.split()
            aux = []
            i = 0
            while i<len(term)-1:
                aux.append(term[i])
                aux.append('AND')
                i = i + 1
            aux.append(term[i])
            query = " ".join(aux)
            res = self.solve_query(query)
        else:
            terms = terms[2:len(terms)-2]
            term = terms.split()
            aux = []
            i = 0
            while i<len(term)-1:
                aux.append(term[i])
                aux.append('AND')
                i = i + 1
            aux.append(term[i])
            query = " ".join(aux)
            aux2 = self.solve_query(query)
            for r in aux2:
                pos = []
                for t in term:
                    lista = self.index2[field][t]
                    pos2 = []
                    for idnoticia,posnoticia in lista:
                        if idnoticia == r:
                            pos2.append(posnoticia)
                    pos.append(pos2)
                for x in pos[0]:
                    posicion = x 
                    consecutivo = True
                    y = 1
                    while y < len(pos) and consecutivo:
                        posiciony = posicion + y
                        if posiciony not in pos[y]:
                            consecutivo = False
                        y = y + 1
                    if consecutivo:
                        if r not in res:
                            res.append(r)
        return res            
                    
        ########################################################
        ## COMPLETAR PARA FUNCIONALIDAD EXTRA DE POSICIONALES ##
        ########################################################


    def get_stemming(self, term, field):
        """
        NECESARIO PARA LA AMPLIACION DE STEMMING

        Devuelve la posting list asociada al stem de un termino.

        param:  "term": termino para recuperar la posting list de su stem.
                "field": campo sobre el que se debe recuperar la posting list, solo necesario se se hace la ampliacion de multiples indices

        return: posting list

        """
        
        stem = self.stemmer.stem(term)

        ####################################################
        ## COMPLETAR PARA FUNCIONALIDAD EXTRA DE STEMMING ##
        ####################################################
        palabras = self.sindex[field].get(stem.lower(), [])
        aux = []
        res = []
        for p in palabras:
            aux.extend(self.index[field].get(p.lower()))
        for a in aux:
            if a not in res:
                res.append(a)
        return res


    def get_permuterm(self, term, field):
        """
        NECESARIO PARA LA AMPLIACION DE PERMUTERM

        Devuelve la posting list asociada a un termino utilizando el indice permuterm.

        param:  "term": termino para recuperar la posting list, "term" incluye un comodin (* o ?).
                "field": campo sobre el que se debe recuperar la posting list, solo necesario se se hace la ampliacion de multiples indices

        return: posting list

        """

        ##################################################
        ## COMPLETAR PARA FUNCIONALIDAD EXTRA PERMUTERM ##
        ##################################################
        listapalabras = []
        esint = False
        if "*" in term:
            pos = term.find("*")
        else:
            esint = True
            pos = term.find("?")
        long = len(term)    
        buscar = term[pos+1:] + "$" + term[:pos]
        claves = self.ptindex[field].keys()
        #print(claves)
        #busca en ptindex todas las palabras que encajan con la busqueda
        for clave in claves:
            if clave.startswith(buscar) or clave==buscar:
                palabras = self.ptindex[field][clave]
                for pal in palabras:
                    if pal not in listapalabras:
                        if esint:
                            if long == len(pal):
                                listapalabras.append(pal)
                        else:
                            listapalabras.append(pal)

        clavesindex = self.index[field].keys()
        postinglist=[]
        #crea una posting list con el conjunto de postinglist de las palabras que encajaron con la busqueda
        for word in listapalabras:
            if word in clavesindex:
                listapost = self.index[field][word]
                for p in listapost:
                    if p not in postinglist:
                        postinglist.append(p)
        return postinglist



    def reverse_posting(self, p):
        """
        NECESARIO PARA TODAS LAS VERSIONES

        Devuelve una posting list con todas las noticias excepto las contenidas en p.
        Util para resolver las queries con NOT.


        param:  "p": posting list


        return: posting list con todos los newid exceptos los contenidos en p

        """

        #pass
        ########################################
        ## COMPLETAR PARA TODAS LAS VERSIONES ##
        ########################################
        lista = list(self.news.keys()) #lista que contiene todos las noticias
        for i in p: 
            lista.remove(i) #eliminar de la lista las noticias contenidas en p
        return lista

    def and_posting(self, p1, p2):
        """
        NECESARIO PARA TODAS LAS VERSIONES

        Calcula el AND de dos posting list de forma EFICIENTE

        param:  "p1", "p2": posting lists sobre las que calcular


        return: posting list con los newid incluidos en p1 y p2

        """
        
        #pass
        ########################################
        ## COMPLETAR PARA TODAS LAS VERSIONES ##
        ########################################
        res = []
        i = 0
        j = 0
        while i<len(p1) and j<len(p2): 
            if p1[i] == p2[j]:
                res.append(p1[i])
                i = i + 1
                j = j + 1
            elif p1[i] < p2[j]:
                i = i + 1
            else:
                j = j + 1
        return res

    def or_posting(self, p1, p2):
        """
        NECESARIO PARA TODAS LAS VERSIONES

        Calcula el OR de dos posting list de forma EFICIENTE

        param:  "p1", "p2": posting lists sobre las que calcular


        return: posting list con los newid incluidos de p1 o p2

        """

        
        #pass
        ########################################
        ## COMPLETAR PARA TODAS LAS VERSIONES ##
        ########################################
        res = []
        i = 0
        j = 0
        while i<len(p1) and j<len(p2):
            if p1[i] == p2[j]:                
                res.append(p1[i])
                i = i + 1
                j = j + 1
            elif p1[i] < p2[j]:
                res.append(p1[i])
                i = i + 1
            else:
                res.append(p2[j])
                j = j + 1
        while i<len(p1):
            res.append(p1[i])
            i = i + 1
        while j<len(p2):
            res.append(p2[j])
            j = j + 1
        return res

    def minus_posting(self, p1, p2):
        """
        OPCIONAL PARA TODAS LAS VERSIONES

        Calcula el except de dos posting list de forma EFICIENTE.
        Esta funcion se propone por si os es util, no es necesario utilizarla.

        param:  "p1", "p2": posting lists sobre las que calcular


        return: posting list con los newid incluidos de p1 y no en p2

        """

        
        pass
        ########################################################
        ## COMPLETAR PARA TODAS LAS VERSIONES SI ES NECESARIO ##
        ########################################################





    #####################################
    ###                               ###
    ### PARTE 2.2: MOSTRAR RESULTADOS ###
    ###                               ###
    #####################################


    def solve_and_count(self, query):
        """
        NECESARIO PARA TODAS LAS VERSIONES

        Resuelve una consulta y la muestra junto al numero de resultados 

        param:  "query": query que se debe resolver.

        return: el numero de noticias recuperadas, para la opcion -T

        """
        result = self.solve_query(query)
        print("%s\t%d" % (query, len(result)))
        return len(result)  # para verificar los resultados (op: -T)


    def solve_and_show(self, query):
        """
        NECESARIO PARA TODAS LAS VERSIONES

        Resuelve una consulta y la muestra informacion de las noticias recuperadas.
        Consideraciones:

        - En funcion del valor de "self.show_snippet" se mostrara una informacion u otra.
        - Si se implementa la opcion de ranking y en funcion del valor de self.use_ranking debera llamar a self.rank_result

        param:  "query": query que se debe resolver.

        return: el numero de noticias recuperadas, para la opcion -T
        
        """
        result = self.solve_query(query)
        if self.use_ranking:
            result = self.rank_result(result, query)   
            
        ########################################
        ## COMPLETAR PARA TODAS LAS VERSIONES ##
        ########################################
        print("========================================")
        print("Query:","'" + query + "'")
        query = query.replace("AND","")
        query = query.replace("OR","")
        query = query.replace("NOT","")
        query = query.replace("(","")
        query = query.replace(")","")
        terms = query.split()
        print("Number of results:",len(result))
        if self.show_snippet:
            posicion = 0
            for r in result:
                posicion = posicion + 1
                if not self.show_all and posicion > 10:
                    break
                print("---------------------------")
                docid = self.news[r][0]
                fichero = self.docs[docid]
                idNoticia = self.news[r][1]
                print("#"+str(posicion))
                score = 0
                if self.use_ranking:
                    #pass #rellenar si se implementa ranking y cambiar valor de score
                    score = self.score[r]
                print("Score:",score)
                print(r)
                numpal = 6 
                with open(fichero) as fich:
                    jlist = json.load(fich)
                    new = jlist[idNoticia-1]
                    print("Date:",new['date'])
                    print("Title:",new['title'])
                    print("Keywords:",new['keywords'])
                    articulo = self.tokenize(new['article'])
                    for term in terms:
                        pos = -1
                        for i,token in enumerate(articulo):
                            if token == term:
                                pos = i
                                break
                        resumen = ""
                        if pos >= 0:
                            for j in range(max((pos - numpal + 1), 0), min(pos + numpal, len(articulo) - 1)):
                                resumen = resumen + articulo[j] + " "
                            resumen = resumen + "... "
                            print(resumen,end="")
                    print()

                

    def rank_result(self, result, query):
        """
        NECESARIO PARA LA AMPLIACION DE RANKING

        Ordena los resultados de una query.

        param:  "result": lista de resultados sin ordenar
                "query": query, puede ser la query original, la query procesada o una lista de terminos


        return: la lista de resultados ordenada

        """

        #pass
        
        ###################################################
        ## COMPLETAR PARA FUNCIONALIDAD EXTRA DE RANKING ##
        ###################################################
        
        query = query.replace("NOT","")
        query = query.replace("AND","")
        query = query.replace("OR","")
        query = query.replace(")","")
        query = query.replace("(","")
        query = query.split()

        sum = 0
        n = len(self.news)
        #cálculo de idf
        idf = []
        for i in range(0,len(query)):
            df = len(self.index['article'][query[i]])
            idf.append(math.log10(n/df))
            sum = sum + idf[i]*idf[i]
        sum = math.sqrt(sum)

        #cálculo de la L-Norm de la consulta
        lnormconsulta = []
        for i in range(0, len(idf)):
            lnormconsulta.append(idf[i]/sum)
        lnormdoc = []

        #cálculo de la L-Norm de todos las noticias que devuelve la consulta
        for r in result:
            lnormdoc.append(self.distCoseno(r, query, idf))

        #cálculo de la similitud coseno entre la consulta y cada una de las noticias    
        w = []
        for i in range(0,len(lnormdoc)):
            sol = 0
            for j in range(0, len(lnormdoc[i])):
                sol = sol + lnormdoc[i][j]*lnormconsulta[j]
            w.append(sol)

        #ordenación de las listas en función del valor calculado de similitud coseno    
        res = []
        for j in range(0,len(w)):
            pos = 0
            for i in range(0,len(w)):
                if w[i]>w[pos]:
                    pos = i
            self.score[result[pos]] = w[pos]
            w[pos] = 0
            res.append(result[pos])
        return res
        

    def distCoseno(self, documento, query, idf):
        """
        NECESARIO PARA LA AMPLIACION DE RANKING

        Calcula L-Normalizada de los documentos 

        param:  "documento": uno de los documentos que devuelve la consulta
                "query": query procesada (Sin términos NOT, AND, etc.)
                "idf": idf de los tokens de la cansulta


        return: distancias similitud coseno

        """
        r=documento
        lnorm = []
        sum = 0
        for i in range(0, len(query)):
            token = query[i]
            dist = 0
            # abrimos fichero para calcular la frecuencia del token en el documento
            docid = self.news[r][0]
            fichero = self.docs[docid]
            posNoticia = self.news[r][1]
            with open(fichero) as fich:
                    jlist = json.load(fich)
                    noticia = jlist[posNoticia-1]
                    articulo = self.tokenize(noticia['article'])
                    f = articulo.count(token) #frecuencia del token en el documento
            t = 0
            if f>0:
                t = 1 + math.log10(f)
            dist = t*idf[i] #peso tf*idf
            sum = sum + dist*dist #valor necesario para calcular L-Norm
            lnorm.append(dist)
        sum = math.sqrt(sum)
        for i in range(0, len(lnorm)):
            lnorm[i] = lnorm[i]/sum
        return lnorm
