# Synthèse d'activité : numerique-gouv (du 06 mai 2026 au 21 mai 2026)

## Résumé de l'activité
L'activité récente de l'organisation numerique-gouv s'est concentrée sur l'amélioration de l'expérience utilisateur et de la robustesse de ses différentes plateformes. Plusieurs dépôts ont bénéficié d'améliorations d'internationalisation, notamment [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-conformes](/repos/numerique-gouv/sites-conformes), permettant une meilleure adaptation aux différents contextes linguistiques. Des efforts importants ont également été déployés pour simplifier les déploiements (Scalingo) et améliorer la sécurité, avec des mises à jour de dépendances et des corrections de vulnérabilités. L'application Ami, tant sur iOS ([ami-app-ios](/repos/numerique-gouv/ami-app-ios)) que sur Android ([ami-app-android](/repos/numerique-gouv/ami-app-android)), a reçu des améliorations d'interface et de navigation.

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de dépendances visant à corriger des vulnérabilités :
- [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage) a mis à jour PostCSS et Next.js.
- [django-dsfr](/repos/numerique-gouv/django-dsfr) a mis à jour plusieurs dépendances, dont `lxml`, Django, `urllib3`, `idna` et `pymdown-extensions`.
- [b3desk](/repos/numerique-gouv/b3desk) a mis à jour plusieurs dépendances.
- [action-trivy-cache](/repos/numerique-gouv/action-trivy-cache) a mis à jour les actions utilisées pour une meilleure sécurité.
- [ami-app-android](/repos/numerique-gouv/ami-app-android) a bénéficié de mises à jour de dépendances.

## Autres changements notables
- [francetransfert](/repos/numerique-gouv/francetransfert) a ajusté la configuration du déploiement pour améliorer la stabilité et la réactivité.
- [sites-conformes](/repos/numerique-gouv/sites-conformes) a ajouté la possibilité de stocker les médias directement dans PostgreSQL.
- [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy) a amélioré la gestion des appels à l'API FranceConnect et simplifié l'intégration sur Scalingo.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) a refactoré la commande de réplication des données et ajouté l'authentification des requêtes vers l'API Github via FranceConnect.
- [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios) a adopté la couleur d'accent par défaut du DSFR et refactoré la structure du projet.

## Dépôts les plus actifs
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Amélioration de l'internationalisation et simplification du déploiement.
- [sites-conformes](/repos/numerique-gouv/sites-conformes) : Ajout de nouvelles fonctionnalités et amélioration de la flexibilité de la plateforme.
- [ami-app-ios](/repos/numerique-gouv/ami-app-ios) : Amélioration de la navigation et correction de bugs d'interface.
- [ami-fc-proxy](/repos/numerique-gouv/ami-fc-proxy) : Amélioration de l'intégration avec FranceConnect et simplification du déploiement.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Refonte de la réplication des données et ajout de l'authentification via FranceConnect.
