## Changelog : st-ansible (30 derniers jours, au 11 mai 2026)

### Résumé
Cette nouvelle version apporte l'ajout d'un rôle pour le service Meet, des améliorations sur le rôle Podman (correction de démarrage et refactoring des permissions) et une refactorisation du déploiement de Rspamd. La documentation de la collection a également été complétée.

### Évolutions fonctionnelles
- Ajout du rôle `meet` pour le déploiement du service Meet. [#22](https://github.com/suitenumerique/st-ansible/issues/22)
- Correction du script de démarrage de l'application systemd dans le rôle `podman`, assurant un démarrage correct.
- Refactorisation du déploiement de Rspamd pour une meilleure gestion des messages.

### Évolutions techniques
- Rationalisation des variables et des valeurs par défaut des ports publiés à travers les différents rôles.
- Refactorisation des tâches de gestion des permissions des fichiers et des répertoires dans le rôle `podman`.
- Correction de la gestion de la propriété des fichiers dans le rôle `podman` ([8c2ebce](https://github.com/suitenumerique/st-ansible/commit/8c2ebce)).

### Autres changements
- Ajout de la documentation complète de la collection Ansible.
- Publication de la version 0.0.17.
- Publication de la version 0.0.16.
