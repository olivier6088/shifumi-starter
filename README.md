# shifumi-starter

Starter code for shifumi.

🧠 Activités proposées:  
• 	Corriger les bugs du jeu  
• 	Ajouter des tests pour les cas limites  
• 	Améliorer les messages utilisateur  
• 	Étendre le jeu en CLI ou web (Flask ?)  
• 	Ajouter `coverage`, `flake8`, ou `black`  dans le pipeline  

## Correction

Lancement des tests avec la commande `pytest` depuis la racine du projet:
```bash
python -m pytest tests/
```

Lancement de la couverture des tests avec:
```bash
pip install coverage
coverage run -m pytest tests/
coverage report
coverage html # rapport visuel
```

Lancement de la vérification du linting avec:
```python
pip install flake8
flake8 shifumi/ tests/
```

Simulation locale des test du CI github:
```bash
pytest
flake8 shifumi/ tests/
coverage run -m pytest tests/
coverage report
```

Reformater automatiquement les fichiers suivant la `pep8` avec `black`:  
```bash
black shifumi tests
```
