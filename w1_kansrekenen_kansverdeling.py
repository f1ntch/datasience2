import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom

############################# Kans rekenen ##########################################

# Dobbelsteenen


dobbelstenen = pd.DataFrame([((d1, d2), d1 + d2) for d1 in range(1, 7) for d2 in range(1, 7)],
                            columns=['worp', 'som'],
                            index=[i for i in range(1, 37)])

print(dobbelstenen)

# Kans op minder dan van is de kans op een 1 OF een 2 OF en 3
minder_dan_vier_ogen = len(dobbelstenen.query('som < 4')) / len(dobbelstenen) * 100
meer_dan_vier_ogen = (1 - len(dobbelstenen.query('som < 4')) / len(dobbelstenen)) * 100

print("Kans op minder dan 4 ogen: %.1f" % minder_dan_vier_ogen + "%")
print("Kans op meer dan 4 ogen: %.1f" % meer_dan_vier_ogen + "% \n")

# Boekkaarten

kleuren = np.array(['Harten', 'Ruiten', 'Schoppen', 'Ruiten'])
nummers = np.arange(2, 11).astype('str')
waarden = np.concatenate((['Aas'], nummers, ['Boer', 'Dame', 'Heer']))
combinaties = np.stack(np.meshgrid(kleuren, waarden), -1).reshape(-1, 2)
boek = pd.DataFrame(combinaties, columns=['kleur', 'waarde'], index=range(1, combinaties.shape[0] + 1))

print(boek)

print("\n\n Waarde is een Aas")
print(boek.query("waarde == 'Aas'"))

print("\n\n Waarde is een Harten")
print(boek.query("kleur == 'Harten'"))

print("\n\n Waarde is een Harten OF Waarde is een Aas")
print(boek.query("kleur == 'Harten' or waarde == 'Aas'"))
print("Aantal kaarten " + str(len(boek.query("kleur == 'Harten' or waarde == 'Aas'"))))




############################# Kans verdelingen ##############################################################

waarde = range(2, 13)

kans = pd.Series([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) / 36.0

plt.figure()
plt.bar(waarde, kans)
plt.xlabel("som van de  Dobbelstenen")
plt.ylabel("kans om som te  gooien")
plt.show()

mu = (waarde * kans).sum()
print("Mu")
print(mu)

sigma = np.sqrt(((waarde - mu) ** 2 * kans).sum())
print("Sigma")
print(sigma)

#### Binomiaal verdeling

# De binomiaalverdeling kan je in de volgende context gebruiken:
#  je doet een experiment een aantal keer achter elkaar
#  de uitkomst van het experiment beïnvloedt het resultaat van het volgende experiment niet
#  de uitkomst van het experiment kan slechts 2 mogelijke waarden opleveren
#  je weet wat de kans is om de 2 waarden te verkrijgen als je het experiment 1 keer uitvoert
#  je vraagt je af wat de kans is dat je een aantal keer een bepaalde waarde verkrijgt


n = 5  # het aantal keer dat je het experiment doet
p = 2 / 10  # de kans (kans op een vraag juist  )
k = 2  # aantal keer dat je wil dat het experiment de waarde oplevert (2 vragen juist)

kansop_2van5_juist = binom.pmf(x, n, p)
print("Binom kans op 2/5 juist")
print(kansop_2van5_juist)


