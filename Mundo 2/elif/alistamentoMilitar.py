from datetime import date
import sys
genero = int(input('''Digite seu gênero abaixo: 
[ 1 ] Para masculino,
[ 2 ] Para feminino '''))
if genero == 1:
    print("Você precisa passar pela análise do alistamento militar, prossiga.")
elif genero == 2:
    print("Você não precisa passar pela análise do alistamento militar, obrigado.")
    sys.exit()
atual = date.today().year
anoNasc = int(input("Digite seu ano de nascimento: "))
idade = atual - anoNasc
print(f"Quem nasceu em {anoNasc}, tem {atual - anoNasc} anos! ")
if idade == 18:
    print("Você deve se alistar IMEDIATAMENTE!")
elif idade < 18:
    print(f"Seu alistamento será daqui a {(18 - idade)} ano(s)")
    print(f"Seu alistamento será em {18 + anoNasc}")
elif idade > 18: #Ou apenas else: 
    print(f"Você já deveria ter alistado há {idade - 18} ano(s)")
    print(f"Seu alistamento foi em {18 + anoNasc} ano(s)")


