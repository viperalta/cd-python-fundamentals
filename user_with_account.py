from account import CuentaBancaria

class Usuario:		
    def __init__(self,nombre,correo):
        self.name = nombre
        self.email = correo
        self.cuenta = CuentaBancaria(tasa_interes=0.02,balance=0)

    def hacer_deposito(self, amount):
        self.cuenta.balance += amount

    def hacer_retiro(self,amount):
        self.cuenta.balance -= amount

    def mostrar_balance_usuario(self):
        print(f"El usuario {self.name} tiene {self.cuenta.balance}")

    def transfer_dinero(self,usuario_destino,amount):
        self.cuenta.balance -= amount
        usuario_destino.cuenta.balance += amount

vicente = Usuario("Vicente","viperalta@gmail.com")
vicente.hacer_deposito(200)
vicente.mostrar_balance_usuario()

espe = Usuario ("Esperanza","espe@gmail.com")
vicente.transfer_dinero(espe,100)

espe.mostrar_balance_usuario()
vicente.mostrar_balance_usuario()

CuentaBancaria.print_cuentas()

