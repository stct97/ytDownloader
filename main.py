from pytube import YouTube


url = input('Introduce una URL: ')
yt = YouTube(url)


def descarga(itag):
    try:
        disk = input('Introduce la letra del disco de la ruta a descargar: ')
        path = input('Introduce una ruta de descarga: ')
        stream = yt.streams.get_by_itag(itag)
        stream.download(output_path=disk+':/' + path)
        print('La descarga se ha procesado correctamente visite la ruta proporcionada: ' + disk+':/' + path)
    except:
        print('Ha ocurrido un error')


def data():
    print('╔════════════════════════════════════════════════╗')
    print('              『 Elige una opción 』             ')
    print(' 1 ➩ Si quieres listar todos las combinaciones  ')
    print(' 2 ➩ Si quieres ver las pistas de audio         ')
    print(' 3 ➩ Si solo quieres ver archivos de video      ')
    print(' 4 ➩ Salir                                      ')
    print('╚════════════════════════════════════════════════╝')
    seleccion = int(input())
    loop = True
    while loop:
        if(seleccion == 1):
            print('')
            print('Has elegido listar todas las posibles acciones')
            stream = yt.streams.filter(adaptive=True)
            for st in stream:
                print(st)
            print("Selecciona un itag para descagar")
            descarga(int(input()))
            break
        if(seleccion == 2):
            print('')
            print('Has elegido listar todas las pistas de audio')
            stream = yt.streams.filter(only_audio=True)
            for st in stream:
                print(st)
            print("Selecciona un itag para descagar")
            descarga(int(input()))
            break
        if(seleccion == 3):
            print('')
            print('Has elegido listar todas las pistas de video con extension mp4')
            stream = yt.streams.filter(file_extension='mp4')
            for st in stream:
                print(st)
            print("Selecciona un itag para descagar")
            descarga(int(input()))
            break
        if(seleccion > 3):
            print('')
            print('Has elegido una opcion imposible')
            print('¿Quieres salir de la aplicación? | si / no')
            if(input() == 'si'):
                loop = False
            else:
                print('╔════════════════════════════════════════════════╗')
                print('    『 Vuelve a elegir una opción 』             ')
                print(' 1 ➩ Si quieres listar todos las combinaciones  ')
                print(' 2 ➩ Si quieres ver las pistas de audio         ')
                print(' 3 ➩ Si solo quieres ver archivos de video      ')
                print('╚════════════════════════════════════════════════╝')
                seleccion = int(input())


data()
