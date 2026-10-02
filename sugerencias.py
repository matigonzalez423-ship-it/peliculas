#Mostrar Un Encabezado.
def encabezado():
   print("=====================================\n")
   print("      SUGERENCIAS DE PELICULAS       \n")
   print("=====================================\n")
# mostrar el perfil del usuario del argumento que se le pasa 
def perfil_usuario(usuario):
    print("perfil de "+usuario["nombre"])
    print("genero favorito "+usuario["genero_fav"])
    print("peliculas sugeridas ",usuario["vistas"])
#Mostrar Generos De Peliculas.
def mostrar_generos():
   generos=["Accion","Comedia","Terror","Animacion"]
   print("-------- GÉNEROS --------")
   #imprimir la lista de generos.
   for genero in generos:
      print(genero)
def main():
    encabezado()
    usuario=input("Buen día, cuál es tu nombre? ")
    print("¿Qué querés ver hoy, "+usuario+"?")
    peliculas=[["Rápidos y Furiosos","Accion",2001,6.8],["Troya","Accion",2004,7.3],["Terminator 2","Accion",1991,8.6],["¿Y dónde está el piloto?","Comedia",1980,7.7],["Blair Witch","Terror",2016,5.1],["Coco","Animacion",2017,8.4],["Toy story","Animacion",1995,8.3],["Shrek","Animacion",2001,7.9],["El exorcista","Terror",1973,8.1],["¿Y dónde están las rubias?","Comedia",2004,5.8],["Son como niños","Comedia",2010,6]]
    mostrar_generos()
    genero_favorito=input("¿Qué género te gusta? ")
    usuario={"nombre":usuario,"genero_fav":genero_favorito,"vistas":[]}
    rating_favorito=float(input("¿Cuál es el rating mínimo? " ))
    print ("Buscando Películas del Género "+genero_favorito)
    encontrar_pelicula=False
    for pelicula in peliculas:
        nombre=pelicula[0]
        genero=pelicula[1]
        rating=pelicula[3]
        if (genero_favorito.lower()==genero.lower()) and (rating_favorito<rating):
            #print(nombre)
            usuario["vistas"].append(nombre)
            encontrar_pelicula=True
    if (not encontrar_pelicula):
        print("No se ha encontrado ninguna película.")
    perfil_usuario(usuario) # usuario es una variable (parametro) dentro del main. Pasando esa variable al procedimiento perfil_usuario
if __name__ == "__main__":
    main()
