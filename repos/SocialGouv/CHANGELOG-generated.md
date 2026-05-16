# Synthèse d'activité : SocialGouv (du 07/05 au 14/05)

## Résumé de l'activité
Au cours des dernières semaines, l'organisation SocialGouv a connu une activité soutenue, avec des mises à jour significatives sur de nombreux dépôts. L'accent a été mis sur l'amélioration de la sécurité (correction de vulnérabilités dans `vao`, `nos1000jours-blues-epds-widget`, `archifiltre-mails` et `archifiltre-docs`), l'amélioration de l'expérience utilisateur (corrections de bugs et ajouts de fonctionnalités dans `vao`, `srdt`, `dashlord`, `domifa`, `cdtn-admin`), et la modernisation technique (migrations vers pnpm dans `token-bureau`, `revu`, `nos1000jours-blues-epds-widget`, `matomo-next`, et refonte de l'architecture dans `iterion`).  Plusieurs projets ont également progressé dans l'automatisation (workflows CI/CD améliorés dans `repo-falcon`, `kube-image-keeper`) et l'intégration de nouvelles technologies (Elasticsearch dans `cdtn-admin`, intégration de Claude dans `git-ai-trace` et `claw-code-go`). L'activité de mise à jour des données a été régulière dans `legi-data`, `kali-data` et `fiches-vdd`.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- Correction de vulnérabilités identifiées par SonarQube dans [vao](/repos/SocialGouv/vao).
- Correction d'une vulnérabilité de sécurité dans [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget).
- Correction d'une vulnérabilité de sécurité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails).
- Correction d'une vulnérabilité de sécurité dans [archifiltre-docs](/repos/SocialGouv/archifiltre-docs).

## Autres changements notables
- Migration vers pnpm pour la gestion des dépendances dans plusieurs dépôts : [token-bureau](/repos/SocialGouv/token-bureau), [revu](/repos/SocialGouv/revu), [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget), [matomo-next](/repos/SocialGouv/matomo-next).
- Refonte de l'architecture de [iterion](/repos/SocialGouv/iterion) pour une meilleure modularité et maintenabilité.
- Intégration d'Elasticsearch dans [cdtn-admin](/repos/SocialGouv/cdtn-admin) pour améliorer la recherche.
- Mise en place d'un système de sandbox basé sur Docker dans [iterion](/repos/SocialGouv/iterion) pour une exécution plus sécurisée des workflows.
- Migration de Python et Django vers des versions plus récentes dans [collecte-pro](/repos/SocialGouv/collecte-pro).

## Dépôts les plus actifs
- [vao](/repos/SocialGouv/vao) : Corrections de bugs et améliorations de l'expérience utilisateur sur les formulaires d'agrément.
- [token-bureau](/repos/SocialGouv/token-bureau) : Corrections de bugs et améliorations de la gestion des permissions.
- [srdt](/repos/SocialGouv/srdt) : Amélioration de la stabilité et de la performance de l'assistant virtuel.
- [matomo-next](/repos/SocialGouv/matomo-next) : Ajout d'un proxy de suivi et prise en charge des tests A/B.
- [cdtn-admin](/repos/SocialGouv/cdtn-admin) : Ajout de la gestion des actualités et migration vers Elasticsearch.
- [git-ai-trace](/repos/SocialGouv/git-ai-trace) : Développement d'un outil pour intégrer un résumé de la collaboration IA/humain dans les commits Git.
- [claw-code-go](/repos/SocialGouv/claw-code-go) : Ajout de nouveaux outils et intégration de fournisseurs d'IA.
- [domifa](/repos/SocialGouv/domifa) : Améliorations de la sécurité et de l'interface d'administration.
