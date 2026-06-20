# Synthèse d'activité : suitenumerique (du 29 mai au 25 juin 2026)

## Résumé de l'activité
La période récente a été marquée par des efforts importants pour améliorer la sécurité, la performance et l'expérience utilisateur des différentes applications de la Suite Numérique. Plusieurs dépôts ont bénéficié de mises à jour significatives, notamment [transfers](/repos/suitenumerique/transfers) avec une refonte de son frontend et des améliorations de la sécurité des téléchargements, et [st-home](/repos/suitenumerique/st-home) avec l'adoption de Dramatiq pour la gestion des tâches asynchrones et des améliorations de l'affichage de la carte de déploiement.  Des améliorations notables ont également été apportées à [meet](/repos/suitenumerique/meet) avec l'ajout d'un nouveau pipeline audio et à [calendars](/repos/suitenumerique/calendars) avec une refonte du RSVP et une migration vers Vite. L'accent a également été mis sur la correction de vulnérabilités et l'amélioration de la qualité du code dans plusieurs projets.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de la sécurité :

- [transfers](/repos/suitenumerique/transfers) : Renforcement de la sécurité des téléchargements et correction de vulnérabilités identifiées lors d'une revue de sécurité.
- [people](/repos/suitenumerique/people) : Mise à jour de dépendances (urllib3, next, django) pour corriger des vulnérabilités de sécurité.
- [meet-sip](/repos/suitenumerique/meet-sip) : Correction d'une condition de concurrence.
- [calendars](/repos/suitenumerique/calendars) : Renforcement de la sécurité du traitement des données ICS pour prévenir les vulnérabilités.

## Autres changements notables
- [transfers](/repos/suitenumerique/transfers) : Migration du frontend vers Vite et TanStack Router pour une meilleure performance et une architecture plus moderne.
- [st-home](/repos/suitenumerique/st-home) : Remplacement de Celery par Dramatiq pour la gestion des tâches asynchrones.
- [calendars](/repos/suitenumerique/calendars) : Migration du frontend de Next.js vers Vite.
- [find](/repos/suitenumerique/find) : Suppression de la recherche par embedding et refonte de la gestion des indices de recherche.
- [conversations](/repos/suitenumerique/conversations) : Mise en place d'un système de surveillance de la santé des modèles d'IA.

## Dépôts les plus actifs
- [transfers](/repos/suitenumerique/transfers) : Refonte du frontend et amélioration de la sécurité des téléchargements.
- [st-home](/repos/suitenumerique/st-home) : Amélioration de la gestion des tâches asynchrones et de l'affichage de la carte de déploiement.
- [meet](/repos/suitenumerique/meet) : Amélioration de la qualité audio et ajout de nouvelles fonctionnalités pour les réunions.
- [calendars](/repos/suitenumerique/calendars) : Refonte du RSVP et migration vers Vite.
- [conversations](/repos/suitenumerique/conversations) : Amélioration de la stabilité, de la surveillance des modèles d'IA et de l'expérience utilisateur.
- [docs](/repos/suitenumerique/docs) : Ajout de nouvelles fonctionnalités et amélioration de l'accessibilité.
