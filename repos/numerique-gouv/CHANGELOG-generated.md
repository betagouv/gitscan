# Synthèse d'activité : numerique-gouv (du 23 avril 2026 au 16 mai 2026)

## Résumé de l'activité
L'activité de l'organisation numerique-gouv au cours des dernières semaines a été marquée par des améliorations significatives sur plusieurs de ses projets, notamment en termes d'internationalisation (sites-faciles, sites-faciles-fork-1, sites-conformes), de sécurité (francetransfert, ami-fc-proxy, ami-app-ios, action-trivy-cache) et d'expérience utilisateur (b3desk, ami-app-ios, ami-app-android, lasuite-landingpage).  Des efforts ont également été déployés pour simplifier le déploiement et la maintenance des applications, avec l'intégration de Scalingo pour plusieurs projets (sites-faciles, sites-conformes, ami-fc-proxy). L'accent est mis sur l'amélioration de la robustesse et de la flexibilité des outils mis à disposition.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- [francetransfert](/repos/numerique-gouv/francetransfert) : Restriction des types de fichiers autorisés pour prévenir des vulnérabilités potentielles.
- [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy) : Stockage de l'origine de la requête pour renforcer la sécurité lors de l'autorisation.
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Corrections et mises à jour pour maintenir la sécurité de l'application.
- [action-trivy-cache](/repos/numerique-gouv/action-trivy-cache) : Mise à jour des actions utilisées pour garantir la fiabilité de l'analyse de vulnérabilités.
- [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage) : Mise à jour de Next.js et PostCSS pour corriger des failles de sécurité.

## Autres changements notables
- [sites-conformes](/repos/numerique-gouv/sites-conformes) : Ajout d'une alternative de stockage des médias en PostgreSQL.
- [b3desk](/repos/numerique-gouv/b3desk) : Refonte de la gestion de la délégation de réunions et intégration de tests associés.
- [ami-app-android](/repos/numerique-gouv/ami-app-android) : Ajout d'un mécanisme de rafraîchissement par glissement vers le bas.
- [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios) : Refactorisation de la structure du projet et ajout de nouveaux composants.
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Refonte de la navigation avec `NavigationStack` et introduction de `AppState`.
- [django-dsfr](/repos/numerique-gouv/django-dsfr) : Ajout de la possibilité de personnaliser la taille du texte dans les composants de citation.

## Dépôts les plus actifs
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Amélioration de l'internationalisation et simplification du déploiement.
- [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1) : Internationalisation et optimisations de performance.
- [sites-conformes](/repos/numerique-gouv/sites-conformes) : Amélioration de la flexibilité et ajout de nouvelles fonctionnalités de stockage.
- [b3desk](/repos/numerique-gouv/b3desk) : Amélioration de la gestion de la délégation de réunions et corrections de bugs.
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Amélioration de la navigation et de l'expérience utilisateur.
- [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy) : Amélioration du support de Scalingo et renforcement de la sécurité.
- [django-dsfr](/repos/numerique-gouv/django-dsfr) : Amélioration de la personnalisation des composants et préparation d'une nouvelle release.
