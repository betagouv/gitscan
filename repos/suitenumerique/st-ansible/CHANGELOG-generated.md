## Changelog : st-ansible (30 derniers jours, au 29 mai 2026)

### Résumé
Cette nouvelle version de st-ansible apporte l'ajout d'un nouveau rôle pour l'application Meet, des corrections pour le déploiement de Keycloak en cluster et des améliorations concernant la gestion des ports publiés et des permissions des fichiers pour les applications Podman. La documentation de la collection a également été complétée.

### Évolutions fonctionnelles
- Ajout du rôle `meet` pour le déploiement de l'application Meet. [#PR non disponible]
- Correction du script de démarrage systemd pour les applications Podman, améliorant la gestion des notifications. [#PR non disponible]
- Correction de la commande `compose` pour les workers de l'application `messages`. [#5ec14bd](https://github.com/suitenumerique/st-ansible/commit/5ec14bd)
- Correction du fichier `compose` pour le déploiement de Keycloak en configuration cluster. [#826ac51](https://github.com/suitenumerique/st-ansible/commit/826ac51)

### Évolutions techniques
- Rationalisation des variables et des valeurs par défaut des ports publiés à travers les différents rôles. [#71d78b0](https://github.com/suitenumerique/st-ansible/commit/71d78b0)
- Refactorisation des tâches de gestion des permissions des fichiers et des répertoires pour les applications Podman. [#fb72f89](https://github.com/suitenumerique/st-ansible/commit/fb72f89)

### Autres changements
- Publication de la version 0.0.17. [#4f5d454](https://github.com/suitenumerique/st-ansible/commit/4f5d454)
- Ajout de la documentation complète de la collection. [#9c62fb5](https://github.com/suitenumerique/st-ansible/commit/9c62fb5)
