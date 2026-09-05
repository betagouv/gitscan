# Synthèse d'activité : numerique-gouv (du 25/08 au 01/09/2026)

## Résumé de l'activité
L'activité de la période est marquée par une montée en maturité des produits, portée par trois axes majeurs : l'internationalisation, la modernisation de l'expérience utilisateur via le Design System de l'État (DSFR) et un renforcement massif de la sécurité.

Les outils de création de sites ([sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1)) intègrent désormais la gestion multilingue pour faciliter l'accès à l'information. Parallèlement, [oots-france](/repos/numerique-gouv/oots-france) et [sites-conformes](/repos/numerique-gouv/sites-conformes) alignent leurs interfaces sur les standards de l'État pour une meilleure cohérence visuelle. Enfin, la suite "AMI" ([ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) et [ami-app-ios](/repos/numerique-gouv/ami-app-ios)) franchit un cap technologique avec l'introduction des Passkeys et de la biométrie, offrant aux utilisateurs une authentification plus fluide, simple et hautement sécurisée.

## Sécurité
- Support des Passkeys et de la biométrie (FaceID) pour [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) et [ami-app-ios](/repos/numerique-gouv/ami-app-ios).
- Renforcement de la sécurité des échanges via le protocole ES256 pour FranceConnect et mise en place du rate limiting dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).
- Sécurisation du stockage local des données sensibles sur [ami-app-ios](/repos/numerique-gouv/ami-app-ios).
- Corrections de vulnérabilités et mises à jour de secrets pour [django-dsfr](/repos/numerique-gouv/django-dsfr), [dockerfiles](/repos/numerique-gouv/dockerfiles) et [francetransfert](/repos/numerique-gouv/francetransfert).

## Autres changements notables
- Migration architecturale majeure de [oots-france](/repos/numerique-gouv/oots-france) vers le framework Ruby on Rails.
- Migration vers l'API de notification v2 pour [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).
- Refonte de la couche de stockage et de la stratégie de tests pour [ami-app-ios](/repos/numerique-gouv/ami-app-ios).
- Optimisation des processus de déploiement (notamment sur Scalingo) pour [sites-faciles](/repos/numerique-gouv/sites-faciles) et [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy).
- Réorganisation structurelle du package Swift pour [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios).

## Dépôts les plus actifs
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Évolutions majeures sur la sécurité (biométrie, Passkeys) et l'architecture de stockage.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Travaux intensifs sur l'internationalisation et l'optimisation du déploiement.
- [oots-france](/repos/numerique-gouv/oots-france) : Transition vers Ruby on Rails et intégration du Design System de l'État.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Modernisation de l'API et support des nouvelles méthodes d'authentification.
