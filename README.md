# Comandos de GIT

* git clear: limpia pantalla
* git init: crea un proyecto
* git status: muestrado el estado en la que se encuentra el proyecto actualmente.
* git add .: Agrega todos los cambios para subirlos.
* git add Name_File.txt agrega unicamente el archivo para subir.
* git rm --cached Name_File.txt: devuelve el comando "git add" para que ya no este en proceso de subir
* git commit -m "mensaje": realiza el commit de lo que ya agrego.
* git alias Name_Alias codigo: despues solo llama el nombre del alias y se ejecuta el codigo
* git log --all: muestra toda la historia del proyecto
* git log --all --graph --decorate --oneline: muestra linea por linea orden de los cambios
* git log Name_File.txt: historial de los commit 
* git log --stat: muestra cantidad de bites en los cambios.
* git chow Name_File.txt: muestra de las modificaciones del archivo (commit, fecha, rama, nombre)
* git diff: por defecto muestra la diferencia del directorio altucla conel STG, el que tiene en "git add"
* git diff IdComit IdComit: comparo dos commit y muetras la diferencia de los cambios.
* git tag: se peuden ver los  tags creados es como tener un add 
* git reser IdComit --hard: Devuelve los cambios al comit selecionado sin dejar historial(Tener cuidado)
* git reser IdComit --hard: borrar el historial de commit anteriores pero guarda los cambios en staging
* git branch: muestra las ramas
* git branch Name_Rama: Crea una rama
* git checkout Name_Rama: ingresarmos a la rama
* git merge Name_Rama: es como un comit pero entre ramas (realizar el merge estando en la rama principal)"falta el comit para subir los cambios."
* git remote: vemos una rama que se llama origin
* git remote -v: podemos ver que tenemos push para enviar y festch de traer
* git remote add origin UR_HTTP : realacionamos el gitHub con nuestro local
* git branch -m main: con un actualizacion toca llamar la rama princial como main.
* git pull origin main: trae cambios de origin(GitHub) a rama main(Mi local)
* git push origin main: enviar a origin(GitHub) lo que tengo rama main(Mi local)
* git pull origin main --allow-unrelated-histories: si sale que se reusa a unir historias usamos este comando
* git clone URl_Http: para clonar un respositorio e GitHub, a nuestro local.

## Configuracion de Git
* Cuando se realiza un comflicto al hacer merge, selecionamos desde visual, que parte queremos y volvemos a intentar el merge.
* git config: muestra configuracion que tiene git
* git config --list: configuracion de mi git muestra datos como (usuario, imail)
* git config --list --show-origin: donde estan las configuraciones guardadas (casos avanzados)
* git config --global user.name "diego pallares": a la configuracion le agrego mi nombre
* git config --global user.email "diego pallares": a la configuracion le agrego mi Imail, si la lista ya esta agregado el correo y nombre
Ecs + chif + zz: salgo despues de poner un comentario que no puse al hacer el commit.

## Pasos de crear llaves pirvadas y publicas 
1) ssh-keygen -t rsa -b 4096 -C "youremail@example.com": Crear llave privada y publica.
2) eval $(ssh-agent -s): Cerificar que este corriendo el proceso de ssh.
3) cd ~/.ssh: validamos que esta ruta es donde quedo las llaves guardadas.
4) ssh-add ~/.ssh/id_rsa: debe mostrar que fue agregado y mostrar el correo.

## Pasos de crear repositorio
### Desde la el PC
1) Estar ubicado en la carpeta del proyecto y poner git init, con esto ya creamos git.
2) Despues de realizar cambios subir estos con git add .
3) Verificar con git status los cambios pendientes.
4) Realizar git commit -m "mensaje" para envia

### desde pagina web de GitHub y relacionar con nuestro loca
1) En Git Hub ir a  Settings/ SSH and GPC keys/ boton new SSH Key
2) Poner nombre y se agrega el codigo de la llave publica
3) Crea un repositorio en GitHub y vamos al boton verde code.
4) Copiar la url del HTTP y vamos a git.
5) Estando el proyecto en la rama master, usamos.
6) git remote add origin https://github.com/DiegoPallares/test.git

### Build
1) npm run Build: crear carpeta Build, para hacer deploy, osea subir a produccion.
2) "homepage": "Ruta_Carpeta_Build": Creamos ruta en el archivo package.json (Se crear con el comando anterior).
3) Ejecutamos de nuevo npm run build: verificamos que este ahora la ruta en el archivo index.html de la carpeta build.
4) bpm i --dave-dev gh-pages: Instalar herramienta para ayduarnos a realizar el deploy. (Vemos que en package.json se crea devDependencies)
5) Crear en el apartado de Scripts, en package.json: {"deploy": "npm run build", "predeploy": "gh-pages -d build"}.
6) En git escribimos npm tun deploy: verificamos que al final diga published y verificar nueva rama "ph-pages" en gitHub (No debe tener errores el compilado del proyecto)
7) Vamos a Settings/pages verificar en Branch que este selecionada la rama "ph-pages"
8) Abrir URL para ver proyecto.

## Linea comandos
* ls: Lista de los archivos en la ruta en la que estoy.
* ls -al : muesta lista oculta
* cd: Carpeta actual.
* pwd: ruta actual.
* mkdir Nombre_carpeta: crea carpeta
* touch Nombre_archivo_con extension: creo archivo
* cat Nombre archivo: muestra ela rchivo.
* History: muestra historial de comando
* rm Nombre_archivo: borrar archivo
* code: redicciona a Visual estudio code.
