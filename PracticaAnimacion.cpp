#define PROYECTO "ISGI::S5E01::Animacion"

#include <iostream>
#include <sstream>
#include <Utilidades.h>

using namespace std;

static float angulo = 0;
static float angulo2 = 0;
static float lookatx = 3;
static float lookaty;
static float lookatz = 3;
static float radio;
static int tasaFPS = 60;
static GLuint palos,vagones,soporte,torus,tuerca,camxyz;


void init()
// Inicializaciones
{
	cout << "Iniciando " << PROYECTO << endl;
	cout << "GL version " << glGetString(GL_VERSION) << endl;

	// Inicializaciones 
	glClearColor(0.0f, 0.5f, 0.8f, 0.8f);
	
	glEnable(GL_DEPTH_TEST);
	glutInitWindowPosition(80, 80);
	glutInitWindowSize(800, 600);
	
	palos = glGenLists(1);
	glNewList(palos, GL_COMPILE);
	glColor3f(0.2, 0.2, 0.2);
	glutSolidCylinder(0.10, 1, 5, 10);
	glColor3fv(NEGRO);
	glutWireCylinder(0.10, 1, 5, 10);
	glEndList();

	vagones = glGenLists(1);
	glNewList(vagones, GL_COMPILE);
	glColor3f(0, 0.0625 * 9, 0.5);
	glutSolidTeapot(0.3);
	glColor3f(0.2, 0.2, 0.2);
	glutWireTeapot(0.3);
	glEndList();

	soporte = glGenLists(1);
	glNewList(soporte, GL_COMPILE);
	glColor3f(0.0625 * 7, 0, 1);
	glutSolidCube(1);
	glColor3fv(NEGRO);
	glutWireCube(1);
	glEndList();

	torus = glGenLists(1);
	glNewList(torus, GL_COMPILE);
	glColor3f(0.2, 0, 0.2);
	glutSolidTorus(0.15, 3, 20, 16);
	glColor3f(0.2, 0.2, 0.2);
	glutWireTorus(0.16, 3, 20, 16);
	glEndList();

	tuerca = glGenLists(1);
	glNewList(tuerca, GL_COMPILE);
	glColor3f(0.0625 * 7, 0, 1);
	glutSolidCylinder(0.5, 0.3, 20, 20);
	glColor3fv(NEGRO);
	glutWireCylinder(0.5, 0.3, 20, 1);
	glEndList();
}

void FPS()
{
	// Muestra en el titulo de la ventana los EPS actuales
	int ahora, tiempo_transcurrido;
	static int antes = glutGet(GLUT_ELAPSED_TIME);
	static int fotogramas = 0;

	// Cada vez que llamo a FPS se incrementa los fotogramas
	fotogramas++;

	// Calculo el tiempo que ha transcurrido entre dos fotogramas
	ahora = glutGet(GLUT_ELAPSED_TIME);
	tiempo_transcurrido = ahora - antes;

	// Si ha transcurrido mas de un segundo, muestro los FPS y reinicio el reloj
	if (tiempo_transcurrido > 1000) {
		// Modifico el titulo de la ventana 
		stringstream titulo;
		titulo << "FPS=" << fotogramas;
		glutSetWindowTitle(titulo.str().c_str());
		// Reiniciar el reloj y los fotogramas
		fotogramas = 0;
		antes = ahora;
	}
}


void display()
// Funcion de atencion al dibujo
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	// Seleccionar la MODELVIEW
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	// Situar y orientar la camara
	
	gluLookAt(lookatx,lookaty, lookatz, 0, 0, 0, 0, 1, 0);
	
	//TORUS 1
	glPushMatrix();
	glRotatef(angulo / 3, 0, 0, 1);
	glCallList(torus);
	glPopMatrix();
	//TORUS 2
	glPushMatrix();
	glRotatef(angulo / 3, 0, 0, 1);
	glTranslatef(0, 0, 1);
	glCallList(torus);
	glPopMatrix();
	//cilindro de en medio
	glPushMatrix();
	glRotatef(angulo/3, 0, 0, 1);
	glTranslatef(0, 0, -0.6);
	glColor3f(0.0625 * 4, 0, 1);
	glutSolidCylinder(0.25, 2.3, 5, 10);
	glColor3fv(NEGRO);
	glutWireCylinder(0.25, 2.3, 5, 10);
	glPopMatrix();
	//tuerca 1 y 2
	glPushMatrix();
	glTranslatef(0, 0, 1.3);
	glCallList(tuerca);
	glPopMatrix();
	glPushMatrix();
	glTranslatef(0, 0, -0.5);
	glCallList(tuerca);
	glPopMatrix();

	//PALOS UNEN DOS RUEDAS
	for (int i = 0; i < 16; i++) {
		glPushMatrix();
		glRotatef(angulo / 3, 0, 0, 1);
		glTranslatef(3 * cos(2 * PI / 16 * i), 3 * sin(2 * PI / 16 * i), 0);
		glCallList(palos);
		glPopMatrix();
		glEndList();
	}

	//ELICES
	for (int j = 0; j < 2; j++) {
		for (int i = 0; i < 16; i++) {
			glPushMatrix();
			glRotatef(angulo / 3 + (360 / 16 * i + 2.7), 0, 0, 1);
			if (j == 0) { glTranslatef(0, 1.5, 1); }
			else { glTranslatef(0, 1.5, 0); }

			glColor3f(0.0625 * i, 0, 1);
			glScalef(0.1, 3, 0.1);
			glutSolidCube(1);
			glColor3fv(NEGRO);
			glutWireCube(1);
			glPopMatrix();
		}
	}

	//vagones
	for (int i = 0; i < 16; i++) {
		glPushMatrix();
		glTranslatef(0, -0.3, 0.5);
		glRotatef(angulo / 3, 0, 0, 1);
		glTranslatef(3 * cos(2 * PI / 16 * i), 3 * sin(2 * PI / 16 * i), 0);
		glRotatef(8 * cos(angulo * PI / 180)*3 , 0, 0, 1);
		glRotatef(8 * sin(angulo * PI / 180)*3 , 0, 0, -1);
		glRotatef(angulo / 3, 0, 0, -1);
		glCallList(vagones);
		glPopMatrix();
		glEndList();
	}

	// Dibujo de la bandeja
	glPushMatrix();
	glTranslatef(0, -4.5, 0);
	glScalef(3.2, 0.1, 3.2);
	glColor3f(0.5, 0.5, 0.5);
	glutSolidCube(2.3);
	glColor3fv(NEGRO);
	glutWireCube(2.3);
	glPopMatrix();


	//soporte noria delante
	glPushMatrix();
	glRotatef(160, 0, 0, 1);
	glTranslatef(0, 2, 1.45);
	glScalef(0.2, 5, 0.1);
	glCallList(soporte);
	glPopMatrix();
	glPushMatrix();
	glRotatef(200, 0, 0, 1);
	glTranslatef(0, 2, 1.45);
	glScalef(0.2,5, 0.1);
	glCallList(soporte);
	glPopMatrix();
	glPushMatrix();
	glRotatef(160, 0, 0, 1);
	glTranslatef(0, 2.2, 1.9);
	glRotatef(20, 1, 1, 0);
	glScalef(0.2, 4.8, 0.1);
	glCallList(soporte);
	glPopMatrix();
	glPushMatrix();
	glRotatef(200, 0, 0, 1);
	glTranslatef(0, 2.2, 1.9);
	glRotatef(20, 1, 1, 0);
	glScalef(0.2, 4.8, 0.1);
	glCallList(soporte);
	glutWireCube(1);
	glPopMatrix();

	//soporte noria detras
	glPushMatrix();
	glRotatef(160, 0, 0, 1);
	glTranslatef(0, 2, -0.35);
	glScalef(0.2, 5, 0.1);
	glCallList(soporte);
	glPopMatrix();
	glPushMatrix();
	glRotatef(200, 0, 0, 1);
	glTranslatef(0, 2, -0.35);
	glScalef(0.2, 5, 0.1);
	glCallList(soporte);
	glPopMatrix();
	glPushMatrix();
	glRotatef(160, 0, 0, 1);
	glTranslatef(0, 2.2, -0.8);
	glRotatef(340, 1, 1, 0);
	glScalef(0.2, 4.8, 0.1);
	glCallList(soporte);
	glPopMatrix();
	glPushMatrix();
	glRotatef(200, 0, 0, 1);
	glTranslatef(0, 2.2, -0.8);
	glRotatef(340, 1, 1, 0);
	glScalef(0.2, 4.8, 0.1);
	glCallList(soporte);
	glPopMatrix();

	glutSwapBuffers();
	glFlush();
	FPS();
}

void reshape(GLint w, GLint h)
// Funcion de atencion al redimensionamiento
{
	glViewport(0, 0, w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	float fovy = asin((3-0.5) / radio) * 180 / PI;
	float razon = float (w) / h;
	gluPerspective(2*fovy, razon, 0.1, 100);
}


void onIdle()
{
	// Callback de atencion al evento idle

	// Sin control del tiempo
	// angulo += 0.1;

	// Con control del tiempo
	static const float vueltasSg = 0.3; // vueltas por segundo
	static int antes = glutGet(GLUT_ELAPSED_TIME);
	int ahora = glutGet(GLUT_ELAPSED_TIME);
	// Incremento de la variable temporal
	// delta = vueltas/sg * 360 * tiempo_transcurrido
	angulo += vueltasSg * 360 * (ahora - antes) / 1000;

	angulo2 = angulo2 + 0.1;
	lookatx = 10 * sin(angulo2 * PI / 180);//* cos((120 - angulo) * PI / 180);
	lookaty = 0;
	lookatz = 10 * cos(angulo2 * PI / 180);
	antes = ahora;

	//  Encolar un evento de dibujo
	glutPostRedisplay();
}

void onTimer(int tiempo)
{
	// Callback de atencion a la cuenta atras de un timer

	// Encolarse a si mismo
	glutTimerFunc(tiempo, onTimer, tiempo);

	onIdle();
}

int main(int argc, char** argv)
// Programa principal
{
	// Inicializaciones
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(600, 600);
	glutCreateWindow("PROYECTO");

	init();
	radio = sqrt(pow(lookatx, 2) + pow(lookaty, 2) + pow(lookatz, 2));
	// Registro de callbacks	
	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	//glutIdleFunc(onIdle);
	glutTimerFunc(1000 / tasaFPS, onTimer, 1000 / tasaFPS);

	// Bucle de atencion a eventos
	glutMainLoop();
}