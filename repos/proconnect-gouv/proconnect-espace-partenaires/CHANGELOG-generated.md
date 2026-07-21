## Changelog : proconnect-espace-partenaires (30 derniers jours, au 20 juillet 2026)

### Résumé
Les dernières mises à jour de l'Espace Partenaires ProConnect se concentrent sur l'amélioration de la documentation, la préparation à la migration vers ProConnect, et l'ajout de fonctionnalités pour faciliter la gestion des accès. Des corrections de bugs et des améliorations techniques ont également été apportées pour une meilleure stabilité et expérience utilisateur.

### Évolutions fonctionnelles

- Ajout d'un bouton ProConnect pour faciliter l'accès à la nouvelle plateforme. [#361](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/361)
- Annonce de la migration vers ProConnect dans l'interface Partenaire. [#408](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/408)
- Possibilité pour les partenaires d'ajouter des collaborateurs à leur compte. [#386](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/386) (temporairement reverté puis réintroduit)
- Prévention de la suppression de son propre compte par les utilisateurs. [#403](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/403)
- Amélioration de la documentation concernant l'authentification multi-facteurs (MFA) avec schémas de flux et contexte pour les FIs. [#390](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/390) et [#375](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/375)
- Classification de l'authentification par email OTP comme MFA faible (eidas1-mfa). [#388](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/388)

### Évolutions techniques

- Amélioration de la robustesse des tests en réduisant leur dépendance à l'environnement ProConnect sandbox. [#370](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/370)
- Correction d'un conflit de dépendance avec `nodemailer`. [#409](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/409)
- Mise à jour des dépendances de développement : TypeScript, Playwright, tsx, @babel/core, js-yaml, form-data, actions/checkout, actions/cache, stefanzweifel/git-auto-commit-action.
- Utilisation de valeurs AMR standard pour le TOTP. [#385](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/385)

### Autres changements

- Application de Prettier pour formater le code. [#402](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/402)
- Ajout d'une checklist de conformité MFA pour les FIs. [#400](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/400)
- Ajout d'exemples de mots de passe et d'emails OTP dans le tableau AMR.
- Numérotation des sections de la note de conformité MFA.
- Correction de typos dans la documentation. [#399](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/399) et [#413](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/413)
- Ajout du dossier de configuration IntelliJ IDEA au `.gitignore`. [#391](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/391)
- Mise à jour du lien vers le code de calcul du service public. [#384](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/384)
