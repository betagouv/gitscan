# Synthèse d'activité : SocialGouv (du 22/04 au 22/05)

## Résumé de l'activité
L'activité de SocialGouv au cours des dernières semaines a été marquée par une forte concentration sur l'amélioration de la qualité des données, la sécurité et la modernisation des infrastructures. Plusieurs projets ont bénéficié de mises à jour de données régulières (legi-data, fiches-vdd, fiches-travail-data), assurant ainsi la pertinence des informations fournies. Des efforts significatifs ont été déployés pour renforcer la sécurité des applications (domifa, archifiltre-mails, dsfr-mcp, matomo-next) et pour migrer vers des technologies plus récentes (Python/Django dans collecte-pro, pnpm dans plusieurs projets). L'automatisation et l'intégration continue ont également été améliorées, notamment avec l'ajout de workflows CI/CD et l'utilisation d'outils comme Tokenbureau et GitHub Container Registry. Plusieurs projets ont vu l'ajout de nouvelles fonctionnalités, comme l'authentification à deux facteurs (domifa), la recherche sémantique (questions-ecrites) et l'intégration de nouveaux fournisseurs de modèles de langage (claw-code-go).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- Correction d'une vulnérabilité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails).
- Renforcement de la sécurité et correction de vulnérabilités dans [domifa](/repos/SocialGouv/domifa) avec l'ajout de l'authentification à deux facteurs et la limitation des sessions.
- Correction de sécurité dans [dsfr-mcp](/repos/SocialGouv/dsfr-mcp).
- Amélioration de la sécurité et correction de vulnérabilités dans [matomo-next](/repos/SocialGouv/matomo-next).
- Correction d'une vulnérabilité de sécurité dans [token-bureau](/repos/SocialGouv/token-bureau).
- Amélioration de la sécurité avec la fermeture de vulnérabilités et l'utilisation de cosign pour la vérification des plugins dans [claw-code-go](/repos/SocialGouv/claw-code-go).
- Correction d'une vulnérabilité dans [archifiltre-docs](/repos/SocialGouv/archifiltre-docs).

## Autres changements notables
- Migration vers pnpm dans plusieurs dépôts : [token-bureau](/repos/SocialGouv/token-bureau), [revu](/repos/SocialGouv/revu), [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget), [kontinuous](/repos/SocialGouv/kontinuous).
- Migration vers Python 3.14 et Django 5.2.13 dans [collecte-pro](/repos/SocialGouv/collecte-pro).
- Remplacement de Qdrant par pg_vector dans [questions-ecrites](/repos/SocialGouv/questions-ecrites).
- Migration vers une instance interne d'Elasticsearch pour la préproduction dans [cdtn-admin](/repos/SocialGouv/cdtn-admin).
- Refonte de l'architecture de [iterion](/repos/SocialGouv/iterion) pour une meilleure modularité.
- Passage à Node 20 dans [token-bureau](/repos/SocialGouv/token-bureau).
- Refonte du processus d'initialisation de la base de données dans [vao](/repos/SocialGouv/vao).

## Dépôts les plus actifs
- [vao](/repos/SocialGouv/vao) : Corrections de bugs et améliorations de l'expérience utilisateur sur les formulaires d'agrément.
- [questions-ecrites](/repos/SocialGouv/questions-ecrites) : Ajout de la recherche sémantique et migration vers pg_vector.
- [cdtn-admin](/repos/SocialGouv/cdtn-admin) : Amélioration de la gestion des contributions et migration vers Elasticsearch interne.
- [domifa](/repos/SocialGouv/domifa) : Ajout de l'authentification à deux facteurs et améliorations de la sécurité.
- [git-ai-trace](/repos/SocialGouv/git-ai-trace) : Initialisation du projet et mise en place du CI/CD.
- [dashlord](/repos/SocialGouv/dashlord) : Amélioration de la pertinence des résultats de recherche et ajout d'un quizz.
- [kontinuous](/repos/SocialGouv/kontinuous) : Corrections de bugs et migration vers pnpm.
- [matomo-next](/repos/SocialGouv/matomo-next) : Ajout d'un proxy de suivi et prise en charge des tests A/B.
- [claw-code-go](/repos/SocialGouv/claw-code-go) : Intégration de nouveaux fournisseurs de modèles de langage et amélioration de la sécurité.
