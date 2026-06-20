# Synthèse d'activité : numerique-gouv (du 2026-05-10 au 2026-06-15)

## Résumé de l'activité
L'activité récente de l'organisation numerique-gouv se concentre sur l'amélioration de l'expérience utilisateur et la robustesse de ses différentes plateformes. Plusieurs projets ont bénéficié d'améliorations en matière d'internationalisation, notamment [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1), avec l'ajout de la gestion de plusieurs langues et de sélecteurs de langue.  Des efforts importants ont également été déployés pour renforcer la sécurité, avec l'intégration de Sentry dans [sites-conformes](/repos/numerique-gouv/sites-conformes) et la correction de vulnérabilités potentielles dans [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy). Enfin, des améliorations significatives ont été apportées à l'application mobile Ami, notamment pour l'affichage des bannières d'information ([ami-app-ios](/repos/numerique-gouv/ami-app-ios)) et la configuration générale ([ami-app-android](/repos/numerique-gouv/ami-app-android)).

## Sécurité
- Correction d'une potentielle vulnérabilité d'intégrité lors de la déconnexion dans [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy).

## Autres changements notables
- Intégration de Sentry pour la surveillance des erreurs dans [sites-conformes](/repos/numerique-gouv/sites-conformes).
- Mise en place d'un déploiement en un clic sur Scalingo pour [sites-faciles](/repos/numerique-gouv/sites-faciles).
- Refonte du packaging et de la configuration Docker pour [sites-conformes](/repos/numerique-gouv/sites-conformes).
- Ajout de la possibilité de stocker les médias en PostgreSQL dans [sites-conformes](/repos/numerique-gouv/sites-conformes).
- Refactoring de la structure du projet [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios) avec un sous-dossier "DesignSystem".

## Dépôts les plus actifs
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Amélioration de l'internationalisation et simplification du déploiement.
- [sites-conformes](/repos/numerique-gouv/sites-conformes) : Renforcement de la sécurité et amélioration de la configuration.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Ajout de l'archivage des éléments de suivi et intégration de FranceConnect.
- [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios) : Ajout de nouveaux composants et refactoring de la structure du projet.
- [b3desk](/repos/numerique-gouv/b3desk) : Amélioration de la gestion des réunions et automatisation de la publication des releases.
