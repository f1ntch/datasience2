# This is a sample Python script.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom











#### Bereken standaard afwijking ###

## De standaardafwijking of standaarddeviatie
# (vaak aangeduid met de Griekse letter σ voor de populatie en s voor de steekproef),
# een begrip in de statistiek, is een maat voor de spreiding van een variabele of van
# een verdeling of populatie. De standaardafwijking is gedefinieerd als de wortel uit de
# variantie, en daardoor vergelijkbaar met de waarden van de variabele zelf.

getallen = (13, 15, 7, 3, 10, 27)
gemiddelde = np.mean(getallen)
n = len(getallen)

sd1 = 0
for getal in getallen:
    sd1 = sd1 + (getal - gemiddelde) ** 2 ##SOM VAN ALLE ELEMENTEN
    print((getal - gemiddelde) ** 2)
print(sd1)
output = np.sqrt(sd1 / (n - 1))
print("Standaard afwijking")
print(output)

### Bereken de variantie (zelfde formule als sd naar zonder wortel)

## De variantie is in de statistiek een maat voor de spreiding van een reeks waarden,
# dat wil zeggen de mate waarin de waarden onderling verschillen. Hoe groter de variantie,
# hoe meer de afzonderlijke waarden onderling verschillen,
# en dus ook hoe meer de waarden van het "gemiddelde" afwijken.

getallen2 = (13, 15, 7, 3, 10, 27)
gemiddelde2 = np.mean(getallen2)
n2 = len(getallen2)

sd4 = 0
for getal2 in getallen2:
    sd4 = sd4 + (getal2 - gemiddelde2) ** 2 ##SOM VAN ALLE ELEMENTEN


output2 = sd4 / (n - 1)
print("Variantie")
print(output2)