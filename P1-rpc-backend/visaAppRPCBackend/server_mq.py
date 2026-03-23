import os
import sys
import django
import pika

# 1. Configuración del entorno de Django para acceder a los modelos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'visaSite.settings') # Ajusta 'visaSite' si tu proyecto se llama distinto
django.setup()

from visaAppRPCBackend.models import Pago

# 2. Función de Callback: Se ejecuta cuando llega un mensaje
def callback(ch, method, properties, body):
    id_pago = body.decode()
    print(f" [x] Recibida petición de cancelación para ID: {id_pago}")
    
    try:
        # Buscamos el pago y cambiamos su código a '111' 
        pago = Pago.objects.get(id=id_pago)
        pago.codigoRespuesta = '111'
        pago.save()
        print(f" [v] Pago {id_pago} cancelado satisfactoriamente.")
    except Pago.DoesNotExist:
        print(f" [!] Error: El pago con ID {id_pago} no existe.")
    
    # Confirmamos a RabbitMQ que procesamos el mensaje
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    if len(sys.argv) != 3:
        print("Debe indicar el host y el puerto")
        exit()

    hostname = sys.argv[1]
    port = int(sys.argv[2])

    # 3. Credenciales y Conexión 
    credentials = pika.PlainCredentials('alumnomq', 'alumnomq')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=hostname, port=port, credentials=credentials)
    )
    channel = connection.channel()

    # 4. Declaración de la cola 
    channel.queue_declare(queue='pago_cancelacion')

    # 5. Configurar el consumo
    channel.basic_consume(queue='pago_cancelacion', on_message_callback=callback)

    print(' [*] Esperando mensajes de cancelación. Para salir presiona CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()
