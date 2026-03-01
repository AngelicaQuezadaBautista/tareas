# tareas
En este repositorio se encuentran las tareas del curso de ciberseguridad
Importación del módulo socket
La línea:
  import socket
importa el módulo socket, el cual permite crear conexiones de red utilizando protocolos como TCP/IP. Es fundamental para la comunicación entre computadoras.

Función scan_port(ip, port)
  Esta función se encarga de escanear un puerto específico de una dirección IP.

def scan_port(ip, port):
    Recibe dos parámetros:
      ip: dirección IP del equipo objetivo.
      port: número de puerto que se desea comprobar.
Creación del socket
    Dentro de la función se crea un socket con:
    socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    AF_INET indica que se usará IPv4.
    SOCK_STREAM indica que se utilizará el protocolo TCP.

Tiempo de espera (timeout)
La instrucción:
    s.settimeout(2)
    establece un tiempo máximo de espera de 2 segundos para cada conexión, evitando que el programa se bloquee si un puerto no responde.

Intento de conexión al puerto
Se utiliza:
    result = s.connect_ex((ip, port))
Esta función intenta conectarse al puerto indicado.
  Si devuelve 0, el puerto está abierto; cualquier otro valor indica que está cerrado.

Detección de puertos abiertos
Cuando el resultado es 0, el programa muestra un mensaje indicando que el puerto está abierto y procede a intentar obtener información del servicio.

Obtención del banner
El programa envía un mensaje simple:

s.send(b"Hello\r\n")
  Luego intenta recibir una respuesta del servicio:
banner = s.recv(1024)
Algunos servicios responden con un banner que indica el tipo de servidor o aplicación.

Manejo de errores
    Se utilizan bloques try-except para evitar que el programa se detenga si ocurre un error durante la conexión o la recepción de datos.
Cierre del socket
La instrucción:
    s.close()
cierra la conexión y libera los recursos del sistema, lo cual es una buena práctica.

Función principal main()
    La función main solicita al usuario la dirección IP y recorre los puertos del 1 al 200 utilizando un ciclo for, llamando a la función scan_port para cada puerto.
Ejecución del programa
La condición:
      if __name__ == "__main__":
        main()
    indica que el programa solo se ejecutará cuando el archivo sea ejecutado directamente.
