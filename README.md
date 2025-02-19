# RouletteBot

## Description
RouletteBot est une extension web qui automatise les mises sur un site de casino en ligne en suivant une stratégie basée sur une martingale utilisant les tiers. En complément, des scripts en Python permettent de tester cette stratégie à l'aide de la bibliothèque `random`.

L'objectif du projet était d'analyser la viabilité de cette approche et d'en tirer des conclusions sur sa rentabilité.

## Fonctionnalités
- **Extension Web** : Automatise les mises sur le site de casino en ligne selon la stratégie martingale.
- **Scripts Python** : Permettent de tester la stratégie avec des simulations aléatoires.
- **Analyse des Résultats** : Évaluation statistique des gains et pertes pour déterminer la rentabilité de la stratégie.

## Résultats de l'étude
Après plusieurs simulations, il a été conclu que cette stratégie **n'est pas rentable** sur le long terme. Dans les meilleurs cas, la probabilité de réaliser un gain de 30 % était de **0.61** (61 %), ce qui ne permet pas de garantir un profit durable.

## Installation
### Extension Web
1. Clonez le dépôt :
   ```sh
   git clone https://github.com/votreutilisateur/RouletteBot.git
   ```
2. Chargez l'extension manuellement dans votre navigateur :
   - Allez dans `chrome://extensions/` (ou équivalent pour votre navigateur).
   - Activez le mode développeur.
   - Cliquez sur "Charger l'extension non empaquetée" et sélectionnez le dossier du projet.

### Scripts Python
1. Installez les dépendances :
   ```sh
   python rouletteTest.py
   ```

## Avertissement
⚠️ **Ce projet est uniquement à but éducatif**. L'utilisation de bots et de scripts automatisés sur les sites de casino en ligne peut être contraire à leurs conditions d'utilisation et entraîner une interdiction de compte. De plus, les jeux de hasard comportent un risque élevé de perte financière.

## Licence
Ce projet est distribué sous la licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---



