# Synthèse d'activité : proconnect-gouv (du 28 avril 2026 au 26 juillet 2026)

## Résumé de l'activité
L'activité récente de l'organisation proconnect-gouv s'est concentrée sur l'amélioration de la sécurité, l'expérience utilisateur et la maintenance des applications existantes. Des efforts importants ont été déployés pour renforcer la sécurité des applications [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) et [federation](/repos/proconnect-gouv/federation), notamment en limitant les méthodes d'authentification et en supprimant des configurations potentiellement vulnérables. L'authentification multifacteur (MFA) est améliorée avec une nouvelle interface utilisateur dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite). Plusieurs projets ont bénéficié de mises à jour de dépendances pour assurer la stabilité et la sécurité, et de nouvelles fonctionnalités ont été ajoutées pour faciliter l'administration et la gestion des utilisateurs, comme la recherche d'utilisateurs fédérés dans [federation](/repos/proconnect-gouv/federation). Le projet [class-validator](/repos/proconnect-gouv/class-validator) a vu l'ajout de nouveaux validateurs pour des formats de données spécifiques.

## Sécurité
Plusieurs changements ont été apportés pour améliorer la sécurité :

- Suppression de `unsafe-inline` de la Content Security Policy dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) et [federation](/repos/proconnect-gouv/federation) pour prévenir les attaques XSS.
- Restriction des méthodes d'authentification autorisées au niveau du token dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- Correction de vulnérabilités de dépendances dans [class-validator](/repos/proconnect-gouv/class-validator).

## Autres changements notables
- Migration du runtime de [docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect) vers Bun pour de meilleures performances.
- Ajout de healthchecks pour le broker dans [federation](/repos/proconnect-gouv/federation).
- Initialisation du buildpack [bun-buildpack](/repos/proconnect-gouv/bun-buildpack) pour permettre le déploiement d'applications Bun sur Scalingo.

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Amélioration de la sécurité, de l'expérience utilisateur de l'authentification multifacteur et maintenance technique.
- [federation](/repos/proconnect-gouv/federation) : Ajout de nouvelles fonctionnalités d'administration et amélioration de la sécurité.
- [proconnect-test-client](/repos/proconnect-gouv/proconnect-test-client) : Amélioration de la flexibilité du flux d'authentification et mises à jour de dépendances.
- [class-validator](/repos/proconnect-gouv/class-validator) : Ajout de nouveaux validateurs et correction de vulnérabilités.
- [docteur-proconnect](/repos/proconnect-gouv/docteur-proconnect) : Correction de bugs d'authentification et migration vers Bun.
