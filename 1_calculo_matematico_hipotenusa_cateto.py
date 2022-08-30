"""
CRIE UM PROGRMA QUE SOLICITARÁ AO USUÁRIO A MEDIDA DE TRÊS SEGMENTOS DE RETA
INFORMARÁ SE ELES PODEM FORMAR UM TRIÂNGULO RETÂNGULO.
DICA: USE O TEOREMA DE PITÁGORAS - " QUADRADI DA MEDIDA DO LADO MAIOR(HIPOTENUSA)
É IGUAL À SOMA DOS QUADRADOS DAS MEDIDAS DO LADOS MENORES (CATETOS)"
"""

import math

lado1 = float(input('Entre com o tamanho do primeiro segmento: '))
lado2 = float(input('Entre com o tamanho do segundo segmento: '))
lado3 = float(input('Entre com o tamanho do terceiro segmento: '))
forma_triangulo = False

if (lado1 > lado2) and (lado2 > lado3) and (lado1 < (lado2 + lado3)):
    
    hipotenusa = lado1
    cateto1 = lado2
    cateto2 = lado3
    forma_triangulo = True
    
elif (lado2 > lado1) and (lado2 > lado3) and (lado2 < (lado1 + lado3)):
    hipotenusa = lado2
    cateto1 = lado1
    cateto2 = lado3
    forma_triangulo = True
    
elif (lado3 > lado2) and (lado3 > lado1) and (lado3 < (lado1 + lado2)):
    hipotenusa = lado3
    cateto1 = lado1
    cateto1 = lado2
    forma_triangulo = True 
    
if forma_triangulo:
    if ((hipotenusa**2) == (cateto1**2) + (cateto2**2)):
        print(f'Os segmentos formam um triangulo retangulo, de hipotenusa {hipotenusa} e catetos {cateto1} e {cateto2}.')
    else:
        print('Os Segmentos NÃO formam um triangulo retangulo.')
            
else:
    print('OS SEGMENTOS NÃO FORAM TRIÂNGULO ALGUM.')