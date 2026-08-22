# Synthèse d'activité : numerique-gouv (du 10/07 au 17/07)

## Résumé de l'activité
L'activité de la période est marquée par des avancées majeures sur l'expérience utilisateur et la modernisation des infrastructures. L'accent a été mis sur l'internationalisation des plateformes de création de sites [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1), ainsi que sur l'amélioration de l'interface et des fonctionnalités de gestion pour les services de notification [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) et de gestion de réunions [b3desk](/repos/numerique-gouv/b3desk).

Parallèlement, des refontes architecturales importantes renforcent la robustesse des outils, notamment avec la migration vers Ruby on Rails pour [oots-france](/repos/numerique-gouv/oots-france) et l'évolution du modèle de données pour [statistiques-impact](/repos/numerique-gouv/statistiques-impact). Ces évolutions visent à offrir des outils plus performants, plus faciles à maintenir et mieux alignés sur les standards de design de l'État.

## Sécurité
- Correction de vulnérabilités critiques via la mise à jour de la bibliothèque `cryptography` dans [django-dsfr](/repos/numerique-gouv/django-dsfr).
- Renforcement de la sécurité des accès avec la mise en place du *rate limiting* pour les clés d'accès dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).
- Mise à jour de secrets et d'images de base (Keycloak) pour garantir l'intégrité des services [francetransfert](/repos/numerique-gouv/francetransfert) et [dockerfiles](/repos/numerique-gouv/dockerfiles).

## Autres changements notables
- **Migrations architecturales majeures** : Transition complète de [oots-france](/repos/numerique-gouv/oots-france) vers le framework Ruby on Rails et migration de [statistiques-impact](/repos/numerique-gouv/statistiques-impact) vers Python 3.14.
- **Évolution des API et des données** : Introduction d'une nouvelle API v2 pour [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) et création d'un nouveau modèle de données "Record" pour [statistiques-impact](/repos/numerique-gouv/statistiques-impact).
- **Optimisation du déploiement et de l'infrastructure** : Simplification de la mise en production sur Scalingo pour [sites-faciles](/repos/numerique-gouv/sites-faciles) et optimisation des processus de build avec Vite pour [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).

## Dépôts les plus actifs
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Évolutions majeures sur les services, l'administration et l'expérience utilisateur.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Travaux intensifs sur l'internationalisation et l'interface d'administration.
- [oots-france](/repos/numerique-gouv/oots-france) : Réécriture complète de l'architecture et modernisation de l'interface.
- [statistiques-impact](/repos/numerique-gouv/statistiques-impact) : Refonte de la gestion des indicateurs et mise à jour de l'environnement technique.
