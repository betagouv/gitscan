# Synthèse d'activité : SocialGouv (derniers 7 jours)

## Résumé de l'activité
Au cours des 7 derniers jours, l'organisation SocialGouv a connu une activité soutenue sur plusieurs de ses dépôts. Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment avec des corrections de bugs et l'ajout de nouvelles fonctionnalités dans des outils comme `cdtn-admin`, `code-du-travail-numerique` et `da-manager`.  Une migration vers le gestionnaire de paquets pnpm a été entreprise dans plusieurs projets (`domifa`, `nos1000jours-blues-epds-widget`, `token-bureau`, `vao`) pour optimiser la gestion des dépendances et améliorer la sécurité. L'infrastructure a également été renforcée avec l'ajout de capacités de CI/CD et l'intégration de nouveaux services d'authentification comme Proconnect (via `charon`).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction de vulnérabilités dans `token-bureau` avec la migration vers pnpm et la mise à jour des dépendances.
- Ajout de vérifications d'autorisation côté serveur dans `srdt` pour les routes API non protégées.
- Correction de vulnérabilités de sécurité identifiées dans les dépendances de `nos1000jours-blues-epds-widget`.

## Autres changements notables
- **Migration vers pnpm :** Plusieurs projets ont migré vers pnpm, incluant `domifa`, `nos1000jours-blues-epds-widget`, `token-bureau` et `vao`, pour une meilleure gestion des dépendances et des performances.
- **CI/CD :** Amélioration significative des pipelines CI/CD dans `da-manager` et `kontinuous`, permettant des déploiements plus fiables et automatisés.
- **Intégration Proconnect :** L'intégration du provider d'authentification Proconnect dans `charon` et `egapro` élargit les options d'authentification pour les utilisateurs.
- **Nouvelle infrastructure PostgreSQL :** Mise en place d'un cluster PostgreSQL pour `srdt`, améliorant la scalabilité et la fiabilité du service.

## Dépôts les plus actifs
- [cdtn-admin](/repos/SocialGouv/cdtn-admin) : Corrections de bugs et ajout de fonctionnalités pour l'administration du Code du travail numérique.
- [code-du-travail-numerique](/repos/SocialGouv/code-du-travail-numerique) : Amélioration de la recherche, corrections de bugs et ajout de widgets pour le site web.
- [da-manager](/repos/SocialGouv/da-manager) : Développement intensif de l'interface utilisateur et mise en place d'un pipeline CI/CD complet.
- [srdt](/repos/SocialGouv/srdt) : Amélioration de la sécurité, ajout de la sauvegarde des conversations et correction de bugs.
- [vao](/repos/SocialGouv/vao) : Corrections de bugs, améliorations de l'interface utilisateur et migration vers pnpm.
