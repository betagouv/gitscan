# Synthèse d'activité : suitenumerique (derniers 7 jours)

## Résumé de l'activité

La semaine écoulée a été marquée par une activité soutenue sur l'ensemble des dépôts de l'organisation suitenumerique. Les efforts se sont concentrés sur l'amélioration de la sécurité, de l'accessibilité et des performances des applications existantes, notamment Calendars, Meet, Messages et Docs. Plusieurs dépôts ont bénéficié de mises à jour techniques importantes, comme la migration vers de nouvelles versions de librairies et l'optimisation du code. L'ajout de nouvelles fonctionnalités, comme le partage de calendriers ([calendars](/repos/suitenumerique/calendars)) et l'importation de fichiers ([messages](/repos/suitenumerique/messages)), témoigne d'une volonté constante d'améliorer l'expérience utilisateur.

## Sécurité

Plusieurs dépôts ont bénéficié d'améliorations en matière de sécurité :

- Correction de vulnérabilités dans Django dans [django-lasuite](/repos/suitenumerique/django-lasuite) et [find](/repos/suitenumerique/find).
- Mise à jour de la librairie Next dans [st-deploycenter](/repos/suitenumerique/st-deploycenter) pour corriger une vulnérabilité.
- Blocage des domaines potentiellement dangereux et des URL non sécurisées provenant de DILA dans [st-home](/repos/suitenumerique/st-home).

## Autres changements notables

Plusieurs changements techniques majeurs ont été effectués :

- Migration de ESLint vers la version 9 dans [conversations](/repos/suitenumerique/conversations).
- Refonte de l'architecture de [messages](/repos/suitenumerique/messages) avec uv, rustfs et caddy.
- Ajout du support de l'architecture ARM64 dans plusieurs dépôts : [calendars](/repos/suitenumerique/calendars), [docs](/repos/suitenumerique/docs), [drive](/repos/suitenumerique/drive), [find](/repos/suitenumerique/find), [st-home](/repos/suitenumerique/st-home).
- Mise en place de tests automatisés avec Molecule et GitHub Actions dans [st-ansible](/repos/suitenumerique/st-ansible).
- Utilisation de `uvicorn` pour le backend de [docs](/repos/suitenumerique/docs) pour potentiellement améliorer les performances.

## Dépôts les plus actifs

- [calendars](/repos/suitenumerique/calendars) : Ajout de fonctionnalités de partage de calendriers, d'importation d'événements et de liens RSVP.
- [docs](/repos/suitenumerique/docs) : Ajout de la fonctionnalité de déplacement de documents et intégration de Blocknote AI.
- [messages](/repos/suitenumerique/messages) : Ajout de la possibilité d'exporter des boîtes aux lettres au format mbox et d'ajouter des images via BlockNote.
- [meet](/repos/suitenumerique/meet) : Amélioration de la sécurité, de l'accessibilité et correction de bugs.
- [drive](/repos/suitenumerique/drive) : Ajout de la création de fichiers à partir de modèles et implémentation du mirroring de fichiers vers S3.
- [django-lasuite](/repos/suitenumerique/django-lasuite) : Amélioration de l'interface d'administration et gestion des types de fichiers.
- [st-deploycenter](/repos/suitenumerique/st-deploycenter) : Amélioration de l'administration et de l'import de données pour les organisations et les rôles.
