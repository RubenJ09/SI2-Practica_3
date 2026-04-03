import os
import django
import time
import statistics

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'visaSite.settings')
django.setup()

from visaAppWSBackend.models import Tarjeta

def medir_orm():
    tiempos = []
    print("Ejercicio 4 - Escenario 3: Django ORM")
    
    for i in range(1, 8):
        start_time = time.time()
        
        # Acceso vía ORM (Equivalente al SELECT * del Escenario 1)
        tarjetas = list(Tarjeta.objects.all())
        
        end_time = time.time()
        duracion = end_time - start_time
        tiempos.append(duracion)
        
        print(f"Medición {i}/7: Tiempo: {duracion:.6f} segundos")

    media = statistics.mean(tiempos)
    desviacion = statistics.stdev(tiempos)
    
    print("RESULTADOS FINALES ORM")
    print(f"Media: {media:.6f} segundos")
    print(f"Desviación estándar: {desviacion:.6f} segundos")

if __name__ == "__main__":
    medir_orm()