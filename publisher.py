import redis
from datetime import datetime

# Conectarse a la base de datos Redis
r = redis.StrictRedis(
    host='redis-11129.c85.us-east-1-2.ec2.redns.redis-cloud.com',
    port=11129,
    password='Ayw1LLdpV0VgUk6vpwXdCbSEACPjC5s6',
    decode_responses=True
)

def publicar_mensaje(mensaje):
    tiempo_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mensaje_con_tiempo = f"[{tiempo_actual}] {mensaje}"
    r.lpush('lista_mensajes', mensaje_con_tiempo)
    print(f'Mensaje almacenado: {mensaje_con_tiempo}')

if __name__ == '__main__':
    mensaje = input("Escribe el mensaje que quieres almacenar: ")
    publicar_mensaje(mensaje)
