import random

# Sorprendi i tuoi compagni!
lnm = ["Pugilato", "Pasta", "Matematica", "Rumeno", "Cubi di Rubik"]
print(random.choice(lnm))
ite = []
d = int(input('Quanti fatti vuoi mettere nella lista'))
for i in range(d):
    s = input('Che fatto vuoi mettere')
    ite.append(s)
print(random.choice(ite))
# Wow
