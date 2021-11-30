cpf = input("informe seu CPF no formato xxx.xxx.xxx-xx:")
cpf.split()
if cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-' and cpf.count('.') == 2:
    print("CPF válido")
else:
    print("CPF inválido, verifique a formatação.")

