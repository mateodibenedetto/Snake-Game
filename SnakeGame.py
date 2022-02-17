import turtle
import time
import random

retraso = 0.04
marcador = 0
marcador_alto = 0


''' Creamos la pantalla '''
s = turtle.Screen()
s.setup(650, 750) # le da un tamaño a la pantalla
s.bgcolor('gray')
s.title('Snake Game')


''' Creamos la serpiente '''
serpiente = turtle.Turtle()
serpiente.speed(1.2)
serpiente.shape('square')
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = 'stop' # cuando la serpiente teermine se queda en el lugar hasta reiniciar el juego
serpiente.color('green')


''' Crear la comida'''
comida = turtle.Turtle()
comida.shape('circle')
comida.color('red')
comida.shapesize(.8)
comida.penup()
comida.goto(0,100)
comida.speed(0)

''' Cuerpo de la serpiente '''
cuerpo = []

''' Creamos el marcador de puntos '''
texto = turtle.Turtle()
texto.speed(0)
texto.color('black')
texto.penup()
texto.hideturtle()
texto.goto(0, 320)
texto.write("Marcador: 0\tPuntaje más alto: 0", align="center", font=("verdana", 18, "normal"))
line = turtle.Turtle()
line.speed(0)
line.hideturtle()
line.penup()
line.goto(-330,300)
line.pendown()
line.pencolor('black')
line.pensize(1)
line.goto(330,300)

''' Movimientos '''
def arriba():
    serpiente.direction = 'up'

def abajo():
    serpiente.direction = 'down'

def derecha():
    serpiente.direction = 'right'

def izquierda():
    serpiente.direction = 'left'
    
    
''' Agregar Movimientos a la serpiente '''
def movimiento():
    if serpiente.direction == 'up':
        y = serpiente.ycor() # Devuelve la ubicacion de la cordenada Y
        serpiente.sety(y + 20) # Va a mover 20 espacios
    if serpiente.direction == 'down':
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    if serpiente.direction == 'right':
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    if serpiente.direction == 'left':
        x = serpiente.xcor()
        serpiente.setx(x - 20)
        
   
''' Asignar teclas y llamar a las funciones de miviento '''
s.listen() # Va a escuchar a la pantalla
s.onkeypress(arriba, "Up") # Cuando apretemos la flechita hacia arriba va a llamar a la funcion arriba()
s.onkeypress(abajo, "Down") # Cuando apretemos la flechita hacia abajo va a llamar a la funcion abajo()
s.onkeypress(derecha, "Right") # Cuando apretemos la flechita hacia la derecha va a llamar a la funcion derecha()
s.onkeypress(izquierda, "Left") # Cuando apretemos la flechita hacia la izquierda va a llamar a la funcion izquierda()


''' Acá es donde se va a estar ejecutando el juego hasta que haya una colision '''
while True:
    s.update() # Actualiza la pantalla, pe si la serpiente se mueve la pantalla se va a actualizar
    
    ''' Colisiones con las paredes '''
    if serpiente.xcor() > 300 or serpiente.xcor() < -300 or serpiente.ycor() > 280 or serpiente.ycor() < -350:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.speed(0)
        serpiente.home()
        serpiente.direction = 'stop'
        cuerpo.clear()
        # Volver el marcador a cero
        marcador = 0
        texto.clear()
        texto.write("Marcador:{}\tPuntaje más alto:{}".format(marcador, marcador_alto), align="center", font=("verdana", 18, "normal"))

    ''' Mandar comida a un punto aleatorio '''
    if serpiente.distance(comida) < 20: # Cuando la serpiente pasa cerca de la comida, la comida va a ir a un putno aleatorio
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        comida.goto(x,y)
          
        ''' Creamos el cuerpo de la serpiente'''
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape('square')
        nuevo_cuerpo.color('green')
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo) # Agregamos el nuevo_cuerpo a la lista de cuerpo
        
        ''' Funcionalidad para el marcador '''
        marcador += 10
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write("Marcador:{}\tPuntaje más alto:{}".format(marcador, marcador_alto), align="center", font=("verdana", 18, "normal"))
        
        
    total = len(cuerpo)
    # El range inicia en total -1, el 0 no se va a contar, y -1 es de a cuanto va ir recorriendo el for
    for index in range(total -1, 0, -1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x,y)   
    
    if total > 0: # Si hay algo en la lista osea que crecio el cuerpo entonces va a ir detras de la cabeza de la sepiente
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x,y)

    movimiento() # Mueve la serpiente
    
    ''' Colisiones con el cuepor de la serpiente '''
    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.speed(0)
            serpiente.home()
            serpiente.direction = 'stop'
            cuerpo.clear()
            
            marcador = 0 
            texto.clear()
            texto.write("Marcador:{}\tMarcador más alto:{}".format(marcador, marcador_alto),align="center", font=("verdana", 18, "normal"))
    
    time.sleep(retraso) # Modifica la velocidad
    
    
turtle.done()