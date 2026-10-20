#!/usr/bin/env python
# -*- coding: utf-8 -*-

def majuscule(mot):
    # TODO completer la fonction ici
    liste_mot = list(mot)
    mot = ""
    for i in liste_mot:
        char_code = ord(i)
        char_code_maj = char_code - 32
        char_maj = chr(char_code_maj)
        mot += (char_maj)
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
