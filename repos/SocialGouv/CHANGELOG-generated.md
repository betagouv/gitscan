# Synthèse d'activité : SocialGouv (du 22/06 au 22/07)

## Résumé de l'activité
L'activité récente de SocialGouv a été marquée par une forte concentration sur l'amélioration de la qualité du code, la sécurité et l'expérience utilisateur. Plusieurs dépôts ont bénéficié de corrections de bugs, de mises à jour de dépendances et d'améliorations de la documentation. Des efforts importants ont été déployés pour préparer l'arrêt de certains services comme Recosanté, tout en lançant de nouveaux projets comme `migration-harbor2` et `appy-quotes-live`. L'intégration de l'IA et l'automatisation des tâches continuent d'être des axes majeurs, avec des avancées notables dans les projets `git-ai-trace`, `repo-falcon` et `dashlord`.  Des améliorations significatives ont été apportées à l'accessibilité de plusieurs applications, notamment `vao` et `dashlord`.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

*   Correction d'une vulnérabilité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails).
*   Migration vers pnpm dans [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget) pour une meilleure gestion des dépendances et réduction des risques de sécurité.
*   Amélioration de la sécurité de la chaîne d'approvisionnement logicielle dans [buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example) avec l'implémentation de la signature cosign et de la génération de SBOM.
*   Correction de vulnérabilités potentielles dans [domifa](/repos/SocialGouv/domifa).

## Autres changements notables
*   **Infrastructure :** Migration vers buildkit-operator dans plusieurs dépôts ([cdtn-admin](/repos/SocialGouv/cdtn-admin), [buildkit-operator-example](/repos/SocialGouv/buildkit-operator-example)) pour améliorer la gestion des builds.
*   **Migration :** Préparation à l'arrêt du service Recosanté ([recosante](/repos/SocialGouv/recosante)) avec l'ajout d'une bannière d'information.
*   **IA :** Intégration de l'IA dans plusieurs projets, notamment `git-ai-trace` pour le suivi des contributions IA/humain et `repo-falcon` pour l'analyse de code et la génération de graphes de connaissances.
*   **Accessibilité :** Amélioration de l'accessibilité (RGAA) dans [vao](/repos/SocialGouv/vao) et [dashlord](/repos/SocialGouv/dashlord).
*   **Modernisation :** Migration vers pnpm dans plusieurs projets ([dashlord-actions](/repos/SocialGouv/dashlord-actions), [cdtn-admin](/repos/SocialGouv/cdtn-admin), [collecte-pro](/repos/SocialGouv/collecte-pro), [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget)).

## Dépôts les plus actifs
*   [vao](/repos/SocialGouv/vao) : Amélioration significative de l'accessibilité et ajout de la gestion des premiers agréments dans le back-office.
*   [srdt](/repos/SocialGouv/srdt) : Ajout de nouvelles fonctionnalités à l'assistant virtuel, comme une section FAQ et une page "Nouveautés".
*   [smart-allow](/repos/SocialGouv/smart-allow) : Ajout d'une fonctionnalité bloquant l'envoi de données à des fournisseurs d'IA externes.
*   [dashlord](/repos/SocialGouv/dashlord) : Amélioration de l'interface utilisateur et ajout de nouvelles fonctionnalités de gestion des utilisateurs.
*   [code-du-travail-numerique](/repos/SocialGouv/code-du-travail-numerique) : Ajout d'un score NPS et correction de plusieurs bugs.
*   [buildkit-operator](/repos/SocialGouv/buildkit-operator) : Amélioration de l'infrastructure de build et de l'authentification.
*   [legi-data](/repos/SocialGouv/legi-data) : Mises à jour régulières des données de législation française.
*   [matomo-next](/repos/SocialGouv/matomo-next) : Ajout d'un proxy de suivi côté serveur et prise en charge des tests A/B.
*   [cdtn-admin](/repos/SocialGouv/cdtn-admin) : Ajout d'une table pour le calcul du NPS et intégration de l'ingestion des accords d'entreprise.
