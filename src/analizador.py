class Analizador:
    def __init__(self, umbral_intentos=3):
        self.umbral_intentos = umbral_intentos

    def analizar(self, trafico):
        intentos = trafico.get('intentos_fallidos', 0)
        return intentos > self.umbral_intentos
