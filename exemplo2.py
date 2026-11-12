class Calculadora:
    def somar(self, x, y):
        return x + y

    def subtrair(self, x, y):
        return x - y

    def multiplicar(self, x, y):
        return x * y

    def dividir(self, x, y):
        if y == 0:
            raise ValueError("Não é possível dividir por zero!")
        return x / y


def main():
    calculadora = Calculadora()
    while True:
        print("Selecione a operação: ")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")
        opcao = input("Digite o número da operação escolhida: ")

        if opcao == '5':
            print("Saindo da calculadora!!")
            break
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if opcao == '1':
                resultado = calculadora.somar(num1,num2)
                print("Resultado: ", resultado)
            elif opcao == '2':
                resultado = calculadora.subtrair(num1,num2)
                print("Resultado: ", resultado)
            elif opcao == '3':
                resultado = calculadora.multiplicar(num1,num2)
                print("Resultado: ",resultado)
            elif opcao == '4':
                resultado = calculadora.dividir(num1,num2)
                print("Resultado: ", resultado)
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except ValueError as e:
            print("Erro: ",e)
        except Exception as e:
            print("Ocorreu um erro inesperado: ",e)
if __name__ == "__main__":
    main()
