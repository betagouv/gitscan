# Synthèse d'activité : suitenumerique (du 22 mai au 11 juillet 2026)

## Résumé de l'activité
L'organisation suitenumerique a connu une période d'activité soutenue, marquée par des améliorations significatives de l'expérience utilisateur et de la sécurité de ses différentes applications. La migration vers des technologies plus modernes comme Vite et Astro se poursuit, notamment pour les projets `transfers`, `docs` et `calendars`, afin d'améliorer les performances et la maintenabilité. L'intégration de la messagerie Matrix dans `hub` et l'ajout de fonctionnalités de partage de fichiers sécurisé dans `st-transfers` sont des avancées notables pour les utilisateurs finaux.  Des efforts importants ont également été consacrés à la correction de bugs et à l'amélioration de la robustesse des applications, notamment `messages`, `conversations` et `find`.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction de vulnérabilités dans `accounts` et `media-sdk` avec la mise à jour de dépendances critiques (PyJWT, cryptography).
- Renforcement de la sécurité du flux de téléchargement dans [transfers](/repos/suitenumerique/transfers).
- Correction de vulnérabilités Dockerfile dans `dictaphone`.
- Renforcement de la sécurité du traitement des données ICS dans [calendars](/repos/suitenumerique/calendars).

## Autres changements notables
- Migration de Next.js vers Vite dans [transfers](/repos/suitenumerique/transfers) et de l'architecture frontend de [calendars](/repos/suitenumerique/calendars) pour une meilleure performance.
- Migration complète du site web [docs](/repos/suitenumerique/docs-website) vers Astro, avec récupération du contenu directement depuis le projet Docs.
- Migration du système de tâches asynchrones de Celery vers Dramatiq dans [st-home](/repos/suitenumerique/st-home) pour une meilleure performance.
- Refonte de l'infrastructure CI/CD dans [accounts](/repos/suitenumerique/accounts) pour une meilleure organisation et réutilisation des workflows.
- Refonte complète du MTA-in en Python pur dans [messages](/repos/suitenumerique/messages), supprimant la dépendance à Postfix.

## Dépôts les plus actifs
- [ui-kit](/repos/suitenumerique/ui-kit) : Ajout de nouveaux composants et améliorations d'accessibilité.
- [st-home](/repos/suitenumerique/st-home) : Refonte du blog et migration vers Dramatiq.
- [messages](/repos/suitenumerique/messages) : Améliorations de l'interface utilisateur, correction de bugs et refonte du MTA-in.
- [hub](/repos/suitenumerique/hub) : Intégration de la messagerie Matrix et ajout de nouvelles fonctionnalités.
- [calendars](/repos/suitenumerique/calendars) : Refonte de la gestion des RSVP et migration vers Vite.
- [docs-website](/repos/suitenumerique/docs-website) : Migration vers Astro et refonte du contenu.
- [meet](/repos/suitenumerique/meet) : Amélioration de l'affichage des participants et ajout d'un formulaire de feedback.
