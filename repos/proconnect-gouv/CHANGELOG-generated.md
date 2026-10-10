# Synthèse d'activité : proconnect-gouv (du 01/10 au 10/10)

## Résumé de l'activité
L'activité récente est marquée par un renforcement significatif de la sécurité des accès et de la gestion des identités, notamment via l'amélioration des mécanismes d'authentification multi-facteurs (MFA) et la protection accrue de la vie privée. Ces évolutions visent à offrir une expérience plus fluide et sécurisée pour les utilisateurs finaux tout en garantissant une meilleure fiabilité des données grâce à l'intégration de nouvelles sources officielles comme l'API RNE.

Parallèlement, l'organisation diversifie son écosystème avec le lancement de plusieurs nouveaux outils et services, incluant un thème de design system pour Tailwind CSS [tailwindcss-dsfr-theme](/repos/proconnect-gouv/tailwindcss-dsfr-theme), un service de résolution DNS [mx-resolver](/repos/proconnect-gouv/mx-resolver) et un buildpack pour Bun [bun-buildpack](/repos/proconnect-gouv/bun-buildpack). L'accompagnement des partenaires est également une priorité, avec une mise à jour majeure de la documentation technique et métier [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires).

## Sécurité
- **Renforcement de l'authentification** : Généralisation du MFA, possibilité de forcer le 2FA par organisation [proconnect-identite](/repos/proconnect-gouv/proconnect-identite), gestion des codes OTP par e-mail [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) et mise à jour des flux d'authentification [proconnect-test-client](/repos/proconnect-gouv/proconnect-test-client).
- **Protection des données et de l'infrastructure** : Mise en place de politiques de limitation de débit (rate limiting) [proconnect-identite](/repos/proconnect-gouv/proconnect-identite), restriction des rôles pour la confidentialité [federation](/repos/proconnect-gouv/federation) et blocage de l'indexation des interfaces sensibles par les moteurs de recherche [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) et [federation](/repos/proconnect-gouv/federation).
- **Sécurisation des accès API** : Suppression des permissions de rôles par défaut dans les scopes [api-partenaires](/repos/proconnect-gouv/api-partenaires).

## Autres changements notables
- **Migrations et refontes techniques** : Migration majeure vers la version 8 de `oidc-provider` [federation](/repos/proconnect-gouv/federation), refonte massive de la suite de tests E2E vers un nouveau moteur [hyyypertool](/repos/proconnect-gouv/hyyypertool) et migration vers l'API RNE pour la gestion des organisations [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- **Nouveaux projets et services** : Lancement du thème DSFR pour Tailwind [tailwindcss-dsfr-theme](/repos/proconnect-gouv/tailwindcss-dsfr-theme), du service de résolution MX [mx-resolver](/repos/proconnect-gouv/mx-resolver), du buildpack pour Scalingo [bun-buildpack](/repos/proconnect-gouv/bun-buildpack) et d'un fournisseur d'identité de test [proconnect-test-idp](/repos/proconnect-gouv/proconnect-test-idp).
- **Évolutions des outils de développement** : Enrichissement de la bibliothèque de validation avec de nouveaux validateurs spécialisés (IBAN, ISO, UUID) [class-validator](/repos/proconnect-gouv/class-validator).

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Améliorations majeures de la sécurité, de la gestion des données et de l'expérience utilisateur.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) : Renforcement de la sécurité des comptes et mise à jour massive de la documentation.
- [hyyypertool](/repos/proconnect-gouv/hyyypertool) : Optimisation de la CI/CD, de la suite de tests et de l'infrastructure.
- [federation](/repos/proconnect-gouv/federation) : Migrations techniques importantes et améliorations de l'expérience utilisateur.
