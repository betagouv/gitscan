## Changelog : messages (30 derniers jours, au 12 mai 2026)

### Résumé
Les dernières mises à jour de Messages se concentrent sur l'amélioration de l'expérience utilisateur, notamment en permettant le redimensionnement des panneaux, l'assignation de threads, et en corrigeant des bugs liés à l'affichage et au traitement des messages. Des améliorations techniques ont également été apportées pour optimiser la recherche, la gestion des index et la sécurité.

### Évolutions fonctionnelles
- Possibilité d'assigner des threads à des utilisateurs [#659].
- Amélioration de l'interface utilisateur : les sections des panneaux sont désormais redimensionnables.
- Indication visuelle pour confirmer le rafraîchissement de la boîte de réception.
- Possibilité d'inviter des utilisateurs qui ne se sont pas encore connectés [#644].
- Ajout d'une action pour marquer les threads comme lus/non lus.
- Amélioration de l'affichage des étiquettes imbriquées dans l'en-tête du panneau des threads [#658].
- Possibilité d'utiliser un ID de canal spécifique pour le widget de feedback.
- Information sur le délai de propagation DNS ajoutée à l'interface utilisateur [#654].
- Permettre aux spectateurs de threads de poster des commentaires internes [#652].
- Ajout de la possibilité d'assigner des étiquettes avec l'archivage et le widget d'étiquettes en masse.

### Évolutions techniques
- Refactorisation de la gestion du cache des requêtes de threads [#642].
- Optimisation de la recherche et de la réindexation : remplacement de `delete_by_query` par une suppression en masse par ID, gestion des erreurs de transport OpenSearch et report des tâches d'indexation.
- Amélioration du payload en masse pour la recherche [#659].
- Correction de problèmes de race condition dans la suppression du dernier éditeur.
- Mise à jour de la logique du widget pour utiliser la dernière version [#649].
- Correction de la configuration des noms de processus dans Procfile pour le déploiement.
- Placement des imports et des files d'attente de worker de réindexation dans des conteneurs dédiés [#643].
- Correction de la gestion des erreurs de tâches Celery non sérialisables et arrêt du polling infini [#633].
- Correction de la gestion des caractères spéciaux dans les mots de passe générés [#640].
- Amélioration de la gestion des erreurs lors de l'analyse des e-mails avec UTF-8 [#656].
- Mise à jour de Keycloak vers la version 26.6.1 [#637].
- Amélioration de la sécurité : factorisation du code SSRF et autorisation des redirections dans le proxy d'image [#631].
- Ajout de backends d'authentification inbound configurables [#636].

### Autres changements
- Localisation du séparateur de pièces jointes.
- Correction de l'initialisation de l'entrée d'événement de thread lors de l'ouverture.
- Correction de l'affichage des popups d'étiquettes avec le modal de création d'étiquette [#635].
- Correction d'un bug empêchant l'utilisation de tous les droits d'édition sur les mutations de thread.
- Alignement du bouton d'envoi sur la gauche.
- Amélioration du format de date de l'événement de thread.
- Mise à jour des dépendances Cunningham et ui-kit.
- Application forcée de la langue par défaut [#647].
- Correction d'un bug empêchant l'affichage correct des étiquettes imbriquées [#658].
- Correction de la gestion des erreurs de tâches Celery non sérialisables et arrêt du polling infini [#633].
- Ajout de logs pour le proxy SOCKS dans la livraison sortante [#626].
- Désactivation du menu d'application lorsque aucune option n'est disponible.
- Correction d'un bug lié à l'affichage des popups d'étiquettes avec le modal de création d'étiquette [#635].
