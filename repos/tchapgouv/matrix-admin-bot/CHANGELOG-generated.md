## Changelog : matrix-admin-bot (30 derniers jours, au 26 juin 2026)

### Résumé
Cette mise à jour apporte des améliorations à la gestion des utilisateurs et des notifications sur le serveur Matrix. Les modifications incluent la suppression d'une commande obsolète, l'ajout d'une commande pour gérer les utilisateurs, la possibilité d'envoyer des notifications à tous les utilisateurs via MAS, et des corrections concernant l'affichage du nom et de l'adresse email des utilisateurs.

### Évolutions fonctionnelles
- Ajout d'une commande `user` pour gérer les utilisateurs. [#34](https://github.com/tchapgouv/matrix-admin-bot/issues/34)
- Possibilité d'envoyer une notification à tous les utilisateurs du serveur via la fonction "Server Notice" en utilisant MAS (Matrix Application Services) pour récupérer la liste des utilisateurs. [#35](https://github.com/tchapgouv/matrix-admin-bot/issues/35)
- Correction de l'affichage du nom d'utilisateur (displayname). [#33](https://github.com/tchapgouv/matrix-admin-bot/issues/33)
- Correction de l'affichage de l'adresse email des utilisateurs. [#32](https://github.com/tchapgouv/matrix-admin-bot/issues/32)

### Évolutions techniques
- Suppression d'une commande legacy. [#36](https://github.com/tchapgouv/matrix-admin-bot/issues/36)
- Ajout d'une vérification pour éviter les erreurs lors du formatage des timestamps. [#37](https://github.com/tchapgouv/matrix-admin-bot/issues/37)
