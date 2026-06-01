## Changelog : messages (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, l'équipe a apporté des améliorations significatives à l'expérience utilisateur, notamment avec l'ajout de prévisualisation des pièces jointes et l'amélioration de la composition des messages. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et la performance, en particulier concernant le calendrier et l'importation de données. Des optimisations techniques ont été réalisées pour améliorer la gestion des pièces jointes et la performance globale.

### Évolutions fonctionnelles
- **Pièces jointes :** Ajout d'une prévisualisation des pièces jointes pour une meilleure expérience utilisateur. [#676](https://github.com/suitenumerique/messages/issues/676)
- **Calendrier :** Possibilité de lier une instance CalDAV pour accepter directement les événements. [#584](https://github.com/suitenumerique/messages/issues/584)
- **Composition de messages :** Amélioration de l'expérience de composition des messages, notamment avec l'ajout de liens profonds vers les threads. [#664](https://github.com/suitenumerique/messages/issues/664)
- **Assignation de threads :** Possibilité d'assigner des threads à des utilisateurs. [#645](https://github.com/suitenumerique/messages/issues/645)
- **Actions sur les threads :** Ajout d'actions de lecture/non-lu sur la barre d'actions des threads. [#659](https://github.com/suitenumerique/messages/issues/659)
- **Interface utilisateur :** Les sections du panneau sont maintenant redimensionnables.
- **Notifications :** Ajout de notifications de mention via `UserEvent`.

### Évolutions techniques
- **Stockage des pièces jointes :** Implémentation d'un stockage en plusieurs niveaux (tiered storage) et refactorisation de la gestion des pièces jointes et des blobs.
- **Performance :** Correction d'un problème de performance lié au grand nombre de destinataires. [#672](https://github.com/suitenumerique/messages/issues/672)
- **Optimisation de la base de données :** Éviter les requêtes N+1 dans l'administration et accélérer les recherches.
- **Refactorisation :** Suppression des champs de modèle dépréciés. [#678](https://github.com/suitenumerique/messages/issues/678)
- **Bibliothèques :** Ajout de `defusedxml` comme dépendance pour une meilleure sécurité. [#677](https://github.com/suitenumerique/messages/issues/677)
- **Email :** Retour à l'utilisation de la bibliothèque standard Python pour la composition des emails.
- **Cache :** Refactorisation de la gestion du cache des requêtes de threads. [#642](https://github.com/suitenumerique/messages/issues/642)

### Autres changements
- Correction de bugs mineurs concernant l'affichage des événements récurrents avec exceptions. [#686](https://github.com/suitenumerique/messages/issues/686)
- Correction d'un bug empêchant la suppression des brouillons de messages de déclencher une actualisation inutile.
- Utilisation de l'adresse email OIDC au lieu de l'adresse email de la boîte aux lettres pour CalDAV. [#679](https://github.com/suitenumerique/messages/issues/679)
- Correction de l'utilisation de l'identifiant `obs-id-left` dans l'en-tête `In-Reply-To`. [#1234](https://github.com/suitenumerique/messages/issues/1234)
- Suppression des messages internes à tout moment. [#669](https://github.com/suitenumerique/messages/issues/669)
- Ajout de la possibilité d'ajouter un champ TOTP obligatoire et un champ de recherche dans l'administration. [#667](https://github.com/suitenumerique/messages/issues/667)
- Correction de problèmes d'encodage UTF-8 dans l'analyse des emails. [#656](https://github.com/suitenumerique/messages/issues/656)
- Amélioration de la logique d'importation des fichiers PST.
- Correction de bugs d'affichage de l'en-tête du panneau de threads.
- Correction de problèmes de superposition de fenêtres contextuelles d'étiquettes.
- Ajout d'informations sur le délai de propagation DNS.
- Possibilité de spécifier un ID de canal pour le widget de feedback.
