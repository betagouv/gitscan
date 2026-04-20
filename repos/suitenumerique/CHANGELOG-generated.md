# Synthèse d'activité : suitenumerique (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par une activité soutenue sur l'ensemble des dépôts de l'organisation suitenumerique. Plusieurs applications ont bénéficié d'améliorations significatives en termes de fonctionnalités et de sécurité. On note notamment des avancées importantes sur [calendars](/repos/suitenumerique/calendars) avec l'intégration de Messages et l'amélioration du partage, sur [conversations](/repos/suitenumerique/conversations) avec l'authentification silencieuse et la prise en charge de nouveaux formats de fichiers, et sur [drive](/repos/suitenumerique/drive) avec l'ajout de la duplication de fichiers et un visualiseur PDF. L'application [meet](/repos/suitenumerique/meet) a également reçu de nombreuses améliorations, notamment en matière de sécurité et de transcription.

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de sécurité :
- [conversations](/repos/suitenumerique/conversations) : Correction de vulnérabilités (CVEs) via la mise à jour des dépendances backend et frontend.
- [drive](/repos/suitenumerique/drive) : Mise à jour de Django et Pillow pour corriger des failles de sécurité.
- [people](/repos/suitenumerique/people) : Mise à jour de plusieurs dépendances (Django, Next.js, pytest, lodash, requests) pour corriger des failles de sécurité.

## Autres changements notables
- **Infrastructure :** Remplacement de Nginx par Caddy comme reverse proxy sur [st-home](/repos/suitenumerique/st-home).
- **CI/CD :** Migration de CircleCI vers GitHub Actions sur [cunningham](/repos/suitenumerique/cunningham).
- **Architecture :** Refonte de l'architecture frontend de [dictaphone](/repos/suitenumerique/dictaphone) avec des composants réutilisables.
- **Gestion des dépendances :** Configuration de Renovate pour la gestion des dépendances sur [menshen](/repos/suitenumerique/menshen).

## Dépôts les plus actifs
- [meet](/repos/suitenumerique/meet) : Améliorations majeures en matière de sécurité, de transcription et d'expérience utilisateur.
- [drive](/repos/suitenumerique/drive) : Ajout de nouvelles fonctionnalités comme la duplication de fichiers et un visualiseur PDF.
- [conversations](/repos/suitenumerique/conversations) : Implémentation de l'authentification silencieuse et support de nouveaux formats de fichiers.
- [ui-kit](/repos/suitenumerique/ui-kit) : Amélioration de la bibliothèque d'icônes et ajout de nouveaux composants d'interface utilisateur.
- [calendars](/repos/suitenumerique/calendars) : Intégration avec l'application Messages et amélioration du partage de calendriers.
