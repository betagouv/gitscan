## Changelog : matrix-admin-bot (30 derniers jours, au 01 août 2026)

### Résumé
Ce bot d'administration Matrix a reçu plusieurs améliorations concernant la gestion des utilisateurs et l'envoi de notifications. Les nouvelles fonctionnalités permettent d'obtenir des rapports utilisateurs plus complets, de remplacer l'adresse email et le nom d'affichage des utilisateurs, et d'envoyer des notifications à tous les utilisateurs du serveur. Des corrections ont également été apportées pour éviter l'exécution multiple de certaines étapes de commande et améliorer la validation des adresses email.

### Évolutions fonctionnelles
- Ajout d'une commande `user` pour afficher des informations détaillées sur les utilisateurs, incluant maintenant le mot de passe (masqué) [#34](https://github.com/tchapgouv/matrix-admin-bot/issues/34).
- Amélioration du rapport utilisateur avec un réordonnancement des informations affichées [#41](https://github.com/tchapgouv/matrix-admin-bot/issues/41).
- Possibilité de remplacer l'adresse email d'un utilisateur [#32](https://github.com/tchapgouv/matrix-admin-bot/issues/32).
- Possibilité de remplacer le nom d'affichage d'un utilisateur [#33](https://github.com/tchapgouv/matrix-admin-bot/issues/33).
- Implémentation de l'envoi de notifications à tous les utilisateurs du serveur via l'API MAS (Matrix Application Services) [#35](https://github.com/tchapgouv/matrix-admin-bot/issues/35).
- Amélioration de la performance de l'envoi de notifications serveur en utilisant le multithreading [#39](https://github.com/tchapgouv/matrix-admin-bot/issues/39).
- Ajout de validations pour l'adresse email lors du remplacement ou de l'ajout d'une adresse email [#38](https://github.com/tchapgouv/matrix-admin-bot/issues/38).

### Évolutions techniques
- Correction d'un problème empêchant l'exécution multiple d'une étape de commande [#40](https://github.com/tchapgouv/matrix-admin-bot/issues/40).
- Suppression d'une commande obsolète [#36](https://github.com/tchapgouv/matrix-admin-bot/issues/36).
- Amélioration de la gestion des timestamps avec une vérification de la valeur `None` [#37](https://github.com/tchapgouv/matrix-admin-bot/issues/37).
