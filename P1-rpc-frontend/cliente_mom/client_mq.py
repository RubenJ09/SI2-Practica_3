import pika
import sys

def cancelar_pago(hostname, port, id_pago):
    try:
        # 1. Credenciales y Conexión (igual que en el servidor)
        credentials = pika.PlainCredentials('alumnomq', 'alumnomq')
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=hostname, port=int(port), credentials=credentials)
        )
        channel = connection.channel()

        # 2. Declarar la cola (por si no existe)
        channel.queue_declare(queue='pago_cancelacion')

        # 3. Enviar el ID del pago como mensaje 
        channel.basic_publish(
            exchange='',
            routing_key='pago_cancelacion',
            body=str(id_pago)
        )
        
        print(f" [x] Enviada petición de cancelación para el pago: {id_pago}")

        # 4. Cerrar conexión 
        connection.close()

    except Exception as e:
        print(f"Error al conectar al host remoto: {e}")
        exit()

def main():
    if len(sys.argv) != 4:
        print("Debe indicar el host, el numero de puerto, y el ID del pago a cancelar") 
        exit()

    hostname = sys.argv[1]
    port = sys.argv[2]
    id_pago = sys.argv[3]

    cancelar_pago(hostname, port, id_pago)

if __name__ == "__main__":
    main()
*