## Changelog : aldo (30 derniers jours, au 10 novembre 2026)

### Résumé
Ce mois-ci, l'outil a été optimisé pour offrir une navigation plus fluide, notamment grâce à des calculs de territoire instantanés sans rechargement de page. Les capacités d'analyse ont été enrichies par l'intégration de nouvelles pratiques agricoles dans le module CAT'ENR. En parallèle, une mise à jour technique majeure a permis de renforcer la sécurité, d'améliorer la rapidité de démarrage et de moderniser l'architecture logicielle.

### Évolutions fonctionnelles
- Amélioration de l'expérience utilisateur avec la mise à jour des calculs de territoire sans rechargement de la page [#207](https://github.com/incubateur-ademe/aldo/issues/207).
- Enrichissement de l'outil CAT'ENR avec l'intégration des pratiques agricoles stockantes [#203](https://github.com/incubateur-ademe/aldo/issues/203).
- Amélioration de la précision des données via la normalisation des codes INSEE et la correction des calculs de flux EPCI.
- Optimisation de l'interface CAT'ENR pour un affichage de l'onglet piloté par les paramètres d'URL.

### Évolutions techniques
- Modernisation de l'architecture : migration vers un TypeScript strict exécuté nativement par Node 24 et suppression de la bibliothèque jQuery pour alléger le front-end.
- Optimisation de l'infrastructure : séparation des processus de build et de démarrage, ajout d'un système de contrôle de santé (health check) pour Coolify [#213](https://github.com/incubateur-ademe/aldo/issues/213) et réduction de la consommation mémoire au démarrage du serveur.
- Renforcement de la sécurité : correction de plusieurs vulnérabilités sur des dépendances critiques (`csvtojson`, `image-size`).
- Refactoring du code pour une meilleure maintenabilité, notamment via la factorisation des listes d'occupations et des paires de flux.
