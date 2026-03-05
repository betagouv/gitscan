## Changelog : st-ansible (30 derniers jours)

### Résumé
Les dernières mises à jour de st-ansible améliorent la flexibilité et la configuration des rôles Ansible, notamment pour les services Podman et Messages. L'ajout de tests automatisés via Molecule et GitHub Actions renforce la qualité et la fiabilité de la collection.

### Évolutions fonctionnelles
- Le rôle `podman` permet désormais de définir une politique de redémarrage Systemd personnalisée via la variable `systemd_restart_policy` [#8](https://github.com/suitenumerique/st-ansible/pull/8).
- Le rôle `messages` offre plus de contrôle sur le mécanisme de notification `sdnotify`, avec la possibilité de le configurer et de définir une valeur par défaut de `container` [#6](https://github.com/suitenumerique/st-ansible/pull/6).
- Une nouvelle variable `st_keycloak_start_command` a été ajoutée au rôle `keycloak` pour permettre la personnalisation de la commande de démarrage.

### Évolutions techniques
- Ajout de tests d'intégration avec Molecule et configuration de GitHub Actions pour l'exécution automatique des tests [#9](https://github.com/suitenumerique/st-ansible/pull/9).
- Correction de la valeur par défaut de `sdnotify` dans le rôle `messages` pour utiliser `container`.
