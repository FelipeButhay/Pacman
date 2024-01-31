Con el archivo "pacman_editor.py" se pueden crear niveles originales, algunos requisitos para que no haya problemas:
1. No dejar caminos sin salida, o sea que desde cada punto del mapa haya 2 o mas direcciones desde las que se pueda avanzar. Si no se sigue esta regla puede dar error si algun fantasma que se mete ahí.
2. Poner un unico spawner de fantasmas con una sola puerta arriba o abajo.
3. Poner un unico spawner para pacman, si se ponen mas lo mas probable es que solo tome uno.
4. No dejar espacios vacios que no puedan ser alcanzados por pacman.

Para crear el archivo del nivel darle a SAVE en el editor y este creara un .txt en la carpeta "levels" que se creara junto con el archivo. Para utilizarlo colocarlo en la carpeta "lvl" y llamarlo "lvl.txt"

Antes de ejecutar el archivo "pacman.py" o "pacman_editor.py":
- Instalar Python 3.12
- Instalar pygame con este comando en la consola CMD "python -m pip install -U pygame==2.5.2 --user".
Para ejecutarlo:
1. Abre el explorador de archivos.
2. Navega al directorio que contiene el archivo Python.
3. Manten presionada la tecla Shift y haz clic derecho en un area vacia del explorador de archivos.
4. Selecciona "Abrir ventana de comandos aquí" o "Abrir ventana de PowerShell aquí".
5. En la ventana de comandos o PowerShell, escribe "python pacman.py" o  "python pacman_editor.py" y presiona Enter.
