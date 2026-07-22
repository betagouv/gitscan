# Synthèse d'activité : numerique-gouv (du 06 mai 2026 au 17 juillet 2026)

## Résumé de l'activité
L'organisation numerique-gouv a connu une période d'activité soutenue, marquée par des améliorations significatives sur plusieurs de ses dépôts. Les efforts se sont concentrés sur l'internationalisation des plateformes ([sites-faciles](/repos/numerique-gouv/sites-faciles), [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1)), l'amélioration de la sécurité (notamment avec la mise à jour de dépendances dans [django-dsfr](/repos/numerique-gouv/django-dsfr) et [statistiques-impact](/repos/numerique-gouv/statistiques-impact)), et l'ajout de nouvelles fonctionnalités, comme le panneau d'information sur [sites-conformes](/repos/numerique-gouv/sites-conformes) et l'intégration de services comme Tchap et Resana sur [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage). Des efforts importants ont également été déployés pour améliorer l'expérience utilisateur et la maintenabilité du code sur plusieurs projets.

## Sécurité
Plusieurs mises à jour ont été apportées pour renforcer la sécurité des différents services :
- Mise à jour de la dépendance `cryptography` dans [django-dsfr](/repos/numerique-gouv/django-dsfr) pour corriger des vulnérabilités.
- Mise à jour de plusieurs dépendances dans [statistiques-impact](/repos/numerique-gouv/statistiques-impact) pour améliorer la sécurité et la performance.
- Modification d'un secret dans [francetransfert](/repos/numerique-gouv/francetransfert) pour assurer la sécurité du service.

## Autres changements notables
- Refonte significative de la gestion des indicateurs et migration vers Python 3.14 dans [statistiques-impact](/repos/numerique-gouv/statistiques-impact).
- Implémentation de tests E2E avec Playwright dans [sites-conformes](/repos/numerique-gouv/sites-conformes) pour améliorer la qualité et la stabilité.
- Mise en place d'un déploiement en un clic sur Scalingo pour [sites-faciles](/repos/numerique-gouv/sites-faciles).
- Utilisation de `django-tasks-db` pour la gestion des tâches asynchrones dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).

## Dépôts les plus actifs
- [statistiques-impact](/repos/numerique-gouv/statistiques-impact) : Refonte de la gestion des indicateurs et migration technique majeure.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Internationalisation de la plateforme et simplification du déploiement.
- [sites-conformes](/repos/numerique-gouv/sites-conformes) : Ajout d'un panneau d'information et implémentation de tests E2E.
- [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage) : Ajout de pages pour les services Tchap et Resana.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Amélioration de l'API de notifications et refactorisation du code.
