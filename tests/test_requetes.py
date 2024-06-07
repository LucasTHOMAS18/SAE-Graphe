from pathlib import Path

from src.collaborateurs import collaborateurs_proches as collaborateurs_sujet
from src.requetes import *

graphe = json_vers_nx(Path(__file__).parent / "data/data_test.txt")
graphe_mini = json_vers_nx(Path(__file__).parent / "data/data_test_mini.txt")


def test_format_personne():
    assert format_personne("[[Michael Raymond-James]]") == "Michael Raymond-James"
    assert format_personne("[[Jack Shea (director)|Jack Shea]]") == "Jack Shea"
    assert format_personne("[[Glenn Beck (actor)|Glenn Beck]]") == "Glenn Beck"
    assert format_personne("[[Antonino Faà di Bruno|Antonino Faa Di Bruno]]") == "Antonino Faà di Bruno"
    assert format_personne("Dennis Cleveland Stewart|Dennis Stewart") == "Dennis Cleveland Stewart"
    assert format_personne("[[John C. Reilly]]") == "John C. Reilly"


def test_json_vers_nx():
    DICO_TEST = {
        "a1": {"a2", "a3", "d1", "d2", "d3", "p1", "p2", "p3", "a5", "a7"},
        "a2": {"a1", "a3", "d1", "d2", "d3", "p1", "p2", "p3", "a4", "a6", "d4", "d6", "p4", "p6"},
        "a3": {"a1", "a2", "d1", "d2", "d3", "p1", "p2", "p3", "a5"},
        "d1": {"a1", "a2", "a3", "d2", "d3", "p1", "p2", "p3"},
        "d2": {"a1", "a2", "a3", "d1", "d3", "p1", "p2", "p3", "a4", "a6", "d4", "d6", "p4", "p6"},
        "d3": {"a1", "a2", "a3", "d1", "d2", "p1", "p2", "p3"},
        "p1": {"a1", "a2", "a3", "d1", "d2", "d3", "p2", "p3"},
        "p2": {"a1", "a2", "a3", "d1", "d2", "d3", "p1", "p3", "a4", "a6", "d4", "d6", "p4", "p6"},
        "p3": {"a1", "a2", "a3", "d1", "d2", "d3", "p1", "p2"},
        "a4": {"a5", "a6", "d4", "d5", "d6", "p4", "p5", "p6", "a2", "d2", "p2"},
        "a5": {"a4", "a6", "d4", "d5", "d6", "p4", "p5", "p6", "a1", "a3"},
        "a6": {"a4", "a5", "d4", "d5", "d6", "p4", "p5", "p6", "a2", "d2", "p2"},
        "d4": {"a4", "a5", "a6", "d5", "d6", "p4", "p5", "p6", "a2", "d2", "p2"},
        "d5": {"a4", "a5", "a6", "d4", "d6", "p4", "p5", "p6"},
        "d6": {"a4", "a5", "a6", "d4", "d5", "p4", "p5", "p6", "a2", "d2", "p2"},
        "p4": {"a4", "a5", "a6", "d4", "d5", "d6", "p5", "p6", "a2", "d2", "p2"},
        "p5": {"a4", "a5", "a6", "d4", "d5", "d6", "p4", "p6"},
        "p6": {"a4", "a5", "a6", "d4", "d5", "d6", "p4", "p5", "a2", "p2", "d2"},
        "a7": {"a1"},
    }
    
    G = nx.Graph(DICO_TEST)
    assert graphe.nodes == G.nodes


def test_collaborateurs_proches():
    assert collaborateurs_proches(graphe, "a1", 0) == set(graphe.adj["a1"])
    assert collaborateurs_proches(graphe_mini, "tom", 1) == {"paire", "OwO", "UwU", "patrick"}


def test_collaborateurs_communs():
    assert collaborateurs_communs(graphe, "a1", "d1") ==  {'a3', 'd3', 'p2', 'd2', 'p1', 'p3', 'a2'}
    assert collaborateurs_communs(graphe, "p5", "d3") ==  set()
    assert collaborateurs_communs(graphe, "a4", "a3") ==  {"a2", "a5", "d2", "p2"}
    assert collaborateurs_communs(graphe, "a2", "p4") ==  {"p2", "a4", "a6", "d4", "d6", "p6", "d2"}


def test_collaborateurs_proches():
    assert collaborateurs_proches(graphe, "a1", 0) ==  collaborateurs_sujet(graphe, "a1", 0)
    assert collaborateurs_proches(graphe, "a1", 1) ==  collaborateurs_sujet(graphe, "a1", 1)
    assert collaborateurs_proches(graphe, "a1", 2) ==  collaborateurs_sujet(graphe, "a1", 2)
    assert collaborateurs_proches(graphe, "a1", 3) ==  collaborateurs_sujet(graphe, "a1", 3)


def test_est_proche():
    assert est_proche(graphe, "a1", "a1", 0)
    assert est_proche(graphe, "a1", "a2")
    assert est_proche(graphe, "a1", "a2", 2)
    assert est_proche(graphe, "a5", "a2", 2)
    assert est_proche(graphe, "a5", "a1", 3)


def test_distance_naive():
    assert distance_naive(graphe, "a1", "a1") == 0
    assert distance_naive(graphe, "a1", "a2") == 1
    assert distance_naive(graphe, "a1", "a5") == 1
    assert distance_naive(graphe, "a2", "a5") == 2
    assert distance_naive(graphe, "a42", "a1") == -1


def test_distance():
    assert distance(graphe, "a1", "a1") == 0
    assert distance(graphe, "a1", "a2") == 1
    assert distance(graphe, "a1", "a5") == 1
    assert distance(graphe, "a2", "a5") == 2
    assert distance(graphe, "a42", "a1") == -1


def test_centralite():
    assert centralite(graphe, "a1") == 2
    assert centralite(graphe, "a5") == 2
    assert centralite(graphe, "p5") == 3
    assert centralite(graphe, "a7") == 3
        
        
def test_centre_hollywood():
    # Les 5 sommets on la même centralité, et la fonction n'est pas déterministe
    assert centre_hollywood(graphe) in ["a1", "a2", "a3", "d2", "p2"]
        

def test_eloignement_max():
    assert eloignement_max(graphe) == 3
