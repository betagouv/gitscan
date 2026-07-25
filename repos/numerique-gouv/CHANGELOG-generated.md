# Synthèse d'activité : numerique-gouv (du 06 mai 2026 au 16 juillet 2026)

## Résumé de l'activité
L'organisation numerique-gouv a connu une période d'activité soutenue, marquée par des améliorations significatives de l'expérience utilisateur et de la sécurité de ses différentes plateformes. On observe un effort important sur l'internationalisation avec l'ajout de la gestion de plusieurs langues sur [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1). Des mises à jour de sécurité ont été déployées sur [django-dsfr](/repos/numerique-gouv/django-dsfr) et des améliorations de l'infrastructure et de la gestion des données ont été apportées à [statistiques-impact](/repos/numerique-gouv/statistiques-impact). Les plateformes La Suite ([lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage)) et b3desk ([b3desk](/repos/numerique-gouv/b3desk)) ont également bénéficié d'améliorations fonctionnelles et techniques.

## Sécurité
Plusieurs dépôts ont reçu des mises à jour liées à la sécurité :

- Correction d'une vulnérabilité dans la dépendance `cryptography` sur [django-dsfr](/repos/numerique-gouv/django-dsfr).
- Mise à jour d'un secret sur [francetransfert](/repos/numerique-gouv/francetransfert) pour renforcer la sécurité du service.

## Autres changements notables
- Refonte du modèle de données et migration vers Python 3.14 sur [statistiques-impact](/repos/numerique-gouv/statistiques-impact).
- Mise en place de tests E2E avec Playwright sur [sites-conformes](/repos/numerique-gouv/sites-conformes) pour améliorer la qualité du code.
- Utilisation de `django-tasks-db` pour la gestion des tâches asynchrones sur [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).
- Refactoring de la structure du projet et adoption de la couleur d'accent par défaut du DSFR sur [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios).

## Dépôts les plus actifs
- [statistiques-impact](/repos/numerique-gouv/statistiques-impact) : Refonte du modèle de données et migration vers Python 3.14.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Ajout de la gestion de plusieurs langues et simplification du déploiement.
- [sites-conformes](/repos/numerique-gouv/sites-conformes) : Amélioration de l'expérience utilisateur avec un système de notifications et mise en place de tests E2E.
- [b3desk](/repos/numerique-gouv/b3desk) : Amélioration de l'interface utilisateur et de la configuration BigBlueButton.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Ajout de nouvelles fonctionnalités et refactorisation technique pour améliorer les performances.
