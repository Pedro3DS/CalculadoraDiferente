#Calculadora normal, porém, quando a  operação soma for escolhida e o primeiro e segundo número forem 1, o resultado será 11
def calculadora():
    operacao = input(
"="*60+"""
Por favor, digite a operação que voce deseja:
+ para adição
- para subtração
* para multiplicação
/ para divisão
"""+"="*60+"\n>> ")
    print("="*60)
    num_1 = int(input("Digite o primeiro número:\n>> "))
    num_2 = int(input("Digite o segundo número:\n>> "))
    #format = formatação comn o uso das chaves
    if operacao == "+" and num_1 == 1 and num_2 == 1:
        print("-"*60)
        print("{} + {} = ".format(num_1, num_2))
        print("11")

    elif operacao == "+":
        print("-"*60)
        print("{} + {} = ".format(num_1, num_2))
        print(num_1 + num_2)    

    elif operacao == "-":
        print("-"*60)
        print("{} - {} = ".format(num_1, num_2))
        print(num_1 - num_2)

    elif operacao == "*":
        print("-"*60)
        print("{} * {} = ".format(num_1, num_2))
        print(num_1 * num_2)

    elif operacao == "/":
        print("-"*60)
        print("{} / {} = ".format(num_1, num_2))
        print(num_1 / num_2)

    else:
        print("-"*60+"\nVocê digitou um operador invalido, por favor reinicie o programa.")
        
    # adiciona função dnv() para a função calculadora()
    reiniciar()

def reiniciar():
    calc_dnv = input(
"="*60+"""
Deseja calcular de novo?
digite S para Sim ou N para Não.
>> """)
    #.upper torna o letra minuscula digitada em maiuscula
    if calc_dnv.upper() == "S":
        calculadora()
    elif calc_dnv.upper() == "N":
        print("Até mais.")
    else:
        reiniciar()

calculadora()