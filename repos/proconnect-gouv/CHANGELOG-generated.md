# Synthèse d'activité : proconnect-gouv (du 01/09 au 30/09)

## Résumé de l'activité
L'activité récente de l'organisation se concentre sur la robustesse et l'extension de son écosystème. Les efforts ont porté sur le renforcement de la sécurité des accès (2FA, WebAuthn) et la garantie de la continuité de service grâce à de nouveaux mécanismes de secours en cas d'indisponibilité de services tiers [federation](/repos/proconnect-gouv/federation). 

Parallèlement, l'organisation enrichit son offre avec le lancement de plusieurs nouveaux outils, notamment un thème visuel pour Tailwind CSS [tailwindcss-dsfr-theme](/repos/proconnect-gouv/tailwindcss-dsfr-theme), un service de résolution DNS [mx-resolver](/repos/proconnect-gouv/mx-resolver) et un buildpack pour le déploiement d'applications Bun [bun-buildpack](/repos/proconnect-gouv/bun-buildpack). Ces évolutions visent à offrir une expérience plus fiable aux utilisateurs finaux tout en simplifiant l'intégration pour les partenaires [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires).

## Sécurité
- Renforcement de l'authentification via le forçage de la 2FA par organisation, la réintroduction de l'interface WebAuthn (Passkeys) et l'augmentation du rate limiting [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- Amélioration de la protection des données par l'anonymisation des exports et la sécurisation des accès via la suppression des rôles de scopes par défaut [proconnect-identite](/repos/proconnect-gouv/proconnect-identite), [api-partenaires](/repos/proconnect-gouv/api-partenaires).
- Sécurisation des processus de validation des domaines pour les partenaires [api-partenaires](/repos/proconnect-gouv/api-partenaires).
- Adoption de l'algorithme de signature RS256 par défaut et correction de failles liées aux politiques de sécurité de contenu (CSP) [federation](/repos/proconnect-gouv/federation).
- Mise à jour des mécanismes d'authentification multi-facteurs (MFA) [proconnect-test-client](/repos/proconnect-gouv/proconnect-test-client) et correction de vulnérabilités de dépendances [class-validator](/repos/proconnect-gouv/class-validator).

## Autres changements notables
- Refonte majeure de l'infrastructure de tests automatisés (E2E) vers un système basé sur Buncept pour améliorer la stabilité [hyyypertool](/repos/proconnect-gouv/hyyypertool).
- Mise en place de mécanismes de résilience (fallback sur cache) pour assurer la continuité de service lors d'indisponibilités des API externes [federation](/repos/proconnect-gouv/federation).
- Modernisation de l'environnement de développement avec l'introduction de Nix [hyyypertool](/repos/proconnect-gouv/hyyypertool).
- Optimisation des processus d'authentification via l'intégration de Keycloak et Entra ID [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires).
- Migration vers une gestion par "feature flags" et découplage de dépendances critiques pour accroître l'autonomie du système [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Évolutions majeures sur la sécurité, l'authentification et la protection des données.
- [hyyypertool](/repos/proconnect-gouv/hyyypertool) : Refonte de la suite de tests et amélioration de l'expérience développeur.
- [federation](/repos/proconnect-gouv/federation) : Amélioration de la résilience du système et optimisation de l'infrastructure.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) : Renforcement de l'authentification et enrichissement de la documentation technique.
- [api-partenaires](/repos/proconnect-gouv/api-partenaires) : Sécurisation des domaines et optimisation des performances.
