## Instrucciones 
Se tiene los archivos de ejemplo para mostrar una aplicación docker con python que genera números. 

**Empaquetar aplicación**

docker build -t api-python-numeros .

**Ejecutar contenedor**
docker run -it -p 8080:8080 api-python-numeros
