# int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);

# Ao final do processamento, qual será o valor da variável SOMA? 
#   RESPOSTA: Ao final do processamento, o valor da variavel SOMA será 91

INDICE = 13
SOMA = 0
k = 0

while k < INDICE:
    k+=1
    SOMA+=k

print(SOMA)