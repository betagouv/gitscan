# Synthèse d'activité : suitenumerique (du 29 mai au 11 juillet 2026)

## Résumé de l'activité
L'organisation suitenumerique a connu une période d'activité intense, marquée par des améliorations significatives en matière de sécurité, de performance et d'expérience utilisateur. Plusieurs projets ont bénéficié de refactorisations architecturales importantes, comme la migration de `transfers` vers Vite + Tanstack Router et de `calendars` de Next.js vers Vite. L'intégration de la messagerie Matrix dans `hub` et l'amélioration de l'authentification dans `accounts` sont des avancées notables. L'accent a également été mis sur la documentation et l'automatisation des processus de développement, notamment avec l'ajout de charts Helm et de tests E2E. L'ensemble de ces efforts vise à renforcer la souveraineté numérique et à offrir des outils plus performants et sécurisés aux utilisateurs.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

*   Correction de vulnérabilités dans `people` avec la mise à jour de dépendances comme `PyJWT` et `cryptography`, ainsi que l'amélioration de la configuration Docker.
*   Renforcement de la sécurité du flux de téléchargement dans [transfers](/repos/suitenumerique/transfers).
*   Sécurisation de l'authentification API dans [dictaphone](/repos/suitenumerique/dictaphone).
*   Renforcement de la sécurité du traitement des données ICS dans [calendars](/repos/suitenumerique/calendars).
*   Chiffrement des données sensibles dans [accounts](/repos/suitenumerique/accounts).

## Autres changements notables
*   **Refactorisations architecturales :** Migration de `transfers` vers Vite + Tanstack Router et de `calendars` de Next.js vers Vite pour améliorer la performance et l'expérience de développement.
*   **Remplacement de technologies :** Remplacement de Celery par Dramatiq dans [st-home](/repos/suitenumerique/st-home) pour une meilleure fiabilité et performance. Suppression de Postfix dans [transfers](/repos/suitenumerique/transfers) et de `tsdav` dans [calendars](/repos/suitenumerique/calendars).
*   **Intégration de nouvelles fonctionnalités :** Intégration de la messagerie Matrix dans [hub](/repos/suitenumerique/hub) et ajout de liens de téléchargement uniques auto-désactivants dans [st-transfers](/repos/suitenumerique/st-transfers).
*   **Amélioration de l'infrastructure :** Ajout d'un chart Helm pour faciliter le déploiement de [menshen](/repos/suitenumerique/menshen) et mise en place d'une stack de tests end-to-end dans [accounts](/repos/suitenumerique/accounts).

## Dépôts les plus actifs
*   [ui-kit](/repos/suitenumerique/ui-kit) : Ajout de nouveaux composants et améliorations d'accessibilité.
*   [transfers](/repos/suitenumerique/transfers) : Migration vers une nouvelle stack frontend et renforcement de la sécurité.
*   [st-home](/repos/suitenumerique/st-home) : Amélioration de la robustesse et refactorisation de la gestion des tâches asynchrones.
*   [messages](/repos/suitenumerique/messages) : Amélioration de la sécurité, correction de bugs et refonte de l'infrastructure MTA-in.
*   [hub](/repos/suitenumerique/hub) : Intégration de la messagerie Matrix et amélioration de l'interface utilisateur.
*   [calendars](/repos/suitenumerique/calendars) : Refonte de la gestion des RSVP et migration vers Vite.
*   [accounts](/repos/suitenumerique/accounts) : Amélioration de la sécurité et de la flexibilité de l'authentification.
*   [docs](/repos/suitenumerique/docs) : Refonte complète du site web et amélioration de la recherche.
*   [drive](/repos/suitenumerique/drive) : Amélioration de la recherche de fichiers et correction de bugs.
