print("Bem vindo ao Quiz!")
inicio = input("Deseja jogar? S/N")

pontos = 0

if inicio !="s":
    quit()

print("Começando...")
pergunta_1 = input("Quem descobriu o Brasil? \n a) bob \n b) Baleia \n c) dinossauro \n d)Pedrão \n")

if pergunta_1 == "d":
    print("Corretabouss!")
    pontos += 1
else:
    resposta_1 = print(f"Resposta: {pergunta_1}")
    print("Errou!")

pergunta_2 = input("Qual é o formato da bola?\n a) redonda \n b) Baleia \n c) dinossauro \n d)Pedrão \n")

if pergunta_2 == "a":
    print("Acertou denovo!")
    pontos += 1
else:
    resposta_2 = print(f"Resposta: {pergunta_2}")
    print("Errou!")

resultado = print(f"Fim do jogo! Sua pontuação foi {pontos} pontos de 2 questões!")    
