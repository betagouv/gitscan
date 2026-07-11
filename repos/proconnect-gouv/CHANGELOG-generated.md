# Synthèse d'activité : proconnect-gouv (du 28 avril 2026 au 9 juillet 2026)

## Résumé de l'activité
L'organisation proconnect-gouv a connu une période d'activité soutenue, marquée par des améliorations significatives de la sécurité, notamment dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) avec la restriction des méthodes d'authentification et la prévention des abus liés à la vérification par email.  Des efforts importants ont été consacrés à l'amélioration de l'expérience utilisateur, en particulier sur [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) avec une documentation plus claire sur l'authentification forte et l'ajout de la gestion des collaborateurs (temporairement revertée). Plusieurs dépôts ont bénéficié de mises à jour de dépendances pour assurer la stabilité et la sécurité, et de nouvelles fonctionnalités ont été ajoutées, comme la validation de formats de données spécifiques dans [class-validator](/repos/proconnect-gouv/class-validator). L'initialisation de nouveaux projets comme [proconnect-test-idp](/repos/proconnect-gouv/proconnect-test-idp) et [mx-resolver](/repos/proconnect-gouv/mx-resolver) témoigne d'une dynamique de développement active.

## Sécurité
Plusieurs changements ont été apportés pour renforcer la sécurité :

- Correction de vulnérabilités et amélioration de la sécurité de l'authentification dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- Mise à jour de dépendances vulnérables dans [class-validator](/repos/proconnect-gouv/class-validator).

## Autres changements notables
- Migration de [docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect) vers un runtime Bun pour de meilleures performances.
- Simplification de l'infrastructure Docker et suppression de PM2 dans [federation](/repos/proconnect-gouv/federation).
- Ajout d'un indicateur de conformité MFA et de la gestion des collaborateurs dans [federation](/repos/proconnect-gouv/federation).
- Initialisation du buildpack Bun pour Scalingo dans [bun-buildpack](/repos/proconnect-gouv/bun-buildpack).

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Corrections de bugs, améliorations de la sécurité et ajout de nouvelles catégories juridiques.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) : Amélioration de la documentation sur l'authentification forte et gestion des collaborateurs.
- [federation](/repos/proconnect-gouv/federation) : Ajout de fonctionnalités de gestion des utilisateurs et d'indicateurs de conformité MFA, ainsi que des refactorings d'infrastructure.
- [class-validator](/repos/proconnect-gouv/class-validator) : Ajout de nouveaux validateurs et amélioration de la validation des données.
- [docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect) : Migration vers Bun et correction de problèmes d'authentification.
