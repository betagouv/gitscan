# Synthèse d'activité : suitenumerique (du 13 mai 2026 au 30 mai 2026)

## Résumé de l'activité
SuiteNumérique a connu une période d'activité soutenue, avec des améliorations significatives apportées à plusieurs de ses produits. L'accent a été mis sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de nouvelles fonctionnalités comme l'exportation de dossiers dans [drive](/repos/suitenumerique/drive), la prévisualisation de fichiers dans [ui-kit](/repos/suitenumerique/ui-kit) et l'intégration de tutoriels dans [conversations](/repos/suitenumerique/conversations). Des efforts importants ont également été déployés pour renforcer la sécurité, notamment dans [people](/repos/suitenumerique/people) et [livekit-sip](/repos/suitenumerique/livekit-sip), et pour améliorer la robustesse et la performance de l'infrastructure, avec des refactorings et des optimisations dans plusieurs dépôts comme [meet-matting](/repos/suitenumerique/meet-matting) et [calendars](/repos/suitenumerique/calendars). L'arrivée de nouvelles fonctionnalités comme le chat dans [hub](/repos/suitenumerique/hub) et l'intégration Outlook (alpha) dans [meet](/repos/suitenumerique/meet) témoignent de l'innovation continue de l'organisation.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- Correction de vulnérabilités dans les dépendances de [people](/repos/suitenumerique/people) (urllib3, next, django, dimail).
- Renforcement de la sécurité dans [st-transfers](/repos/suitenumerique/st-transfers) avec le verrouillage des brouillons et la protection contre les attaques potentielles.
- Ajout de la bibliothèque `defusedxml` dans [messages](/repos/suitenumerique/messages) pour améliorer la sécurité.
- Mise à jour de dépendances dans [conversations](/repos/suitenumerique/conversations) et [calendars](/repos/suitenumerique/calendars) pour corriger des failles de sécurité.

## Autres changements notables
Plusieurs changements techniques majeurs ont été effectués :

- Migration du frontend de [hub](/repos/suitenumerique/hub) vers React et Next.js.
- Refonte de l'infrastructure de test avec Playwright dans [hub](/repos/suitenumerique/hub).
- Migration de `pip` à `uv` pour la gestion des dépendances dans [docs](/repos/suitenumerique/docs).
- Refactorisation du code et ajout de linters dans [meet-matting](/repos/suitenumerique/meet-matting).
- Passage à Python 3.14.5 et Django 5.12.4 dans [conversations](/repos/suitenumerique/conversations).

## Dépôts les plus actifs
Voici les dépôts les plus actifs de la période :

- [meet](/repos/suitenumerique/meet) : Amélioration significative de l'expérience utilisateur avec l'ajout de fonctionnalités PiP, l'amélioration des réactions et le support initial d'un add-in Outlook.
- [conversations](/repos/suitenumerique/conversations) : Ajout d'un tutoriel d'intégration, amélioration de la gestion des documents et des projets, et correction de bugs.
- [ui-kit](/repos/suitenumerique/ui-kit) : Ajout de nouvelles fonctionnalités de prévisualisation de fichiers et amélioration de la gestion des icônes.
- [drive](/repos/suitenumerique/drive) : Ajout de la possibilité d'exporter des dossiers et amélioration de la prévisualisation des fichiers.
- [hub](/repos/suitenumerique/hub) : Refonte complète de l'interface utilisateur et ajout d'une fonctionnalité de chat.
- [messages](/repos/suitenumerique/messages) : Ajout de la prévisualisation des pièces jointes et de l'intégration CalDAV.
- [meet-matting](/repos/suitenumerique/meet-matting) : Optimisation des performances et amélioration de la qualité de la segmentation.
