
total_segundos = int (input("Insira o tempo em segundos:"))

horas = total_segundos // 3600
resto = total_segundos % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas} hora (s), {minutos} minuto(s) e {segundos} segundo(s) ")