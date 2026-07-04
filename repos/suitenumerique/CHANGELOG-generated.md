# Synthèse d'activité : suitenumerique (du 15/06 au 15/07)

## Résumé de l'activité
L'organisation suitenumerique a connu une période d'activité soutenue, marquée par des améliorations significatives en termes de sécurité, d'expérience utilisateur et de performance. Plusieurs projets ont bénéficié de refontes techniques majeures, notamment la migration vers Vite pour les applications `calendars` et `messages`, et l'adoption de Dramatiq pour la gestion des tâches asynchrones dans `st-home`. L'accent a également été mis sur l'amélioration de la sécurité, avec des corrections de vulnérabilités dans `people` et `conversations`, et le renforcement de la sécurité des transferts de fichiers dans `transfers`. De nouvelles fonctionnalités ont été introduites, comme les liens de téléchargement uniques dans `transfers` et `st-transfers`, et l'amélioration du blog dans `st-home`.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations en matière de sécurité :

- Correction de vulnérabilités dans `people` avec la mise à jour de plusieurs dépendances (PyJWT, cryptography, tornado, etc.) et la mise à jour de Python.
- Renforcement de la sécurité des téléchargements dans [transfers](/repos/suitenumerique/transfers) avec l'ajout d'un scanner de fichiers et la correction de failles identifiées lors d'une revue de code.
- Correction d'une vulnérabilité OIDC dans [conversations](/repos/suitenumerique/conversations) exposant le port interne.

## Autres changements notables
Plusieurs évolutions techniques majeures ont été réalisées :

- Migration du frontend de `calendars` vers Vite pour améliorer les performances. [calendars](/repos/suitenumerique/calendars)
- Migration du frontend de `messages` vers Vite et Tanstack Router pour améliorer les performances et la maintenabilité. [messages](/repos/suitenumerique/messages)
- Migration du système de tâches asynchrones de Celery vers Dramatiq dans `st-home` pour une meilleure performance et fiabilité. [st-home](/repos/suitenumerique/st-home)
- Refonte de l'infrastructure CI/CD dans `accounts` pour une meilleure organisation et réutilisation des workflows. [accounts](/repos/suitenumerique/accounts)
- Intégration de Ruff pour l'analyse statique du code dans `accounts`. [accounts](/repos/suitenumerique/accounts)

## Dépôts les plus actifs
- [ui-kit](/repos/suitenumerique/ui-kit) : Amélioration de l'accessibilité, ajout de traductions et corrections de bugs.
- [transfers](/repos/suitenumerique/transfers) : Améliorations de la sécurité, ajout de liens de téléchargement uniques et migration vers Vite et Tanstack Router.
- [st-home](/repos/suitenumerique/st-home) : Refonte du blog, corrections de la carte de déploiement et migration vers Dramatiq.
- [messages](/repos/suitenumerique/messages) : Amélioration de l'expérience utilisateur, refonte technique vers Vite et Tanstack Router et renforcement de la sécurité.
- [calendars](/repos/suitenumerique/calendars) : Refonte des RSVP, migration vers Vite et renforcement de la sécurité du traitement des données ICS.
- [conversations](/repos/suitenumerique/conversations) : Amélioration de la gestion des erreurs, intégration de Celery et correction de vulnérabilités de sécurité.
