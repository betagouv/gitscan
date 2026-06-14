## Changelog : api-tabular (30 derniers jours, au 12 juin 2026)

### Résumé
Cette nouvelle version apporte des améliorations significatives à la configuration de l'agrégation des données, permettant un contrôle plus fin sur cette fonctionnalité. Des corrections ont également été apportées pour améliorer la robustesse du pipeline CI/CD et la qualité du code, notamment en corrigeant des problèmes de linting et en améliorant la gestion des commits avec des messages de type "breaking change".

### Évolutions fonctionnelles
- Amélioration de la configuration de l'agrégation des données : introduction d'une configuration générale pour autoriser l'agrégation, avec la possibilité de définir des exceptions. ([#102](https://github.com/datagouv/api-tabular/pull/102))
- Possibilité d'utiliser des conditions complexes dans les requêtes. ([#103](https://github.com/datagouv/api-tabular/pull/103))
- Support des sauts de ligne dans les messages de commit de type "breaking change". ([#111](https://github.com/datagouv/api-tabular/pull/111))

### Évolutions techniques
- Correction de problèmes de linting détectés par l'analyse statique du code. ([#110](https://github.com/datagouv/api-tabular/pull/110))
- Amélioration du pipeline CI/CD :
    - Publication de l'image Docker uniquement lors d'un push sur la branche `main`.
    - Simplification de la configuration CircleCI. ([#99](https://github.com/datagouv/api-tabular/pull/99), [#97](https://github.com/datagouv/api-tabular/pull/97))
- Correction de l'initialisation de Sentry pour assurer le bon fonctionnement du suivi des performances. ([#91](https://github.com/datagouv/api-tabular/pull/91))
- Utilisation de `uptime_since` au lieu de `uptime_seconds` dans l'endpoint de santé pour une meilleure lisibilité. ([#104](https://github.com/datagouv/api-tabular/pull/104))
- Correction de la publication de l'image Docker lors de l'absence de tag Git. ([#112](https://github.com/datagouv/api-tabular/pull/112))
