# Proyectos

Hay subidos 5 archivos los cuales son:
  - recomendador.pl --> El sistema recomendador hecho con ProbLog
  - interfazweb.html --> La interfaz web
  - jsonconimagen.json --> Base de datos en formato JSON utilizada por la web para mostrar datos de los libros
  - tfgprueba.csv --> Misma base de datos anterior, sin imagenes, en formato CSV, finalmente no se utiliza para nada porque he añadido los hechos al ProbLog
  - app.py --> Comunicador entre Web-Problog


Para que funcione desde web es necesario tener todos los archivos en una misma carpeta.
Desde esa carpeta hay que abrir dos terminales:
  - python -m http.server --> donde se aloja la web --> puerto 8000
  - python app.py --> actúa como un comunicador entre la página web y el sistema ProbLog --> puerto 8001

Si se quiere probar el sistema ProbLog sin la web habría que añadir querys:
  - similitudUsuarios(Usuario1, Usuario2) --> Usuario1 y/o 2 deben ser UserID del csv o, lo que viene a ser lo mismo, de los hechos Problog iniciales.
  - similitudLibros(ISBN1,ISBN2) --> ISBN 1 y/o 2 deben ser ISBN que esten en el csv o en los hechos ProbLog iniciales.
