## Changelog : messages (30 derniers jours, au 12 mai 2026)

### Résumé
Les dernières mises à jour de Messages se concentrent sur l'amélioration de l'expérience utilisateur, notamment en permettant le redimensionnement des panneaux, l'assignation de threads, et l'ajout de fonctionnalités de rafraîchissement et de lecture/non-lecture des messages. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Possibilité d'assigner des threads à des utilisateurs. [#2673725](https://github.com/suitenumerique/messages/issues/2673725)
- Ajout d'une confirmation visuelle (tooltip) lors du rafraîchissement de la boîte de réception. [#858e995](https://github.com/suitenumerique/messages/commit/858e995)
- Ajout des actions "Marquer comme lu/non lu" sur la barre d'actions des threads. [#659](https://github.com/suitenumerique/messages/issues/659)
- Possibilité de redimensionner les sections des panneaux de l'interface utilisateur. [#8a7cb8e](https://github.com/suitenumerique/messages/commit/8a7cb8e)
- Possibilité d'inviter des utilisateurs qui ne se sont pas encore connectés. [#644](https://github.com/suitenumerique/messages/issues/644)
- Amélioration de l'affichage des étiquettes imbriquées dans l'en-tête du panneau des threads. [#658](https://github.com/suitenumerique/messages/issues/658)

### Évolutions techniques
- Refactorisation de la gestion du cache des requêtes de threads. [#642](https://github.com/suitenumerique/messages/issues/642)
- Amélioration de la performance de la recherche en utilisant des suppressions en masse par ID au lieu de requêtes de suppression.
- Optimisation du chargement des tâches d'indexation pour améliorer la réactivité.
- Correction de problèmes de gestion des erreurs de tâches Celery pour éviter les boucles infinies.
- Correction de problèmes liés aux erreurs de transport OpenSearch.
- Amélioration de la gestion des erreurs lors de la suppression des derniers éditeurs.
- Correction de la gestion des caractères spéciaux dans les mots de passe générés pour renforcer la sécurité. [#640](https://github.com/suitenumerique/messages/issues/640)
- Correction de la gestion des erreurs liées à la sérialisation Boto3.
- Mise à jour de Keycloak vers la version 26.6.1. [#637](https://github.com/suitenumerique/messages/issues/637)
- Amélioration de la gestion des erreurs SSRF et ajout de la possibilité de rediriger dans le proxy d'images. [#631](https://github.com/suitenumerique/messages/issues/631)
- Ajout de backends d'authentification entrants configurables. [#636](https://github.com/suitenumerique/messages/issues/636)

### Autres changements
- Localisation du séparateur de pièces jointes. [#1b03e1d](https://github.com/suitenumerique/messages/commit/1b03e1d)
- Ajout d'informations sur le délai de propagation DNS. [#654](https://github.com/suitenumerique/messages/issues/654)
- Correction d'un bug empêchant l'affichage correct des commentaires internes sur les threads. [#632](https://github.com/suitenumerique/messages/issues/632)
- Correction d'un bug lié à l'empilement des popups d'étiquettes. [#635](https://github.com/suitenumerique/messages/issues/635)
- Correction d'un bug empêchant le focus sur le champ "à" lors d'un transfert.
- Correction de la logique du widget pour utiliser la dernière version. [#649](https://github.com/suitenumerique/messages/issues/649)
- Correction de la configuration des noms de processus dans Procfile. [#648](https://github.com/suitenumerique/messages/issues/648)
- Placement des importations et des files d'attente de worker de réindexation dans des conteneurs dédiés. [#643](https://github.com/suitenumerique/messages/issues/643)
- Suppression du marquage des emails "De=À" comme expéditeur. [#652](https://github.com/suitenumerique/messages/issues/652)
- Ajout de la possibilité d'utiliser un ID de canal spécifique pour le widget de feedback. [#655](https://github.com/suitenumerique/messages/issues/655)
- Forcer l'inclusion de caractères spéciaux dans les mots de passe générés.
- Correction de la gestion des cas limites d'analyse d'e-mails avec UTF8. [#656](https://github.com/suitenumerique/messages/issues/656)
- Forcer la langue par défaut. [#647](https://github.com/suitenumerique/messages/issues/647)
- Support des attributs legacy et nouveaux pour le widget. [#650](https://github.com/suitenumerique/messages/issues/650)
