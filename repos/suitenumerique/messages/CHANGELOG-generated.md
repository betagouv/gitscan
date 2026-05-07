## Changelog : messages (30 derniers jours, au 6 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la performance, la stabilité et l'expérience utilisateur. Des corrections de bugs ont été apportées concernant l'affichage des en-têtes de threads, le parsing d'emails UTF-8, et la gestion des erreurs de tâches Celery. De nouvelles fonctionnalités incluent l'invitation d'utilisateurs non-inscrits, l'assignation de threads et des améliorations de la sécurité.

### Évolutions fonctionnelles
- Possibilité d'inviter des utilisateurs qui ne se sont pas encore connectés [#644](https://github.com/suitenumerique/messages/issues/644).
- Ajout de la possibilité d'assigner des threads à des utilisateurs [#622](https://github.com/suitenumerique/messages/issues/622).
- Amélioration de l'affichage des en-têtes de threads imbriqués [#658](https://github.com/suitenumerique/messages/issues/658).
- Ajout de notifications pour les mentions d'utilisateurs [#621](https://github.com/suitenumerique/messages/issues/621).
- Possibilité de voir et de poster des commentaires internes sur les threads [#632](https://github.com/suitenumerique/messages/issues/632).
- Ajout d'un indicateur de délai de propagation DNS [#654](https://github.com/suitenumerique/messages/issues/654).

### Évolutions techniques
- Optimisation de la gestion du cache des requêtes de threads sur le frontend [#642](https://github.com/suitenumerique/messages/issues/642).
- Amélioration de la performance de la réindexation de la recherche, avec suppression par ID en masse et gestion des erreurs transport OpenSearch [#643](https://github.com/suitenumerique/messages/issues/643).
- Refonte de la gestion des tâches asynchrones pour éviter les boucles infinies [#633](https://github.com/suitenumerique/messages/issues/633).
- Amélioration de la sécurité en empêchant le marquage incorrect des emails "De=À" comme étant envoyés par l'utilisateur [#652](https://github.com/suitenumerique/messages/issues/652).
- Renforcement de la sécurité en forçant l'inclusion de caractères spéciaux dans les mots de passe générés [#640](https://github.com/suitenumerique/messages/issues/640).
- Mise à jour de Keycloak vers la version 26.6.1 [#637](https://github.com/suitenumerique/messages/issues/637).
- Amélioration de la gestion des erreurs lors du parsing des emails avec des caractères UTF-8 [#656](https://github.com/suitenumerique/messages/issues/656).
- Amélioration de la configuration des backends d'authentification pour les emails entrants [#636](https://github.com/suitenumerique/messages/issues/636).
- Amélioration de la gestion des processus dans l'environnement PaaS [#648](https://github.com/suitenumerique/messages/issues/648).

### Autres changements
- Correction d'un bug lié à l'affichage des popups de labels [#635](https://github.com/suitenumerique/messages/issues/635).
- Correction d'un bug dans le focus du champ "à" lors du transfert d'un email [#632](https://github.com/suitenumerique/messages/issues/632).
- Correction d'un bug lié à l'initialisation de l'entrée d'événements de thread [#649](https://github.com/suitenumerique/messages/issues/649).
- Correction d'un bug lié à l'affichage du bouton d'envoi [#649](https://github.com/suitenumerique/messages/issues/649).
- Amélioration du format de la date des événements de thread [#649](https://github.com/suitenumerique/messages/issues/649).
- Ajout d'une information sur le délai de propagation DNS sur le frontend [#654](https://github.com/suitenumerique/messages/issues/654).
- Correction d'un bug lié à la réindexation à partir d'une date spécifique.
- Suppression d'une réversion de la fonctionnalité d'assignation de threads.
