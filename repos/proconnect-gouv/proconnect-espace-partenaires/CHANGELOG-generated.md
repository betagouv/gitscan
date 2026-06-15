## Changelog : proconnect-espace-partenaires (30 derniers jours, au 11 juin 2026)

### Résumé
Les dernières semaines ont été marquées par une amélioration significative de la documentation relative à l'eIDAS et à l'ANSSI, ainsi que par des corrections et des clarifications concernant les erreurs et les flux d'authentification. Des ajustements ont également été apportés à l'infrastructure et aux dépendances pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Amélioration de la documentation concernant les niveaux eIDAS pour les fournisseurs de service ([#352](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/352)).
- Clarification de la différence entre eIDAS1-MFA et eIDAS2 dans la documentation ([#349](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/349)).
- Ajout d'une page dédiée à l'erreur Y030031 (redirect_uri mismatch) dans la documentation ([#339](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/339)).
- Mise en place d'une authentification multi-facteurs (MFA) plus fiable et forte ([cf9d849](https://github.com/proconnect-gouv/proconnect-espace-partenaires/commit/cf9d849)).
- Correction d'informations inexactes dans les tests d'identifiants FI ([#346](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/346)).

### Évolutions techniques
- Mise à jour de la base de données MongoDB : renommage de la base en "corev2" et de l'utilisateur en "proconnect-app-api-partner" ([#337](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/337)).
- Suppression d'anciennes adresses IP ([#360](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/360)).
- Intégration de la norme eIDAS et du guide ANSSI dans la documentation, avec ajout au sidebar ([#355](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/355), [#350](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/350)).
- Refactoring de la documentation pour clarifier l'origine des données fournies ([#317](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/317)).
- Regroupement des données additionnelles et complémentaires dans la documentation ([#347](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/347)).
- Mise à jour des dépendances : `@uuv/playwright`, `proconnect-gouv/federation/api-partner`, `@playwright/test`, `tsx`, `fast-xml-parser`, `@aws-sdk/xml-builder`, `nodemailer`, `picomatch`.

### Autres changements
- Ajout de mentions concernant la table des matières de l'organisation dans la documentation ([#351](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/351), [#348](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/348)).
- Suppression d'une exigence d'autorisation obsolète pour les rôles dans la documentation ([#353](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/353)).
- Amélioration du linter.
- Correction d'une faute de frappe ([#340](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/340), [#354](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/354)).
- Correction d'un problème de configuration du serveur web UUV dans les tests E2E.
