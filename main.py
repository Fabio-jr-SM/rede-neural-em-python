import math
input = 0
output_desire = 0
learning_rate = 0.1
input_weight = 0.5

def activation(sum):
  if sum >= 0:
    return 1
  else:
    return 0
print("Entrada", input)
print("Desejado", output_desire)

erro = math.inf

iteration = 0

bias = 1
bias_weight = 0.5

while not erro == 0:
  iteration += 1
  print("######## Iteraçâo:", iteration)
  print("peso", input_weight)
    
  sum = (input * input_weight) + (bias * bias_weight) 

  output = activation(sum)

  print("Saida", output)

  erro = output_desire - output

  print("ERRO", erro)

  if not erro == 0:
    input_weight = input_weight + (learning_rate * input * erro)
    bias_weight = bias_weight + (learning_rate * bias * erro)

print("PARABENS!!! A REDE APRENDEU BABYY")