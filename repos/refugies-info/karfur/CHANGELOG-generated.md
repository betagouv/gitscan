## Changelog : karfur (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la qualité du code, la correction de bugs, et l'ajout de fonctionnalités pour l'intégration de nouveaux contenus et l'amélioration de l'expérience utilisateur, notamment sur mobile. Une attention particulière a été portée à la gestion des doublons et à la préparation de l'intégration de nouveaux "skills" pour l'agent Letta.

### Évolutions fonctionnelles
- Correction de bugs d'affichage sur les fiches RCO sur Android et iOS [#3792](https://github.com/refugies-info/karfur/pull/3792).
- Amélioration de la gestion des erreurs lors de la prévisualisation des fiches [#3813](https://github.com/refugies-info/karfur/pull/3813).
- Correction de l'affichage des adresses postales tronquées sur les fiches RCO [#3778](https://github.com/refugies-info/karfur/pull/3778).
- Correction de problèmes de connexion et de réinitialisation de mot de passe [#3789](https://github.com/refugies-info/karfur/pull/3789).
- Correction de l'affichage des accents dans le moteur de recherche [#3769](https://github.com/refugies-info/karfur/pull/3769).
- Mise à jour des mentions légales sur le site et l'application [#3785](https://github.com/refugies-info/karfur/pull/3785).
- Correction de l'affichage des labels de département qui pouvaient masquer les pop-up [#3766](https://github.com/refugies-info/karfur/pull/3766).
- Amélioration de la réactivité des écrans de login sur mobile [#3767](https://github.com/refugies-info/karfur/pull/3767) et [#3753](https://github.com/refugies-info/karfur/pull/3753).

### Évolutions techniques
- Intégration de Letta Code pour l'analyse automatique du code via un workflow GitHub Actions [#3815](https://github.com/refugies-info/karfur/pull/3815).
- Ajout de tests et de validations pour la structure des "skills" QMD et corpus [#3797](https://github.com/refugies-info/karfur/pull/3797).
- Refactorisation et correction de la gestion des doublons, notamment pour l'agent Letta, avec ajout d'un endpoint dédié [#3754](https://github.com/refugies-info/karfur/pull/3754).
- Mise en place de scans de vulnérabilités de dépendances en pré-commit [#3779](https://github.com/refugies-info/karfur/pull/3779).
- Mise à jour des dépendances et correction de problèmes liés à la gestion des versions.
- Suppression des paramètres de configuration Claude.
- Suppression de code obsolète et nettoyage du code.

### Autres changements
- Documentation et clarification de la structure des "skills" pour l'agent Letta.
- Correction de coquilles et amélioration de la lisibilité de la documentation.
- Mise à jour des informations de contact dans les mentions légales.
- Suppression de badges RCO et simplification du code associé.
- Correction de problèmes liés à la gestion des valeurs nulles et des types de données.
- Amélioration des messages de log et de la gestion des erreurs.
