## Changelog : st-ansible (30 derniers jours)

### Résumé
Cette nouvelle version de st-ansible apporte des améliorations significatives à la gestion des applications conteneurisées avec Podman, notamment en ajoutant des mécanismes de restauration et en permettant une configuration plus fine des services. Des tests automatisés ont été intégrés pour garantir la qualité du code, et la documentation a été corrigée.

### Évolutions fonctionnelles
- Possibilité de définir une politique de redémarrage personnalisée pour les services Podman via la variable `systemd_restart_policy` [#8](https://github.com/suitenumerique/st-ansible/pull/8).
- Amélioration de la gestion de l'authentification pour la connexion à Podman, avec correction du chemin du fichier d'authentification [#6](https://github.com/suitenumerique/st-ansible/pull/6).
- Possibilité de configurer `sdnotify` pour le rôle `st-messages`, avec une valeur par défaut plus appropriée et des options de personnalisation [#6](https://github.com/suitenumerique/st-ansible/pull/6).
- Ajout d'une fonctionnalité de restauration (rollback) pour les rôles `drive`, `keycloak` et `messages`, permettant de revenir à un état précédent en cas de problème. Cette fonctionnalité utilise la variable `st_podman_application_files`.
- Correction de fautes de frappe dans la documentation.

### Évolutions techniques
- Migration des tests Molecule vers le driver Lima pour une meilleure compatibilité et performance.
- Ajout de tests automatisés avec Molecule et GitHub Actions pour garantir la qualité du code et faciliter les contributions.
- Amélioration de la configuration de l'unité systemd pour Podman.
- Correction des permissions dans le workflow CI/CD.
- Suppression d'une fonctionnalité systemd unit watchdog qui posait problème.

### Autres changements
- Mise à jour de la version à 0.0.14 et 0.0.13.
