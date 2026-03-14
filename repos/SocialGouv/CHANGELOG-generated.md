# Synthèse d'activité : SocialGouv (derniers 7 jours)

## Résumé de l'activité
L'organisation SocialGouv a connu une semaine riche en activités, marquée par des améliorations de sécurité, des corrections de bugs et l'ajout de nouvelles fonctionnalités dans plusieurs de ses dépôts. Des efforts importants ont été consacrés à la préparation de l'arrêt de certains services, comme Recosanté, et à l'amélioration de l'expérience utilisateur de plateformes comme DomiFa et Matomo. L'intégration de modèles de langage (LLM) et l'amélioration de l'infrastructure (migration vers pnpm, utilisation de Sentry) sont également des thèmes récurrents. Plusieurs dépôts ont bénéficié de mises à jour significatives, notamment [cdtn-admin](/repos/SocialGouv/cdtn-admin), [domifa](/repos/SocialGouv/domifa), [matomo-next](/repos/SocialGouv/matomo-next) et [questions-ecrites](/repos/SocialGouv/questions-ecrites).

## Sécurité
Plusieurs dépôts ont bénéficié de correctifs de sécurité :
- Correction d'une vulnérabilité de sécurité dans [archifiltre-docs](/repos/SocialGouv/archifiltre-docs).
- Correction d'une vulnérabilité de sécurité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails).
- Renforcement de la sécurité des API dans [srdt](/repos/SocialGouv/srdt).
- Correction de vulnérabilités dans [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget).

## Autres changements notables
- Migration vers pnpm dans plusieurs dépôts ([cdtn-admin](/repos/SocialGouv/cdtn-admin), [domifa](/repos/SocialGouv/domifa), [revu](/repos/SocialGouv/revu), [token-bureau](/repos/SocialGouv/token-bureau)) pour une meilleure gestion des dépendances.
- Intégration de Sentry pour la surveillance et la gestion des erreurs dans [domifa](/repos/SocialGouv/domifa).
- Migration vers Drizzle ORM dans [egapro](/repos/SocialGouv/egapro).
- Intégration de l'outil Fleet pour la recherche multi-dépôts dans [repo-falcon](/repos/SocialGouv/repo-falcon).
- Mise en place d'un cluster PostgreSQL pour [srdt](/repos/SocialGouv/srdt).

## Dépôts les plus actifs
- [cdtn-admin](/repos/SocialGouv/cdtn-admin) : Corrections de bugs, amélioration de la gestion des alertes et migration vers pnpm, React et Next.js.
- [domifa](/repos/SocialGouv/domifa) : Corrections de bugs, ajout de l'envoi de SMS et amélioration de la surveillance avec Sentry.
- [questions-ecrites](/repos/SocialGouv/questions-ecrites) : Refactorisation du code, intégration de modèles de langage et amélioration de l'évaluation des résultats.
- [matomo-next](/repos/SocialGouv/matomo-next) : Ajout d'un proxy de suivi côté serveur, prise en charge des tests A/B et migration vers pnpm.
- [revu](/repos/SocialGouv/revu) : Corrections de bugs, intégration de feature flags et avancées dans l'intégration avec le stockage S3.
