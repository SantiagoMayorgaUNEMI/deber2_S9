
from Menu import principal

Salida = principal()
list  = ["1) Saludo","2) Variables","3) Conversiones","4) Concatenacion","5) Operadores matematicos","6) Cadenas","7) Tuplas",
         "8) lista","9)Diccionario", "10)LenData",
         "11)Condicional if-else-elif", "12)Funciones", "13)Operadores Lógicos","14)Operadores Ternario", "15)IF con tupla", "16)Función Range",
         "17)Bucle for", "18)Factorial de un número", "19)Bucle While", "20)Sentencias", "21)Generador yiel",
         "22)Generador yiel from", "23)Excepciones", "24)Sentencia Raise", "25)Importaciones","26)Prueba Paquetes",
         "27)Programación orientada a objeto", "28)Constructor en clases","29)Encapsulamiento de variable",
         "30)Encapsulamiento de metodos en clases","31)Métodos Accesores","32)Método de clase __STR__","33)Herencia"
         ,"34)Método Super()","35)Principio de Sustitución","36)Herencia Multiple","37)Polimorfismo","38)Relaciones entre clases","0) Salir"]

opcion = ""
while opcion != "0":
    opcion = Salida.menu(list,"***Menú de opciones***")

    if opcion == "1":
        print("Hola Mundo")
        print("            ")


    elif opcion == "2":
        listVar = ["1) Nombre","2) Edad","3) Sueldo","0) Salir"]
        opcvar = ""
        while opcvar != "0":
            opcvar = Salida.menu(listVar,"---Menu en Varaiables---")
            if opcvar == "1":
                nombre = "Santiago Mayorga"
                print(nombre)
            elif opcvar == "2":
                edad = 20
                print(edad)
                print("ªªªValores Booleanosªªª")
                edad = True
                print(edad)
            elif opcvar == "3":
                sueldo = 205.45
                print(sueldo)
        print("            ")

    elif opcion == "3":
        listCon = ["1) Concatenacion de char ","2) Conversion de char a int ","3) Float a int ","4) Char a float","5) leer un int","0) Salir"]
        opcCon = ""
        while opcCon != "0":
            opcCon = Salida.menu(listCon, "--- Menu de Conversiones ---")
            if opcCon == "1":
                numero1 = "35"
                numero2 = "18"
                print(numero2 + numero1)
            elif opcCon == "2":
                numero1 = "35"
                numero2 = "18"
                numero1 = int(numero1)
                numero2 = int(numero2)
                print(numero1 + numero2)
            elif opcCon == "3":
                sueldo = 456.23
                sueldoint = int(sueldo)
                print(sueldoint)
            elif opcCon == "4":
                valor = "4500.56"
                valordecimal = float(valor)
                print(valordecimal * 3)
            elif opcCon == "5":
                edad = 100
                print(len(str(edad)))
        print("              ")
    elif opcion == "4":
        print("--Concatenacion Simple--")
        texto1 = "Hola soy"
        texto2 = "Santaigo Mayorga"
        textend = texto1 + " " + texto2
        print(textend)

        print("--Concatenacion con comodines--")
        print("Me presento: %s %s" % (texto1, texto2))

        print("--Concatenacion .format -1-")
        presentend = "Presentacion: {0} {1}".format(texto1, texto2)
        print(presentend)

        print("--Concatenacion .format -2-")
        presentend2 = "Presentacion: {x} {y}".format(x=texto1, y=texto2)
        print(presentend2)
        print("              ")

    elif opcion == "5":

        print("Tipos de datos numéricos")
        entero = 45
        decimal = 74.26
        complejo = 12 + 5j
        bollean = False

        print(entero)
        print(decimal)
        print(complejo)
        print(bollean)

        print("Operaciones ")
        num = 20
        num2 = 45
        print("Suma:", (num + num2))
        print("Resta:", (num - num2))
        print("Multiplicacion:", (num * num2))
        print("Division:", (num / num2))
        print("Division Exacta:", (num // num2))
        print("Potencia:", (num ** num2))

    elif opcion == "6":
        texto = "Hola soy Santiago Mayorga"
        print(texto)
        print(".LOWER")
        print(texto.lower())
        print(".UPPER")
        print(texto.upper())
        print(".TITLE")
        print(texto.title())
        print(".FIND")
        print(texto.find("soy"))
        print(".COUNT")
        print(texto.count("t"))
        print(".REPLACE")
        textofinal = texto.replace("a", "4")
        print(textofinal)
        print(".IS NUMERIC")
        valor = texto.isnumeric()
        print(valor)
        print(".SPLIT")
        cadenaseparada = texto.split(" ")
        print(cadenaseparada)
        print("              ")
    elif opcion == "7":

        tupla = (1, 2, 3)
        print(tupla)

        tupla2 =  (7, "ronaldo", False, 450.3, 16 + 7j,"Kakarotto",True)
        print(tupla2)

        tupla3 = (9,3,(4,5,6))
        print(tupla3)

        print(tupla2[2])
        #tupla2[2] = "Messi"
        print(tupla2[-2])

        print(tupla2[0:4])

        a,b,c = tupla
        print(a)
        print(b)
        print(c)

        tuplafinal = tupla + tupla3
        print(tuplafinal)

        print(tuplafinal.count(3))

        print(tuplafinal.index(3))

    elif opcion == "8":
        lista1 = ["Santiago", 25, 98.3, False, "Rengoku", 56.3]
        print(lista1)
        print(lista1[:])
        print(lista1[2])
        print(lista1[-1])

        print(lista1[0:3])
        print(lista1[:2])
        print(lista1[3:])

        lista1.append("Colombia")
        print(lista1)

        lista1.insert(4, "Ecuador")
        print(lista1)

        lista1.extend(["Rui", 110, False])
        print(lista1)

        print(lista1.index("flavio"))

        lista1.remove(56.3)
        print(lista1)

        lista1.pop()
        print(lista1)

        lista2 = ["Andre", "Mario"]
        lista3 = lista1 + lista2
        print(lista3)

        print("1", lista2 * 4)

        print("Colombia" in lista1)

    elif opcion == "9":
        miDiccionario = {"España": "Madrid", "Peru": "Lima", "Alemania": "Berlin"}
        print(miDiccionario["Peru"])
        print(miDiccionario)

        miDiccionario["Venezuela"] = "Caracas"
        print(miDiccionario)

        miDiccionario["España"] = "Barcelona"
        print(miDiccionario)

        del miDiccionario["España"]
        print(miDiccionario)

        dic2 = {"Garcia": "Oscar", 25: True, "Sueldo": 150.8}
        print(dic2[25])

        llave = ("España", "Franciaa", "Inglaterra")
        dicPaises = {llave[0]: "Madrid", llave[1]: "Paris", llave[2]: "Londres"}
        print(dicPaises)

        datosPersonales = {"Apellido": "Contreras", "Anio": {1: 2020, 2: 2021, 3: 2022}}
        print(datosPersonales)
        print(datosPersonales["Anio"])
        print(datosPersonales.get("Ape", "Andy"))

        print(datosPersonales.keys())

        print(datosPersonales.values())

        valores = list(datosPersonales.values())
        print(valores)

        valores = tuple(datosPersonales.values())
        print(valores)



    elif opcion == "10":
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        sueldo = float(input("Ingrese un sueldo: "))
        print("Hola, " + nombre)
        edadFutura = edad + 20
        print("Tu edad es:", edad)
        print("Tu edad (dentro de 20 años) sera:", edadFutura)
        print("Tu sueldo es:", sueldo)



    elif opcion == "11":
        edad = int(input("Ingrese la edad: "))
        if edad > 18:
            print("Eres mayor de edad.")
        elif edad == 18:
            print("Tienes 18 años!")
        else:
            print("No eres mayor de edad.")


    elif opcion == "12":
        opc1 = ""
        while opc1 != "3":
            os.system("cls")
            opc1 = respuesta.menu(["1)Funciones sin parametros", "2)Funciones con parametros", "3)Salir"], "Funciones")
            os.system("cls")
            if opc1 == "1":
                def saludar():
                    print("Andy")
                    print("Contreas")
                    print("Andy159")
                    return "Hola"


                print(saludar())

            elif opc1 == "2":
                def evaluacionSueldoMinimo(sueldo):
                    if sueldo >= 850:
                        print("Cumple con el sueldo")
                    else:
                        print("Ganas menos que el sueldo minimo")


                evaluacionSueldoMinimo(1200)



    elif opcion == "13":
        distancia = 1200
        numerohermano = 3
        salarioPadre = 1500
        tienebeneficio = False
        if (distancia > 1000 and numerohermano > 2) or salarioPadre < 2000:
            tienebeneficio = True
        print(not tienebeneficio)

        if (5 > 3) and (8 < 15):
            print("Verdad ")
        else:
            print("Es falso ese argumento...")


    elif opcion == "14":
        sexos = ("Hombre", "Mujer")
        posicion = True
        sexo = sexos[posicion]
        print(sexo)
        sexo = sexos[not posicion]
        print(sexo)




    elif opcion == "15":
        print("--- Cursos ---")
        print("Matematica - Biologia - Lenguaje - Ciencias")

        cursos = input("Ingrese el curso deseado: ")

        if cursos in ("Matematica - Biologia - Lenguaje - Ciencias"):
            print("Curso {} seleccionado.".format(cursos))
        else:
            print("No existe este curso")



    elif opcion == "16":
        numeros = range(5)
        print(numeros[0])

        numeros1 = range(4, 10)
        print(numeros1[5])

        numeros2 = range(10, 100, 8)
        print(numeros2[9])



    elif opcion == "17":
        for num in range(0, 10):
            print("Valor actual: {}".format(num))

        for num in range(0, 20, 2):
            print("Valor actual: {}".format(num))

        for i in range(1, 13):
            print("{} * {} es : {}".format(i, i, (i * i)))

        # Recorrer una tupla, len muestra la longitud
        for nom in ["Karen", "Lesli", "Lila", "Hector", "Leonardo"]:
            print("Cantidad de letras de {} es: {}".format(nom, len(nom)))



    elif opcion == "18":
        numero = int(input("Ingrese un número: "))
        factorial = 1
        for i in range(1, (numero + 1)):
            factorial = factorial * i
        print("El factorial de {} es: {}".format(numero, factorial))



    elif opcion == "19":
        opc1 = ""
        while opc1 != "3":
            opc1 = respuesta.menu(["1)Bucle", "2)Finalizar el bucle", "3)Salir"], "Bucles")
            if opc1 == "1":
                indice = 1
                while indice < 10:
                    print("Valor actual: {}".format(indice))
                print("Hemos terminado el bucle while")

            elif opc1 == "2":
                inicio = 2
                while inicio <= 100:
                    print("Número par: {}".format(inicio))
                    inicio += 2
                print("Hemos terminado el bucle while")



    elif opcion == "20":
        opc1 = ""
        while opc1 != "3":
            opc1 = respuesta.menu(["1)Break", "2)Continue", "3)Pass", "4)Salir"], "Distintas Sentencias")
            if opc1 == "1":
                for numero in range(1, 6):
                    if numero == 3:
                        break  # Descanso o interrupción
                    print("El numero es: {}".format(numero))
                print("Bucle terminador")

            elif opc1 == "2":
                for numero in range(1, 6):
                    if numero == 3:
                        continue  # Continuar con el resto del bucle
                    print("El numero es: {}".format(numero))
                print("Bucle terminador")

            elif opc1 == "3":
                for numero in range(1, 6):
                    if numero <= 3:
                        pass  # aqui no pasa nada y el bluque sigue trabajando
                    else:
                        print("El siguiente valor es mayor a 3: ")
                    print("El numero es: {}".format(numero))
                print("Bucle terminador")




    elif opcion == "21":
        opc1 = ""
        while opc1 != "3":
            opc1 = respuesta.menu(["1)Uso del yield", "2)Uso del next", "3)Salir"], "Distintas Formas de usar el yield")
            if opc1 == "1":
                def generadorMultiplo7(limite):
                    numero = 1
                    while numero <= limite:
                        yield numero * 7
                        numero = numero + 1


                obtieneMultiplo7 = generadorMultiplo7(10)
                print(obtieneMultiplo7)

            elif opc1 == "2":
                def generadorMultiplo7(limite):
                    numero = 1

                    while numero <= limite:
                        yield numero * 7
                        numero = numero + 1


                obtieneMultiplo7 = generadorMultiplo7(10)
                print(next(obtieneMultiplo7))
                print("Aca hay 300 linea de codigo ...")
                print(next(obtieneMultiplo7))
                print("Aca hay 1000 linea de codigo ...")
                print(next(obtieneMultiplo7))


    elif opcion == "22":
        def devuelveLenguaje(*lenguaje):
            for leng in lenguaje:
                yield from leng


        lenguajesObtenido = devuelveLenguaje("Python", "Java", "Php", "Ruby", "JavaScrip")
        print(next(lenguajesObtenido))
        print(next(lenguajesObtenido))


    elif opcion == "23":
        opc1 = ""
        while opc1 != "3":
            opc1 = respuesta.menu(["1)Primara forma", "2)Segunda forma", "3)Salir"], "Distintas Formas")
            if opc1 == "1":
                numero = 20
                numero1 = 0
                try:  # Intento
                    resultado = numero / numero1
                except:
                    print("Error en el programa")
                print("Aquí termina mi programa")

            elif opc1 == "2":
                numero = 20
                numero1 = 2
                try:  # Intento
                    resultado = numero / numero1
                except ZeroDivisionError:
                    print("No se puede dividir entre zero")
                finally:  # Siempre se va a ejecutar
                    print("Yo siempre aparezco")
                print("Aquí termina mi programa")



    elif opcion == "24":
        def evaluarNota(nota):
            if nota < 0:
                raise ValueError("Valor incorrecto")
            # raise ZeroDivisionError("Este mensaje es personalizado")
            elif nota >= 16:
                print("Excelente")
            elif nota >= 11:
                print("Aprobado")
            else:
                print("Desaprobado")


        evaluarNota(-7)
        print("Este es el fin de mi programa")



    elif opcion == "25":
        print("La suma es: {}".format(sumar(5, 6)))
        print("La multiplicación es: {}".format(multiplicar(5, 6)))




    elif opcion == "26":
        print(contarletra("Harigato"))
        print(multiplicar(5, 6))



    elif opcion == "27":
        class Persona():
            apellido = ""
            nombres = ""
            edad = 0
            despierta = False

            def despertar(self):
                self.despierta = True
                print("Buen dia.")


        persona1 = Persona()
        persona1.apellido = "Garcia fuentes"
        print(persona1.apellido)
        persona1.despertar()
        print(persona1.despierta)

        persona2 = Persona()
        persona2.apellido = "Contreras Salas"
        print(persona2.apellido)
        persona2.despertar()
        print(persona2.despierta)



    elif opcion == "28":
        class Curso():
            def __init__(self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro


        curso1 = Curso("Matematica", 5, "Ingeniera en Software")
        print(curso1.nombre)

        curso2 = Curso("Lenguaje", 5, "Ingeniera en Software")
        print(curso2.nombre)



    elif opcion == "29":
        class Curso():
            def __init__(self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "Presencial"

            def mostrar(selfs):
                dat = "Nombre {} / creditos {} / Modo de impartición {}"
                print(dat.format(selfs.nombre, selfs.creditos, selfs.__imparticion))


        curso1 = Curso("Matematica", 5, "Ingeniera en Software")
        print(curso1.nombre)
        curso1.mostrar()



    elif opcion == "30":
        class Curso():
            def __init__(self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "Presencial"

            def mostrar(selfs):
                dat = "Nombre {} / creditos {} / Modo de impartición {}"
                print(dat.format(selfs.nombre, selfs.creditos, selfs.__imparticion))
                docenteAsignado = selfs.__verificardocente()
                if docenteAsignado:
                    print("Docente Asignado")
                else:
                    print("No es necesario asignar docente")

            def __verificardocente(self):
                print("Verificando si existe docente asignado...")
                if self.__imparticion == "Presencial":
                    return True
                else:
                    return False


        curso1 = Curso("Matematica", 5, "Ingeniera en Software")
        print(curso1.nombre)
        curso1.mostrar()


    elif opcion == "31":
        class cuenta():
            def __init__(self, pro, sal, mon):
                self.__propietario = pro
                self.__saldo = sal
                self.__moneda = mon

            #  Getter (méetodo Get) #para obtener un valor
            def get_Saldo(self):
                return self.__saldo

            def get_propietario(self):
                return self.__propietario

            def get_moneda(self):
                return self.__moneda

            #  Setters (méetodo Set), modificar o cambiar el valor de la moneda

            def set_moneda(self, moneda):
                self.__moneda = moneda


        cuenta1 = cuenta("Santiago Mayorga",2500, "dólares")
        print(cuenta1.get_Saldo())
        cuenta1.set_moneda("Dolares")
        print(cuenta1.get_moneda())


    elif opcion == "32":
        class Curso():
            def __init__(self, nom, cre, pro):
                self.nombre = nom
                self.creditos = cre
                self.profesion = pro
                self.__imparticion = "Presencial"

            def mostrar(selfs):
                dat = "Nombre {} / creditos {} / Modo de impartición {}"
                print(dat.format(selfs.nombre, selfs.creditos, selfs.__imparticion))
                docenteAsignado = selfs.__verificardocente()
                if docenteAsignado:
                    print("Docente Asignado")
                else:
                    print("No es necesario asignar docente")

            def __verificardocente(self):
                print("Verificando si existe docente asignado...")
                if self.__imparticion == "Presencial":
                    return True
                else:
                    return False

            def __str__(self):
                texto = "Nombre: {} - Créditos: {}"
                return texto.format(self.nombre, self.creditos)


        curso1 = Curso("Matematica", 5, "Ingeniera en Software")
        print(curso1)
        curso1.mostrar()



    elif opcion == "33":
        class persona():
            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombre = nom

            def mostrarNombreCompleto(self):
                txt = "{} {} {}"
                return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)


        class estudiantes(persona):
            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro


        estu1 = estudiantes("Valencia", "Gallegos", "Martin", "Derecho")
        print(estu1.mostrarNombreCompleto())
        print(estu1.profesion)


    elif opcion == "34":
        class persona():
            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombre = nom

            def mostrarNombreCompleto(self):
                txt = "{} {} {}"
                return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)

            def datos(self):
                print(self.mostrarNombreCompleto())


        class estudiantes(persona):
            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro

            def datos(self):
                super().datos()
                print("Profesion {}".format(self.profesion))


        estu1 = estudiantes("Torres", "Lopez", "Juan", "Ingeniería Civil")
        estu1.datos()



    elif opcion == "35":
        class persona():
            def __init__(self, apePat, apeMat, nom):
                self.apellidoPaterno = apePat
                self.apellidoMaterno = apeMat
                self.nombre = nom

            def mostrarNombreCompleto(self):
                txt = "{} {} {}"
                return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)

            def datos(self):
                print(self.mostrarNombreCompleto())


        class estudiantes(persona):
            def __init__(self, apePat, apeMat, nom, pro):
                super().__init__(apePat, apeMat, nom)
                self.profesion = pro

            def datos(self):
                super().datos()
                print("Profesion {}".format(self.profesion))


        estu1 = estudiantes("Torres", "Lopez", "Juan", "Ingeniería Civil")
        print(isinstance(estu1, estudiantes))
        per1 = persona("Torres", "Lopez", "Juan")
        print(isinstance(per1, estudiantes))


    elif opcion == "36":
        class ClaseA():
            def __init__(self, par1, par2):
                self.parametro1 = par1
                self.parametro2 = par2


        class ClaseB():
            def __init__(self, par3, par4, par5):
                self.parametro3 = par3
                self.parametro4 = par4
                self.parametro5 = par5


        class claseX(ClaseA, ClaseB):
            pass


        cX1 = claseX(15, 21)





    elif opcion == "37":
        class Estudiante():
            def describir(self):
                print("Soy un buen estudiante.")


        class docente():
            def describir(self):
                print("Me dedico a enseñar curso.")


        class trabajador():
            def describir(self):
                print("Trabajo dentro de una gran empresa.")


        def describirPersona(persona):
            persona.describir()


        doc1 = docente()
        describirPersona(doc1)




    elif opcion == "38":
        class Pais():
            def __init__(self, nom, pre):
                self.nombre = nom
                self.presidente = pre

            def __str__(self):
                txt = "Pais: {} - Presidente: {} "
                return txt.format(self.nombre, self.presidente)


        class ciudad():
            def __init__(self, nom, hab, pai):
                self.nombre = nom
                self.habitante = hab
                self.pais = pai

            def __str__(self):
                txt = "Ciudad: {} - Nº Habitantes: {} ({}) "
                return txt.format(self.nombre, self.habitante, self.pais)


        class Urbanizacion():
            def __init__(self, nom, ciu):
                self.nombre = nom
                self.ciudad = ciu

            def __str__(self):
                txt = "Urbanización: {} ({})"
                return txt.format(self.nombre, self.ciudad)


        pais1 = Pais("Colombia", "Juan Carlos Benal")
        print(pais1)

        ciudad1 = ciudad("Barranquilla", 150000, pais1)
        print(ciudad1)

        urbanizacion1 = Urbanizacion("Manatí", ciudad1)
        print(urbanizacion1)





    elif opcion == "0":
        print("Finalizacion de la tarea")











