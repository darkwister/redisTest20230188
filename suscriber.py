import redis

r = redis.StrictRedis(
    host='redis-11129.c85.us-east-1-2.ec2.redns.redis-cloud.com',
    port=11129,
    password='Ayw1LLdpV0VgUk6vpwXdCbSEACPjC5s6',
    decode_responses=True
)

def mostrar_mensajes():
    mensajes = r.lrange('lista_mensajes', 0, -1)
    if mensajes:
        print("Mensajes almacenados en Redis:")
        for i, mensaje in enumerate(mensajes, start=1):
            print(f"{i}. {mensaje}")
    else:
        print("No hay mensajes almacenados.")

if __name__ == '__main__':
    mostrar_mensajes()
