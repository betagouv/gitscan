# Synthèse d'activité : SocialGouv (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par une activité soutenue sur l'ensemble des dépôts SocialGouv, avec un focus important sur la sécurité, la correction de bugs et l'amélioration de l'expérience utilisateur. Plusieurs projets ont bénéficié de mises à jour de dépendances et de migrations vers pnpm, renforçant ainsi la sécurité et la stabilité des applications. Des améliorations significatives ont été apportées à des outils clés comme cdtn-admin, iterion, matomo-next et vao, avec l'ajout de nouvelles fonctionnalités et la correction de problèmes existants. L'accent a également été mis sur l'automatisation des processus, notamment avec l'intégration d'agents d'IA dans repo-falcon et l'amélioration des workflows CI/CD.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- [archifiltre-docs](/repos/SocialGouv/archifiltre-docs) a reçu une correction de sécurité.
- [archifiltre-mails](/repos/SocialGouv/archifiltre-mails) a corrigé une vulnérabilité de sécurité.
- [token-bureau](/repos/SocialGouv/token-bureau) a amélioré la gestion des permissions configurables et corrigé des bugs liés à la migration vers pnpm, contribuant à une meilleure sécurité globale.
- [srdt](/repos/SocialGouv/srdt) a ajouté des vérifications d'autorisation côté serveur pour les routes API non protégées.

## Autres changements notables
- **Migrations vers pnpm:** Plusieurs projets, dont [revu](/repos/SocialGouv/revu), [matomo-next](/repos/SocialGouv/matomo-next), [token-bureau](/repos/SocialGouv/token-bureau) et [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget) ont migré vers pnpm pour une meilleure gestion des dépendances.
- **Amélioration de l'infrastructure:** Des améliorations ont été apportées à l'infrastructure de plusieurs projets, notamment avec l'ajout d'un cluster PostgreSQL pour [srdt](/repos/SocialGouv/srdt) et l'augmentation de la taille du disque pour Metabase dans [infra-apps](/repos/SocialGouv/infra-apps).
- **Intégration d'IA:** [repo-falcon](/repos/SocialGouv/repo-falcon) a continué à progresser dans l'intégration avec des agents de codage comme Claude.
- **Refonte de l'éditeur visuel:** [iterion](/repos/SocialGouv/iterion) a connu une refonte majeure de son éditeur visuel.
- **Nouvelles API:** [questions-ecrites](/repos/SocialGouv/questions-ecrites) a ajouté une API FastAPI pour exposer les attributions de questions.

## Dépôts les plus actifs
- [cdtn-admin](/repos/SocialGouv/cdtn-admin) : Corrections de bugs, amélioration de la gestion des alertes et migration vers pnpm, Next.js et React-DSFR.
- [iterion](/repos/SocialGouv/iterion) : Refonte majeure de l'éditeur visuel et intégration d'agents d'IA.
- [matomo-next](/repos/SocialGouv/matomo-next) : Ajout d'un proxy de suivi, prise en charge des tests A/B et migration vers pnpm.
- [vao](/repos/SocialGouv/vao) : Amélioration du parcours de renouvellement d'agrément et ajout de la messagerie pour les agréments.
- [repo-falcon](/repos/SocialGouv/repo-falcon) : Amélioration de l'intégration avec les agents de codage et automatisation des processus de publication.
