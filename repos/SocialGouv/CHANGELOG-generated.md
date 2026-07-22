# Synthèse d'activité : SocialGouv (du 29 juin au 26 juillet 2026)

## Résumé de l'activité
L'activité récente de SocialGouv a été marquée par une forte concentration sur la maintenance, la sécurité et la préparation de nouvelles fonctionnalités. Plusieurs dépôts ont bénéficié de corrections de bugs et de mises à jour de dépendances, notamment pour assurer la compatibilité avec les dernières versions de Node.js et Python. Des efforts importants ont également été déployés pour améliorer l'accessibilité de certains services, notamment via l'intégration de l'outil ultra11y et des corrections RGAA. Plusieurs projets ont également progressé dans l'intégration d'outils d'IA pour l'analyse de code et l'automatisation de tâches, comme repo-falcon et git-ai-trace. Enfin, plusieurs projets ont débuté ou ont été initialisés, comme appy-quotes-live et appy-demo-quotes, témoignant d'une dynamique de création continue.

## Sécurité
Plusieurs dépôts ont reçu des corrections de sécurité :

*   [dsfr-mcp](/repos/SocialGouv/dsfr-mcp) a bénéficié d'une correction de vulnérabilité.
*   [domifa](/repos/SocialGouv/domifa) a reçu des corrections pour renforcer la sécurité, notamment concernant l'authentification et la gestion des accès.
*   [buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example) a mis en place des mesures pour renforcer la sécurité de la chaîne d'approvisionnement logicielle.

## Autres changements notables
*   **Infrastructure et outils :** Migration vers pnpm dans plusieurs dépôts ([token-bureau](/repos/SocialGouv/token-bureau), [revu](/repos/SocialGouv/revu), [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget), [dashlord-actions](/repos/SocialGouv/dashlord-actions), [cdtn-admin](/repos/SocialGouv/cdtn-admin)) pour une meilleure gestion des dépendances. Adoption de buildkit-operator dans plusieurs projets ([buildkit-operator](/repos/SocialGouv/buildkit-operator), [cdtn-admin](/repos/SocialGouv/cdtn-admin)).
*   **IA et automatisation :** Progrès significatifs dans l'intégration d'outils d'IA pour l'analyse de code et l'automatisation de tâches dans [repo-falcon](/repos/SocialGouv/repo-falcon), [git-ai-trace](/repos/SocialGouv/git-ai-trace) et [claw-code-go](/repos/SocialGouv/claw-code-go).
*   **Accessibilité :** Amélioration de l'accessibilité de [vao](/repos/SocialGouv/vao) et [egapro](/repos/SocialGouv/egapro).
*   **Préparation à l'arrêt :** Préparation à l'arrêt du service [recosante](/repos/SocialGouv/recosante) avec l'ajout d'une bannière d'information.

## Dépôts les plus actifs
*   [vao](/repos/SocialGouv/vao) : Amélioration significative de l'accessibilité et implémentation de la gestion des agréments dans le back-office.
*   [egapro](/repos/SocialGouv/egapro) : Ajout d'une API publique et amélioration de l'accessibilité.
*   [cdtn-admin](/repos/SocialGouv/cdtn-admin) : Ajout de l'ingestion des accords d'entreprise et amélioration de l'analyse des contributions.
*   [dashlord-actions](/repos/SocialGouv/dashlord-actions) : Amélioration des rapports et intégration de tests E2E.
*   [buildkit-operator](/repos/SocialGouv/buildkit-operator) : Amélioration de la sécurité et de la flexibilité de l'opérateur.
*   [legi-data](/repos/SocialGouv/legi-data) : Mises à jour régulières des données de législation.
*   [matomo-next](/repos/SocialGouv/matomo-next) : Ajout d'un proxy de suivi côté serveur et prise en charge des tests A/B.
*   [klaude-code-go](/repos/SocialGouv/klaude-code-go) : Ajout d'un outil "oracle" et implémentation de sous-agents dynamiques.
