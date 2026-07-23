## Changelog : proconnect-espace-partenaires (30 derniers jours, au 22 juillet 2026)

### Résumé
Les dernières mises à jour de l'Espace Partenaires ProConnect se concentrent sur l'amélioration de la sécurité avec l'implémentation de la double authentification (MFA) et l'ajout de fonctionnalités pour faciliter la gestion des accès, notamment la possibilité d'ajouter des collaborateurs. Des améliorations de la documentation et des corrections de bugs ont également été apportées.

### Évolutions fonctionnelles
- Les partenaires peuvent désormais supprimer leurs applications. [#416](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/416)
- Possibilité pour les partenaires d'ajouter des collaborateurs à leur espace. [#386](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/386) (Annulation temporaire puis réintégration)
- Une annonce concernant la migration vers ProConnect est désormais visible dans l'interface. [#408](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/408)
- Un bouton ProConnect a été ajouté à l'Espace Partenaires. [#413](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/413)
- Amélioration de la documentation concernant la double authentification (MFA) avec schémas de flux et contexte pour les Fournisseurs d'Identité (FI). [#390](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/390) et [#375](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/375)
- Ajout d'une checklist de conformité MFA pour les FI. [#400](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/400)

### Évolutions techniques
- Amélioration de la robustesse des tests en réduisant leur dépendance à l'environnement ProConnect de test.
- Correction d'un conflit de dépendance avec `nodemailer`. [#409](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/409)
- Mise à jour des dépendances : `tsx`, `actions/setup-node`, `typescript`, `@uuv/playwright`, `@playwright/test`, `stefanzweifel/git-auto-commit-action`, `actions/cache`.
- Utilisation de valeurs AMR (Authentification Multi-Facteur) standard pour le TOTP. [#385](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/385)
- Suppression du code lié à l'authentification par email OTP (One-Time Password).
- Correction d'un problème empêchant la suppression d'utilisateurs. [#403](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/403)

### Autres changements
- Amélioration du wording du bandeau ProConnect.
- Clarification de l'annonce de migration ProConnect.
- Application de Prettier pour formater le code. [#402](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/402)
- Corrections de typos et améliorations de la documentation. [#401](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/401), [#399](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/399), [#393](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/393)
- Ajout du dossier de configuration IntelliJ IDEA au `.gitignore`. [#391](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/391)
- Classification de l'email OTP comme MFA faible (eidas1-mfa). [#388](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/388)
