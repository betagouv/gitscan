## Changelog : st-ansible (30 derniers jours, au 09 mai 2026)

### Résumé
Cette nouvelle version de st-ansible apporte un nouveau rôle pour le déploiement de l'outil de visioconférence Meet, ainsi que des corrections et améliorations concernant le rôle Podman, notamment pour la gestion des permissions des fichiers d'application et le démarrage des services via systemd. Une refactorisation du déploiement de RSPAMD a également été effectuée.

### Évolutions fonctionnelles
- Ajout d'un nouveau rôle Ansible pour déployer et configurer l'outil Meet. [#22](https://github.com/suitenumerique/st-ansible/issues/22)
- Correction du script de démarrage systemd pour les applications Podman, assurant un bon fonctionnement des notifications.
- Amélioration de la gestion des permissions des fichiers d'application dans le rôle Podman.

### Évolutions techniques
- Refactorisation des tâches de gestion des permissions et de structure des fichiers dans le rôle Podman.
- Refactorisation du déploiement de RSPAMD pour améliorer la clarté et la maintenabilité du code.

### Autres changements
- Publication de la version 0.0.16.
- Correction de la gestion du propriétaire des fichiers dans le rôle `st_podman_application_files`.
