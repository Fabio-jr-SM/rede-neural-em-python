import math

# Definição das variáveis iniciais
input = 0  # Entrada para a rede neural
output_desire = 0  # Saída desejada (rótulo alvo)
learning_rate = 0.001  # Taxa de aprendizado para o algoritmo de aprendizado
input_weight = 0.5  # Peso associado à entrada

# Função de ativação: Retorna 1 se a soma for maior ou igual a 0, senão retorna 0
def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

# Exibindo a entrada e a saída desejada
print("Entrada", input)
print("Desejado", output_desire)

# Inicializando a variável de erro com infinito para começar o loop
erro = math.inf

# Contador de iterações
iteration = 0

# Bias e peso do bias (termo de deslocamento)
bias = 1  # O bias é uma constante adicional à soma
bias_weight = 0.5  # Peso associado ao bias

# Loop de aprendizado
while not erro == 0:
    iteration += 1  # Incrementa a contagem de iterações
    print("######## Iteração:", iteration)
    print("Peso", input_weight)
    
    # Calcula a soma ponderada da entrada e do bias
    sum = (input * input_weight) + (bias * bias_weight)

    # Calcula a saída usando a função de ativação
    output = activation(sum)

    # Exibe a saída da rede
    print("Saída", output)

    # Calcula o erro entre a saída desejada e a saída da rede
    erro = output_desire - output

    # Exibe o erro calculado
    print("ERRO", erro)

    # Atualiza os pesos se o erro não for zero
    if not erro == 0:
        # Atualiza o peso da entrada com base no erro, entrada e taxa de aprendizado
        input_weight = input_weight + (learning_rate * input * erro)
        # Atualiza o peso do bias com base no erro, bias e taxa de aprendizado
        bias_weight = bias_weight + (learning_rate * bias * erro)

# Quando o erro for zero, a rede aprendeu e o loop para
print("PARABÉNS!!! A REDE APRENDEU BABY")
