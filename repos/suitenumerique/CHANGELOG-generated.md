# Synthèse d'activité : suitenumerique (du 08/04 au 18/05/2026)

## Résumé de l'activité
L'organisation suitenumerique a connu une période d'activité soutenue, marquée par des améliorations significatives sur plusieurs de ses produits. Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de nouvelles fonctionnalités comme la prévisualisation de fichiers, la gestion des permissions et l'intégration de l'IA. Des refontes architecturales importantes ont été réalisées sur des projets comme `hub` et `docs`, modernisant leur codebase et ouvrant la voie à de nouvelles fonctionnalités. La sécurité a également été une priorité, avec des mises à jour de dépendances et des améliorations de l'authentification. Plusieurs projets ont progressé dans leur développement initial, comme `encryption` et `accounts`, posant les bases pour de futures fonctionnalités.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Mise à jour de dépendances vulnérables dans [django-lasuite](/repos/suitenumerique/django-lasuite)
- Renforcement de l'authentification dans [dictaphone](/repos/suitenumerique/dictaphone) avec la migration vers JWT et PKCE.
- Restriction de l'accès à la configuration de l'analyse dans [conversations](/repos/suitenumerique/conversations).

## Autres changements notables
- Refonte complète du frontend de [hub](/repos/suitenumerique/hub) avec Next.js et TypeScript.
- Migration de l'outil de construction de paquets de `pip` vers `uv` dans [docs](/repos/suitenumerique/docs).
- Mise en place d'un benchmark pour mesurer les performances de [meet-matting](/repos/suitenumerique/meet-matting).
- Initialisation du projet [accounts](/repos/suitenumerique/accounts) et ajout d'un outil de tests de charge locaux.
- Implémentation d'une première version de l'échange de jetons OAuth 2.0 dans [menshen](/repos/suitenumerique/menshen).

## Dépôts les plus actifs
- [docs](/repos/suitenumerique/docs) : Refonte majeure avec migration vers de nouvelles technologies et amélioration de la gestion des documents.
- [meet](/repos/suitenumerique/meet) : Ajout de la fonctionnalité Picture-in-Picture et améliorations de l'accessibilité et de la sécurité.
- [conversations](/repos/suitenumerique/conversations) : Ajout d'un tutoriel d'onboarding, amélioration de la gestion des fichiers et du contexte hybride.
- [drive](/repos/suitenumerique/drive) : Amélioration de la prévisualisation des fichiers PDF et ajout d'une modal de disclaimer configurable.
- [calendars](/repos/suitenumerique/calendars) : Corrections de bugs et ajout de scopes pour une gestion plus fine des permissions des canaux.
