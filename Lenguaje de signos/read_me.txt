Uso:

Con dataCollection.py se obtienen las imagenes de cada mano(letra) hecha con signos
Una vez la mano se encunetre dentro del rectangulo verde, a una distancia de nu metro aprox. hay que pulsar la tecla s
y mantenerla pulsada, mover un poco la mano para que capture bien todas las imagenes de una letra y por último, al llegar
a 200 imagenes paramos. editar el codigo fuente: 

line: 12 -> var: folder = "ruta de la carpeta"

teachable machine -> hacer training y descargar como "keras" en la version no lite. NO USAR WEBCAM


Librerias usadas y python --version:

python 3.8.0 (64 bits)
python -m pip install --upgrade pip
pip install opencv-contrib-python
pip install mediapipe
pip install cvzone
pip install msvc-runtime
pip install tensorflow (2.11.0)