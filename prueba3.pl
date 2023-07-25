
:- use_module(library(db)).
:- use_module(library(lists)).
%:- csv_load('tfgbdversion300.csv', 'tfgdb').
%:- csv_load('a.csv', 'tfgdb').
:- csv_load('tfgprueba.csv', 'tfgdb').
%Filtrado Colaborativo
gustaISBN(IDUser, ISBN) :-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion),
    Calificacion >= 6.


gustaTitulo(IDUser, Titulo) :-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion),
    Calificacion >= 6.

gustaGeneros(IDUser, [Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10]):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion),
    Calificacion >= 6.

gustaISBNGen(IDUser, ISBN, [Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10]):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion),
    Calificacion >= 6.

gustaISBNAutor(IDUser,ISBN, Autor):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion),
    Calificacion >= 6.

gustaISBNIdio(IDUser,ISBN,Idioma):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion),
    Calificacion >= 6.


gustaAutor(IDUser, Autor):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion),
    Calificacion >= 6.

gustaAnyo(IDUser,FechaPublicacion):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion),
    Calificacion >= 6.

gustaPaginas(IDUser,Paginas):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion),
    Calificacion >= 6.

gustaIdioma(IDUser,Idioma):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion),
    Calificacion >= 6.

esDe(IDUser,Location):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion).

tieneEdad(IDUser,Edad):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion).

%Filtrado basado en contenido
generos(ISBN,[Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10]):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion).

titulo(ISBN, Titulo):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion).

autor(ISBN, Autor):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion).

numpags(ISBN, Paginas):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion).

idioma(ISBN, Idioma):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion).

anyopubli(ISBN,FechaPublicacion):-
    tfgdb(IDUser,Location,Edad,ISBN,Calificacion,Titulo,Autor,Idioma,Generos1,Generos2,Generos3,Generos4,Generos5,Generos6,Generos7,Generos8,Generos9,Generos10,Paginas,FechaPublicacion).



%Similitud dos libros

0.5:: similitudLibros(ISBN1, ISBN2) :- 
    autor(ISBN1, Autor1),
    autor(ISBN2, Autor1),
    titulo(ISBN1,Titulo1),
    titulo(ISBN2,Titulo2),
    ISBN1 \= ISBN2.

%Similitud en generos 
0.05:: similitudLibros(ISBN1,ISBN2):-
    generos(ISBN1, Generos1),
    generos(ISBN2, Generos2),
    contador_generos(Generos1,Generos2,Contador),
    Contador > 0,
    Contador =< 2,
    ISBN1 \= ISBN2.

0.20:: similitudLibros(ISBN1,ISBN2):-
    generos(ISBN1, Generos1),
    generos(ISBN2, Generos2),
    contador_generos(Generos1,Generos2,Contador),
    Contador >= 3,
    Contador < 7,
    ISBN1 \= ISBN2.

0.4:: similitudLibros(ISBN1,ISBN2):-
    generos(ISBN1, Generos1),
    generos(ISBN2, Generos2),
    contador_generos(Generos1,Generos2,Contador),
    Contador >= 7,
    ISBN1 \= ISBN2.

0.05 :: similitudLibros(ISBN1,ISBN2):-
    anyopubli(ISBN1,Anyo1),
    anyopubli(ISBN2,Anyo2),
    abs(Anyo1-Anyo2) < 11,
    ISBN1 \= ISBN2.

0.05 :: similitudLibros(ISBN1,ISBN2):-
    idioma(ISBN1,Idioma1),
    idioma(ISBN2,Idioma1),
    ISBN1 \= ISBN2.

0.05 :: similitudLibros(ISBN1,ISBN2):-
    numpags(ISBN1,Num1),
    numpags(ISBN2,Num2),
    abs(Num1-Num2) < 150,
    ISBN1 \= ISBN2.

%Similitud usuarios: TITULO 
libros_en_comun(Usuario1,Usuario2,LibrosEnComun):-
    findall(Libro1, gustaISBN(Usuario1, Libro1), Lista1),
    findall(Libro2, gustaISBN(Usuario2, Libro2), Lista2),
    intersection(Lista1,Lista2,LibrosEnComun).


0.3 :: similitudUsuarios(Usuario1, Usuario2):-
    libros_en_comun(Usuario1,Usuario2,LibrosEnComun),
    Usuario1 \= Usuario2,
    length(LibrosEnComun,Len),
    Len > 0,
    Len < 2.

0.7 :: similitudUsuarios(Usuario1, Usuario2):-
    tfgdb(Usuario2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_),
    Usuario1 \= Usuario2,
    libros_en_comun(Usuario1,Usuario2,LibrosEnComun),
    length(LibrosEnComun,Len),
    Len > 1.

%Similitud autores

contador_autores(Usuario1, Usuario2,Contador):-
 findall(Autor1, (gustaISBNAutor(Usuario1, ISBN1, Autor1), \+ gustaISBNAutor(Usuario2, ISBN1, _)), ListaAutores1), 
 findall(Autor2, (gustaISBNAutor(Usuario2, ISBN2, Autor2), \+ gustaISBNAutor(Usuario1, ISBN2, _)), ListaAutores2), 
 intersection(ListaAutores1, ListaAutores2, AutoresComunes), 
 length(AutoresComunes, Contador).

libros_no_comun(Usuario1, Usuario2,LibrosNoComun1,LibrosNoComun2) :-
    findall(Libro1, gustaISBN(Usuario1, Libro1), Lista1),
    findall(Libro2, gustaISBN(Usuario2, Libro2), Lista2),
    subtract(Lista1,Lista2,LibrosNoComun1),
    subtract(Lista2,Lista1,LibrosNoComun2).

0.25 :: similitudUsuarios(Usuario1,Usuario2):-
    contador_autores(Usuario1,Usuario2,Len),
    Len > 0,
    Len < 2.

0.35 :: similitudUsuarios(Usuario1,Usuario2):-
    contador_autores(Usuario1,Usuario2,Len),
    Len > 1,
    Len < 3.

0.6 :: similitudUsuarios(Usuario1,Usuario2):-
    contador_autores(Usuario1,Usuario2,Len),
    Len > 2.

%si es menor de 20 se consifderan similares si se llevan dos años maximo
0.5 :: similitudUsuarios(Usuario1,Usuario2):-
    tieneEdad(Usuario1,Edad1),
    tieneEdad(Usuario2,Edad2),
    Edad1 =< 20,
    abs(Edad1-Edad2) < 3.

%si es mayor de 20 a 40

0.2 :: similitudUsuarios(Usuario1,Usuario2):-
    tieneEdad(Usuario1,Edad1),
    tieneEdad(Usuario2,Edad2),
    Edad1 > 20,
    Edad1 < 41,
    abs(Edad1-Edad2) < 6.

0.2 :: similitudUsuarios(Usuario1,Usuario2):-
    Usuario1 \= Usuario2,
    tieneEdad(Usuario1,Edad1),
    tieneEdad(Usuario2,Edad2),
    Edad1 > 40,
    Edad1 < 60,
    Edad2 > 40,
    Edad2 < 60.

0.2 :: similitudUsuarios(Usuario1,Usuario2):-
    tieneEdad(Usuario1,Edad1),
    tieneEdad(Usuario2,Edad2),
    Edad1 >= 60,
    Edad2 >= 60.


%Similitud usuarios: GENEROS
%notiene que ser mismo libro

contador_generos(Usuario1, Usuario2,Contador):-
 findall(Generos1, (gustaISBNGen(Usuario1, ISBN1, Generos1), \+ gustaISBNGen(Usuario2, ISBN1, _)), ListaGeneros1), 
 findall(Generos2, (gustaISBNGen(Usuario2, ISBN2, Generos2), \+ gustaISBNGen(Usuario1, ISBN2, _)), ListaGeneros2), 
 flatten(ListaGeneros1, ListaPlana1), 
 flatten(ListaGeneros2, ListaPlana2), 
 list_to_set(ListaPlana1, Conjunto1), 
 list_to_set(ListaPlana2, Conjunto2), 
 intersection(Conjunto1, Conjunto2, GenerosComunes), 
 length(GenerosComunes, Contador).



0.5:: similitudUsuarios(Usuario1, Usuario2):-
    contador_generos(Usuario1,Usuario2,Cont),
    Cont > 8.

%%localizacion
0.15 :: similitudUsuarios(Usuario1,Usuario2):-
    esDe(Usuario1,Local1),
    esDe(Usuario2,Local1).

%idioma
listaidiomas([],[]).
listaidiomas([X|Resto],Res):-
    generos(X,Idioma),
    listaidiomas(Resto,RestoRes),
    append(Idioma,RestoRes,Res).

comprobar_idiomas(Usuario1, Usuario2,ListaPlana):-
 findall(Idioma1, (gustaISBNIdio(Usuario1, ISBN1, Idioma1), \+ gustaISBNIdio(Usuario2, ISBN1, _)), ListaIdioma1), 
 findall(Idioma2, (gustaISBNIdio(Usuario2, ISBN2, Idioma2), \+ gustaISBNIdio(Usuario1, ISBN2, _)), ListaIdioma2), 
 flatten([ListaIdioma1,ListaIdioma2],ListaPlana).

todos_iguales([_]).
todos_iguales([X, X|Resto]) :-
    todos_iguales([X|Resto]).

0.05 :: similitudUsuarios(Usuario1,Usuario2):-
    comprobar_idiomas(Usuario1, Usuario2,Lista),
    todos_iguales(Lista).




%%tema paginas



contador_menor_cien([], _, Contador,Num) :-
    Contador = 0.
contador_menor_cien([X|RestoLista1], Lista2, Contador,Num) :-
    resta_menor_cien(X, Lista2, ResultadoResta,Num),
    contador_menor_cien(RestoLista1, Lista2, ContadorResto,Num),
    Contador is ResultadoResta + ContadorResto.

resta_menor_cien(_, [], 0,Num).
resta_menor_cien(X, [Y|RestoLista2], ResultadoResta, Num) :-
    Resta is abs(X - Y),
    Resta =< Num,
    resta_menor_cien(X, RestoLista2, RestoResta,Num),
    ResultadoResta is 1 + RestoResta.
resta_menor_cien(X, [Y|RestoLista2], ResultadoResta,Num) :-
    Resta is abs(X - Y),
    Resta > Num,
    resta_menor_cien(X, RestoLista2, ResultadoResta,Num).


listapag([],[]).
listapag([X|Resto],Res):-
    numpags(X,Pag),
    listapag(Resto,RestoRes),
    append(Pag,RestoRes,Res).

0.005 :: similitudUsuarios(Usuario1, Usuario2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listapag(Lista1,ListaPag1),
    listapag(Lista2,ListaPag2),
    contador_menor_cien(ListaPag1,ListaPag2,Cont,100),
    Cont>0,
    Cont<2.

0.008 :: similitudUsuarios(Usuario1, Usuario2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listapag(Lista1,ListaPag1),
    listapag(Lista2,ListaPag2),
    contador_menor_cien(ListaPag1,ListaPag2,Cont,100),
    Cont>1,
    Cont<3.

0.01 :: similitudUsuarios(Usuario1, Usuario2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listapag(Lista1,ListaPag1),
    listapag(Lista2,ListaPag2),
    contador_menor_cien(ListaPag1,ListaPag2,Cont,100),
    Cont>2.

%%tema anyopubli
condicion(X,Res):-
    X < 10,
    Res is X + 100.
condicion(X,Res):-
    X > 9,
    Res is X.

listaanyos([],[]).
listaanyos([X|Resto],Res):-
    anyopubli(X,Anyo),
    listaanyos(Resto,RestoRes),
    condicion(Anyo,AnyoRes),
    append(AnyoRes,RestoRes,Res).

0.02 :: similitudUsuarios(Usuario1, Usuario2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listaanyos(Lista1,ListaAnyo1),
    listaanyos(Lista2,ListaAnyo2),
    contador_menor_cien(ListaAnyo1,ListaAnyo2,Cont,10),
    Cont>0,
    Cont<2.

0.06 :: similitudUsuarios(Usuario1, Usuario2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listaanyos(Lista1,ListaAnyo1),
    listaanyos(Lista2,ListaAnyo2),
    contador_menor_cien(ListaAnyo1,ListaAnyo2,Cont,10),
    Cont>1,
    Cont<3.

0.09 :: similitudUsuarios(Usuario1, Usuario2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listaanyos(Lista1,ListaAnyo1),
    listaanyos(Lista2,ListaAnyo2),
    contador_menor_cien(ListaAnyo1,ListaAnyo2,Cont,10),
    Cont>2.


query(similitudUsuarios(0,B)):-
    tfgdb(B,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_),
    B \= 0.
query(similitudLibros(ISBN,_)):-
   tfgdb(0,_,_,ISBN,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_).
%query(similitudLibros(425184226,812550757)).
%query(similitudUsuarios(265313,270713)).
%query(gustaISBN(0,_)).
%books1bestbooks


