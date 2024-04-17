# cs50w-project1
## Django 
En python creamos las funciones index, entries, search, create, edit y random_page:
### index
En index creamos una función que solicite la lista de entradas dentro del proyecto utilizando la función list_entries() de util.
### entries
En entries creamos una función que obtenga una entrada solicitada por el usuario por medio de la url usando al función get_entry(), si no existe devuelve un error 404.
### search:
En search creamos una función que busque si hay alguna coincidencia en el nombre de alguna de las entradas: si existe una lo redirecciona, si no existe una manda un error 404, si existe coincidencia como parte del nombre de alguna entrada se listan las coincidencias y si existen dos coincidencias con el nombre pero distinguidas por mayúsculas se listan todas.
### create: 
En create creamos una función que recepcione el titulo y el contenido de una nueva entrada, la guarde con save_entry() si no existe una con el mismo titulo y redireccione a la página creada.
### edit
En edit creamos una función que permita editar una entrada previamente creada, mostrando en el textarea el contenido prepoblado.
### random_page
En random_page creamos una función que devuelva una función al azar dentro de las entradas del proyecto.
Creamos plantillas html para cargar el contenido y mostrar los errores, para el style utilizamos las tecnologías Boostrap y Sass.
### markdown2
Usamos el paquete mardown2 para convertir el Markdown en contenido cargable por HTML.
