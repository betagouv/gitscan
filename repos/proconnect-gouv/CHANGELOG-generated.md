# Synthèse d'activité : proconnect-gouv (du 22/07/2026 au 28/07/2026)

## Résumé de l'activité
L'activité de proconnect-gouv au cours des dernières semaines a été marquée par des améliorations significatives de l'expérience utilisateur et de la sécurité. Plusieurs dépôts ont été mis à jour pour renforcer l'authentification multi-facteurs (MFA), notamment avec l'ajout d'indicateurs de conformité et de tests pour les fournisseurs d'identité ([federation](/repos/proconnect-gouv/federation)). L'espace partenaires ([proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires)) a été enrichi de nouvelles fonctionnalités permettant aux partenaires de mieux gérer leurs collaborateurs et applications. Des améliorations ont également été apportées à l'outil de diagnostic "docteur-proconnect" ([docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect)) et à la librairie de validation de données [class-validator](/repos/proconnect-gouv/class-validator).

## Sécurité
Plusieurs changements ont été apportés pour améliorer la sécurité :
- Renforcement de la sécurité en supprimant `unsafe-inline` de la Content Security Policy dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- Refonte de la gestion des secrets OIDC dans [api-partenaires](/repos/proconnect-gouv/api-partenaires).
- Correction d'un bug autorisant des valeurs non sécurisées pour la configuration OIDC dans [api-partenaires](/repos/proconnect-gouv/api-partenaires).
- Mise à jour des dépendances vulnérables dans [class-validator](/repos/proconnect-gouv/class-validator).

## Autres changements notables
- Refactorisation de services en applications autonomes dans [federation](/repos/proconnect-gouv/federation) pour une meilleure architecture.
- Publication standalone du package `@proconnect-gouv/proconnect.email` dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- Migration vers la nouvelle image `api-partenaires` dans [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires).
- Amélioration du processus de tests d'intégration dans [idp-status-monitoring](/repos/proconnect-gouv/idp-status-monitoring).

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Améliorations de l'interface utilisateur pour le MFA et renforcement de la sécurité.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) : Ajout de fonctionnalités de gestion des collaborateurs et des applications pour les partenaires.
- [federation](/repos/proconnect-gouv/federation) : Ajout d'indicateurs de conformité MFA et refactorisation de l'architecture.
- [class-validator](/repos/proconnect-gouv/class-validator) : Ajout de nouveaux validateurs et correction de vulnérabilités.
- [proconnect-test-client](/repos/proconnect-gouv/proconnect-test-client) : Amélioration de la flexibilité du flux d'authentification et mises à jour de dépendances.
