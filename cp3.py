temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]
registros = []

for i in range(4):
    media = 0
    registroCritico = 0
    for j in range(4):
        media += temperaturas[i][j]
        if temperaturas[i][j] >= 33:
            registroCritico += 1
    media /= 4
    registros.append(registroCritico)
    print(f"Sala {i+1}")
    print(f"Media: {media}")
    print(f"Registro Critícos: {registroCritico}")
    print("")
sala = registros.index(max(registros))
sala += 1

print(f"Sala com maior risco: Sala {sala}")