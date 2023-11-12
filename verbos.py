import random
from tkinter import *

# La tabla de verbos irregulares
verb_table = [
    ["Arise", "Arose", "Arisen", "Levantarse"],
    ["Awake", "Awoke", "Awoken", "Despertarse"],
    ["Be", "Was / Were", "Been", "Ser"],
    ["Bear", "Bore", "Borne", "Soportar"],
    ["Beat", "Beat", "Beaten", "Golpear"],
    ["Become", "Became", "Become", "Llegar a ser"],
    ["Begin", "Began", "Begun", "Comenzar"],
    ["Bend", "Bent", "Bent", "Doblar"],
    ["Bet", "Bet", "Betted", "Apostar"],
    ["Bite", "Bit", "Bitten", "Morder"],
    ["Bleed", "Bled", "Bled", "Sangrar"],
    ["Blow", "Blew", "Blown", "Soplar"],
    ["Break", "Broke", "Broken", "Romper"],
    ["Bring", "Brought", "Brought", "Traer"],
    ["Broadcast", "Broadcast", "Broadcast", "Retransmitir"],
    ["Build", "Built", "Built", "Construir"],
    ["Burn", "Burnt", "Burnt", "Quemar"],
    ["Burst", "Burst", "Burst", "Estallar"],
    ["Buy", "Bought", "Bought", "Comprar"],
    ["Can", "Could", "Been able to", "Poder"],
    ["Catch", "Caught", "Caught", "Coger"],
    ["Choose", "Chose", "Chosen", "Escoger"],
    ["Come", "Came", "Come", "Venir"],
    ["Cost", "Cost", "Cost", "Costar"],
    ["Cut", "Cut", "Cut", "Cortar"],
    ["Deal", "Dealt", "Dealt", "Tratar"],
    ["Dig", "Dug", "Dug", "Cavar"],
    ["Do", "Did", "Done", "Hacer"],
    ["Draw", "Drew", "Drawn", "Dibujar"],
    ["Dream", "Dreamt", "Dreamt", "Soñar"],
    ["Drink", "Drank", "Drunk", "Beber"],
    ["Drive", "Drove", "Driven", "Conducir"],
    ["Eat", "Ate", "Eaten", "Comer"],
    ["Fall", "Fell", "Fallen", "Caer"],
    ["Feed", "Fed", "Fed", "Alimentar"],
    ["Feel", "Felt", "Felt", "Sentirse"],
    ["Fight", "Fought", "Fought", "Luchar"],
    ["Find", "Found", "Found", "Encontrar"],
    ["Flee", "Fled", "Fled", "Huir"],
    ["Fly", "Flew", "Flown", "Volar"],
    ["Forbid", "Forbade", "Forbidden", "Prohibir"],
    ["Forget", "Forgot", "Forgotten", "Olvidar"],
    ["Forgive", "Forgave", "Forgiven", "Perdonar"],
    ["Freeze", "Froze", "Frozen", "Congelar"],
    ["Get", "Got", "Got", "Conseguir"],
    ["Give", "Gave", "Given", "Dar"],
    ["Go", "Went", "Gone", "Ir"],
    ["Grow", "Grew", "Grown", "Crecer"],
    ["Hang", "Hung", "Hung", "Colgar"],
    ["Have", "Had", "Had", "Tener"],
    ["Hear", "Heard", "Heard", "Oir"],
    ["Hide", "Hid", "Hidden", "Ocultar"],
    ["Hit", "Hit", "Hit", "Golpear"],
    ["Hold", "Held", "Held", "Sostener"],
    ["Keep", "Kept", "Kept", "Guardar"],
    ["Kneel", "Knelt", "Knelt", "Arrodillarse"],
    ["Knit", "Knit", "Knit", "Hacer punto"],
    ["Know", "Knew", "Known", "Saber"],
    ["Lay", "Laid", "Laid", "Poner"],
    ["Lead", "Led", "Led", "Llevar"],
    ["Lean", "Leant", "Leant", "Inclinarse"],
    ["Learn", "Learnt", "Learnt", "Aprender"],
    ["Leave", "Left", "Left", "Dejar"],
    ["Lend", "Lent", "Lent", "Prestar"],
    ["Let", "Let", "Let", "Dejar"],
    ["Lie", "Lay", "Lain", "Tumbarse"],
    ["Light", "Lit", "Lit", "Encender"],
    ["Lose", "Lost", "Lost", "Perder"],
    ["Make", "Made", "Made", "Hacer"],
    ["May", "Might", "Might", "Poder"],
    ["Mean", "Meant", "Meant", "Significar"],
    ["Meet", "Met", "Met", "Conocer"],
    ["Must", "Had to", "Had to", "Deber"],
    ["Overcome", "Overcame", "Overcome", "Vencer"],
    ["Pay", "Paid", "Paid", "Pagar"],
    ["Put", "Put", "Put", "Poner"],
    ["Quit", "Quit", "Quit", "Dejar"],
    ["Read", "Read", "Read", "Leer"],
    ["Ride", "Rode", "Ridden", "Montar"],
    ["Ring", "Rang", "Rung", "Sonar"],
    ["Rise", "Rose", "Risen", "Levantarse"],
    ["Run", "Ran", "Run", "Correr"],
    ["Saw", "Sawed", "Sawn", "Serrar"],
    ["Say", "Said", "Said", "Decir"],
    ["See", "Saw", "Seen", "Ver"],
    ["Seek", "Sought", "Sought", "Buscar"],
    ["Sell", "Sold", "Sold", "Vender"],
    ["Send", "Sent", "Sent", "Enviar"],
    ["Set", "Set", "Set", "Colocar"],
    ["Shake", "Shook", "Shaken", "Agitar"],
    ["Shine", "Shone", "Shone", "Brillar"],
    ["Shoot", "Shot", "Shot", "Disparar"],
    ["Show", "Showed", "Shown", "Mostrar"],
    ["Shut", "Shut", "Shut", "Cerrar"],
    ["Sing", "Sang", "Sung", "Cantar"],
    ["Sink", "Sank", "Sunk", "Hundirse"],
    ["Sit", "Sat", "Sat", "Sentarse"],
    ["Sleep", "Slept", "Slept", "Dormir"],
    ["Smell", "Smelt", "Smelt", "Oler"],
    ["Speak", "Spoke", "Spoken", "Hablar"],
    ["Spell", "Spelt", "Spelt", "Deletrear"],
    ["Spend", "Spent", "Spent", "Gastar dinero"],
    ["Spill", "Spilt", "Spilled", "Derramarse"],
    ["Spit", "Spat", "Spat", "Escupir"],
    ["Split", "Split", "Split", "Partirse"],
    ["Spoil", "Spoilt", "Spoilt", "Estropear"],
    ["Spread", "Spread", "Spread", "Extender"],
    ["Stand", "Stood", "Stood", "Estar de pie"],
    ["Steal", "Stole", "Stolen", "Robar"],
    ["Stick", "Stuck", "Stuck", "Pegar"],
    ["Sting", "Stung", "Stung", "Picar"],
    ["Stink", "Stank", "Stunk", "Apestar"],
    ["Strike", "Struck", "Struck", "Golpear"],
    ["Swear", "Swore", "Sworn", "Jurar"],
    ["Sweat", "Sweat", "Sweat", "Sudar"],
    ["Sweep", "Swept", "Swept", "Barrer"],
    ["Swell", "Swelled", "Swollen", "Hincharse"],
    ["Swim", "Swam", "Swum", "Nadar"],
    ["Take", "Took", "Taken", "Coger"],
    ["Teach", "Taught", "Taught", "Enseñar"],
    ["Tear", "Tore", "Torn", "Rasgarse"],
    ["Tell", "Told", "Told", "Decir"],
    ["Think", "Thought", "Thought", "Pensar"],
    ["Throw", "Threw", "Thrown", "Tirar"],
    ["Understand", "Understood", "Understood", "Entender"],
    ["Upset", "Upset", "Upset", "Enfadar"],
    ["Wake", "Woke", "Woken", "Despertarse"],
    ["Wear", "Wore", "Worn", "Llevar puesto"],
    ["Weep", "Wept", "Wept", "Sollozar"],
    ["Win", "Won", "Won", "Ganar"],
    ["Wind", "Wound", "Wound", "Enrollar"],
    ["Write", "Wrote", "Written", "Escribir"]
]

def reset ():

    Guardado.config(text="")

    global random_verb
    global numero
    numero = random.choice(range(0,numero_filas))
    random_verb = verb_table[numero]

    global random_form
    random_form = random.choice(random_verb[:4])

    verb.config(text=random_form)

def bucle():

    global numero_filas
    global result
    global random_verb
    global numero
    global random_form
    global verb_table

    result = f"{Presente.get()},{Pasado.get()},{Participio.get()},{Traduccion.get()}"

    if result == f"{random_verb[0]},{random_verb[1]},{random_verb[2]},{random_verb[3]}":

        verb_table.pop(numero)
        Guardado.place(x=180, y=70)
        Guardado.config(text="BIEN")
        numero_filas = numero_filas - 1

        if numero_filas == 0:
            Guardado.config(text="TERMINADO, reinicia la app")

    else:      
        Guardado.place(x=100, y=70)
        Guardado.config(text=f"MAL. {random_verb[0]},{random_verb[1]},{random_verb[2]},{random_verb[3]}")
    
    numero = random.choice(range(0,numero_filas))
    random_verb = verb_table[numero]
    random_form = random.choice(random_verb[:4])
    verb.config(text=random_form)

    Presente.delete(0, 'end')
    Pasado.delete(0, 'end')
    Participio.delete(0, 'end')
    Traduccion.delete(0, 'end')
        

ventana = Tk()
ventana.geometry("400x200")     #Tamaño ventana
ventana.title("Reloj-Alarma Digital")     #Título ventana

Boton1 = Button(text="COMPROBAR", borderwidth=2, highlightthickness=2, highlightbackground="green", fg="red", width=10, font=("Arial", 10))  # Boton que establece la alarma
Boton1.place(x=100, y=130)
Boton1.config(command=bucle)

Boton2 = Button(text="NEXT", borderwidth=2, highlightthickness=2, highlightbackground="red", fg="red", width=5, font=("Arial", 10))  # Boton que resetea la alarma
Boton2.place(x=210, y=130)
Boton2.config(command=reset)

global Guardado
Guardado = Label(text="", fg="black", font=("Arial", 10))
Guardado.place(x=100, y=70)

global verb
verb = Label(text="", fg="black", font=("Arial", 10))
verb.place(x=175, y=90)

tx_presente = Label(text="Presente", fg="black", font=("Arial", 10))
tx_presente.place(x=90, y=20)
tx_pasado = Label(text="Pasado", fg="black", font=("Arial", 10))
tx_pasado.place(x=150, y=20)
tx_participio = Label(text="Participio", fg="black", font=("Arial", 10))
tx_participio.place(x=200, y=20)
tx_traducion = Label(text="Traduccion", fg="black", font=("Arial", 10))
tx_traducion.place(x=260, y=20)
tx = Label(text="Hecho por Jorge Baeza Díaz", fg="black", font=("Arial", 10))
tx.place(x=20, y=180)

Presente = Entry(width=7, font=("Arial", 10))
Presente.place(x=100, y=50)

Pasado = Entry(width=7, font=("Arial", 10))
Pasado.place(x=150, y=50)

Participio = Entry(width=7, font=("Arial", 10))
Participio.place(x=200, y=50)

Traduccion = Entry(width=7, font=("Arial", 10))
Traduccion.place(x=250, y=50)

# Elegir aleatoriamente un verbo de la lista
global random_verb
global numero_filas
numero_filas = 131
numero = random.choice(range(0,numero_filas))
random_verb = verb_table[numero]

# Elegir aleatoriamente una forma del verbo
global random_form
random_form = random.choice(random_verb[:4])

verb.config(text=random_form)

ventana.mainloop()
