# Synthèse d'activité : SocialGouv (du 17 mai 2026 au 17 juin 2026)

## Résumé de l'activité
Au cours des dernières semaines, l'organisation SocialGouv a connu une activité soutenue, marquée par des améliorations significatives de la sécurité, de la stabilité et de l'expérience utilisateur de ses différentes applications.  Plusieurs dépôts ont bénéficié de corrections de bugs, de mises à jour de dépendances et de l'ajout de nouvelles fonctionnalités. Des efforts importants ont été déployés pour préparer l'arrêt de certains services, comme Recosanté, et pour faciliter l'intégration de l'IA dans les processus de développement, notamment avec des outils comme repo-falcon et git-ai-trace. L'accent a également été mis sur la documentation et l'amélioration des processus de CI/CD. Les dépôts les plus actifs incluent [vao](/repos/SocialGouv/vao), [dashlord](/repos/SocialGouv/dashlord) et [domifa](/repos/SocialGouv/domifa).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

*   Correction d'une vulnérabilité dans [archifiltre-mails](/repos/SocialGouv/archifiltre-mails).
*   Renforcement de la sécurité et correction de vulnérabilités dans [dsfr-mcp](/repos/SocialGouv/dsfr-mcp).
*   Implémentation d'un mécanisme de "fail closed" pour l'antivirus dans [vao](/repos/SocialGouv/vao).
*   Correction de vulnérabilités dans [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget).

## Autres changements notables
*   **Infrastructure:** Augmentation des ressources CPU et mémoire pour la base de données PostgreSQL dans [vao](/repos/SocialGouv/vao).
*   **Migration:** Migration vers pnpm pour la gestion des dépendances dans plusieurs dépôts, notamment [token-bureau](/repos/SocialGouv/token-bureau), [revu](/repos/SocialGouv/revu), [nos1000jours-blues-epds-widget](/repos/SocialGouv/nos1000jours-blues-epds-widget) et [dashlord-actions](/repos/SocialGouv/dashlord-actions).
*   **Intégration IA:** Développement et amélioration d'outils d'intégration de l'IA, comme [git-ai-trace](/repos/SocialGouv/git-ai-trace) et [repo-falcon](/repos/SocialGouv/repo-falcon).
*   **Abandon de service:** Préparation de l'arrêt du service Recosanté avec l'ajout d'une bannière d'information dans [recosante](/repos/SocialGouv/recosante).
*   **Refonte d'interface:** Refonte majeure de l'interface utilisateur de [dashlord](/repos/SocialGouv/dashlord).
*   **Changement de stockage:** Remplacement de Qdrant par pg\_vector dans [srdt](/repos/SocialGouv/srdt).

## Dépôts les plus actifs
*   **[vao](/repos/SocialGouv/vao):** Améliorations significatives de l'accessibilité, de la robustesse et de la sécurité de l'application, notamment au niveau de la gestion des agréments et de l'authentification.
*   **[dashlord](/repos/SocialGouv/dashlord):** Refonte de l'interface utilisateur et ajout de nouvelles fonctionnalités pour la gestion des données.
*   **[domifa](/repos/SocialGouv/domifa):** Corrections de bugs, améliorations de la sécurité et ajout de l'authentification à deux facteurs.
*   **[legi-data](/repos/SocialGouv/legi-data):** Mises à jour régulières des données de la base LEGI.
*   **[srdt](/repos/SocialGouv/srdt):** Amélioration de l'expérience utilisateur et de la précision de l'assistant virtuel.
*   **[code-du-travail-numerique](/repos/SocialGouv/code-du-travail-numerique):** Ajout des accords d'entreprise et amélioration de la gestion du SMIC.
*   **[infra-apps](/repos/SocialGouv/infra-apps):** Déploiement et configuration de l'application Iterion sur l'environnement OVH.
