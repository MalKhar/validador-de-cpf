CPF = "99999999565"

def multiplierCPF(CPF, position, multiplier):
    if multiplier <= 1:
        return 0
    return int(CPF[position]) * multiplier + multiplierCPF(CPF, position + 1, multiplier - 1)

def validaCPF(CPF):
    resto = []    
    pesos, pesos2 = multiplierCPF(CPF, 0, 10), multiplierCPF(CPF, 0, 11)
    resto.append(pesos % 11)
    resto.append(pesos2 % 11)
    
    def validaDigito(num):
        if resto[num - 1] <= 1:
            if int(CPF[num + 8]) != 0:
                return False
        elif resto[num - 1] > 1:
            if 11 - resto[num - 1] != int(CPF[num + 8]):
                return False
        return True

    if validaDigito(1) == False or validaDigito(2) == False:
        print("Não é válido!")
    else:
        print("CPF válido!")
                
validaCPF(CPF)