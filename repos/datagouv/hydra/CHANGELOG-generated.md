## Changelog : hydra (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette version apporte des améliorations à la robustesse du système, notamment dans la gestion des requêtes HTTP et des erreurs.  Elle inclut également une mise à jour de la librairie `csv-detective` et des ajustements pour aligner le comportement de l'outil en ligne de commande avec l'API. Enfin, des refactorings internes ont été effectués pour améliorer la structure du code.

### Évolutions fonctionnelles
- Amélioration de la commande `check resource` en ligne de commande pour l'aligner avec le comportement de l'API. [#459](https://github.com/datagouv/hydra/pull/459)
- Correction d'un problème lié à la gestion des requêtes HEAD, améliorant la fiabilité de la vérification des ressources. [#460](https://github.com/datagouv/hydra/pull/460)

### Évolutions techniques
- Mise à jour de la librairie `csv-detective` vers la version 0.12.0. [#463](https://github.com/datagouv/hydra/pull/463)
- Refactorisation des utilitaires de base de données pour une meilleure organisation du code. (Annulé par la suite) [#452](https://github.com/datagouv/hydra/pull/452)
- Utilisation du token UV recommandé pour les publications CI/CD. [#451](https://github.com/datagouv/hydra/pull/451)

### Autres changements
- Documentation mise à jour pour refléter le comportement actuel de l'API, de la ligne de commande et des workers.
- Suppression de cibles obsolètes liées au chemin de stockage.
- Ajout de tests unitaires pour le module `file.py`.
