# declarar una clase y darle el nombre Usuario
class Usuario:		
    def __init__(self,nombre,correo):
        self.name = nombre
        self.email = correo
        self.balance_cuenta = 0

    def hacer_deposito(self, amount):	# toma un argumento que es el monto del depósito
        self.balance_cuenta += amount

    def hacer_retiro(self,amount):
        self.balance_cuenta -= amount

    def mostrar_balance_usuario(self):
        print(f"El usuario {self.name} tiene {self.balance_cuenta}")

    def transfer_dinero(self,usuario_destino,amount):
        self.balance_cuenta -= amount
        usuario_destino.balance_cuenta += amount

vicente = Usuario("Vicente","viperalta@gmail.com")
vicente.hacer_deposito(200)
vicente.mostrar_balance_usuario()

espe = Usuario ("Esperanza","espe@gmail.com")
vicente.transfer_dinero(espe,100)

espe.mostrar_balance_usuario()
vicente.mostrar_balance_usuario()

