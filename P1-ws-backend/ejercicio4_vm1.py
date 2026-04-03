#!/usr/bin/env python3
import psycopg2
import time
import statistics

# Configuración de la base de datos en VM1
db_config = {
    'dbname': 'si2db',
    'user': 'alumnodb',
    'password': 'alumnodb',
    'host': 'localhost',
    'port': 15432,
}

def medir_tiempo_lectura():
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        
        query_fetch_1000 = "SELECT * FROM tarjeta LIMIT 1000"
        cursor.execute(query_fetch_1000)
        rows = cursor.fetchall()
        
        print(f"  → {len(rows)} tarjetas encontradas")
        
        if len(rows) == 0:
            print(" No hay tarjetas")
            return None
        
        start_time = time.time()
        
        search_query = 'SELECT * FROM tarjeta WHERE "numero" = %s'
        for row in rows:
            id_value = row[0]
            cursor.execute(search_query, (id_value,))
            result = cursor.fetchone()
        
        end_time = time.time()
        return end_time - start_time
        
    except Exception as e:
        print(f" Error: {e}")
        return None
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

def main():
    print("Ejercicio 4 - Escenario 1: Base de datos en VM1")
    print("Realizando 7 mediciones...\n")
    
    tiempos = []
    for i in range(7):
        print(f"Medición {i+1}/7:")
        tiempo = medir_tiempo_lectura()
        if tiempo is not None:
            tiempos.append(tiempo)
            print(f" Tiempo: {tiempo:.6f} segundos")
        else:
            print(f" Medición {i+1} fallida")
        time.sleep(1)
        print()
    
    if tiempos:
        media = statistics.mean(tiempos)
        desviacion = statistics.stdev(tiempos) if len(tiempos) > 1 else 0
        
        print("RESULTADOS FINALES")
        print(f"Número de mediciones exitosas: {len(tiempos)}/7")
        print(f"Tiempos (segundos):")
        for i, t in enumerate(tiempos, 1):
            print(f"  Medición {i}: {t:.6f}")
        print(f"\nMedia: {media:.6f} segundos")
        print(f"Desviación estándar: {desviacion:.6f} segundos")
    else:
        print(" No se pudo completar ninguna medición")

if __name__ == "__main__":
    main()