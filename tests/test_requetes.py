from pathlib import Path

from src.requetes import *

graphe = json_vers_nx(Path(__file__).parent / "data/data_test.json")
graphe_mini = json_vers_nx(Path(__file__).parent / "data/data_test_mini.json")


def test_format_personne():
    assert format_personne("[[Michael Raymond-James]]") == "Michael Raymond-James"
    assert format_personne("[[Jack Shea (director)|Jack Shea]]") == "Jack Shea"
    assert format_personne("[[Glenn Beck (actor)|Glenn Beck]]") == "Glenn Beck"
    assert format_personne("[[Antonino Faà di Bruno|Antonino Faa Di Bruno]]") == "Antonino Faà di Bruno"
    assert format_personne("Dennis Cleveland Stewart|Dennis Stewart") == "Dennis Cleveland Stewart"
    assert format_personne("[[John C. Reilly]]") == "John C. Reilly"


def test_json_vers_nx():
    DICO_TEST = {
        "a1": {"a2": {}, "a3": {}, "d1": {}, "d2": {}, "d3": {}, "p1": {}, "p2": {}, "p3": {}, "a5": {}},
        "a2": {"a1": {}, "a3": {}, "d1": {}, "d2": {}, "d3": {}, "p1": {}, "p2": {}, "p3": {}, "a4": {}, "a6": {}, "d4": {}, "d6": {}, "p4": {}, "p6": {}},
        "a3": {"a1": {}, "a2": {}, "d1": {}, "d2": {}, "d3": {}, "p1": {}, "p2": {}, "p3": {}, "a5": {}},
        "d1": {"a1": {}, "a2": {}, "a3": {}, "d2": {}, "d3": {}, "p1": {}, "p2": {}, "p3": {}},
        "d2": {"a1": {}, "a2": {}, "a3": {}, "d1": {}, "d3": {}, "p1": {}, "p2": {}, "p3": {}, "a4": {}, "a6": {}, "d4": {}, "d6": {}, "p4": {}, "p6": {}},
        "d3": {"a1": {}, "a2": {}, "a3": {}, "d1": {}, "d2": {}, "p1": {}, "p2": {}, "p3": {}},
        "p1": {"a1": {}, "a2": {}, "a3": {}, "d1": {}, "d2": {}, "d3": {}, "p2": {}, "p3": {}},
        "p2": {"a1": {}, "a2": {}, "a3": {}, "d1": {}, "d2": {}, "d3": {}, "p1": {}, "p3": {}, "a4": {}, "a6": {}, "d4": {}, "d6": {}, "p4": {}, "p6": {}},
        "p3": {"a1": {}, "a2": {}, "a3": {}, "d1": {}, "d2": {}, "d3": {}, "p1": {}, "p2": {}},
        "a4": {"a5": {}, "a6": {}, "d4": {}, "d5": {}, "d6": {}, "p4": {}, "p5": {}, "p6": {}, "a2": {}, "d2": {}, "p2": {}},
        "a5": {"a4": {}, "a6": {}, "d4": {}, "d5": {}, "d6": {}, "p4": {}, "p5": {}, "p6": {}},
        "a6": {"a4": {}, "a5": {}, "d4": {}, "d5": {}, "d6": {}, "p4": {}, "p5": {}, "p6": {}, "a2": {}, "d2": {}, "p2": {}},
        "d4": {"a4": {}, "a5": {}, "a6": {}, "d5": {}, "d6": {}, "p4": {}, "p5": {}, "p6": {}, "a2": {}, "d2": {}, "p2": {}},
        "d5": {"a4": {}, "a5": {}, "a6": {}, "d4": {}, "d6": {}, "p4": {}, "p5": {}, "p6": {}},
        "d6": {"a4": {}, "a5": {}, "a6": {}, "d4": {}, "d5": {}, "p4": {}, "p5": {}, "p6": {}, "a2": {}, "d2": {}, "p2": {}},
        "p4": {"a4": {}, "a5": {}, "a6": {}, "d4": {}, "d5": {}, "d6": {}, "p5": {}, "p6": {}, "a2": {}, "d2": {}, "p2": {}},
        "p5": {"a4": {}, "a5": {}, "a6": {}, "d4": {}, "d5": {}, "d6": {}, "p4": {}, "p6": {}},
        "p6": {"a4": {}, "a5": {}, "a6": {}, "d4": {}, "d5": {}, "d6": {}, "p4": {}, "p5": {}, "a2": {}, "p2": {}, "d2": {}},
    }
        
    G = nx.Graph(DICO_TEST)
    assert graphe.nodes == G.nodes


def test_collaborateurs_proches():
    assert collaborateurs_proches(graphe, "a1", 0) == set(graphe.adj["a1"])
    assert collaborateurs_proches(graphe_mini, "tom", 1) == {"paire", "OwO", "UwU", "patrick"}
    