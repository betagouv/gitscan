# Synthèse d'activité : proconnect-gouv (du 13 juillet 2026 au 28 juillet 2026)

## Résumé de l'activité
L'activité récente de l'organisation proconnect-gouv s'est concentrée sur l'amélioration de la sécurité, l'enrichissement des fonctionnalités des outils existants et la mise en place de nouveaux services. Des avancées significatives ont été réalisées sur l'API Partenaires, qui est désormais opérationnelle avec une infrastructure CI/CD complète. L'authentification multi-facteurs (MFA) est également un axe majeur d'amélioration, avec des interfaces utilisateur modernisées et une meilleure gestion des méthodes d'authentification. Plusieurs dépôts ont bénéficié de mises à jour de dépendances pour assurer la stabilité et la sécurité des applications.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Restriction des méthodes d'authentification au niveau du point d'accès au token, suppression de `unsafe-inline` de la CSP, correction d'une copie anonymisée incorrecte.
- [federation](/repos/proconnect-gouv/federation) : Suppression des configurations TLS obsolètes et des certificats orphelins, suppression de `unsafe-inline` dans la CSP.
- [class-validator](/repos/proconnect-gouv/class-validator) : Mise à jour des dépendances vulnérables.

## Autres changements notables
- [api-partenaires](/repos/proconnect-gouv/api-partenaires) : Migration vers Bun et mise en place d'une infrastructure CI/CD complète.
- [class-validator](/repos/proconnect-gouv/class-validator) : Ajout de nouveaux validateurs (IBAN, ISO 639-1, ISO 3166-1 numérique, UUID) et introduction de l'option `validateIf`.
- [hyyypertool](/repos/proconnect-gouv/hyyypertool) : Refactorisation et amélioration de l'interface utilisateur pour la gestion des utilisateurs et des organisations.

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Amélioration de la sécurité, modernisation de l'interface MFA et amélioration des tests d'intégration.
- [federation](/repos/proconnect-gouv/federation) : Ajout de fonctionnalités d'administration (blocage d'utilisateurs, recherche par email, gestion des collaborateurs) et renforcement de la sécurité.
- [api-partenaires](/repos/proconnect-gouv/api-partenaires) : Mise en place complète de l'API de configuration des partenaires avec une infrastructure CI/CD.
- [class-validator](/repos/proconnect-gouv/class-validator) : Ajout de nouveaux validateurs et amélioration de la flexibilité de la validation.
- [hyyypertool](/repos/proconnect-gouv/hyyypertool) : Amélioration de l'interface utilisateur et de la gestion des utilisateurs.
