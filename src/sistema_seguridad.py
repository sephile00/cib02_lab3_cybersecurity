class SistemaSeguridad:
    def __init__(self):
        self.ips_bloqueadas = set()

    def bloquear_ip(self, ip):
        self.ips_bloqueadas.add(ip)

    def desbloquear_ip(self, ip):
        if ip in self.ips_bloqueadas:
            self.ips_bloqueadas.remove(ip)
