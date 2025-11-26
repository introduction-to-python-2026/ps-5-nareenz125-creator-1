from main import balance_reaction

def test_balance():
    assert balance_reaction("Fe2O3 + H2 -> Fe + H2O") == [1/3, 1, 2/3, 1]
    assert balance_reaction("CH4 + O2 -> CO2 + H2O") == [1/2, 1, 1/2, 1]
    assert balance_reaction("C3H8 + O2 -> CO2 + H2O") == [1/4, 5/4, 3/4, 1]
    assert balance_reaction("H2 + O2 -> H2O") == [1, 1/2, 1]
    assert balance_reaction("N2 + H2 -> NH3") == [1/2, 3/2, 1]

