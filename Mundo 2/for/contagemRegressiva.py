from time import sleep
import emoji
for x in range (10, -1, -1):
    sleep(1)
    print(x)
print("-="*10)
print(emoji.emojize("Feliz Ano Novo!:sparkles::boom:",use_aliases=True))
print("-="*10)