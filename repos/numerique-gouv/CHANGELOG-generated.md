# Synthèse d'activité : numerique-gouv (du 23/04 au 13/08)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par des transformations structurelles majeures et une amélioration continue de l'expérience utilisateur. Les efforts se sont concentrés sur l'internationalisation des plateformes de création de sites [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1), ainsi que sur la modernisation de l'interface de [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).

Par ailleurs, des refontes architecturales importantes, comme le passage vers Ruby on Rails pour [oots-france](/repos/numerique-gouv/oots-france) et l'évolution du modèle de données pour [statistiques-impact](/repos/numerique-gouv/statistiques-impact), renforcent la robustesse et la flexibilité des services. L'alignement avec le Design System de l'État (DSFR) progresse également via [oots-france](/repos/numerique-gouv/oots-france) et [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios).

## Sécurité
- Mise à jour de secrets pour sécuriser le service [francetransfert](/repos/numerique-gouv/francetransfert).
- Correction de vulnérabilités via la mise à jour de la bibliothèque `cryptography` dans [django-dsfr](/repos/numerique-gouv/django-dsfr).
- Amélioration de la gestion de la déconnexion FranceConnect pour garantir une redirection sécurisée via [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy).
- Mise à jour de l'image de base Keycloak pour bénéficier de correctifs de sécurité dans [dockerfiles](/repos/numerique-gouv/dockerfiles).

## Autres changements notables
- Migration architecturale complète vers Ruby on Rails pour [oots-france](/repos/numerique-gouv/oots-france), incluant une simplification de l'installation et l'intégration du DSFR.
- Refonte du modèle de données avec l'introduction du modèle "Record" et migration vers Python 3.14 pour [statistiques-impact](/repos/numerique-gouv/statistiques-impact).
- Mise en place de tests de bout en bout (E2E) avec Playwright et de pipelines de comparaison visuelle pour [sites-conformes](/repos/numerique-gouv/sites-conformes).
- Refonte de la structure du projet et du Swift Package pour [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios).
- Implémentation d'un mécanisme de *feature flags* pour la gestion dynamique des fonctionnalités dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).

## Dépôts les plus actifs
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Refonte de l'interface utilisateur, gestion des services externes et amélioration de l'accessibilité.
- [oots-france](/repos/numerique-gouv/oots-france) : Réécriture complète de l'architecture et modernisation de l'interface.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Travaux importants sur l'internationalisation et l'optimisation du déploiement.
- [statistiques-impact](/repos/numerique-gouv/statistiques-impact) : Évolution majeure du modèle de données et mise à jour de l'environnement technique.
- [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios) : Développement de nouveaux composants et restructuration du projet.
