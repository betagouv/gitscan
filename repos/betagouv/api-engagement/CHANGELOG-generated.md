## Changelog : api-engagement (30 derniers jours, au 2026-06-04)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse de l'API, notamment en gérant mieux les erreurs et en ajoutant des mécanismes de limitation du taux de requêtes. L'interface utilisateur de la plateforme a également été améliorée, en particulier pour l'accessibilité et l'expérience utilisateur sur mobile. Des refactorings importants ont été effectués pour préparer l'avenir du projet et simplifier la maintenance.

### Évolutions fonctionnelles

- **API :** Ajout d'une file d'attente de lettres mortes pour gérer les erreurs de traitement des missions [#1113](https://github.com/betagouv/api-engagement/issues/1113).
- **API :** Amélioration de la gestion des erreurs lors de la mise en file d'attente des missions, pour une meilleure résilience en cas de problèmes de file d'attente [#1088](https://github.com/betagouv/api-engagement/issues/1088).
- **Plateforme :** Amélioration de l'accessibilité de la carte des missions [#1103](https://github.com/betagouv/api-engagement/issues/1103).
- **Plateforme :** Amélioration de l'interface utilisateur du quiz et des missions sur la plateforme [#1090](https://github.com/betagouv/api-engagement/issues/1090).
- **Plateforme :** Redesign de la page des résultats sur mobile [#1074](https://github.com/betagouv/api-engagement/issues/1074).
- **API :** L'endpoint `v2/activity` est maintenant compatible avec l'utilisation par les diffuseurs [#1091](https://github.com/betagouv/api-engagement/issues/1091).
- **API :** Ajout de journaux d'audit pour le suivi des actions [#1019](https://github.com/betagouv/api-engagement/issues/1019).
- **Plateforme :** Ajout de la possibilité d'afficher la clé API pour les annonceurs dans les paramètres [#1015](https://github.com/betagouv/api-engagement/issues/1015).
- **Plateforme :** Amélioration de l'accessibilité des champs de formulaire (labels associés, attributs autocomplete) [#1086](https://github.com/betagouv/api-engagement/issues/1086), [#1087](https://github.com/betagouv/api-engagement/issues/1087), [#1089](https://github.com/betagouv/api-engagement/issues/1089).
- **Plateforme :** Amélioration de l'accessibilité des combobox et dialogs [#1053](https://github.com/betagouv/api-engagement/issues/1053), [#1054](https://github.com/betagouv/api-engagement/issues/1054), [#1055](https://github.com/betagouv/api-engagement/issues/1055), [#1057](https://github.com/betagouv/api-engagement/issues/1057), [#1058](https://github.com/betagouv/api-engagement/issues/1058).

### Évolutions techniques

- **API :** Implémentation d'une limitation du taux de requêtes (rate limiting) pour protéger l'API contre les abus [#1075](https://github.com/betagouv/api-engagement/issues/1075).
- **API :** Refactorisation du système de règles de diffusion des publications, passant d'une approche basée sur des exclusions à un moteur basé sur des règles [#1078](https://github.com/betagouv/api-engagement/issues/1078).
- **API :** Ajout d'un index unique pour optimiser les requêtes sur les enrichissements de missions [#1092](https://github.com/betagouv/api-engagement/issues/1092).
- **API :** Suppression d'un ancien modèle de taxonomie [#1079](https://github.com/betagouv/api-engagement/issues/1079).
- **Plateforme :** Suppression de l'expiration du score utilisateur [#1105](https://github.com/betagouv/api-engagement/issues/1105).
- **CI/CD :** Configuration de Typesense pour la production [#1068](https://github.com/betagouv/api-engagement/issues/1068).
- **CI/CD :** Ajout de tests et de workflows de linting pour la plateforme [#1085](https://github.com/betagouv/api-engagement/issues/1085).
- **API :** Amélioration de la résilience du worker d'enrichissement des missions en cas de limitation du taux de requêtes [#1073](https://github.com/betagouv/api-engagement/issues/1073).
- **Plateforme :** Utilisation d'un proxy serveur pour signer les requêtes [#1059](https://github.com/betagouv/api-engagement/issues/1059).

### Autres changements

- Mise à jour de la documentation.
- Ajout d'un fichier `AGENTS.md` pour la documentation des agents.
- Corrections mineures de style et de code.
- Publication des versions v1.5.0, v1.5.1, v1.6.0, v1.7.0 et v1.8.0/v1.8.1.
