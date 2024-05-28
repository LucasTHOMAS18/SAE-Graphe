from src.requetes import *


def test_format_personne():
    assert format_personne("[[Michael Raymond-James]]") == "Michael Raymond-James"
    assert format_personne("[[Jack Shea (director)|Jack Shea]]") == "Jack Shea"
    assert format_personne("[[Glenn Beck (actor)|Glenn Beck]]") == "Glenn Beck"
    assert format_personne("[[Antonino Faà di Bruno|Antonino Faa Di Bruno]]") == "Antonino Faà di Bruno"
    assert format_personne("Dennis Cleveland Stewart|Dennis Stewart") == "Dennis Cleveland Stewart"
    assert format_personne("[[John C. Reilly]]") == "John C. Reilly"


def test_collaborateurs_proches():
    assert collaborateurs_proches(graphe, "a1", 0) == set(graphe.adj["a1"])
    assert collaborateurs_proches(graphe_mini, "tom", 1) == {"paire", "OwO", "UwU", "patrick"}
    