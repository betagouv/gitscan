# Synthèse d'activité : proconnect-gouv (du 22/07 au 31/07)

## Résumé de l'activité
L'activité de cette période est marquée par une amélioration significative de l'expérience utilisateur, notamment via l'évolution des interfaces d'authentification multi-facteurs (MFA) [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) et [proconnect-test-client](/repos/proconnect-gouv/proconnect-test-client), ainsi que par une simplification des parcours pour les partenaires [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires).

Sur le plan technique, l'organisation poursuit la modernisation de son infrastructure avec une refactorisation vers une architecture de microservices [federation](/repos/proconnect-gouv/federation) et le lancement de nouveaux services de support et de monitoring [mx-resolver](/repos/proconnect-gouv/mx-resolver) et [monitoring-pinger](/repos/proconnect-gouv/monitoring-pinger).

## Sécurité
- Renforcement de la sécurité via la mise à jour des politiques de sécurité du contenu (CSP) pour limiter les risques d'injection [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) et [federation](/repos/proconnect-gouv/federation).
- Amélioration de la gestion des secrets OIDC pour une cryptographie plus robuste et ajout de tests de régression suite à un audit de sécurité [api-partenaires](/repos/proconnect-gouv/api-partenaires).
- Correction de vulnérabilités dans les dépendances de la librairie de validation [class-validator](/repos/proconnect-gouv/class-validator).

## Autres changements notables
- Refactorisation majeure de l'architecture par l'extraction de plusieurs microservices en applications autonomes [federation](/repos/proconnect-gouv/federation).
- Initialisation de nouveaux projets structurants : un fournisseur d'identité de test [proconnect-test-idp](/repos/proconnect-gouv/proconnect-test-idp), un service de résolution MX [mx-resolver](/repos/proconnect-gouv/mx-resolver), un outil de monitoring [monitoring-pinger](/repos/proconnect-gouv/monitoring-pinger) et un buildpack pour Bun [bun-buildpack](/repos/proconnect-gouv/bun-buildpack).
- Mise à jour importante de la cartographie des identifiants SIRET pour la précision de la fédération d'identité [oidc2fer](/repos/proconnect-gouv/oidc2fer).
- Optimisation de l'outil de gestion interne avec de nouvelles fonctionnalités d'édition et d'affichage [hyyypertool](/repos/proconnect-gouv/hyyypertool).

## Dépôts les plus actifs
- [federation](/repos/proconnect-gouv/federation) : Refactorisation architecturale majeure et préparation du MFA.
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Évolutions de l'interface MFA et de la gestion des communications.
- [api-partenaires](/repos/proconnect-gouv/api-partenaires) : Gestion des clients OIDC et sécurisation des secrets.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) : Améliorations fonctionnelles et interface pour les partenaires.
- [hyyypertool](/repos/proconnect-gouv/hyyypertool) : Optimisation de l'interface de gestion et de l'expérience utilisateur.
