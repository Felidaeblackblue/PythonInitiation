import re
#String

#Exo1
# def reverse_string(s):
#     return s[::-1]
# result = reverse_string ("salut")
# print(result)


#Exo2
# def count_letters(input_string):
#     countOfChars = dict()
#     for character in input_string:
#         if character in countOfChars:
#             countOfChars[character] += 1
#         else:
#             countOfChars[character] = 1
#     return countOfChars

# input_string = "Bonjour, monde!"
# print(count_letters(input_string))


# Exo3
# def est_un_palindrome(chaine):
#     chaine = chaine.lower().replace(' ', '')
# #La syntaxe [::-1] signifie commencez à la fin de la chaîne et 
# # aller vers le début, avec un pas de -1". Cela crée une copie de la chaîne en ordre inversé.
#     return chaine == chaine[::-1]

# chaine = "Radar"
# print(est_un_palindrome(chaine)) 

#Exo4
# def replace_space_with_dash(string):
#     return string.replace(' ', '-')

# string = "Hello, word!"
# print(replace_space_with_dash(string)) 

# #Exo5
# def find_longest_word(chaine):
#     mots = chaine.split()
#     return max(mots, key=len)

# print(find_longest_word("Le python est un excellent langage de programmation")) 


#Exo6
# def detecter_dates(chaine):
#     dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', chaine)
#     return dates

# print(detecter_dates("Les dates importantes sont 12/05/2022 et 23/11/2023.")) 

#Lists
# #Exo7
# def inverser_liste(liste):
#     liste.reverse()
#     return liste

# print(inverser_liste([1, 2, 3, 4, 5])) 

# #Exo8
# def elements_communs(liste1, liste2):
#     return list(set(liste1) & set(liste2))

# print(elements_communs([1, 2, 3, 4], [2, 4, 6, 8])) 


# #Exo10
# def compter_occurrences(liste, element):
#     return liste.count(element)

# print(compter_occurrences([1, 4, 2, 7, 4, 4, 3], 4)) # Affiche : 3

# #Tuple
# #Exo11 
# # Création du tuple
# mon_tuple = (1, "chat", 3.14, True)

# # Accès et impression du deuxième élément
# print(mon_tuple[1]) 


#Exo12
# mon_tuple = (1, "chat", 3.14, True)
# mon_tuple[2] = "python" 
## Cela provoquera une erreur

# mon_tuple2 = (1, "chat", 3.14, True)
# mon_tuple2 = mon_tuple2[:2] + ("python",) + mon_tuple2[3:]
# ##Cela ne provoquera pas d'erreur

#Exo13
# def max_min_moyenne(numeros):
#     max_numero = max(numeros)
#     min_numero = min(numeros)
#     somme_numero = sum(numeros)
#     moyen_numero = somme_numero / len(numeros)
#     return max_numero, min_numero, moyen_numero

# test_tuple = (10, 20, 30, 40, 50)
# resultat = max_min_moyenne(test_tuple)
# print("Max, Min, Moyenne:", resultat) # Affiche : (50, 10, 30.0)

#Exo14
# def trier_etudiants(etudiants):
#     return sorted(etudiants, key=lambda x: x[1], reverse=True)

# etudiants = [("Alice", 88), ("Bob", 95), ("Charlie", 78)]
# etudiants_tries = trier_etudiants(etudiants)
# print("Etudiants triés:", etudiants_tries) 

#Exo15
# def traiter_data(data):
#     # Filtrer pour ne garder que les tuples où le statut est "actif"
#     data_actif = [tup for tup in data if tup[2] == "actif"]
    
#     # Trier les tuples filtrés par le nombre en ordre décroissant
#     data_actif.sort(key=lambda x: x[1], reverse=True)
    
#     # Retourner une nouvelle liste de tuples, mais chaque tuple doit uniquement contenir l'identifiant et le nombre, sans le statut
#     return [(tup[0], tup[1]) for tup in data_actif]

# data = [("id1", 10, "actif"), ("id2", 15, "inactif"), ("id3", 20, "actif")]
# print(traiter_data(data)) # Affiche : [('id3', 20), ('id1', 10)]

#Dictionnaires (dict)

#Exo16
# Création du dictionnaire
livre = {"titre": "Les Misérables", "auteur": "Victor Hugo", "année": 1862}

# Affichage de la valeur associée à la clé "auteur"
print(livre["auteur"]) # Affiche : Victor Hugo


#Ensemble(set)
#Exo21
def intersection_without_multiples_of_three(set1, set2):
    # Calculer l'intersection des deux ensembles
    intersection = set1 & set2
    
    # Supprimer les multiples de 3
    intersection = {num for num in intersection if num % 3 != 0}
    
    return intersection
set1 = {1, 2, 3, 4, 6, 9}
set2 = {2, 3, 5, 6, 7, 9}
print(intersection_without_multiples_of_three(set1, set2)) # Output: {2}

