## Changelog : proconnect-espace-partenaires (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, l'espace partenaires a bénéficié d'améliorations significatives en matière de documentation, notamment concernant l'authentification multifacteur (MFA) et le fonctionnement de ProConnect. Une nouvelle fonctionnalité permettant aux partenaires d'ajouter des collaborateurs a été introduite, puis temporairement revertée pour correction. Des corrections de typos et de dépendances ont également été apportées pour améliorer la stabilité et la qualité du code.

### Évolutions fonctionnelles
- Les partenaires peuvent maintenant ajouter des collaborateurs à leur espace, bien que cette fonctionnalité ait été temporairement désactivée pour correction. [#386](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/386)
- Amélioration de la documentation concernant l'authentification multifacteur (MFA) : schémas de flux, calendrier de déploiement et contexte ACR pour les Fournisseurs d'Identité (FI). [#390](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/390) et [#375](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/375)
- Classification de l'authentification par email OTP comme MFA faible (eidas1). [#388](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/388)
- Annonce de la migration ProConnect dans l'espace partenaire. [#408](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/408)

### Évolutions techniques
- Correction d'une dépendance conflictuelle avec `nodemailer`. [#409](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/409)
- Mise à jour de plusieurs dépendances de développement : `@uuv/playwright`, `@playwright/test`, `js-yaml`, `@babel/core`, `form-data`, `nodemailer`, `stefanzweifel/git-auto-commit-action`, `actions/cache`, `actions/checkout`.
- Suppression d'une note de prudence concernant la définition des niveaux ACR. [#367](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/367)
- Utilisation de valeurs standard pour le TOTP dans l'AMR. [#385](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/385)
- Ajout du dossier de configuration IntelliJ IDEA au `.gitignore`. [#391](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/391)
- Validation de la compatibilité `npm prune` dans la CI. [#407](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/407)
- Application de Prettier sur l'ensemble du projet. [#402](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/402)
- Correction pour empêcher les utilisateurs de s'auto-supprimer. [#403](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/403)

### Autres changements
- Ajout d'une checklist de conformité MFA pour les FI.
- Documentation : schéma explicatif du fonctionnement de ProConnect. [#400](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/400)
- Ajout d'un exemple de mot de passe et d'email OTP dans le tableau AMR.
- Numérotation des sections de la note de conformité MFA.
- Corrections de typos diverses. [#399](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/399), [#401](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/401), [#393](https://github.com/proconnect-gouv/proconnect-espace-partenaires/pull/393), [#9ad5321](https://github.com/proconnect-gouv/proconnect-espace-partenaires/commit/9ad5321c11120285459935c83582786391135927)
