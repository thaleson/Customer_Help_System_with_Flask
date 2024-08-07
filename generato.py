import secrets

# Gera uma chave secreta de 32 bytes (256 bits) codificada em hexadecimal
secret_key = secrets.token_hex(32)

print("Chave Secreta:", secret_key)
