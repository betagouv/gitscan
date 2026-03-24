# Synthèse d'activité : suitenumerique (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par une activité soutenue sur l'ensemble des dépôts de l'organisation suitenumerique, avec un focus particulier sur l'amélioration de l'expérience utilisateur et la correction de bugs. Plusieurs applications ont bénéficié de nouvelles fonctionnalités, notamment Calendars avec le partage de calendriers et les RSVP, Conversations avec une recherche améliorée, et Drive avec la création de fichiers à partir de modèles. Des efforts importants ont également été consacrés à la sécurité, avec des mises à jour de dépendances et des corrections de vulnérabilités dans plusieurs dépôts comme People et st-ansible. L'infrastructure et les processus de développement ont été optimisés, notamment avec l'adoption de nouvelles technologies comme `uv` et `ruff` et la mise à jour des outils CI/CD.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- Correction de vulnérabilités dans [django-lasuite](/repos/suitenumerique/django-lasuite) et [people](/repos/suitenumerique/people) via des mises à jour de dépendances.
- Ajout d'une liste noire de domaines pour renforcer la sécurité dans [st-home](/repos/suitenumerique/st-home).

## Autres changements notables
Plusieurs évolutions techniques majeures ont été déployées :

- Refonte de l'architecture de [messages](/repos/suitenumerique/messages) avec l'adoption de `uv`, `rustfs` et `caddy`.
- Migration des tests Molecule vers le driver Lima dans [st-ansible](/repos/suitenumerique/st-ansible).
- Mise à jour de Next.js vers la version 16 dans [docs](/repos/suitenumerique/docs).
- Passage de ESLint vers la version 9 dans [conversations](/repos/suitenumerique/conversations).
- Ajout du support de l'architecture ARM64 pour les images Docker dans plusieurs dépôts : [calendars](/repos/suitenumerique/calendars), [drive](/repos/suitenumerique/drive], [docs](/repos/suitenumerique/docs], [st-ansible](/repos/suitenumerique/st-ansible).

## Dépôts les plus actifs
Voici les dépôts les plus actifs de la semaine :

- [docs](/repos/suitenumerique/docs) : Amélioration significative de l'expérience utilisateur avec l'ajout d'un modal d'onboarding et l'intégration de l'IA.
- [messages](/repos/suitenumerique/messages) : Refonte architecturale majeure et ajout de nouvelles fonctionnalités comme l'export de boîtes aux lettres.
- [people](/repos/suitenumerique/people) : Corrections de sécurité et améliorations de l'interface utilisateur.
- [drive](/repos/suitenumerique/drive) : Ajout de la création de fichiers à partir de modèles et amélioration de la gestion des fichiers volumineux.
- [calendars](/repos/suitenumerique/calendars) : Ajout de fonctionnalités de partage de calendriers et de RSVP.
- [st-deploycenter](/repos/suitenumerique/st-deploycenter) : Amélioration de l'administration et de l'import de données pour les organisations et les rôles.
