## Changelog : messages (30 derniers jours, au 28 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment une prévisualisation des pièces jointes, un lien direct vers les événements CalDAV, et des améliorations de la composition des messages. Des corrections de bugs et des optimisations de performance ont également été apportées, notamment concernant la gestion des pièces jointes volumineuses et l'indexation.  Plusieurs améliorations de sécurité ont été implémentées.

### Évolutions fonctionnelles
- **Pièces jointes :** Ajout d'une prévisualisation des pièces jointes. [#676](https://github.com/suitenumerique/messages/issues/676)
- **CalDAV :** Possibilité de lier une instance CalDAV pour accepter les événements directement depuis l'interface. [#584](https://github.com/suitenumerique/messages/issues/584)
- **Composition de messages :** Amélioration de l'expérience de composition des messages. [#681](https://github.com/suitenumerique/messages/issues/681)
- **Assignation de threads :** Possibilité d'assigner un thread à un utilisateur. [#645](https://github.com/suitenumerique/messages/issues/645)
- **Invitations :** Possibilité d'inviter des utilisateurs qui ne se sont pas encore connectés. [#644](https://github.com/suitenumerique/messages/issues/644)
- **Liens profonds :** Ajout de liens directs vers des threads spécifiques. [#664](https://github.com/suitenumerique/messages/issues/664)
- **Stockage des pièces jointes :** Mise en place d'un stockage des pièces jointes en plusieurs niveaux.
- **Authentification :** Ajout d'un champ TOTP obligatoire et d'un champ de recherche dans l'interface d'administration. [#667](https://github.com/suitenumerique/messages/issues/667)

### Évolutions techniques
- **Backend :** Suppression des champs de modèle dépréciés. [#678](https://github.com/suitenumerique/messages/issues/678)
- **Backend :** Ajout de la bibliothèque `defusedxml` comme dépendance pour améliorer la sécurité. [#677](https://github.com/suitenumerique/messages/issues/677)
- **Backend :** Amélioration de la logique d'importation des fichiers PST.
- **Backend :** Optimisation de la suppression des données dans OpenSearch, en utilisant une suppression en masse par ID.
- **Backend :** Gestion améliorée des erreurs de transport OpenSearch.
- **Backend :** Autorisation de la suppression des messages internes à tout moment. [#669](https://github.com/suitenumerique/messages/issues/669)
- **Backend :** Préservation de l'identifiant `obs-id-left` dans l'en-tête `In-Reply-To`. [#1234](https://github.com/suitenumerique/messages/issues/1234)
- **Backend :** Correction d'un problème de performance lié au grand nombre de destinataires. [#672](https://github.com/suitenumerique/messages/issues/672)
- **Backend :** Optimisation des requêtes dans l'interface d'administration pour éviter les requêtes N+1.
- **Frontend :** Refonte de la gestion du cache des requêtes de threads.
- **Frontend :** Amélioration de la réactivité de l'interface utilisateur.
- **Frontend :** Correction d'un bug empêchant le déchargement correct de la vue des threads.
- **Frontend :** Localisation du séparateur de pièces jointes.
- **Paas :** Correction des noms des processus dans le fichier Procfile.
- **Paas :** Déplacement des tâches d'importation et des files d'attente de worker vers des conteneurs dédiés. [#643](https://github.com/suitenumerique/messages/issues/643)

### Autres changements
- **Sécurité :** Empêche le marquage des emails avec `From=To` comme expéditeurs. [#652](https://github.com/suitenumerique/messages/issues/652)
- **Sécurité :** Force l'inclusion de caractères spéciaux dans les mots de passe générés. [#640](https://github.com/suitenumerique/messages/issues/640)
- **Documentation :** Ajout d'informations sur le délai de propagation DNS. [#654](https://github.com/suitenumerique/messages/issues/654)
- **Divers :** Mise à jour de la bibliothèque Keycloak vers la version 26.6.1. [#637](https://github.com/suitenumerique/messages/issues/637)
