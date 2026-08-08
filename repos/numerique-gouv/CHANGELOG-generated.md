# Synthèse d'activité : numerique-gouv (du 10/07 au 31/07)

## Résumé de l'activité
L'activité de cette période est marquée par une forte orientation vers l'amélioration de l'expérience utilisateur et l'internationalisation des services. Les outils de création de sites ([sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1)) progressent significativement sur la gestion multilingue, tandis que l'application [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) bénéficie d'une refonte majeure de son interface et de l'intégration de nouveaux services externes.

Parallèlement, des évolutions structurelles importantes sont visibles sur [statistiques-impact](/repos/numerique-gouv/statistiques-impact) avec une refonte de son modèle de données, et des avancées fonctionnelles sont notables dans [b3desk](/repos/numerique-gouv/b3desk) avec l'amorce de l'intégration de la transcription par IA. L'accessibilité et la visibilité des services sont également renforcées via [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage).

## Sécurité
- Correction de vulnérabilités critiques via la mise à jour de la bibliothèque `cryptography` dans [django-dsfr](/repos/numerique-gouv/django-dsfr).
- Amélioration de la gestion des déconnexions avec FranceConnect via [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy).
- Mise à jour des secrets de l'application pour [francetransfert](/repos/numerique-gouv/francetransfert).
- Mise à jour des images de base pour Keycloak afin de bénéficier des derniers correctifs de sécurité dans [dockerfiles](/repos/numerique-gouv/dockerfiles).

## Autres changements notables
- **Refonte de données et infrastructure :** Migration vers Python 3.14 et introduction d'un nouveau modèle de données "Record" pour [statistiques-impact](/repos/numerique-gouv/statistiques-impact).
- **Qualité logicielle :** Introduction de tests de bout en bout (E2E) avec Playwright et de pipelines de comparaison visuelle pour [sites-conformes](/repos/numerique-gouv/sites-conformes).
- **Architecture mobile :** Refonte de la structure du package Swift pour [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios).
- **Déploiement et pilotage :** Mise en place de *feature flags* pour le pilotage des fonctionnalités dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) et simplification du déploiement sur Scalingo pour [sites-faciles](/repos/numerique-gouv/sites-faciles).

## Dépôts les plus actifs
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Refonte de l'interface utilisateur, gestion des suivis et intégration de nouveaux services.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1) : Travaux majeurs sur l'internationalisation et la gestion multilingue.
- [statistiques-impact](/repos/numerique-gouv/statistiques-impact) : Migration technique majeure et restructuration profonde du modèle de données.
- [b3desk](/repos/numerique-gouv/b3desk) : Améliorations de l'interface d'administration et développement de fonctionnalités liées à l'IA.
