# 🧠 Le compte est bon

Un jeu interactif de **calcul mental** où le joueur combine des nombres pour atteindre un **nombre cible**. 
Un bot *'intelligent'* peut également proposer une solution optimale.

## 🎮 Fonctionnalités
- **Génération aléatoire** d’un nombre cible entre **101 et 999**
- **Sélection de nombres** parmi une liste de départ
- **Choix d’opérateurs** mathématiques (+, -, *, /)
- **Calculs successifs** avec mise à jour des nombres disponibles
- **Détection automatique de victoire ou impossibilité de continuer**
- **Suggestion de solution** par un bot utilisant une approche récursive

### 🧰 Technologies utilisées
- **Python 3**
- **Modules standards** : random, operator, itertools

### 🚀 Pour lancer le jeu
    python main.py

### 📦 Structure du projet
- **main()** : point d’entrée du jeu
- **generate_target_number()** : génère le nombre cible
- **generate_balance_numbers()** : génère les nombres disponibles
- **get_user_operation()** : prend en input l'opération entière de l'utilisateur
- **calculate_operation()** : exécute l’opération et met à jour la liste
- **bot_solver()** : algorithme de résolution automatique
- **show_bot_solution()** : affiche la solution du bot
- **display_game_state()** : affiche l’état du jeu
- **ask_continue()** : demande au joueur s’il souhaite continuer à jouer

### 🤖 Algorithme du bot
Le bot explore **toutes les combinaisons possibles** de deux nombres avec les quatre opérateurs, en utilisant une **approche récursive**.
Il cherche la **solution la plus proche** du nombre cible.

### ✅ Conditions de fin
- Le **joueur atteint le nombre cible**
- Il ne reste **plus assez de nombres pour continuer**
- Le joueur choisit de **quitter**