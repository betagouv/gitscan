# Synthèse d'activité : suitenumerique (du 29 mai 2026 au 26 juin 2026)

## Résumé de l'activité
L'organisation suitenumerique a connu une période d'activité intense, marquée par des améliorations significatives de la sécurité, de la performance et de l'expérience utilisateur de ses différents produits.  Des refontes architecturales majeures, notamment la migration vers Vite dans plusieurs dépôts ([messages](/repos/suitenumerique/messages), [calendars](/repos/suitenumerique/calendars)), visent à moderniser la base de code et à améliorer la scalabilité. L'accent a également été mis sur la sécurité, avec des corrections de vulnérabilités et l'implémentation de nouvelles mesures de protection dans [people](/repos/suitenumerique/people), [meet](/repos/suitenumerique/meet) et [accounts](/repos/suitenumerique/accounts).  Des fonctionnalités importantes ont été ajoutées, comme l'export de dossiers dans [drive](/repos/suitenumerique/drive) et l'amélioration du système de RSVP dans [calendars](/repos/suitenumerique/calendars).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

*   Correction de vulnérabilités dans [people](/repos/suitenumerique/people) avec la mise à jour de dépendances critiques (PyJWT, cryptography) et la correction du Dockerfile.
*   Correction d'une vulnérabilité de redirection OIDC dans [conversations](/repos/suitenumerique/conversations).
*   Renforcement de la sécurité du traitement des données ICS dans [calendars](/repos/suitenumerique/calendars).
*   Mises à jour de dépendances dans [drive](/repos/suitenumerique/drive) et [conversations](/repos/suitenumerique/conversations) pour corriger des failles de sécurité.

## Autres changements notables
*   **Refonte architecturale :** Migration vers Vite dans [messages](/repos/suitenumerique/messages) et [calendars](/repos/suitenumerique/calendars) pour une meilleure performance et expérience de développement.
*   **Migration de tâches asynchrones :** Passage de Celery à Dramatiq dans [st-home](/repos/suitenumerique/st-home) pour une meilleure performance et fiabilité.
*   **Amélioration de l'infrastructure CI/CD :** Optimisations et refactorisation importantes de l'infrastructure CI/CD dans [accounts](/repos/suitenumerique/accounts) pour une meilleure efficacité et maintenance.
*   **Intégration de nouveaux services :** Intégration du client Matrix pour la messagerie dans [hub](/repos/suitenumerique/hub) et OnlyOffice pour la conversion de fichiers dans [drive](/repos/suitenumerique/drive).

## Dépôts les plus actifs
*   **[meet](/repos/suitenumerique/meet)** : Améliorations significatives de la fonctionnalité, de la sécurité et de la performance, incluant l'ajout de nouvelles fonctionnalités et la correction de bugs.
*   **[calendars](/repos/suitenumerique/calendars)** : Refonte majeure avec migration vers Vite, amélioration du système RSVP et de l'interface utilisateur.
*   **[messages](/repos/suitenumerique/messages)** : Migration vers Vite et Tanstack Router, renforcement de la sécurité et amélioration de l'expérience utilisateur.
*   **[people](/repos/suitenumerique/people)** : Améliorations de la sécurité, notamment l'import automatique de boîtes aux lettres depuis DiMail et la correction de vulnérabilités.
*   **[hub](/repos/suitenumerique/hub)** : Ajout de nouvelles fonctionnalités de chat et intégration du client Matrix.
*   **[st-home](/repos/suitenumerique/st-home)** : Amélioration du blog, de la carte de déploiement et migration du système de tâches asynchrones.
*   **[drive](/repos/suitenumerique/drive)** : Ajout de l'export de dossiers, intégration d'OnlyOffice et amélioration de l'interface utilisateur.
*   **[accounts](/repos/suitenumerique/accounts)** : Amélioration de l'infrastructure CI/CD et préparation pour l'ajout d'une interface utilisateur.
