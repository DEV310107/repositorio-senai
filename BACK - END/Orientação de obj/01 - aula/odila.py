import os
from mat import Pessoa


carlos = Pessoa ("carlos")

carlos.andar()

carlos.SetNome("andre")

maria = Pessoa ("maria clara")
maria.falar()
print(carlos.GetNome())

print(maria.GetNome())
