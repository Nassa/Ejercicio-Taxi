def calcular_tarifa_taxi(KilometrosRecorridos: float)->int:

    metrosRecorridos = KilometrosRecorridos * 1000
    distancia_mt_recorrida = metrosRecorridos / 100
    
    tarifa = round(distancia_mt_recorrida * 82 + 4000)

    return tarifa

print(calcular_tarifa_taxi(5.2))