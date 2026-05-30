# Synthèse d'activité : proconnect-gouv (du 05 mai 2026 au 28 mai 2026)

## Résumé de l'activité
L'activité récente de l'organisation proconnect-gouv s'est concentrée sur l'amélioration de la sécurité, de la stabilité et de l'expérience utilisateur de ses différentes applications. Plusieurs dépôts ont bénéficié de mises à jour de dépendances pour corriger des vulnérabilités et améliorer les performances. Des fonctionnalités importantes ont été ajoutées à [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) avec l'implémentation de l'authentification multi-facteur (MFA) et des améliorations de la documentation.  [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) a vu des améliorations du diagnostic des problèmes OIDC et le début de la migration des emails MonComptePro.  La librairie [class-validator](/repos/proconnect-gouv/class-validator) a reçu des ajouts de validateurs pour des formats de données spécifiques (IBAN, ISO, UUID) et des améliorations de la validation conditionnelle.

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de dépendances pour corriger des vulnérabilités :
- [proconnect-test-client](/repos/proconnect-gouv/proconnect-test-client) a mis à jour plusieurs dépendances, dont `node-openid-client`.
- [proconnect-landing-page](/repos/proconnect-gouv/proconnect-landing-page) a mis à jour `dotenv` et `openid-client`.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) a rétrogradé une mise à jour de `nodemailer` causant des problèmes.
- [proconnect-federation](/repos/proconnect-gouv/federation) a mis à jour de nombreuses dépendances pour améliorer la sécurité.
- [class-validator](/repos/proconnect-gouv/class-validator) a corrigé des vulnérabilités de dépendances.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) a implémenté une limitation du débit par adresse IP.

## Autres changements notables
- [proconnect-federation](/repos/proconnect-gouv/federation) a mis à jour Node.js en version 24.16 et refondue l'indicateur d'environnement de production.
- [class-validator](/repos/proconnect-gouv/class-validator) a ajouté des validateurs pour les formats IBAN, ISO 639-1, ISO 3166-1 numérique et UUID, ainsi qu'une option de validation conditionnelle.
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) a débuté la migration des emails MonComptePro et a corrigé l'importation du type `pg`.

## Dépôts les plus actifs
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) : Ajout de la gestion de l'authentification multi-facteur (MFA) et améliorations de la documentation.
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Amélioration du diagnostic des problèmes OIDC et début de la migration des emails MonComptePro.
- [proconnect-federation](/repos/proconnect-gouv/federation) : Améliorations de la sécurité, de la gestion des rôles et de l'accessibilité.
- [class-validator](/repos/proconnect-gouv/class-validator) : Ajout de nouveaux validateurs et amélioration de la validation conditionnelle.
- [hyyypertool](/repos/proconnect-gouv/hyyypertool) : Ajout du mode sombre, amélioration de la gestion des modérations et renforcement de la sécurité.
