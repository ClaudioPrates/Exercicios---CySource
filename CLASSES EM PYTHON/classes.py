
class Funcionario(object):
    num_func = 0
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        Funcionario.num_func +=1

    def mostrar_salario(self): # Método (Função dentro de classes) que mostra o salário
        print(f"Seu salario eh {self.salario}")

    def atualizar_salario(self ,salario): # Método (Função dentro de classes) que atualiza o salário
        self.salario = salario

    def mostrar_funcionario(self): # Método (Função dentro de classes) que mostra o Funcionário
        return (f"{self.nome} trabalha em {self.cargo} e ganha {self.salario}")


    def numer_func(self):
        return  Funcionario.num_func
funcionario1 = Funcionario("Cláudio", "Cyber", 2000)
funcionario2 = Funcionario("Jorge", "Cyber", 3000)
funcionaria3 = Funcionario("Marcela", "Cyber", 7000)

print(funcionario1.numer_func())
print(funcionario1.nome)
print(funcionario2.numer_func())
print(funcionario2.nome)
print(funcionaria3.numer_func())
print(funcionaria3.nome)
