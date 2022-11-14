#Calculadora contínua
print("Calculadora de Várias operações.")
continuar = "s"
digitaInicial = True

while continuar == "s":
    if digitaInicial:
        numeroCalc = input("Digite o número de cálculo: ")
    else:
        print("Resultado Gravado = " + str(resultadoCalc))
    operadorCalc = input("Digite o Operador: ")
    numeroCalcSec = input("Digite o outro número que será calculado: ")

    try:
        if operadorCalc == "+":
            resultadoCalc = float(numeroCalc) + float(numeroCalcSec)
        elif operadorCalc == "-" :
            resultadoCalc = float(numeroCalc) - float(numeroCalcSec)
        elif operadorCalc == "*":
            resultadoCalc = float(numeroCalc) * float(numeroCalcSec)
        elif operadorCalc == "/":
            resultadoCalc = float(numeroCalc) / float(numeroCalcSec)
        elif operadorCalc == "%":
            resultadoCalc = float(numeroCalc) % float(numeroCalcSec)
        elif operadorCalc == "//":
            resultadoCalc = float(numeroCalc) // float(numeroCalcSec)
        elif operadorCalc == "**":
            resultadoCalc = float(numeroCalc) ** float(numeroCalcSec)
        else:  
            print("Operador inválido - Só são aceitos + - * / ** // %")
            print("Cálculo Cancelado")
            break
    except:
        print("Valor inválido para calculo")
        break

    if not numeroCalcSec.isdigit() or not numeroCalc.isdigit():
        print("Não foi digitado um número para cálculo")
        break

    print(f"{numeroCalc} {operadorCalc} {numeroCalcSec} = {resultadoCalc}")
    continuar = input("Continua Calculando? [s] [n] ")
    if continuar =="s":
        numeroCalc = float(resultadoCalc)
        digitaInicial = False
        continue
    elif continuar == "n":
        print("Finalizado com o Resultado de: " + str(resultadoCalc))
        break
    else:
        print("Ocorreu um erro ao decidir a continuação do calculo")
        break