# Synthèse d'activité : proconnect-gouv (du 13 mai 2026 au 23 juillet 2026)

## Résumé de l'activité
L'activité récente de proconnect-gouv se concentre sur l'amélioration de la sécurité, la modernisation de l'expérience utilisateur et la mise en place de nouvelles fonctionnalités pour les partenaires. Des efforts importants ont été déployés pour renforcer la sécurité des applications, notamment avec la suppression de configurations non sécurisées et l'implémentation de politiques de sécurité plus strictes. L'interface utilisateur a été améliorée pour faciliter la gestion des organisations partenaires et l'authentification multi-facteurs. Le développement de nouvelles API, comme l'API Partenaires, vise à offrir plus d'autonomie aux partenaires dans la gestion de leur configuration. Les dépôts [proconnect-identite](/repos/proconnect-gouv/proconnect-identite), [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) et [api-partenaires](/repos/proconnect-gouv/api-partenaires) ont été particulièrement actifs.

## Sécurité
Plusieurs améliorations de sécurité ont été apportées :
- Renforcement de la sécurité des clients OIDC dans [api-partenaires](/repos/proconnect-gouv/api-partenaires).
- Suppression de configurations SSL non sécurisées dans [api-partenaires](/repos/proconnect-gouv/api-partenaires).
- Mise en place d'une politique de sécurité du contenu (CSP) plus stricte dans [api-partenaires](/repos/proconnect-gouv/api-partenaires).
- Suppression de `unsafe-inline` de la Content Security Policy dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- Restriction des méthodes d'authentification au niveau du point d'accès au token dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- Correction de vulnérabilités de dépendances dans [class-validator](/repos/proconnect-gouv/class-validator).

## Autres changements notables
- Mise à jour de PostgreSQL en version 18 dans l'environnement Docker Compose de [api-partenaires](/repos/proconnect-gouv/api-partenaires).
- Migration des routes de gestion des clients OIDC de pcdbapi vers [api-partenaires](/repos/proconnect-gouv/api-partenaires).
- Initialisation et déploiement du buildpack Bun pour Scalingo [bun-buildpack](/repos/proconnect-gouv/bun-buildpack).
- Ajout de tests d'intégration pour l'API Partenaires [api-partenaires](/repos/proconnect-gouv/api-partenaires).

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Amélioration de l'authentification multi-facteurs et renforcement de la sécurité.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) : Ajout de nouvelles fonctionnalités pour la gestion des partenaires et correction de bugs.
- [proconnect-test-client](/repos/proconnect-gouv/proconnect-test-client) : Amélioration de la flexibilité du flux d'authentification et mises à jour de dépendances.
- [api-partenaires](/repos/proconnect-gouv/api-partenaires) : Développement initial de l'API pour les partenaires et implémentation de la gestion des clients OIDC.
- [class-validator](/repos/proconnect-gouv/class-validator) : Ajout de nouveaux validateurs et correction de vulnérabilités.
