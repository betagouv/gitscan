# Synthèse d'activité : numerique-gouv (du 15 avril 2026 au 23 avril 2026)

## Résumé de l'activité
L'activité récente de l'organisation numerique-gouv s'est concentrée sur l'amélioration de l'expérience utilisateur et la sécurité de ses différentes plateformes. Plusieurs dépôts ont bénéficié d'améliorations d'accessibilité, d'internationalisation et de correction de bugs. Des efforts importants ont également été déployés pour renforcer la sécurité, notamment sur [francetransfert](/repos/numerique-gouv/francetransfert) avec la restriction des types de fichiers autorisés. L'application _La Suite_ ([lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage)) a vu l'ajout de la sélection de créneau pour la prise de rendez-vous et la correction d'un bug sur le formulaire de contact. Les applications mobiles [ami-app-ios](/repos/numerique-gouv/ami-app-ios) et [ami-app-android](/repos/numerique-gouv/ami-app-android) ont bénéficié d'améliorations de l'interface et de la gestion de l'authentification.

## Sécurité
- [francetransfert](/repos/numerique-gouv/francetransfert) : Restriction des types de fichiers autorisés (HTML et HTM) pour renforcer la sécurité.
- [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage) : Mise à jour de Next.js incluant une correction de sécurité.
- [django-dsfr](/repos/numerique-gouv/django-dsfr) : Mises à jour de plusieurs dépendances pour bénéficier des dernières corrections de sécurité.
- [ami-app-android](/repos/numerique-gouv/ami-app-android) : Contournement de la vérification SSL en mode DEBUG (uniquement pour le développement).

## Autres changements notables
- [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1) : Internationalisation des plateformes avec gestion de plusieurs langues.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Migration des variables d'environnement vers un fichier de configuration pour une meilleure gestion et sécurité.
- [django-dsfr](/repos/numerique-gouv/django-dsfr) : Mise à jour du système de design DSFR vers la version 1.14.4.

## Dépôts les plus actifs
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Ajout de la gestion de plusieurs langues et déploiement en un clic sur Scalingo.
- [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1) : Internationalisation et optimisations de performance.
- [b3desk](/repos/numerique-gouv/b3desk) : Implémentation de la délégation de réunions et corrections de bugs.
- [ami-app-android](/repos/numerique-gouv/ami-app-android) : Amélioration de l'expérience utilisateur avec le rafraîchissement par glissement et l'intégration de la DSFR.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Ajout de la gestion des agents et des rôles, intégration de l'agenda et amélioration des notifications.
