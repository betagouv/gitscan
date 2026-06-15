## Changelog : agreste (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, le projet agreste a connu des évolutions majeures, notamment l'ajout de fonctionnalités pour la gestion des publications, des thématiques et des collections. Ces nouveautés visent à enrichir l'expérience utilisateur et à faciliter la publication de contenus. Des améliorations techniques ont également été apportées pour préparer le projet à une nouvelle phase de développement et améliorer sa stabilité.

### Évolutions fonctionnelles
- Ajout de la gestion des Publications, Thématiques et Collections, avec une interface dédiée et des tests associés. [#7](https://github.com/betagouv/agreste/pulls/7)
- Implémentation de filtres sur les Publications, permettant aux utilisateurs d'affiner leurs recherches par thématique.
- Intégration d'un bloc "Publications récentes" pour afficher les dernières publications sur les pages. [#11](https://github.com/betagouv/agreste/pulls/11)
- Suppression des thèmes sur les cartes et index des publications pour une présentation plus claire. [#9](https://github.com/betagouv/agreste/pulls/9)
- Amélioration de la navigation et de l'affichage des paramètres d'URL pour les filtres.
- Ajout d'une fonctionnalité de promotion de page corrigée pour éviter les erreurs liées à l'ORM.
- Ajout d'une indication claire pour les utilisateurs lors de l'exécution de migrations en mode "dry run".

### Évolutions techniques
- Préparation à la version 4.0.0-rc1 avec plusieurs itérations et corrections.
- Mise en place d'un système de versionnement pour faciliter le suivi des évolutions.
- Refactorisation du code pour améliorer la réutilisation et la maintenabilité, notamment pour la gestion des taxonomies.
- Intégration de Sentry pour la surveillance des erreurs et l'amélioration de la qualité du code. [#445](https://github.com/betagouv/agreste/pulls/445)
- Mise à jour de la documentation pour refléter les dernières modifications. [#511](https://github.com/betagouv/agreste/pulls/511)
- Préparation à la "packagification" du projet pour une meilleure distribution et gestion des dépendances. [#506](https://github.com/betagouv/agreste/pulls/506)
- Suppression des thèmes sur les cartes et index des publications pour une présentation plus claire.

### Autres changements
- Mise à jour du fichier README pour refléter l'abandon du rebasage des changements sur Sites Conformes.
- Suppression d'un script de gestion des traductions devenu obsolète.
- Ajout de commentaires pour faciliter la compréhension du code et le suivi des modifications.
- Corrections de linting pour améliorer la qualité du code.
- Ajout d'une commande `just` supplémentaire pour la gestion des traductions.
- Mise à jour des dépendances et des configurations.
- Amélioration de la procédure de mise à niveau du projet.
- Ajout d'une règle `robots.txt` pour interdire l'indexation par les moteurs de recherche.
- Ajout d'un fichier `slugignore` pour exclure certains éléments de l'URL.
