#!/usr/bin/env python
#-*- coding: utf-8 -*-
import matplotlib
from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    tab_index = []
    for i in range(len(some_list)):
        tab_index.append(i)
    dict(zip(some_list[:],tab_index))
    return dict(zip(some_list[:],tab_index))


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    liste_couleur = []
    for color in colors :
        liste_couleur.append((color,cnames[color]))
    return liste_couleur


def create_list() -> list:
    # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350
    liste = []
    for i in range(0,10000) :
        if i>=15 and i<=350 :
            continue
        else :
            liste.append(i)


    return liste


def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    erreur = 0
    my_dict = {}
    for key,element in model_dict.items():
        for elem in element:
            erreur += (elem[1]-elem[0])**2
    my_dict[key] = erreur/len(element)
    return my_dict


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
