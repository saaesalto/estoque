# Bem-vindo à máquina de ingresso do Cinema

idade = int(input('Qual sua idade? '))

if idade < 12:
    print('Recomendamos o filme infantil Carros.')
elif 12 <= idade < 18:
    print('Recomendamos o filma adolescente Mazze Runner')
else:
    print('Recomendamos emocionadamente O Clube da Sorte e da Felicidade')