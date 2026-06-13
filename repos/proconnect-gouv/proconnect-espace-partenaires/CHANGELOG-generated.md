## Changelog : proconnect-espace-partenaires (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la documentation relative à l'eIDAS et à l'ANSSI, ainsi que sur la stabilisation et la correction de bugs. Des améliorations ont également été apportées à la gestion des erreurs et à la configuration de l'environnement de test.

### Évolutions fonctionnelles
- Amélioration de la documentation concernant les niveaux eIDAS pour les fournisseurs de service ([#352](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/352)).
- Clarification de la distinction entre eIDAS1-MFA et eIDAS2 dans la documentation ([#349](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/349)).
- Ajout d'une page dédiée dans la documentation pour l'erreur `redirect_uri mismatch` (Y030031) ([#339](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/339)).
- Mise à jour des informations inexactes dans les tests d'identifiants FI ([#346](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/346)).
- Intégration de l'authentification multi-facteurs (MFA) fiable/forte ([cf9d849](https://github.com/proconnect-gouv/proconnect-espace-partenaires/commit/cf9d849)).

### Évolutions techniques
- Refactorisation de la documentation eIDAS : ajout de la norme eIDAS et intégration des guides ANSSI ([#362](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/362), [#355](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/355), [#350](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/350)).
- Suppression d'anciennes adresses IP ([#360](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/360)).
- Renommage de la base de données MongoDB en `corev2` et de l'utilisateur en `proconnect-app-api-partner` ([#337](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/337)).
- Mise à jour des dépendances : `proconnect-gouv/federation/api-partner`, `@uuv/playwright`, `@playwright/test`, `tsx`, `fast-xml-parser`, `@aws-sdk/xml-builder`, `picomatch` (mises à jour automatiques).
- Correction de la configuration du serveur web UUV dans les tests E2E.
- Suppression d'une mise à jour de `nodemailer` qui causait des problèmes.

### Autres changements
- Ajout de mentions concernant l'organisation des labels dans la documentation ([#351](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/347), [#348](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/348)).
- Restructuration des données fournies dans la documentation pour clarifier leur origine ([#317](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/317)).
- Regroupement des données additionnelles et complémentaires dans la documentation ([#347](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/347)).
- Suppression d'une exigence d'autorisation obsolète pour le scope des rôles ([#353](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/353)).
- Amélioration du linter.
