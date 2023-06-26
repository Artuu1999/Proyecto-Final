import random

#Se define la función que de la bienvenida y los nombres del equipo
def bienvenida():
    print("Bienvenid@ a nuestro ahorcado")
    print("somos Arturo Moreno y Juan Morales de Team comillas")


#Se define la funcion para que escoja una palabra al azar de la lista
def Palabra(diccionario):
    palabra = random.choice(diccionario).lower()
    return palabra

#Se pregunta la dificultad respecto a la cantidad de letras que va a tener la palabra
def dificultades(diccionario):
    a =input("Ingrese la dificultad en la que desea jugar (facil, normal, dificil): ").lower()
    palabra = Palabra(diccionario)
    b = 1
    while b == 1:
        if a == "facil":
            if len(palabra) > 7:
                b = 2
                return palabra
            else:
                palabra = Palabra(diccionario)
        elif a == "normal":
            if 5 < len(palabra) <= 7:
                b = 2
                return palabra
            else:
                palabra = Palabra(diccionario)
        elif a == "dificil":
            if len(palabra) <= 5:
                b = 2
                return palabra
            else:
                palabra = Palabra(diccionario)
        else:
            print("Ingrese bien la dificultad en la que desea jugar")
            dificultades(diccionario)

#Se define la función para que tome la palabra previamente escogida y ponga el número de rayas y se devuelva la lista para las palabras erroneas, el tablero y la palabra
def encontrarPalabra(diccionario:dict):
    palabra = dificultades(diccionario)
    tablero = ['_']*len(palabra)
    return tablero, palabra,[]

#Se muestra el escenario con numeros que seran reemplazados sucesivamente por los carácteres
escenario = \
'''
      ------- 
      |      |
    1        |
   4 2       |
    3        |
   657       |
   8 9       |
             |
          -------
          |     |
          -------
          '''

#Simbolos por los cuales se van a reemplazar los números
simbolos = '--|-||/\/\)'

#Va mostrando el escenario y si esta bien la letra reemplaza la letra por el simbolo
def escenarios(errores:int):
    escena = escenario
    for i in range (0, len(simbolos)):
      simbolo = simbolos[i] if i  < errores else ''
      escena = escena.replace(str(i), simbolo)
      print(escena)

#Se van a ir mostrando las letras erroneas con espacios
def tableros(tablero, letrasErroneas):
    for i in tablero:
        print(i, end=' ')
    print()
    print()
    if len(letrasErroneas) > 0:
        print('letras erroneas', *letrasErroneas)
        print()

#Se define la función para verificar si la letra esta bien, si ya esta, si no ingreso una letra o si ingreso más de dos
def letras(letrasErroneas):
    while True:
        letra = input("Ingrese una letra: ").lower()
        if letra in letrasErroneas:
            print("Ya intento esa letra, pruebe con otra")
        elif len(letra) != 1:
            print("Introducir solo una letra")
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print("Debe ingresar una letra")
        else:
            return letra

#Si la la palabra esta bien da un mensaje, sino la adivinaste da otro mensaje
def verificarLetra(letra,palabra,tablero,letrasErroneas:list):
    if letra in palabra:
        print("muy bien")
        actualizarTablero(letra, palabra, tablero)
    else:
        print("¡Lo mataste!, sigue intentando :(")
        letrasErroneas.append(letra)

#Enumera la palabra con indice para saber indice y letra, para ir reemplazando si la letra ingresada se encuentra en el tablero
def actualizarTablero(letra, palabra, tablero):
    for indice, letra1 in enumerate(palabra):
        if letra == letra1:
            tablero[indice] = letra
    
#Comprueba que no quede un espacio
def comrpoPalabra(tablero):
    return '_' not in tablero

#Todas las funciones se unen en esta en orden de secuencia 
def jugar(diccionario):
    tablero, palabra, letrasErroneas = encontrarPalabra(diccionario)
    while len(letrasErroneas) < len(simbolos):
        escenarios(len(letrasErroneas))
        tableros(tablero,letrasErroneas)
        letra = letras(letrasErroneas)
        verificarLetra(letra,palabra,tablero,letrasErroneas)
        if comrpoPalabra(tablero):
            print("Lo has logrado")
            break

#Se le pregunta a la persona si desea jugar otra vez
def jugarOtraVez():
    a = input("Desea jugar otra vez, ingrese sí o no: ").lower()
    if a == "sí":
        return a
    elif a == "no":
        return a
    else:
        print('Ingrese "sí", si desea seguir jugando. Ingrese "no" si no desea seguir jugando')
        jugarOtraVez()

#Da mensaje de despedida      
def despedida():
    print("¡Gracias por jugar, somos Team comillas!")

if __name__ == "__main__":

    #Lista con palabras por secciones paices, jugadores, desportes, marcas, etc...
    diccionario = ["perro", "gato", "ratón", "elefante", "jirafa", "cebra", "tigre", "león", "lobo", "oso",
    "rinoceronte", "hipopótamo", "camello", "cocodrilo", "serpiente", "araña", "arañazo", "murciélago", "pingüino", "loro",
    "pájaro", "águila", "halcón", "búho", "pollo", "gallina", "gallo", "pavo", "pato", "cisne",
    "rana", "sapo", "tortuga", "tiburón", "ballena", "delfín", "tucán", "colibrí", "hormiga", "abeja",
    "mosquito", "escarabajo", "ciervo", "cebrilla", "puma", "pantera", "caracol", "hipopótamo", "araña", "langosta",
    "gusano", "medusa", "pulpo", "calamar", "tortuga", "camarón", "langosta", "cocodrilo", "cocodrilo", "elefante",
    "jirafa", "cebra", "león", "lobo", "oso", "rinoceronte", "serpiente", "murciélago", "pingüino", "loro",
    "pájaro", "águila", "búho", "pollo", "gallina", "pavo", "pato", "cisne", "rana", "sapo",
    "tortuga", "tiburón", "ballena", "delfín", "tucán", "colibrí", "hormiga", "abeja", "mosquito", "escarabajo",
    "ciervo", "cebrilla", "puma", "pantera", "caracol", "hipopótamo", "araña", "langosta", "gusano", "medusa",
    "pulpo", "calamar", "tortuga", "camarón", "Afganistán", "Alemania", "Argentina", "Australia", "Brasil", "Canadá", "China", "Colombia", "Corea del Sur", "Cuba",
    "Egipto", "España", "Estados Unidos", "Francia", "India", "Indonesia", "Italia", "Japón", "México", "Noruega",
    "Países Bajos", "Perú", "Reino Unido", "Rusia", "Sudáfrica", "Suecia", "Suiza", "Tailandia", "Turquía", "Ucrania",
    "Arabia Saudita", "Emiratos Árabes Unidos", "Venezuela", "Vietnam", "Bélgica", "Chile", "Dinamarca", "Ecuador", "Finlandia", "Grecia",
    "Hungría", "Irlanda", "Israel", "Malasia", "Nueva Zelanda", "Polonia", "Portugal", "Singapur", "Argentina", "Australia",
    "Brasil", "Canadá", "China", "Colombia", "Corea del Sur", "Cuba", "Egipto", "España",
    "Estados Unidos", "Francia", "India", "Indonesia", "Italia", "Japón", "México", "Noruega", "Países Bajos", "Perú",
    "Reino Unido", "Rusia", "Sudáfrica", "Suecia", "Suiza", "Tailandia", "Turquía", "Ucrania", "Arabia Saudita",
    "Emiratos Árabes Unidos", "Venezuela", "Vietnam", "Bélgica", "Chile", "Dinamarca", "Ecuador", "Finlandia", "Grecia",
    "Hungría", "Irlanda", "Israel", "Malasia", "Nueva Zelanda", "Polonia", "Portugal", "Singapur",
    "correr", "saltar", "bailar", "cantar", "nadar", "escribir", "leer", "cocinar", "pintar", "aprender",
    "enseñar", "trabajar", "viajar", "comer", "dormir", "soñar", "reír", "llorar", "escuchar", "hablar",
    "observar", "pensar", "crear", "caminar", "jugar", "competir", "ganar", "perder", "ayudar", "amar",
    "odiar", "descansar", "relajarse", "respirar", "meditar", "ejercitar", "plantar", "cosechar", "construir", "destruir",
    "reciclar", "lavar", "barrer", "limpiar", "cuidar", "organizar", "planificar", "decorar", "programar", "investigar",
    "resolver", "compartir", "celebrar", "reunirse", "despedirse", "saludar", "comprar", "vender", "negociar", "ahorrar",
    "invertir", "viajar", "explorar", "disfrutar", "reproducir", "conducir", "navegar", "volar", "construir", "componer",
    "dibujar", "diseñar", "grabar", "editar", "filmar", "fotografiar", "enseñar", "aprender", "estudiar", "investigar",
    "entrenar", "competir", "participar", "colaborar", "ayudar", "voluntariar", "asistir", "entrevistar", "presentar", "negociar",
    "responder", "preguntar", "conversar", "discutir", "debatir", "convencer", "persuadir", "inspirar", "motivar", "alentar",
    "guiar", "dirigir", "liderar", "seguir", "aplaudir", "reconocer", "felicitar", "apoyar", "consolar", "perdonar",
    "agradecer", "celebrar", "disculpar", "desafiar", "superar", "adaptar", "innovar", "experimentar", "descubrir", "investigar",
    "solucionar", "resolver", "crear", "imaginarse", "soñar", "visualizar", "relajarse", "meditar", "desconectar", "concentrarse",
    "organizar", "planificar", "priorizar", "establecer", "evaluar", "analizar", "optimizar", "optimizar", "simplificar", "automatizar",
    "colaborar", "delegar", "motivar", "inspirar", "aprender", "enseñar", "crecer", "mejorar", "transformar", "empoderar",
    "perseverar", "arriesgarse", "innovar", "cambiar", "adaptarse", "Python", "programación", "código", "desarrollo", "programador", "lenguaje", "algoritmo", "sintaxis", "depuración", "compilador",
    "intérprete", "variable", "función", "clase", "objeto", "método", "librería", "framework", "repositorio", "git",
    "depósito", "ramificación", "confirmar", "solicitud", "API", "GUI", "debugging", "refactorización", "bucle", "condición",
    "declaración", "lista", "tupla", "diccionario", "conjunto", "cadena", "indexación", "slicing", "recursión", "iteración",
    "ciclo", "archivo", "entrada", "salida", "error", "excepción", "prueba", "depuración", "documentación", "comentario",
    "implementación", "compilación", "interpretación", "compilador", "intérprete", "IDE", "entorno", "desarrollo", "depurador", "versión",
    "control", "flujo", "paradigma", "orientación", "objetos", "herencia", "polimorfismo", "encapsulamiento", "abstracción", "modularidad",
    "biblioteca", "paquete", "módulo", "importar", "instalar", "actualizar", "pip", "virtualenv", "análisis", "datos",
    "estructuras", "algoritmos", "programación", "dinámica", "recursiva", "ordenamiento", "búsqueda", "grafos", "árboles", "búsqueda",
    "amplitud", "profundidad", "conexión", "base", "datos", "SQL", "MySQL", "PostgreSQL", "MongoDB", "SQLite",
    "web", "HTML", "CSS", "JavaScript", "framework", "Django", "Flask", "PyQt", "Pygame", "automatización",
    "el padrino", "el caballero oscuro", "pulp fiction", "cadena perpetua", "el bueno, el malo y el feo",
    "el club de la lucha", "12 hombres en pugna", "el rey león", "la lista de schindler", "forrest gump",
    "inception", "la naranja mecánica", "el gran dictador", "interstellar", "el viaje de chihiro",
    "taxi driver", "deseando amar", "fight club", "ciudad de dios", "matrix", "el silencio de los corderos",
    "seven", "la vida es bella", "v de vendetta", "gladiator", "parasite", "interestelar",
    "memento", "el pianista", "blade runner", "el gran lebowski", "rocky", "2001: odisea del espacio",
    "titanic", "los siete samuráis", "pulp fiction", "kill bill", "reservoir dogs", "el resplandor",
    "la guerra de las galaxias", "el golpe", "american history x", "apocalypse now", "scarface",
    "la trilogía del dólar", "el exorcista", "la pasión de cristo", "el club de los poetas muertos",
    "el secreto de sus ojos", "el gran hotel budapest",
    "Real Madrid", "Barcelona", "Manchester United", "Liverpool", "Bayern de Múnich",
    "Juventus", "AC Milan", "Inter de Milán", "Paris Saint-Germain", "Arsenal", "Chelsea", "Manchester City", 
    "Borussia Dortmund", "Atlético de Madrid", "Tottenham Hotspur", "Ajax", "Benfica", "Porto", "Roma", "Napoli", 
    "Millonarios", "Nacional", "América", "Santa Fe", "River Plate", "Boca Juniors", "Al-Nassr",
    "Lionel Messi", "Cristiano Ronaldo", "Neymar", "Robert Lewandowski", "Sergio Ramos",
    "Kevin De Bruyne", "Luka Modric", "Kylian Mbappé", "Erling Haaland", "Vinicius Jr.",
    "Mohamed Salah", "Virgil van Dijk", "Sadio Mané", "Harry Kane", "Manuel Neuer",
    "Pelé", "Diego Maradona", "Johan Cruyff", "Michel Platini", "Alfredo Di Stefano",
    "Franz Beckenbauer", "Ronaldo Nazário", "Zinedine Zidane", "Roberto Baggio",
    "Garrincha", "Ferenc Puskas", "George Best", "Marco van Basten",
    "James Rodríguez", "Radamel Falcao", "Carlos Valderrama", "Iván Córdoba", "Fredy Guarín",
    "Juan Guillermo Cuadrado", "Carlos Bacca", "Mario Yepes", "David Ospina", "Karim Benzema",
    "fútbol", "baloncesto", "tenis", "béisbol", "golf", "rugby", "críquet", "voleibol", "atletismo",
    "hockey", "boxeo", "automovilismo", "ciclismo", "natación", "esgrima", "surf", "ski", "snowboard",
    "patinaje artístico", "gimnasia", "karate", "taekwondo", "ajedrez", "halterofilia", "waterpolo",
    "salto con pértiga", "windsurf", "kayak", "lucha libre", "escalada", "snooker", "yoga", "squash",
    "triatlón", "salto de altura", "esquí acuático", "hándbol", "vela", "maratón", "bádminton", "paddle",
    "fórmula 1", "canotaje", "natación sincronizada", "pentatlón moderno", "hockey sobre hielo",
    "salto en longitud", "taekwondo", "tenis de mesa", "bobsleigh", "patinaje de velocidad",
    "salto de trampolín", "paracaidismo", "orientación", "tenis de playa", "softbol", "tiro con arco",
    "gimnasia rítmica", "carrera de obstáculos", "kickboxing", "salto ecuestre", "pentatlón de tiro",
    "carrera de motocross", "wrestling", "triatlón de invierno", "balonmano", "patinaje de velocidad en pista corta",
    "esquí de fondo", "rafting", "freestyle motocross", "buceo", "parapente", "cróquet", "bowling", "tenis de playa",
    "kárate", "salto en esquí", "rugby a siete", "judo", "pentatlón militar", "escalada en hielo",
    "Don Quijote de la Mancha", "1984", "Matar a un ruiseñor", "Orgullo y prejuicio", "El gran Gatsby",
    "Cien años de soledad", "Ulises", "En busca del tiempo perdido", "El señor de los anillos",
    "Crimen y castigo", "Las aventuras de Huckleberry Finn", "Moby Dick", "Hamlet", "El principito",
    "Anna Karenina", "La Odisea", "Romeo y Julieta", "Los hermanos Karamazov", "La divina comedia",
    "1984", "En el camino", "Orgullo y prejuicio", "El gran Gatsby", "Cien años de soledad", "Ulises",
    "En busca del tiempo perdido", "El señor de los anillos", "Crimen y castigo", "Las aventuras de Huckleberry Finn",
    "Moby Dick", "Hamlet", "El principito", "Anna Karenina", "La Odisea", "Romeo y Julieta",
    "Los hermanos Karamazov", "La divina comedia", "Moby Dick", "Hamlet", "El principito", "Anna Karenina",
    "La Odisea", "Romeo y Julieta", "Los hermanos Karamazov", "La divina comedia", "Moby Dick", "Hamlet",
    "Manzana", "Banana", "Naranja", "Uva", "Fresa", "Mango", "Piña", "Sandía", "Melón", "Kiwi",
    "Tomate", "Zanahoria", "Lechuga", "Papa", "Cebolla", "Espárragos", "Brócoli", "Espinaca", "Calabaza", "Remolacha",
    "Pollo", "Carne de res", "Cerdo", "Pescado", "Atún", "Salmón", "Camarones", "Huevo", "Queso", "Leche",
    "Arroz", "Pan", "Pasta", "Avena", "Maíz", "Lentejas", "Frijoles", "Garbanzos", "Cereal", "Aceite de oliva",
    "Nuez", "Almendra", "Avellana", "Castaña", "Coco", "Pistacho", "Semillas de girasol", "Chirimoya", "Pera", "Ciruela",
    "Durazno", "Melocotón", "Higo", "Mora", "Frambuesa", "Arándano", "Morcilla", "Chorizo", "Salchicha", "Jamón",
    "Tocino", "Sopa", "Ensalada", "Sándwich", "Tostada", "Tortilla", "Sushi", "Burrito", "Quesadilla", "Hamburguesa",
    "Pizza", "Hot dog", "Tacos", "Pollo asado", "Filete de ternera", "Lasagna", "Paella", "Ceviche", "Cangrejo",
    "Camarón", "Pulpo", "Langosta", "Helado", "Pastel", "Brownie", "Galleta", "Chocolate", "Yogur", "Flan",
    "Malteada", "Sorbete", "Mousse", "Tarta", "Mermelada", "Jugo", "Batido", "Smoothie", "Café", "Té",
    "Agua", "Refresco", "Cerveza", "Vino", "Whisky", "Ron", "Sidra", "Coctel", "Agua de coco", "Agua de horchata",
    "Champiñones", "Níspero", "Pepino", "Acelga", "Albahaca", "Aceitunas", "Alcachofa", "Anacardos", "Apio", "Berro",
    "Calabacín", "Canela", "Cilantro", "Coco rallado", "Dátiles", "Estragón", "Frutos secos", "Guisantes", "Habas", "Jengibre",
    "Kale", "Lima", "Mandarina", "Nabo", "Orégano", "Papaya", "Quinoa", "Rábano", "Salsa de soja", "Tamarindo",
    "Uvas pasas", "Vainilla", "Xoconostle", "Yema de huevo", "Zarzamora",
    "Medicina", "Ingeniería Civil", "Derecho", "Psicología", "Administración de Empresas", "Arquitectura", "Ingeniería Eléctrica",
    "Contabilidad", "Economía", "Ingeniería Mecánica", "Enfermería", "Ciencias de la Computación", "Comunicación Social",
    "Ingeniería Química", "Biología", "Educación Primaria", "Marketing", "Ciencias Ambientales", "Ingeniería Industrial",
    "Periodismo", "Ciencias Políticas", "Historia", "Matemáticas", "Ingeniería de Software", "Física", "Química",
    "Educación Física", "Farmacia", "Nutrición", "Ingeniería Biomédica", "Ingeniería de Telecomunicaciones",
    "Ingeniería de Sistemas", "Odontología", "Ciencias Sociales", "Lengua y Literatura", "Trabajo Social",
    "Ingeniería de Petróleo", "Ingeniería Ambiental", "Relaciones Internacionales", "Geología", "Música",
    "Ingeniería Aeroespacial", "Ingeniería de Alimentos", "Traducción e Interpretación", "Ingeniería Naval",
    "Diseño Gráfico", "Artes Plásticas", "Turismo", "Antropología", "Ciencias del Deporte",
    "Música", "Canción", "Instrumento", "Piano", "Guitarra", "Batería", "Bajo", "Violín", "Flauta", "Trompeta",
    "Saxofón", "Tambor", "Trombón", "Clarinete", "Cello", "Harp", "Ukulele", "Órgano", "Acordeón", "Gaita",
    "Arpa", "Banjo", "Xilófono", "Marimba", "Violonchelo", "Voz", "Cantante", "Guitarrista", "Baterista", "Pianista",
    "Compositor", "Director de orquesta", "Notas", "Escalas", "Acordes", "Melodía", "Ritmo", "Armonía", "Solfeo",
    "Partitura", "Improvisación", "Concierto", "Sinfonía", "Ópera", "Banda", "Coro", "Pop", "Rock", "Jazz",
    "Blues", "R&B", "Hip hop", "Reggae", "Salsa", "Bachata", "Merengue", "Cumbia", "Flamenco", "Country",
    "Electrónica", "Folk", "Clásica", "Funk", "Soul", "Indie", "Reguetón", "Trap", "Dance", "Metal",
    "Alternativa", "Góspel", "Punk", "Grunge", "Disco", "Techno", "House", "Rap", "Instrumental", "Festival",
    "Concurso", "Premio", "Grammy", "Billboard", "MTV", "Streaming", "Descarga", "Álbum", "Single", "EP",
    "Banda sonora", "Remix", "Tour", "Recital", "Estudio de grabación", "Productor", "Promotor", "Distribuidor", "Giradiscos",
    "Audífonos", "Amplificador", "Micrófono", "Mezcladora", "Cable", "Altavoz", "Guitarra eléctrica", "Piano digital", "Cajón",
    "Sintetizador", "Bajo eléctrico", "Afinador", "Pedal de efectos", "Cuerdas", "Púa", "Baquetas", "Notación musical", "Aplausos",
    "Fanáticos", "Concierto en vivo", "Artista revelación", "Banda local", "Canción del año", "Letra", "Estrofa", "Estribillo",
    "Intro", "Outro", "Bridge", "Verso", "Coro", "Interludio", "Arreglo", "Estudio de música", "Contrabajo", "Música clásica",
    "Música experimental", "Música contemporánea", "Música barroca", "Música renacentista", "Música minimalista", "Música coral", "Música religiosa",
    "Música sacra", "Música de película", "Música ambiental", "Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Freddie Mercury", "Michael Jackson",
    "Elvis Presley", "John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr", "Bob Dylan", "David Bowie",
    "Prince", "Madonna", "Stevie Wonder", "Frank Sinatra", "Johnny Cash", "Beyoncé", "Aretha Franklin", "Ray Charles",
    "Whitney Houston", "Ella Fitzgerald", "Billie Holiday", "Nat King Cole", "Miles Davis", "Louis Armstrong",
    "Jimi Hendrix", "Eric Clapton", "Carlos Santana", "Jimmy Page", "Robert Plant", "Freddy Mercury", "Elton John",
    "Queen", "The Beatles", "Rolling Stones", "Led Zeppelin", "Pink Floyd", "Nirvana", "AC/DC", "Metallica", "U2",
    "Guns N' Roses", "Bob Marley", "David Gilmour", "Bruce Springsteen", "Amy Winehouse", "Kurt Cobain", "Sting",
    "Carlos Gardel", "Ed Sheeran", "Justin Bieber", "J Balvin", "Maluma", "Shakira", "Carlos Vives", "Feid",
    "Bad Bunny", "Manuel Turizo", "Juanes", "Daddy Yankee", "Anuel AA",
    "Caja", "Lámpara", "Silla", "Mesa", "Computadora", "Teléfono", "Libro", "Bolígrafo", "Papel", "Reloj",
    "Cuchara", "Tenedor", "Cuchillo", "Plato", "Vaso", "Taza", "Pintura", "Cepillo", "Espejo", "Cámara",
    "Perfume", "Pendientes", "Collar", "Anillo", "Zapatos", "Bolsa", "Billetera", "Llaves", "Coche", "Bicicleta",
    "Patineta", "Pelota", "Raqueta", "Cuerda", "Guitarra", "Micrófono", "Altavoz", "Televisor", "Reproductor de DVD",
    "Cama", "Almohada", "Manta", "Toalla", "Secadora de pelo", "Secadora de ropa", "Plancha", "Aspiradora",
    "Herramientas", "Martillo", "Destornillador", "Cinta adhesiva", "Tijeras", "Caja de herramientas", "Laptop",
    "Teclado", "Ratón", "Monitor", "Impresora", "Escáner", "Disco duro", "Cable", "Enchufe", "Bombilla", "Aire acondicionado",
    "Refrigerador", "Lavadora", "Horno", "Microondas", "Licuadora", "Tostadora", "Batidora", "Exprimidor", "Sartén",
    "Olla", "Tetera", "Tabla de cortar", "Plancha de cocina", "Termómetro", "Cepillo de dientes", "Pasta de dientes",
    "Cepillo de pelo", "Champú", "Acondicionador", "Jabón", "Toalla sanitaria", "Pañales", "Crema hidratante",
    "Lápiz labial", "Sombra de ojos", "Rímel", "Base de maquillaje", "Delineador de ojos", "Crema para manos",
    "Desodorante", "Perfume", "Maquinilla de afeitar", "Cepillo de afeitar", "Crema de afeitar", "Papel higiénico",
    "Toallas de papel", "Fósforos", "Encendedor", "Cenicero", "Lápiz", "Cuaderno", "Globo", "Peluche", "Rompecabezas",
    "Ajedrez", "Tarjeta de felicitación", "Bolsa de regalo", "Película", "CD", "DVD", "Bocina", "Botella", "Bicicleta estática",
    "Baraja de cartas", "Lámina", "Caja de música", "Radiograbadora", "Guitarra eléctrica", "Casco", "Monopatín",
    "Cámara fotográfica", "Candelabro", "Lupa", "Ventilador", "Espejo retrovisor", "Lámpara de escritorio", "Jarrón",
    "Estatua", "Saxofón", "Bongó", "Campana",
    "Tokio", "Nueva York", "Londres", "París", "Pekín", "Roma", "Moscú", "Estambul", "Dubái", "Sídney", "San Petersburgo",
    "Los Ángeles", "Seúl", "Shanghái", "Río de Janeiro", "Cairo", "Ciudad de México", "Nueva Delhi", "Buenos Aires",
    "Amsterdam", "Berlín", "Bangkok", "Toronto", "Singapur", "Chicago", "Mumbai", "Madrid", "Viena", "Hong Kong",
    "Barcelona", "San Francisco", "Riad", "Kuala Lumpur", "Las Vegas", "Johannesburgo", "Marrakech", "Budapest",
    "Munich", "Vancouver", "Varsovia", "Ámsterdam", "Praga", "Copenhague", "Oslo", "Edimburgo", "Zúrich", "Atenas",
    "Estocolmo", "Beirut", "Helsinki", "Dublín", "Bruselas", "Reikiavik", "Lisboa", "Viena", "Bogotá", "Quito",
    "Lima", "Caracas", "Santiago", "Montevideo", "La Habana", "San Juan", "Buenos Aires", "Río de Janeiro",
    "São Paulo", "Lagos", "Nairobi", "Casablanca", "El Cairo", "Istambul", "Tel Aviv", "Dubai", "Abu Dhabi",
    "Doha", "Seúl", "Tokio", "Pekín", "Shanghái", "Hong Kong", "Singapur", "Bangkok", "Sydney", "Melbourne",
    "Auckland", "Wellington", "Toronto", "Vancouver", "Montreal", "Nueva York", "Los Ángeles", "San Francisco",
    "Chicago", "Las Vegas", "Miami", "Londres", "París", "Roma", "Barcelona", "Madrid", "Ámsterdam", "Berlín",
    "Múnich", "Viena", "Praga", "Zurich", "Estocolmo", "Moscú", "San Petersburgo", "Estambul", "El Cairo",
    "Apple", "Samsung", "Google", "Microsoft", "Amazon", "Facebook", "Coca-Cola", "Nike", "Adidas", "Louis Vuitton",
    "Gucci", "Chanel", "Rolex", "Toyota", "Mercedes-Benz", "BMW", "Audi", "Volkswagen", "Ferrari", "Lamborghini",
    "Porsche", "McDonald's", "Burger King", "KFC", "Starbucks", "Subway", "Sony", "Nintendo", "HP", "Dell",
    "Lenovo", "Intel", "Nvidia", "Canon", "Nikon", "GoPro", "Netflix", "Spotify", "Uber", "Airbnb",
    "PayPal", "Visa", "Mastercard", "American Express", "Tesla", "SpaceX", "Virgin", "Boeing", "Airbus",
    "L'Oréal", "Estée Lauder", "Maybelline", "Zara", "H&M", "GAP", "Prada", "Hermès", "Tiffany & Co.",
    "Cartier", "Tiffany & Co.", "Ralph Lauren", "Calvin Klein", "Tommy Hilfiger", "Adidas", "Puma", "Under Armour",
    "Hugo Boss", "Chanel", "Dior", "Gucci", "Yves Saint Laurent", "Bentley", "Jaguar", "Land Rover",
    "Ducati", "Chrysler", "Dodge", "Jeep", "Fender", "Gibson", "Yamaha", "Casio", "Tag Heuer", "Swatch"]

    #Se ejecuta el juego
    bienvenida()
    while True:
        jugar(diccionario)
        a = jugarOtraVez()
        if a == "sí":
            continue
        else:
            break
    despedida()
        