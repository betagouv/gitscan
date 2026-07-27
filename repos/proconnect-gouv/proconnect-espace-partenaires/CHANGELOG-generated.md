## Changelog : proconnect-espace-partenaires (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'espace partenaires, notamment la possibilité pour les partenaires de supprimer leurs applications et d'ajouter des collaborateurs. Des corrections de sécurité et des mises à jour de documentation ont également été intégrées, ainsi qu'une meilleure préparation pour la migration vers ProConnect.

### Évolutions fonctionnelles
- Les partenaires peuvent maintenant supprimer leurs applications. [#416](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/416)
- Possibilité d'ajouter des collaborateurs à un compte partenaire. [#386](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/386) (réverté puis réintroduit)
- Annonce de la migration vers ProConnect visible dans l'espace partenaire. [#408](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/408)
- Amélioration de la formulation du bandeau ProConnect.
- Clarification de l'annonce de migration ProConnect.
- Ajout d'un bouton ProConnect dans l'espace partenaires. [#413](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/413)
- Ajout d'une checklist de conformité MFA pour les FI.
- Ajout d'exemples de mots de passe et d'emails OTP dans le tableau AMR.
- Numérotation des sections de la note de conformité MFA.

### Évolutions techniques
- Amélioration de la robustesse des tests en réduisant leur dépendance à l'environnement ProConnect sandbox.
- Correction d'une dépendance cyclique avec `nodemailer`. [#409](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/409)
- Mise à jour des dépendances de développement : `tsx`, `typescript`, `@uuv/playwright`, `actions/setup-node`, `@playwright/test`, `stefanzweifel/git-auto-commit-action`, `actions/cache`.
- Utilisation de valeurs AMR standard pour le TOTP.
- Suppression du code lié à l'email OTP (considéré comme MFA faible).
- Ajout du dossier `.idea` à `.gitignore`.
- Mise à jour du lien vers le code de calcul du service public.

### Autres changements
- Application de `prettier` pour formater le code. [#402](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/402)
- Correction d'une erreur empêchant les utilisateurs de se supprimer eux-mêmes. [#403](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/403)
- Documentation du fonctionnement de ProConnect avec un schéma explicatif. [#400](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/400)
- Classification de l'email OTP comme eidas1-mfa (MFA faible). [#388](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/388)
- Corrections typographiques diverses. [#399](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/399) et [#401](https://github.com/proconnect-gouv/proconnect-espace-partenaires/issues/401)
