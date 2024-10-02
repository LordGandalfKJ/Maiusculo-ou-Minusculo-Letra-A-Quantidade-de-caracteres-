def verificar_letra_a(texto):
    # Contar a ocorrência de 'a', 'A', 'ã', 'Ã', 'á', 'Á', 'à', 'À', 'â' e 'Â'
    count_a = (texto.count('a') + texto.count('A') +
               texto.count('ã') + texto.count('Ã') +
               texto.count('á') + texto.count('Á') +
               texto.count('à') + texto.count('À') +
               texto.count('â') + texto.count('Â'))
    
    # Verificar se a letra 'a' ou suas variações existem na Palavra
    if count_a > 0:
        print(f"As letras 'a', 'A', 'ã', 'Ã', 'á', 'Á', 'à', 'À', 'â' ou 'Â' aparecem {count_a} vezes na palavra ou texto.")
    else:
        print("Nenhuma ocorrência de 'a', 'A', 'ã', 'Ã', 'á', 'Á', 'à', 'À', 'â' ou 'Â' foi encontrada na palavra ou texto.")

# Loop para continuar a verificação
while True:
    # Digite a palavra/texto para a verificação do número de caracteres "a, A, ã, Ã, á, Á, à, À, â ou Â"
    texto_usuario = input("Digite uma palavra ou texto para verificar: ")

    # Verificar a ocorrência da letra 'a' ou suas variações
    verificar_letra_a(texto_usuario)

    # Perguntar ao usuário se deseja continuar ou encerrar
    continuar = input("Deseja continuar a verificação? (sim/não): ").strip().lower()
    if continuar != 'sim':
        print("Encerrando o programa ....")
        break
