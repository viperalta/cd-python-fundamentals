class CuentaBancaria:

    todas_las_cuentas = []

    def __init__(self,tasa_interes,balance):
        self.tasa=tasa_interes
        self.balance=balance
        CuentaBancaria.todas_las_cuentas.append(self)

    def deposito(self, amount):	# toma un argumento que es el monto del depósito
        self.balance += amount
        return self

    def retiro(self,amount):
        self.balance -= amount
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}")
        return self

    def generar_interes(self):
        self.balance += self.balance*self.tasa
        return self

    @classmethod
    def print_cuentas (cls):
        for account in cls.todas_las_cuentas:
            print(account.__dict__)

cuenta1 = CuentaBancaria(0.1,1000)
cuenta1.deposito(100).deposito(200).deposito(300).retiro(150).generar_interes().mostrar_info_cuenta()

cuenta2 = CuentaBancaria(0.1,2000)
cuenta2.deposito(100).deposito(200).retiro(150).retiro(10).retiro(50).retiro(15).generar_interes().mostrar_info_cuenta()

CuentaBancaria.print_cuentas()
