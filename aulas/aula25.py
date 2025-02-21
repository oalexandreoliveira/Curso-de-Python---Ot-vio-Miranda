# interpolação com %

# serve para formatar tal como as f strings.

#nome = 'Alexandre'
#preco= 10500
#variavel = '%s, o preço é R$%.2f' % (nome, preco)

# nesse código, o sinal '%' está sendo utilizado para substituir o que seriam as variáveis no decorrer da expressão.
# você pode substituir quantas variáveis quiser utilizando o %
# ao final, você irá novamemte utilizar $, abrir parênteses, e colocar na ordem as variáveis que foram substituídas ao longo do código.

name = 'Rebeca'
age = 23
course = 'database admin'
position = 'BI Intern'
gross_salary = 1500

variable = 'My name is %s, i am %s years old, i am studying %s and working as a %s at Pacific Continental. Also making %.2f per month.' % (name, age, course, position, gross_salary)
print(variable)