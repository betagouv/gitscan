## Changelog : matrix-admin-bot (30 derniers jours, au 18 septembre 2026)

### Résumé
Ce mois-ci, le bot a gagné en capacité de gestion avec l'ajout de la suppression des liens OAuth. Une part importante du travail a été consacrée à la robustesse et à la stabilité du système, notamment via une meilleure gestion des erreurs, une traçabilité accrue grâce à de nouveaux outils de journalisation (logs) et une optimisation des processus de déploiement et de tests.

### Évolutions fonctionnelles
- Ajout de la possibilité de supprimer les liens OAuth amont ([#56](https://github.com/tchapgouv/matrix-admin-bot/pull/56)).

### Évolutions techniques
- **Framework de commande** : Refonte de l'exécution des commandes pour inclure une gestion des verrous (locks) et une structure par étapes (steps), améliorant la fiabilité des opérations.
- **Gestion des données** : Optimisation de la gestion des sessions et du cache pour éviter la pollution de données en cas d'échec de commande.
- **Observabilité** : Renforcement du système de logging avec des niveaux configurables et une intégration directe au framework de base.
- **Infrastructure et CI/CD** : 
    - Mise à jour de l'image Docker de base vers Debian 13.
    - Optimisation de la CI/CD : fixation des versions des GitHub Actions, construction de l'image Docker lors des Pull Requests et restriction de l'exécution des tests à la branche principale.
- **Qualité logicielle** : Amélioration significative de la suite de tests grâce à l'introduction de helpers dédiés et de messages d'erreur plus explicites.

### Autres changements
- **Nettoyage du code** : Suppression de la bibliothèque `requests` devenue inutile, ajout de typage (type hints) et correction de commentaires et de noms de tests.
