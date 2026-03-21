# Synthèse d'activité : SocialGouv (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par une activité soutenue sur l'ensemble des dépôts de SocialGouv, avec un focus particulier sur la sécurité, la correction de bugs et l'amélioration de l'expérience utilisateur. Plusieurs projets ont bénéficié de mises à jour importantes, notamment `cdtn-admin` avec une migration vers pnpm et une mise à jour majeure des technologies utilisées, et `domifa` avec des corrections de bugs et l'ajout de l'envoi de SMS. L'intégration de modèles de langage (LLM) progresse dans plusieurs projets comme `questions-ecrites` et `repo-falcon`, ouvrant la voie à de nouvelles fonctionnalités d'assistance au développement. Plusieurs dépôts ont également mis l'accent sur la préparation à des arrêts de service ou des transitions importantes, comme `recosante` et `vao`.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction d'une vulnérabilité de sécurité dans [archifiltre-docs](/repos/SocialGouv/archifiltre-docs).
- Correction d'une vulnérabilité de sécurité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails).
- Renforcement de la sécurité des API dans [srdt](/repos/SocialGouv/srdt).
- Correction de vulnérabilités dans [matomo-next](/repos/SocialGouv/matomo-next).

## Autres changements notables
- Migration vers pnpm dans plusieurs dépôts : [cdtn-admin](/repos/SocialGouv/cdtn-admin), [domifa](/repos/SocialGouv/domifa), [revu](/repos/SocialGouv/revu), [token-bureau](/repos/SocialGouv/token-bureau).
- Intégration de Claude pour l'automatisation et l'assistance au développement dans [repo-falcon](/repos/SocialGouv/repo-falcon).
- Mise en place de *feature flags* dans [vao](/repos/SocialGouv/vao) pour une gestion plus flexible des fonctionnalités.
- Migration vers Drizzle ORM dans [egapro](/repos/SocialGouv/egapro).
- Intégration de Sentry pour la surveillance des erreurs dans [domifa](/repos/SocialGouv/domifa) et [egapro](/repos/SocialGouv/egapro).

## Dépôts les plus actifs
- [cdtn-admin](/repos/SocialGouv/cdtn-admin) : Corrections de bugs, migration vers pnpm et mise à jour des technologies.
- [domifa](/repos/SocialGouv/domifa) : Corrections de bugs, ajout de l'envoi de SMS et amélioration de la surveillance.
- [vao](/repos/SocialGouv/vao) : Améliorations de l'interface utilisateur, corrections de bugs et intégration de *feature flags*.
- [questions-ecrites](/repos/SocialGouv/questions-ecrites) : Intégration de modèles de langage et refactoring du code.
- [repo-falcon](/repos/SocialGouv/repo-falcon) : Amélioration de l'intégration avec les agents de codage et automatisation des processus.
