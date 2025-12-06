# shifumi-starter

Petit projet de démarrage pour (re)mettre en place un pierre-feuille-ciseaux en Python. Il contient la logique minimale du jeu et quelques tests de base pour s'entraîner à corriger et faire évoluer l'application.

## Prérequis
- Python 3.10+
- `pip`
- Un environnement virtuel (fortement recommandé)

## Installation
```bash
python -m venv .venv
source .venv/bin/activate  # sous Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Lancer les tests
```bash
pytest
```

## Structure du dépôt
- `shifumi/game.py` : logique actuelle du jeu.
- `tests/test_game.py` : tests unitaires existants.
- `requirements.txt` : dépendances Python.

## Idées d'amélioration
- Corriger les bugs et couvrir les cas limites manquants.
- Ajouter de nouveaux tests et mesurer la couverture.
- Améliorer les messages utilisateur (CLI ou web).
- Étendre le jeu via une interface CLI ou Flask.
- Intégrer des outils de qualité (coverage, flake8, black) au pipeline.

## Contribution
1. Créer une branche à partir de `main`.
2. Effectuer vos changements avec des commits clairs.
3. Vérifier que les tests passent (`pytest`).
4. Ouvrir une Pull Request en décrivant le problème et la solution.
