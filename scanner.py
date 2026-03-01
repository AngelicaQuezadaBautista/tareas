import socket

def scan_port(ip, port):
    try:
        # Crear socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        # Intentar conectar
        result = s.connect_ex((ip, port))

        if result == 0:
            print(f"[+] Puerto {port} abierto")

            try:
                # Intentar recibir banner
                s.send(b"Hello\r\n")
                banner = s.recv(1024)
                print(f"    Banner: {banner.decode(errors='ignore')}")
            except:
                print("    No se pudo obtener banner")

        s.close()

    except Exception as e:
        print(f"Error en puerto {port}: {e}")

def main():
    ip = input("Ingresa la IP objetivo: ")

    print(f"\nEscaneando {ip}...\n")

    for port in range(1, 201):
        scan_port(ip, port)

if __name__ == "__main__":
    main()
