# Synthèse d'activité : SocialGouv (du 17/05 au 26/06)

## Résumé de l'activité
L'activité récente de SocialGouv est marquée par une forte concentration sur l'amélioration de la sécurité, la modernisation des infrastructures et l'amélioration de l'expérience utilisateur. Plusieurs dépôts ont bénéficié de corrections de vulnérabilités et de mises à jour de dépendances. Des efforts importants ont été déployés pour faciliter l'intégration avec des outils d'IA (Claude, OpenAI) et pour automatiser les processus de développement et de déploiement.  Des améliorations significatives ont été apportées à des services clés comme `vao` (accessibilité, recherche), `token-bureau` (gestion des permissions), `srdt` (expérience utilisateur) et `matomo-next` (analyse). Plusieurs projets ont également débuté, comme `migration-harbor2` et `JIA-demo-atelier-1`, témoignant de l'innovation continue au sein de l'organisation.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

*   `smart-allow` : Ajout d'une fonctionnalité bloquant l'envoi de données à des fournisseurs d'IA externes.
*   `nos1000jours-blues-epds-widget` : Correction de vulnérabilités de sécurité dans les dépendances.
*   `archifiltre-mails` : Correction d'une vulnérabilité de sécurité.
*   `buildkit-operator` : Renforcement de la sécurité avec des politiques réseau et attestations de supply-chain.

## Autres changements notables
Plusieurs changements techniques majeurs ont été effectués :

*   `token-bureau` : Migration vers pnpm et refactorisation en monorepo.
*   `revu` : Migration vers pnpm.
*   `matomo-postgres` : Correction de problèmes liés aux ressources PostgreSQL.
*   `dsfr-mcp` : Ajout d'un outil pour extraire des informations sur l'accessibilité RGAA.
*   `buildkit-operator` : Nouvelle architecture à trois namespaces pour une meilleure isolation.
*   `legi-data` : Passage à pg_vector pour le stockage des vecteurs.
*   `cdtn-admin` : Ajout d'un challenger pour les modifications du SMIC.

## Dépôts les plus actifs
*   `vao` : Amélioration de l'accessibilité, ajout de filtres de recherche et correction de bugs liés au renouvellement d'agrément.
*   `token-bureau` : Corrections de bugs, améliorations de la gestion des permissions et migration vers pnpm.
*   `srdt` : Amélioration de l'expérience utilisateur, refonte de l'affichage du statut de la convention collective et ajout de la possibilité de changer de modèle d'IA.
*   `matomo-next` : Ajout d'un proxy pour contourner les bloqueurs de publicités et prise en charge des tests A/B.
*   `cdtn-admin` : Amélioration de la gestion des contributions et ajout de nouvelles fonctionnalités pour le SMIC.
*   `buildkit-operator` : Amélioration de la sécurité, refonte de l'architecture et ajout de tests E2E.
*   `dashlord` : Amélioration de l'interface utilisateur et ajout de nouvelles fonctionnalités.
*   `JIA-atelier` et `JIA-atelier-gary` : Préparation et documentation de l'atelier sur l'Intelligence Artificielle.
