## Changelog : st-ansible (30 derniers jours, au 20 mai 2026)

### Résumé
Cette nouvelle version de st-ansible apporte l'ajout du rôle `meet`, permettant le déploiement de cette application. Des améliorations ont été apportées à la gestion des ports publiés et aux permissions des fichiers pour le rôle `podman`. De plus, la documentation de la collection a été complétée.

### Évolutions fonctionnelles
- Ajout du rôle `meet` pour le déploiement de l'application Meet [#22](https://github.com/suitenumerique/st-ansible/issues/22).
- Correction de la commande `compose` pour les workers.
- Amélioration de la configuration des ports publiés et des valeurs par défaut dans différents rôles.

### Évolutions techniques
- Refactorisation des tâches de gestion des permissions des fichiers et des répertoires pour le rôle `podman`.
- Correction du script de démarrage systemd pour les applications Podman afin d'assurer une configuration correcte des notifications.
- Rationalisation des variables et des valeurs par défaut concernant les ports publiés à travers les rôles.
- Refactorisation du déploiement de rspamd.

### Autres changements
- Ajout de la documentation complète de la collection.
- Publication de la version 0.0.17.
- Publication de la version 0.0.16.
