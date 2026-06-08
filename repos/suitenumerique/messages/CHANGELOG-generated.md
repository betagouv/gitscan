## Changelog : messages (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité, la performance et l'expérience utilisateur. Des corrections de bugs ont été apportées concernant l'affichage des événements récurrents, l'importation de fichiers PST, et la gestion des accès aux threads. Des fonctionnalités attendues comme la prévisualisation des pièces jointes et l'intégration CalDAV ont été ajoutées, ainsi que des améliorations de l'interface utilisateur pour la composition et l'envoi de messages.

### Évolutions fonctionnelles
- **CalDAV :** Possibilité de lier une instance CalDAV pour accepter les événements directement depuis l'interface. [#584](https://github.com/suitenumerique/messages/issues/584)
- **Pièces jointes :** Prévisualisation des pièces jointes dans l'interface utilisateur. [#676](https://github.com/suitenumerique/messages/issues/676)
- **Lien profond vers les threads :** Ajout de liens directs vers des threads spécifiques. [#664](https://github.com/suitenumerique/messages/issues/664)
- **Assignation de threads :** Possibilité d'assigner des threads à des utilisateurs. [#645](https://github.com/suitenumerique/messages/issues/645)
- **Amélioration de l'expérience d'envoi :** Optimisation du processus d'envoi de messages. [#681](https://github.com/suitenumerique/messages/issues/681)
- **Stockage des pièces jointes :** Implémentation d'un stockage en plusieurs niveaux pour les pièces jointes et refactorisation de la gestion des blobs/attachments.
- **Interface utilisateur :** Amélioration de l'interface de composition des messages.

### Évolutions techniques
- **Backend :** Utilisation de la bibliothèque `defusedxml` pour améliorer la sécurité lors du traitement de fichiers XML. [#677](https://github.com/suitenumerique/messages/issues/677)
- **Performance :** Correction d'un problème de performance lié au grand nombre de destinataires. [#672](https://github.com/suitenumerique/messages/issues/672)
- **Backend :** Évitement des requêtes N+1 dans l'interface d'administration et accélération des recherches.
- **Backend :** Suppression des champs de modèle dépréciés. [#678](https://github.com/suitenumerique/messages/issues/678)
- **Backend :** Utilisation de la bibliothèque standard Python pour la composition des e-mails.
- **Backend :** Amélioration de la logique d'importation des fichiers PST.
- **Backend :** Possibilité de supprimer les messages internes à tout moment. [#669](https://github.com/suitenumerique/messages/issues/669)
- **Backend :** Utilisation de l'adresse e-mail OIDC au lieu de l'adresse e-mail de la boîte aux lettres pour CalDAV. [#679](https://github.com/suitenumerique/messages/issues/679)
- **Backend :** Correction d'un problème de permission sur le socket Milter au démarrage. [#693](https://github.com/suitenumerique/messages/issues/693)
- **Backend :** Rapport de l'état de l'auto-vérification au Sentry. [#694](https://github.com/suitenumerique/messages/issues/694)

### Autres changements
- Mise à jour de la dépendance `django-lasuite` vers la version 0.0.26. [#689](https://github.com/suitenumerique/messages/issues/689)
- Correction de l'affichage des événements récurrents avec des exceptions. [#686](https://github.com/suitenumerique/messages/issues/686)
- Correction d'un bug empêchant le rechargement des messages d'un thread lors de la suppression d'un brouillon.
- Publication des versions 0.6.0 et 0.7.0.
