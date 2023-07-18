
:- use_module(library(db)).
:- use_module(library(lists)).
:- csv_load('tfgbdversion300.csv', 'tfgdb').


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
    contador_generos_comunes(Generos1,Generos2,Contador),
    Contador > 0,
    Contador =< 2,
    ISBN1 \= ISBN2.

0.20:: similitudLibros(ISBN1,ISBN2):-
    generos(ISBN1, Generos1),
    generos(ISBN2, Generos2),
    contador_generos_comunes(Generos1,Generos2,Contador),
    Contador >= 3,
    Contador < 7,
    ISBN1 \= ISBN2.

0.4:: similitudLibros(ISBN1,ISBN2):-
    generos(ISBN1, Generos1),
    generos(ISBN2, Generos2),
    contador_generos_comunes(Generos1,Generos2,Contador),
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
libros_en_comun(UserID1,UserID2,LibrosEnComun):-
    findall(Libro1, gustaISBN(Usuario1, Libro1), Lista1),
    findall(Libro2, gustaISBN(Usuario2, Libro2), Lista2),
    intersection(Lista1,Lista2,LibrosEnComun).


0.3 :: similitudUsuarios(UserID1, UserID2):-
    libros_en_comun(UserID1,UserID2,LibrosEnComun),
    length(LibrosEnComun,Len),
    Len > 0,
    Len < 2.

0.7 :: similitudUsuarios(UserID1, UserID2):-
    tfgdb(UserID2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_),
    libros_en_comun(UserID1,UserID2,LibrosEnComun),
    length(LibrosEnComun,Len),
    Len > 1.

%Similitud autores
listaautores([],[]).
listaautores([X|Resto],Res):-
    autor(X,Autor),
    listageneros(Resto,RestoRes),
    append(Autor,RestoRes,Res).

libros_no_comun(Usuario1, Usuario2,LibrosNoComun1,LibrosNoComun2) :-
    findall(Libro1, gustaISBN(Usuario1, Libro1), Lista1),
    findall(Libro2, gustaISBN(Usuario2, Libro2), Lista2),
    subtract(Lista1,Lista2,LibrosNoComun1),
    subtract(Lista2,Lista1,LibrosNoComun2).

0.25 :: similitudUsuarios(UserID1,UserID2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listaautores(Lista1,ListaAutores1),
    listaautores(Lista2,ListaAutores2),
    intersection(ListaAutores1,ListaAutores2,AutoresEnComun),
    length(AutoresEnComun,Len),
    Len > 0,
    Len < 2.

0.35 :: similitudUsuarios(UserID1,UserID2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listaautores(Lista1,ListaAutores1),
    listaautores(Lista2,ListaAutores2),
    intersection(ListaAutores1,ListaAutores2,AutoresEnComun),
    length(AutoresEnComun,Len),
    Len > 1,
    Len < 3.

0.6 :: similitudUsuarios(UserID1,UserID2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listaautores(Lista1,ListaAutores1),
    listaautores(Lista2,ListaAutores2),
    intersection(ListaAutores1,ListaAutores2,AutoresEnComun),
    length(AutoresEnComun,Len),
    Len > 2.

%si es menor de 20 se consifderan similares si se llevan dos años maximo
0.5 :: similitudUsuarios(UserID1,UserID2):-
    tieneEdad(UserID1,Edad1),
    tieneEdad(UserID2,Edad2),
    Edad1 =< 20,
    abs(Edad1-Edad2) < 3.

%si es mayor de 20 a 40
0.2 :: similitudUsuarios(UserID1,UserID2):-
    tieneEdad(UserID1,Edad1),
    tieneEdad(UserID2,Edad2),
    Edad1 > 20,
    Edad1 < 41,
    abs(Edad1-Edad2) < 6.

0.2 :: similitudUsuarios(UserID1,UserID2):-
    tieneEdad(UserID1,Edad1),
    tieneEdad(UserID2,Edad2),
    Edad1 > 40,
    Edad1 < 60,
    Edad2 > 40,
    Edad2 < 60.

0.2 :: similitudUsuarios(UserID1,UserID2):-
    tieneEdad(UserID1,Edad1),
    tieneEdad(UserID2,Edad2),
    Edad1 >= 60,
    Edad2 >= 60.


%Similitud usuarios: GENEROS
%notiene que ser mismo libro


listageneros([],[]).
listageneros([X|Resto],Res):-
    generos(X,Generos),
    listageneros(Resto,RestoRes),
    append(Generos,RestoRes,Res).

0.5:: similitudUsuarios(Usuario1, Usuario2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listageneros(Lista1,ListaGeneros1),
    listageneros(Lista2,ListaGeneros2),
    contador_generos_comunes(ListaGeneros1,ListaGeneros2,Cont),
    Cont > 8.


contador_menor_diez([], _, Contador,Baremo) :-
    Contador = 0.
contador_menor_diez([X|RestoLista1], Lista2, Contador,Baremo) :-
    resta_menor_diez(X, Lista2, ResultadoResta,Baremo),
    contador_menor_diez(RestoLista1, Lista2, ContadorResto,Baremo),
    Contador is ResultadoResta + ContadorResto.

% Predicado aux
resta_menor_diez(_, [], 0,Baremo).
resta_menor_diez(X, [Y|RestoLista2], ResultadoResta, Baremo) :-
    Resta is abs(X - Y),
    Resta =< Baremo,
    resta_menor_diez(X, RestoLista2, RestoResta,Baremo),
    ResultadoResta is 1 + RestoResta.
resta_menor_diez(X, [Y|RestoLista2], ResultadoResta,Baremo) :-
    Resta is abs(X - Y),
    Resta > Baremo,
    resta_menor_diez(X, RestoLista2, ResultadoResta,Baremo).

%%localizacion
0.15 :: similitudUsuarios(UserID1,UserID2):-
    esDe(UserID1,Local1),
    esDe(UserID2,Local1).

%idioma
listaidiomas([],[]).
listaidiomas([X|Resto],Res):-
    generos(X,Idioma),
    listaidiomas(Resto,RestoRes),
    append(Idioma,RestoRes,Res).

0.05 :: similitudUsuarios(Usuario1,Usuario2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listaidiomas(Lista1,ListaIdio1),
    listaidiomas(Lista2,ListaIdio2),
    flatten([ListaIdio1,ListaIdio2],Lista),
    todos_iguales(Lista).


todos_iguales([_]).
todos_iguales([X, X|Resto]) :-
    todos_iguales([X|Resto]).


contador_generos_comunes([], _, 0).
contador_generos_comunes([X | Resto], Lista2, Contador) :-
    member(X, Lista2),
    contador_generos_comunes(Resto, Lista2, ContadorResto),
    Contador is ContadorResto + 1.
contador_generos_comunes([_ | Resto], Lista2, Contador) :-
    contador_generos_comunes(Resto, Lista2, Contador).
contador_generos_comunes(Lista1,[],0).


%%tema paginas
listapag([],[]).
listapag([X|Resto],Res):-
    numpags(X,Pag),
    listapag(Resto,RestoRes),
    append(Pag,RestoRes,Res).

0.005 :: similitudUsuarios(Usuario1, Usuario2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listapag(Lista1,ListaPag1),
    listapag(Lista2,ListaPag2),
    contador_menor_diez(ListaPag1,ListaPag2,Cont,100),
    Cont>0,
    Cont<2.

0.008 :: similitudUsuarios(Usuario1, Usuario2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listapag(Lista1,ListaPag1),
    listapag(Lista2,ListaPag2),
    contador_menor_diez(ListaPag1,ListaPag2,Cont,100),
    Cont>1,
    Cont<3.

0.01 :: similitudUsuarios(Usuario1, Usuario2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listapag(Lista1,ListaPag1),
    listapag(Lista2,ListaPag2),
    contador_menor_diez(ListaPag1,ListaPag2,Cont,100),
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
    contador_menor_diez(ListaAnyo1,ListaAnyo2,Cont,10),
    Cont>0,
    Cont<2.

0.06 :: similitudUsuarios(Usuario1, Usuario2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listaanyos(Lista1,ListaAnyo1),
    listaanyos(Lista2,ListaAnyo2),
    contador_menor_diez(ListaAnyo1,ListaAnyo2,Cont,10),
    Cont>1,
    Cont<3.

0.09 :: similitudUsuarios(Usuario1, Usuario2):-
    libros_no_comun(Usuario1,Usuario2,Lista1,Lista2),
    listaanyos(Lista1,ListaAnyo1),
    listaanyos(Lista2,ListaAnyo2),
    contador_menor_diez(ListaAnyo1,ListaAnyo2,Cont,10),
    Cont>2.



%query(esDeLocal('spain')).
query(similitudUsuarios(187822,_)).
query(similitudLibros(385486804,_)).

%query(similitudUsuarios(2033,10560)).
%query(contador_menor_diez([20, 30, 100], [10, 35, 90], Contador,5)).
%query(listalibrosnocomun(70541,3917,A,B)).
%query(listageneros([671742515],_)).
%query(listageneros([679723226],_)).


