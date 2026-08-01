# Synthèse d'activité : SocialGouv (du 22 juillet au 29 juillet 2026)

## Résumé de l'activité
L'activité récente de SocialGouv est marquée par une forte concentration sur l'amélioration de la qualité du code, la sécurité et l'expérience utilisateur. Plusieurs dépôts ont bénéficié de mises à jour de dépendances, de corrections de bugs et d'optimisations de performance. Des efforts importants ont été déployés pour préparer l'arrêt de certains services, comme Recosanté, tout en développant de nouvelles fonctionnalités pour d'autres, notamment vao avec le support complet du premier agrément DREETS. L'intégration de l'IA et l'automatisation des tâches sont également des thèmes récurrents, avec des avancées notables dans des projets comme `claw-code-go` et `dashlord`.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

*   `nos1000jours-blues-epds-widget` : Correction de vulnérabilités de sécurité dans les dépendances.
*   `dsfr-mcp` : Ajout d'une correction de sécurité.
*   `archifiltre-mails` : Correction d'une vulnérabilité de sécurité.
*   `buildkit-operator` : Renforcement de la sécurité avec la suppression de l'authentification par token et le passage à OIDC.

## Autres changements notables
*   `vao` : Ajout du support complet du premier agrément DREETS, incluant les étapes de demande de compléments, de confirmation de complétude, de refus et d'acceptation.
*   `smart-allow` : Ajout d'une fonctionnalité bloquant l'envoi de données à des fournisseurs d'IA externes.
*   `token-bureau` : Amélioration de la flexibilité avec l'accès aux projets V2 et correction de problèmes de configuration des permissions.
*   `srdt` : Ajout d'une section FAQ, d'une page "Nouveautés" et d'un écran d'introduction pour améliorer l'expérience utilisateur.
*   `matomo-postgres` : Correction de bugs liés à la migration de schéma, à la gestion des partitions et à la compatibilité avec les versions de Node.js.
*   `infra-apps` : Migration vers buildkit-operator et décommissionnement de certains services.
*   `cdtn-admin` : Migration vers buildkit-operator et ajout de l'ingestion des accords d'entreprise.
*   `dashlord` : Ajout d'un système de notation des contributions et implémentation du Net Promoter Score (NPS).

## Dépôts les plus actifs
*   `vao` : Développement du support du premier agrément DREETS et améliorations de l'accessibilité.
*   `token-bureau` : Amélioration de la gestion des permissions et de l'intégration avec GitHub.
*   `srdt` : Amélioration de l'expérience utilisateur avec de nouvelles fonctionnalités et corrections de bugs.
*   `infra-apps` : Optimisation de l'infrastructure et migration vers de nouvelles technologies.
*   `dashlord` : Ajout de nouvelles fonctionnalités pour l'analyse et l'amélioration de l'application.
*   `cdtn-admin` : Ajout de l'ingestion des accords d'entreprise et migration vers buildkit-operator.
*   `matomo-postgres` : Correction de bugs et amélioration de la stabilité.
*   `buildkit-operator` : Amélioration de la sécurité et de la gestion des builds.
*   `legi-data` : Mises à jour régulières des données de législation.
*   `fiches-vdd` : Mises à jour régulières des données des fiches d'informations.
