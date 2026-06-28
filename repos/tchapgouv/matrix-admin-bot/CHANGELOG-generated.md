## Changelog : matrix-admin-bot (30 derniers jours, au 26 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées au bot d'administration Matrix au cours du dernier mois. Les modifications se concentrent sur l'amélioration des commandes de gestion des utilisateurs, notamment le remplacement de l'adresse email et du nom d'affichage, ainsi que l'ajout de validations pour l'adresse email. Une commande obsolète a également été supprimée et une nouvelle fonctionnalité permet d'envoyer des notifications à tous les utilisateurs via le MAS (Matrix Application Services).

### Évolutions fonctionnelles
- Ajout de la validation de l'adresse email lors du remplacement d'une adresse email existante ou de l'ajout d'une nouvelle adresse. [#38](https://github.com/tchapgouv/matrix-admin-bot/issues/38)
- Implémentation d'une commande pour envoyer une notification à tous les utilisateurs du serveur Matrix, en utilisant le MAS pour récupérer la liste des utilisateurs. [#35](https://github.com/tchapgouv/matrix-admin-bot/issues/35)
- Ajout de commandes pour remplacer le nom d'affichage d'un utilisateur. [#33](https://github.com/tchapgouv/matrix-admin-bot/issues/33)
- Ajout de commandes pour remplacer l'adresse email d'un utilisateur. [#32](https://github.com/tchapgouv/matrix-admin-bot/issues/32)
- Nouvelle commande `user` implémentée. [#34](https://github.com/tchapgouv/matrix-admin-bot/issues/34)

### Évolutions techniques
- Suppression d'une commande obsolète. [#36](https://github.com/tchapgouv/matrix-admin-bot/issues/36)
- Correction d'un problème potentiel de formatage de timestamp en ajoutant une vérification `None`. [#37](https://github.com/tchapgouv/matrix-admin-bot/issues/37)
