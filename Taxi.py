tarifa_base = int(4000)
distancia_km = float(input("entre la distacia recorrida en km:"))
distancia_mt = distancia_km*1000
precio_a_pagar = tarifa_base + ((distancia_mt/100)*82)
print("El precio a pagar es:",precio_a_pagar)