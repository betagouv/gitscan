# Synthèse d'activité : numerique-gouv (du 06 mai 2026 au 29 juillet 2026)

## Résumé de l'activité
L'organisation numerique-gouv a connu une période d'activité soutenue, avec des améliorations significatives sur plusieurs de ses dépôts. Les efforts se sont concentrés sur l'internationalisation des plateformes ([sites-faciles](/repos/numerique-gouv/sites-faciles), [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1)), l'amélioration de l'expérience utilisateur (ajout de pages Tchap et Tchao sur [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage), amélioration de l'interface utilisateur de [b3desk](/repos/numerique-gouv/b3desk) et [ami-app-ios](/repos/numerique-gouv/ami-app-ios)), et le renforcement de la sécurité (corrections de vulnérabilités dans [django-dsfr](/repos/numerique-gouv/django-dsfr)). Des efforts importants ont également été déployés pour moderniser l'infrastructure et les processus de développement, notamment avec l'introduction de tests e2e dans [sites-conformes](/repos/numerique-gouv/sites-conformes) et l'amélioration du déploiement sur Scalingo ([sites-faciles](/repos/numerique-gouv/sites-faciles)).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction d'une vulnérabilité dans la dépendance `cryptography` dans [django-dsfr](/repos/numerique-gouv/django-dsfr).
- Mise à jour de secret dans [francetransfert](/repos/numerique-gouv/francetransfert).

## Autres changements notables
- Refonte du modèle de données dans [statistiques-impact](/repos/numerique-gouv/statistiques-impact) avec l'introduction de "Record".
- Migration vers Python 3.14 dans [statistiques-impact](/repos/numerique-gouv/statistiques-impact).
- Ajout de la redirection vers la page de déconnexion FranceConnect dans [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy).
- Introduction de tests end-to-end avec Playwright dans [sites-conformes](/repos/numerique-gouv/sites-conformes).

## Dépôts les plus actifs
- [statistiques-impact](/repos/numerique-gouv/statistiques-impact) : Refonte du modèle de données et migration vers Python 3.14.
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Internationalisation et simplification du déploiement.
- [sites-conformes](/repos/numerique-gouv/sites-conformes) : Introduction de tests e2e et amélioration de l'interface utilisateur.
- [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage) : Ajout de pages pour Tchap et Tchao, et mises à jour des webinaires.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Ajout de la section "Services" et renommage des sections "Requests" et "Inventory".
