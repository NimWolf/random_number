import random
max_number = None

max_number = int(input('Elige el rango de tu dado. Indica el número máximo:'))
randomizer = random.randint(1, max_number)
input('Tu dado está listo para ser tirado. [Pulsa ENTER]')
input('Resultado: {}'.format(randomizer))