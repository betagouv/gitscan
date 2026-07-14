## Changelog : proconnect-espace-partenaires (30 derniers jours, au 10 juillet 2026)

### Résumé
Les dernières mises à jour de l'espace partenaires ProConnect se concentrent sur l'amélioration de la documentation, la gestion des accès et la correction de bugs. Les partenaires peuvent désormais ajouter des collaborateurs à leur compte. Des améliorations ont été apportées à la documentation concernant l'authentification multifacteur (MFA) et les niveaux d'assurance.

### Évolutions fonctionnelles
- Les partenaires peuvent maintenant ajouter des collaborateurs à leur compte. [#386](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/386) (Annulé puis réintroduit)
- Correction d'un bug empêchant les utilisateurs de se supprimer eux-mêmes. [#403](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/403)
- Ajout d'une checklist de conformité MFA pour les Fournisseurs d'Identité (FI).
- Ajout d'un exemple de mot de passe et d'email OTP (One-Time Password) dans le tableau AMR (Assurance Métier Référentiel).
- Numérotation des sections de la note de conformité MFA pour une meilleure lisibilité.

### Évolutions techniques
- Mise à jour de la documentation pour classifier l'email OTP comme un MFA de niveau eIDAS1. [#388](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/388)
- Remplacement des valeurs TOTP (Time-based One-Time Password) non standard par des valeurs conformes.
- Suppression d'une note de mise en garde concernant la définition du niveau ACR (Assurance Certification Référentiel).
- Suppression de la distinction "géré par l'organisation" pour eIDAS2/eIDAS3 dans la documentation.
- Mise à jour des dépendances : Playwright, git-auto-commit-action, actions/cache, @babel/core, form-data, js-yaml, esbuild, actions/checkout et proconnect-gouv/federation/api-partner.
- Application de l'outil Prettier pour formater le code. [#402](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/402)
- Ajout du dossier de configuration IntelliJ IDEA au fichier .gitignore. [#391](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/391)

### Autres changements
- Amélioration de la documentation sur le fonctionnement de ProConnect avec un schéma explicatif. [#400](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/400)
- Mise à jour de la documentation sur l'authentification double. [#376](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/376)
- Correction de typos dans la documentation. [#399](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/399) et [#401](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/401)
- Mise à jour du lien vers le code de calcul du service public. [#384](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/384)
- Clarification du wording concernant la MFA. [#375](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/375)
