## Changelog : proconnect-test-client (30 derniers jours, au 01 juin 2026)

### Résumé
Ce changelog fait état de plusieurs améliorations concernant la gestion de l'authentification multi-facteurs (MFA) et la configuration des variables d'environnement. Des corrections mineures ont également été apportées pour améliorer la robustesse du code. De nombreuses mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la compatibilité du projet.

### Évolutions fonctionnelles
- Mise à jour des valeurs ACR (Authentication Context Class) pour supporter l'authentification multi-facteurs (2FA). Cela permet de tester plus précisément les scénarios d'authentification avec MFA. [#193](https://github.com/proconnect-gouv/proconnect-test-client/pull/193)
- Correction d'une erreur liée au nom d'une variable et à la gestion des chaînes de caractères vides. [#194](https://github.com/proconnect-gouv/proconnect-test-client/pull/194)

### Évolutions techniques
- Harmonisation des variables d'environnement pour une meilleure cohérence et maintenabilité. [#194](https://github.com/proconnect-gouv/proconnect-test-client/pull/194)
- Nettoyage du fichier `.env` pour supprimer les éléments inutiles. [#194](https://github.com/proconnect-gouv/proconnect-test-client/pull/194)

### Autres changements
- Mises à jour de plusieurs dépendances :
    - `qs` (6.14.2 -> 6.15.2)
    - `@cypress/request`
    - `tmp` (0.2.5 -> 0.2.7)
    - `systeminformation` (5.31.1 -> 5.31.6)
    - `cypress` (15.13.0 -> 15.14.2)
    - `path-to-regexp` (8.2.0 -> 8.4.0)
    - `prettier` (3.8.1 -> 3.8.3)
    - `postcss` (8.5.2 -> 8.5.12)
    - `ejs` (4.0.1 -> 5.0.2)
    - `openid-client` (6.8.2 -> 6.8.4)
