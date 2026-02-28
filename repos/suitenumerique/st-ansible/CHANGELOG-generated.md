## Changelog : st-ansible (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations significatives à la gestion des services et des notifications système, notamment pour les conteneurs Podman. De plus, des tests automatisés ont été ajoutés pour garantir la qualité et la stabilité de la collection Ansible. Une variable a été ajoutée pour configurer la commande de démarrage de Keycloak.

### Évolutions fonctionnelles
- Possibilité de personnaliser la politique de redémarrage systemd pour les conteneurs Podman (#8).
- Configuration plus flexible de la notification système (sdnotify) pour les services, avec la possibilité de choisir entre différents modes et un comportement par défaut plus adapté aux conteneurs (#6, #7, #8).
- Ajout de la variable `st_keycloak_start_command` pour configurer la commande de démarrage de Keycloak (#9).

### Évolutions techniques
- Ajout de tests automatisés avec Molecule et GitHub Actions (#10).
- Correction de la valeur par défaut de `sdnotify` pour utiliser `conmon` (#11).

### Autres changements
- Aucune information disponible.
