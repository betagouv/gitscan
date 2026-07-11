# Synthèse d'activité : SocialGouv (du 27 mai 2026 au 29 juin 2026)

## Résumé de l'activité
L'activité récente de SocialGouv est marquée par une forte concentration sur la maintenance, la sécurité et l'amélioration de l'expérience utilisateur de ses outils. Plusieurs dépôts ont bénéficié de corrections de bugs, de mises à jour de dépendances et d'ajustements de configuration pour garantir la stabilité et la performance des applications. Des efforts significatifs ont également été déployés pour préparer l'arrêt de certains services, comme Recosanté, en informant les utilisateurs et en assurant une transition en douceur. Plusieurs projets ont progressé dans l'intégration de nouvelles fonctionnalités, notamment l'ajout de support pour des technologies émergentes comme l'IA et l'automatisation, ainsi que l'amélioration de l'accessibilité et de la sécurité des applications. Les dépôts les plus actifs incluent [vao](/repos/SocialGouv/vao), [token-bureau](/repos/SocialGouv/token-bureau), [matomo-next](/repos/SocialGouv/matomo-next) et [cdtn-admin](/repos/SocialGouv/cdtn-admin).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

*   Correction d'une vulnérabilité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails).
*   Renforcement de la sécurité dans [domifa](/repos/SocialGouv/domifa) avec des corrections et des ajustements.
*   Amélioration de la sécurité des builds avec l'intégration de Kata Containers dans [buildkit-operator](/repos/SocialGouv/buildkit-operator).
*   Mise en place d'une gestion des secrets locale scellée dans [iterion](/repos/SocialGouv/iterion).

## Autres changements notables
*   **Migration vers pnpm:** Plusieurs dépôts, dont [token-bureau](/repos/SocialGouv/token-bureau), [revu](/repos/SocialGouv/revu), [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget), et [dashlord](/repos/SocialGouv/dashlord) ont migré vers pnpm pour une meilleure gestion des dépendances.
*   **Intégration de l'IA:** Des avancées ont été réalisées dans l'intégration de l'IA, notamment avec l'ajout de support pour Claude Opus 4.8 dans [claw-code-go](/repos/SocialGouv/claw-code-go) et l'exploration de l'utilisation de l'IA pour la génération de code dans [git-ai-trace](/repos/SocialGouv/git-ai-trace).
*   **Amélioration de l'infrastructure:** Des améliorations ont été apportées à l'infrastructure, notamment avec la migration des builds vers buildkit-operator dans [cdtn-admin](/repos/SocialGouv/cdtn-admin) et l'optimisation des ressources PostgreSQL dans [vao](/repos/SocialGouv/vao).
*   **Préparation de l'arrêt de Recosanté:** Une bannière d'information a été ajoutée à [recosante](/repos/SocialGouv/recosante) pour informer les utilisateurs de l'arrêt du service.

## Dépôts les plus actifs
*   [vao](/repos/SocialGouv/vao) : Amélioration significative du flux de premier agrément et de la gestion des documents.
*   [token-bureau](/repos/SocialGouv/token-bureau) : Corrections de bugs et amélioration de la gestion des permissions.
*   [matomo-next](/repos/SocialGouv/matomo-next) : Ajout d'un proxy pour contourner les bloqueurs de publicités et prise en charge des tests A/B.
*   [cdtn-admin](/repos/SocialGouv/cdtn-admin) : Amélioration du sitemap, ajout de nouvelles fonctionnalités d'analyse et corrections de bugs.
*   [srdt](/repos/SocialGouv/srdt) : Amélioration de l'interface utilisateur de l'assistant virtuel.
*   [iterion](/repos/SocialGouv/iterion) : Ajout de l'authentification GitHub SSO et lancement d'un marketplace public.
*   [legi-data](/repos/SocialGouv/legi-data) : Mises à jour régulières des données légales.
*   [dashlord](/repos/SocialGouv/dashlord) : Amélioration de l'interface utilisateur et ajout de nouvelles fonctionnalités.
