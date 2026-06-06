# Synthèse d'activité : SocialGouv (du 07/05 au 07/06)

## Résumé de l'activité
L'activité récente de SocialGouv a été marquée par une forte concentration sur la maintenance, la sécurité et l'amélioration de l'infrastructure. Plusieurs dépôts ont bénéficié de mises à jour de dépendances et de corrections de bugs pour assurer la stabilité et la fiabilité des services. Des efforts significatifs ont également été déployés pour améliorer l'expérience utilisateur, notamment avec l'ajout de nouvelles fonctionnalités dans des outils comme `dashlord` et `matomo-next`, et des améliorations de l'accessibilité dans `vao`.  L'organisation a continué à investir dans l'automatisation et l'intégration continue, avec des améliorations des workflows CI/CD dans plusieurs projets.  Enfin, des mises à jour régulières des données législatives et des conventions collectives ont été effectuées pour garantir la pertinence des informations fournies par les services.

## Sécurité
Plusieurs dépôts ont reçu des correctifs de sécurité importants :

*   Correction d'une vulnérabilité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails).
*   Correction d'une vulnérabilité et renforcement de la sécurité dans [domifa](/repos/SocialGouv/domifa) avec l'ajout de l'authentification à deux facteurs et des mesures anti-bot.
*   Correction d'une vulnérabilité dans [token-bureau](/repos/SocialGouv/token-bureau).
*   Correction d'une vulnérabilité dans [dsfr-mcp](/repos/SocialGouv/dsfr-mcp).

## Autres changements notables
*   **Refonte d'infrastructure :** Migration vers pnpm dans plusieurs dépôts (token-bureau, revu, domifa, archifiltre-docs, cdtn-admin) pour une meilleure gestion des dépendances.
*   **Amélioration de l'intégration continue :** Amélioration des workflows CI/CD dans plusieurs projets, notamment [dashlord-actions] et [infra-apps].
*   **Refactorisation majeure :** Refonte de l'architecture de [questions-ecrites](/repos/SocialGouv/questions-ecrites) pour utiliser `pg_vector` à la place de `qdrant`.
*   **Nouvelles fonctionnalités :** Ajout de la gestion des permissions configurables dans [token-bureau](/repos/SocialGouv/token-bureau) et de l'authentification à deux facteurs dans [domifa](/repos/SocialGouv/domifa).
*   **Automatisation :** Intégration de Claude pour la revue de code et la gestion des pull requests dans [da-manager](/repos/SocialGouv/da-manager).

## Dépôts les plus actifs
*   [vao](/repos/SocialGouv/vao) : Amélioration de l'accessibilité et ajout de nouvelles fonctionnalités pour la gestion des agréments.
*   [token-bureau](/repos/SocialGouv/token-bureau) : Corrections de bugs, améliorations de la gestion des permissions et migration vers pnpm.
*   [srdt](/repos/SocialGouv/srdt) : Amélioration de l'expérience utilisateur et corrections de bugs pour l'assistant virtuel.
*   [matomo-next](/repos/SocialGouv/matomo-next) : Ajout d'un proxy de suivi côté serveur et prise en charge des tests A/B.
*   [cdtn-admin](/repos/SocialGouv/cdtn-admin) : Amélioration de la gestion des contributions et corrections de bugs.
*   [legi-data](/repos/SocialGouv/legi-data) : Mises à jour régulières des données législatives.
*   [fiches-travail-data](/repos/SocialGouv/fiches-travail-data) : Mises à jour régulières des données des fiches de travail.
*   [dashlord](/repos/SocialGouv/dashlord) : Amélioration de l'interface utilisateur et ajout de nouvelles statistiques.
*   [crossplane-function-js](/repos/SocialGouv/crossplane-function-js) : Amélioration de l'intégration avec les modèles d'IA et ajout de nouvelles fonctionnalités.
*   [domifa](/repos/SocialGouv/domifa) : Ajout de l'authentification à deux facteurs et amélioration de la sécurité.
