from PIL import Image
filename = input('ingrese el nombre y la extension del archivo que va a guardar como icono con la siguiente sintaxis:\n\nnombre_del_archivo.ext\n\n los formatos soportados son:\npng\njpg\n\n>>> ')
icon_name = input('ingrese el nombre del archivo a guardar\n La extension sera siempre .ico,\n NO LA ESCRIBA\n>>>' )
img = Image.open(filename)
img.save('{}.ico'.format(icon_name))
print('imagen salvada con exito: {}.ico'.format(icon_name))
quit()
 
