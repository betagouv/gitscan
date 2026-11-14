# Synthèse d'activité : numerique-gouv (du 28/10 au 04/11)

## Résumé de l'activité
Cette période est marquée par une transformation majeure de l'offre avec le rebranding de la suite de création de sites en "Sites Conformes" ([sites-conformes-saas](/repos/numerique-gouv/sites-conformes-saas)) et une refonte architecturale profonde du projet OOTS vers Ruby on Rails ([oots-france](/repos/numerique-gouv/oots-france)).

Parallèlement, l'expérience utilisateur et la fiabilité des services de messagerie et mobiles ont été considérablement renforcées ([messages](/repos/numerique-gouv/messages), [ami-app-ios](/repos/numerique-gouv/ami-app-ios), [ami-app-android](/repos/numerique-gouv/ami-app-android)), notamment grâce à l'introduction de nouvelles fonctionnalités comme le mode hors-ligne, la gestion automatisée du stockage ou le support des Passkeys. Les efforts d'internationalisation se sont également intensifiés sur les outils de création de sites ([sites-faciles](/repos/numerique-gouv/sites-faciles), [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1)).

## Sécurité
- Renforcement de la confidentialité avec le chiffrement des aperçus de notifications push ([messages](/repos/numerique-gouv/messages)).
- Amélioration de la protection des données sensibles, incluant la suppression du logging des clés API et des jetons ([b3desk](/repos/numerique-gouv/b3desk)) et la protection contre les fuites de secrets ([sites-conformes](/repos/numerique-gouv/sites-conformes)).
- Durcissement des politiques de sécurité (CSP, cookies, whitelist IP) ([ami-notifications-api](/repos/numerique-gouv/ami-notifications-api), [francetransfert](/repos/numerique-gouv/francetransfert)).
- Mise à jour de dépendances critiques pour corriger des vulnérabilités ([django-dsfr](/repos/numerique-gouv/django-dsfr)).
- Introduction d'une authentification moderne et sécurisée via les Passkeys ([ami-app-android](/repos/numerique-gouv/ami-app-android)).

## Autres changements notables
- Migration technologique majeure de l'application OOTS vers le framework Ruby on Rails ([oots-france](/repos/numerique-gouv/oots-france)).
- Refonte structurelle profonde du composant WebView pour améliorer la stabilité des applications mobiles ([ami-app-ios](/repos/numerique-gouv/ami-app-ios)).
- Modernisation de la chaîne de tests système avec la migration vers WebdriverIO 10 et une nouvelle architecture de Page Objects ([ami-system-tests](/repos/numerique-gouv/ami-system-tests)).

## Dépôts les plus actifs
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Travaux importants sur l'internationalisation et l'interface d'administration.
- [messages](/repos/numerique-gouv/messages) : Évolutions sur la gestion du stockage, l'UX mobile et la sécurité.
- [oots-france](/repos/numerique-gouv/oots-france) : Réécriture complète de l'architecture et modernisation de l'interface (DSFR).
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Refonte technique majeure et ajout de fonctionnalités de résilience (mode hors-ligne).
- [ami-app-android](/repos/numerique-gouv/ami-app-android) : Améliorations de la sécurité (Passkeys) et de l'automatisation du build.
- [b3desk](/repos/numerique-gouv/b3desk) : Avancées sur les fonctionnalités du Backoffice et la sécurisation des données.
- [sites-conformes](/repos/numerique-gouv/sites-conformes) : Améliorations de l'accessibilité et de la gestion SEO/Performance.
