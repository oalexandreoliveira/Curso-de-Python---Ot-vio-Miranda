#Variáveis, constantes e complexidade de código

"""
CONSTANTE = 'Variáveis' que não vão mudar.
Em python as variáveis podem ser redefinidas, por isso, convencionou-se que quando a variável for escrita em caixa alta, o valor não deve ser redefinido.

"""

# Evitar muitas condições num mesmo if
# Evitar identações muito longe da margem

velocidade = 61
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
                    
if velocidade_carro_passou_radar_1:
    print('Você está acima da velocidade')

if carro_multado_radar_1 and velocidade_carro_passou_radar_1:
    print('Você será multado')