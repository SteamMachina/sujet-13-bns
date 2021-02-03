from exercices.exercice2 import *

def test_plus_ou_moins_succes():
    plus_ou_moins.nb_mystere = 25
    plus_ou_moins.input = lambda x: 25
    output = []
    plus_ou_moins.print = lambda x,y: output.append((x,y))

    plus_ou_moins()

    assert output == [("Bravo ! Le nombre était ", 25),
    ("Nombre d'essais: ",1)
    ]

def test_plus_ou_moins_succes():
    plus_ou_moins.nb_mystere = 25
    plus_ou_moins.input = lambda x: 26
    output = []
    plus_ou_moins.print = lambda x,y: output.append((x,y))

    plus_ou_moins()

    assert output == [("Perdu ! Le nombre était ", 25)]
