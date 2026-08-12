mensagem_finalizacao = "Validação concluída"

idade = 22
tem_ingresso = True
esta_bloqueado = True
eh_vip = True

if eh_vip and idade >= 18 and not esta_bloqueado:
    print("Entrada permitida como VIP")
elif idade >= 18 and tem_ingresso and not esta_bloqueado:
    print("Entrada permitida")
else:
    print("Entrada negada")

print(mensagem_finalizacao)