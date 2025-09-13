"""Imports et définition des variables globales"""
import csv
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, 'r', encoding='utf8') as f:
        r = csv.reader(f, delimiter=';')
        for ligne in r:
            ligne_entier = [int(x) for x in ligne]
            l.append(ligne_entier)
    return l

def get_list_k(data, k):
    """donne la k ieme liste"""
    l = data[k]
    return l

def get_first(l):
    """donne le premier element d'une liste"""
    return l[0]

def get_last(l):
    "donne le dernier element d'une liste"
    return l[-1]

def get_max(l):
    """donne la valeur maximale d'une liste"""
    return max(l)

def get_min(l):
    """donne la valeur minimale d'une liste"""
    return min(l)

def get_sum(l):
    """donne la somme des elements d'une liste"""
    return sum(l)


#### Fonction principale


def main():
    """programme principal"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
