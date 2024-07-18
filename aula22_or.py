# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeiras avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,  
# a expressão inteira será avaliada naquele valor.
# São consideradoos falsy (que vc já viu)
# 0 0.0 "" False
# Também existe o tipo None que é 
# usado para representar um não valor 

# entrada = input("[E]ntrar [S]air: ")

# if entrada == "E":
#     senha_digitada = input("Senha: ")

# senha_permitida = "123456"
# if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
#     print("Entrar")
# elif (entrada == "E" or entrada == "e") and senha_digitada != senha_permitida:
#     print(" Senha incorreta.")
# else:
#     print("Sair")

# Avaliação de curto circuito
print(False or False or True)