# Synthèse d'activité : proconnect-gouv (du 07/09 au 14/09)

## Résumé de l'activité
L'activité de la période est marquée par une montée en maturité des services d'identité et une refonte structurelle majeure visant à accroître la modularité de l'organisation. Les utilisateurs bénéficieront d'une expérience plus fluide grâce à l'automatisation des Passkeys et à une gestion optimisée des flux d'authentification dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) et [proconnect-test-client](/repos/proconnect-gouv/proconnect-test-client).

Parallèlement, l'écosystème s'enrichit de nouveaux outils et services, notamment le thème visuel [tailwindcss-dsfr-theme](/repos/proconnect-gouv/tailwindcss-dsfr-theme) pour l'intégration des standards de l'État, le service de résolution DNS [mx-resolver](/repos/proconnect-gouv/mx-resolver), ainsi que le buildpack [bun-buildpack](/repos/proconnect-gouv/bun-buildpack) pour faciliter les déploiements.

## Sécurité
- Correction d'une faille permettant le contournement du code de vérification des contacts officiels dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- Mise à jour des dépendances pour corriger des vulnérabilités dans [class-validator](/repos/proconnect-gouv/class-validator).
- Renforcement de la sécurité par l'adoption de l'algorithme RS256 par défaut dans [federation](/repos/proconnect-gouv/federation).

## Autres changements notables
- **Refonte architecturale** : Migration massive de la logique métier vers un nouveau système de "connecteurs" pour améliorer la modularité dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- **Résilience du système** : Mise en place de mécanismes de secours (fallback) utilisant des données en cache pour pallier l'indisponibilité des API externes (Entreprise, SIRENE) dans [federation](/repos/proconnect-gouv/federation).
- **Modernisation technique** : Introduction d'un environnement de développement sans privilèges via Nix dans [hyyypertool](/repos/proconnect-gouv/hyyypertool) et extension du support de l'architecture arm64 dans [api-partenaires](/repos/proconnect-gouv/api-partenaires).
- **Nouveaux projets** : Initialisation de [proconnect-test-idp](/repos/proconnect-gouv/proconnect-test-idp) pour les tests OIDC et de [mx-resolver](/repos/proconnect-gouv/mx-resolver) pour la résolution de domaines.

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Refonte architecturale majeure et enrichissement des fonctionnalités d'identité.
- [federation](/repos/proconnect-gouv/federation) : Amélioration de la résilience face aux services tiers et renforcement de la sécurité.
- [hyyypertool](/repos/proconnect-gouv/hyyypertool) : Optimisation de la gestion des organisations et modernisation de l'infrastructure.
- [class-validator](/repos/proconnect-gouv/class-validator) : Extension des capacités de validation de données et maintenance de sécurité.
