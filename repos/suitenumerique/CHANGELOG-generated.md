# Synthèse d'activité : suitenumerique (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par une activité soutenue sur l'ensemble des dépôts de l'organisation. Les améliorations se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de nouvelles fonctionnalités comme le partage de calendriers ([calendars](/repos/suitenumerique/calendars)), la recherche améliorée dans les conversations ([conversations](/repos/suitenumerique/conversations)), et la corbeille dans Dictaphone ([dictaphone](/repos/suitenumerique/dictaphone)).  Des efforts importants ont également été déployés pour renforcer la sécurité, avec des mises à jour de dépendances et des corrections de vulnérabilités dans plusieurs dépôts, dont [people](/repos/suitenumerique/people). L'organisation continue d'investir dans l'infrastructure et les outils de développement, avec des migrations vers des technologies plus performantes et des améliorations des processus CI/CD.

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de sécurité :

- Correction de vulnérabilités dans [people](/repos/suitenumerique/people) avec la mise à jour de Django, joserfc et tornado.
- Blocage des domaines potentiellement dangereux dans [st-home](/repos/suitenumerique/st-home) pour renforcer la sécurité.

## Autres changements notables
Plusieurs changements techniques majeurs ont été effectués :

- Migration vers `uv` et RustFS dans [messages](/repos/suitenumerique/messages) pour améliorer la performance et la sécurité.
- Refonte de l'architecture avec uv, rustfs et caddy dans [messages](/repos/suitenumerique/messages).
- Passage de Django à la version 5.2.12 dans [drive](/repos/suitenumerique/drive) et [st-deploycenter](/repos/suitenumerique/st-deploycenter).
- Adoption de Lima pour les tests Molecule dans [st-ansible](/repos/suitenumerique/st-ansible).
- Mise à jour de Next.js vers la version 16 dans [docs](/repos/suitenumerique/docs).

## Dépôts les plus actifs
Voici les dépôts les plus actifs de la semaine :

- [docs](/repos/suitenumerique/docs) : Amélioration significative de l'expérience utilisateur avec l'ajout d'un modal d'onboarding et l'intégration de l'IA.
- [messages](/repos/suitenumerique/messages) : Refonte de l'architecture pour améliorer la performance et la sécurité.
- [people](/repos/suitenumerique/people) : Corrections de sécurité et améliorations de l'interface utilisateur.
- [calendars](/repos/suitenumerique/calendars) : Ajout de fonctionnalités de partage de calendriers et d'importation d'événements.
- [drive](/repos/suitenumerique/drive) : Amélioration de la gestion des fichiers volumineux et ajout de menus contextuels.
- [dictaphone](/repos/suitenumerique/dictaphone) : Ajout d'une fonctionnalité de corbeille et intégration de la documentation.
- [meet](/repos/suitenumerique/meet) : Amélioration de la sécurité et de l'interface utilisateur.
