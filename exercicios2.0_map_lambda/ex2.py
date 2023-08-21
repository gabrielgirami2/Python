lista_palavras = ["FIAP", "fiap", "ADS", "ads", "GABRIEL", "gabriel"]

inverter_palavras = list(map(lambda y : y.lower() if(y.isupper()) else y.upper(), lista_palavras))

print(inverter_palavras)