class CuentaBancaria:
    tasa_interes = 0.03

    def __init__(self, titular, saldo_inicial, pin):
        self.titular = titular 
        self._saldo = saldo_inicial 
        self.__pin = pin

    def validar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

    def consultar_saldo(self):
        return f"Saldo de {self.titular}: ${self._saldo}"

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

cuenta = CuentaBancaria("Simon Sierra", 1000, "1234")

print(cuenta.titular)

print(cuenta._saldo)

print(f"Pin correcto: {cuenta.validar_pin('1234')}")
print(f"Pin incorrecto: {cuenta.validar_pin('0000')}")

try:
    print(cuenta.__pin)
except AttributeError as e:
    print(f"Error: {e}")

cuenta.depositar(500)
print(cuenta.consultar_saldo())