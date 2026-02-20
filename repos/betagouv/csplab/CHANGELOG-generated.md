## Changelog : csplab (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'ingestion et du traitement des offres d'emploi, ainsi que sur le développement de nouvelles fonctionnalités pour le module Tycho, notamment l'ajout d'un flux de gestion des candidatures avec affichage des CVs et un système de correspondance entre les CVs et les offres. Des améliorations techniques ont également été apportées à l'infrastructure et aux outils de développement.

### Évolutions fonctionnelles
- **Tycho (Candidatures):** Ajout d'un flux de gestion des candidatures, incluant l'affichage des CVs et un système de correspondance entre les CVs et les offres (#167, #180, #182, #183).
- **Tycho (Ingestion):** Amélioration de l'ingestion des offres d'emploi, notamment en permettant de traiter les documents par lots (#208) et en vectorisant les offres (#166).
- **Interface utilisateur:** Ajout de filtres pour les résultats de CV dans Tycho (#178, #204).
- **Ingestion:** Possibilité de nettoyer les documents ingérés (#138).

### Évolutions techniques
- **Authentification:** Sécurisation de toutes les API avec une authentification JWT (#210).
- **Infrastructure:** Mise à jour de Django en version 6.0.1 et de psycopg en version 3.3.2 (#143, #144).
- **Outils de développement:** Amélioration de la configuration de l'environnement de développement, ajout du Django Debug Toolbar (#186), et configuration de Sentry (#192).
- **Refactoring:** Refactorisation des administrateurs Django pour rendre certains champs en lecture seule (#184).
- **Architecture:** Remplacement des identifiants d'entités par des UUID (#201).
- **Tests:** Réduction de la verbosité des tests (#199) et amélioration des tests d'ingestion (#130).
- **Frontend:** Migration du CSS vers SCSS modulaire et mise en place d'outils de linting (prettier, stylelint) (#121, #122).

### Autres changements
- Nettoyage du code et de la configuration du dépôt (#211).
- Mise à jour de la documentation et du CHANGELOG (#131, #87).
- Amélioration de la gestion des erreurs dans le flux de candidature (#164).
- Ajout de la gestion des images CSP pour les intégrations futures (#179).
- Exploration des DTOs Talentsoft dans les notebooks (#124).
- Correction de bugs liés à la localisation et au nettoyage des références (#154).
- Correction d'un problème de swapping de contenu dans le polling (#165).
- Correction d'un problème de configuration de Tycho avec Django 6 (#151).
