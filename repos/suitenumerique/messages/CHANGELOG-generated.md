## Changelog : messages (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité, la performance et l'expérience utilisateur. Des corrections de bugs ont été apportées concernant l'affichage des événements récurrents, l'importation de PST, et la gestion des accès aux threads. De nouvelles fonctionnalités ont été ajoutées, notamment la prévisualisation des pièces jointes, l'intégration CalDAV pour l'acceptation directe des événements, et l'amélioration de l'expérience d'envoi de messages. Des optimisations de performance ont également été réalisées, notamment pour les recherches avec un grand nombre de destinataires.

### Évolutions fonctionnelles
- **Pièces jointes :** Ajout de la prévisualisation des pièces jointes [#676](https://github.com/suitenumerique/messages/issues/676).
- **Calendrier :** Possibilité de lier une instance CalDAV pour accepter directement les événements [#584](https://github.com/suitenumerique/messages/issues/584).
- **Envoi de messages :** Amélioration de l'expérience d'envoi de messages [#681](https://github.com/suitenumerique/messages/issues/681).
- **Assignation de threads :** Ajout de la possibilité d'assigner un thread [#645](https://github.com/suitenumerique/messages/issues/645).
- **Liens profonds :** Ajout de liens profonds vers les threads [#664](https://github.com/suitenumerique/messages/issues/664).
- **Actions sur les threads :** Ajout d'actions "lu/non lu" sur la barre d'actions des threads [#659](https://github.com/suitenumerique/messages/issues/659).

### Évolutions techniques
- **Backend :** Retour à la bibliothèque standard Python pour la composition des emails.
- **Performance :** Correction d'un problème de performance lié au grand nombre de destinataires [#672](https://github.com/suitenumerique/messages/issues/672).
- **Optimisation :** Éviter les requêtes N+1 dans l'administration et accélérer les recherches.
- **Architecture :** Implémentation d'un stockage en plusieurs niveaux (tiered storage) et refactorisation des blobs/attachments.
- **Sécurité :** Ajout de champs TOTP obligatoires et d'un champ de recherche dans l'administration.
- **Dépendances :** Mise à jour de `django-lasuite` vers la version 0.0.26 [#689](https://github.com/suitenumerique/messages/issues/689).
- **Milter :** Correction d'une condition de concurrence concernant les permissions du socket Milter au démarrage [#693](https://github.com/suitenumerique/messages/issues/693).
- **Selfcheck :** Rapport de l'état du selfcheck à Sentry [#694](https://github.com/suitenumerique/messages/issues/694).

### Autres changements
- **Documentation :** Suppression des champs de modèle dépréciés.
- **Développement :** Ajout de `defusedxml` comme dépendance [#677](https://github.com/suitenumerique/messages/issues/677).
- **Frontend :** Amélioration de l'interface utilisateur, notamment pour la composition des messages et la gestion des panneaux.
- **Correction :** Correction de l'affichage des événements récurrents avec exceptions [#686](https://github.com/suitenumerique/messages/issues/686).
- **CalDAV :** Utilisation de l'email OIDC au lieu de l'email de la boîte aux lettres [#679](https://github.com/suitenumerique/messages/issues/679).
