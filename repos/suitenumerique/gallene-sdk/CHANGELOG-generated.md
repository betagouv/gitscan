## Changelog : gallene-sdk (30 derniers jours, au 21 avril 2026)

### Résumé
Ce changelog marque le début du développement du SDK Gallene. Les premiers pas ont été réalisés avec la mise en place de la structure du projet, l'implémentation initiale de l'API côté client et la création de tests unitaires pour valider le fonctionnement de l'authentification et la gestion des erreurs.

### Évolutions fonctionnelles
- Implémentation initiale de l'API Gallene côté client, permettant l'interaction avec les fonctionnalités de Gallene. [#1](https://github.com/suitenumerique/gallene-sdk/pull/1)
- Mise en place des tests unitaires pour l'authentification (gestion des tokens d'accès) et la gestion des exceptions.

### Évolutions techniques
- Initialisation du dépôt avec la structure de base du SDK. [#1](https://github.com/suitenumerique/gallene-sdk/commit/9743a29)
- Intégration de `respx` pour la simulation des requêtes lors des tests.
- Utilisation de `pytest` pour l'exécution des tests unitaires.

### Autres changements
- Importation des fichiers initiaux depuis un dépôt privé.
