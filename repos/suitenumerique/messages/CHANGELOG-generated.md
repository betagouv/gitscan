## Changelog : messages (30 derniers jours, au 7 mai 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à l'expérience utilisateur, notamment la possibilité de marquer les threads comme lus/non lus, d'assigner des threads, et d'inviter des utilisateurs qui ne se sont pas encore connectés. Des corrections de bugs et des optimisations techniques ont également été implémentées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité de marquer un thread comme lu ou non lu via la barre d'actions du thread [#659](https://github.com/suitenumerique/messages/issues/659).
- Possibilité d'assigner un thread à un utilisateur [#644](https://github.com/suitenumerique/messages/issues/644).
- Permet d'inviter des utilisateurs qui ne se sont pas encore connectés [#644](https://github.com/suitenumerique/messages/issues/644).
- Amélioration de l'affichage de l'en-tête du panneau de thread pour les labels imbriqués [#658](https://github.com/suitenumerique/messages/issues/658).
- Ajout d'informations sur le délai de propagation DNS [#654](https://github.com/suitenumerique/messages/issues/654).
- Possibilité d'utiliser un ID de canal spécifique pour le widget de feedback de la page d'accueil [#655](https://github.com/suitenumerique/messages/issues/655).
- Ajout de notifications de mention via UserEvent [#621](https://github.com/suitenumerique/messages/issues/621).
- Ajout de la possibilité pour les spectateurs de thread de poster des commentaires internes [#632](https://github.com/suitenumerique/messages/issues/632).

### Évolutions techniques
- Refactorisation de la gestion du cache des requêtes de thread côté frontend [#642](https://github.com/suitenumerique/messages/issues/642).
- Correction de cas limites dans l'analyse des emails avec UTF8 (flanker) [#656](https://github.com/suitenumerique/messages/issues/656).
- Arrêt du marquage des emails "De=À" comme étant envoyés par l'expéditeur [#652](https://github.com/suitenumerique/messages/issues/652).
- Amélioration de la performance de la réindexation de la recherche en utilisant des requêtes en masse et en différant les tâches d'indexation [#648](https://github.com/suitenumerique/messages/issues/643), [#647](https://github.com/suitenumerique/messages/issues/647), [#649](https://github.com/suitenumerique/messages/issues/649).
- Correction de conditions de course dans la suppression du dernier éditeur [#633](https://github.com/suitenumerique/messages/issues/633), [#635](https://github.com/suitenumerique/messages/issues/635).
- Amélioration de la gestion des erreurs des tâches Celery et arrêt du polling infini [#633](https://github.com/suitenumerique/messages/issues/633).
- Mise à jour de Keycloak vers la version 26.6.1 [#637](https://github.com/suitenumerique/messages/issues/637).
- Amélioration de la sécurité avec la factorisation du code SSRF et l'autorisation des redirections dans le proxy d'image [#631](https://github.com/suitenumerique/messages/issues/631).
- Ajout de backends d'authentification entrants configurables [#636](https://github.com/suitenumerique/messages/issues/636).
- Correction de la gestion des caractères spéciaux dans la génération des mots de passe [#640](https://github.com/suitenumerique/messages/issues/640).

### Autres changements
- Correction de la réinitialisation de l'entrée de l'événement de thread à l'ouverture [#650](https://github.com/suitenumerique/messages/issues/650).
- Correction de l'empilement des popups de labels avec le modal de création de label [#650](https://github.com/suitenumerique/messages/issues/650).
- Correction d'un bug lié à l'utilisation de `boto3` dans les tests [#646](https://github.com/suitenumerique/messages/issues/646).
- Mise à jour des dépendances cunningham et ui-kit [#645](https://github.com/suitenumerique/messages/issues/645).
- Correction de l'application des droits d'édition complets sur les mutations de thread [#645](https://github.com/suitenumerique/messages/issues/645).
- Amélioration du format de la date de l'événement de thread [#645](https://github.com/suitenumerique/messages/issues/645).
- Correction de la configuration des noms de processus dans le Procfile [#648](https://github.com/suitenumerique/messages/issues/648).
- Ajout de la possibilité de réindexer à partir d'une date [#644](https://github.com/suitenumerique/messages/issues/644).
- Suppression de l'implémentation de la fonctionnalité d'assignation de thread (révert) [#644](https://github.com/suitenumerique/messages/issues/644).
