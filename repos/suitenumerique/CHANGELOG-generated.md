# Synthèse d'activité : suitenumerique (du 22 avril 2026 au 01 mai 2026)

## Résumé de l'activité
La semaine écoulée a été marquée par une activité intense sur plusieurs dépôts de l'organisation SuiteNumérique. Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment avec le développement d'une application mobile pour Dictaphone et l'ajout de nouvelles fonctionnalités à l'interface utilisateur de Drive. La sécurité a également été une priorité, avec des mises à jour de dépendances et des corrections de vulnérabilités dans plusieurs projets. Des améliorations significatives ont été apportées à l'infrastructure, avec la migration vers GitHub Actions pour la CI/CD et l'optimisation des performances de plusieurs services. L'intégration avec des services externes, comme Docs et Microsoft Outlook, a également progressé.

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de sécurité :
- Correction de vulnérabilités dans [people](/repos/suitenumerique/people) avec la mise à jour de plusieurs dépendances (Pillow, Django, lodash, Next.js, pytest).
- Correction de vulnérabilités dans [meet](/repos/suitenumerique/meet) avec la mise à jour de plusieurs dépendances (Django, aiohttp, vite, pytest, Pillow).
- Correction de vulnérabilités dans [conversations](/repos/suitenumerique/conversations) avec la mise à jour de ses dépendances.
- Correction d'une vulnérabilité JavaScript dans [docs](/repos/suitenumerique/docs).

## Autres changements notables
- Migration de CircleCI vers GitHub Actions pour la CI/CD dans [cunningham](/repos/suitenumerique/cunningham), améliorant la sécurité et la gestion des workflows.
- Remplacement de Nginx par Caddy comme reverse proxy dans [st-home](/repos/suitenumerique/st-home), optimisant l'infrastructure.
- Refonte de l'architecture des workers dans [messages](/repos/suitenumerique/messages) pour une meilleure séparation des tâches et une gestion plus efficace du reindex.
- Ajout d'un support initial pour un add-in Microsoft Outlook dans [meet](/repos/suitenumerique/meet).
- Création du projet [accounts](/repos/suitenumerique/accounts) pour la gestion des comptes utilisateurs.

## Dépôts les plus actifs
- [ui-kit](/repos/suitenumerique/ui-kit) : Ajout de nombreux nouveaux composants et fonctionnalités, améliorant l'interface utilisateur.
- [st-home](/repos/suitenumerique/st-home) : Amélioration de la carte de déploiement et intégration de nouvelles données.
- [meet](/repos/suitenumerique/meet) : Ajout d'un support initial pour un add-in Microsoft Outlook et amélioration de l'authentification.
- [drive](/repos/suitenumerique/drive) : Amélioration de l'expérience utilisateur avec l'ajout de fonctionnalités comme la duplication d'éléments et la gestion des droits d'accès.
- [dictaphone](/repos/suitenumerique/dictaphone) : Développement d'une application mobile (iOS et Android) et intégration avec Docs.
