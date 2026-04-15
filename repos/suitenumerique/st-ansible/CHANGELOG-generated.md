## Changelog : st-ansible (30 derniers jours, au 2026-04-02)

### Résumé
Cette mise à jour apporte des améliorations à la structure des rôles Ansible pour faciliter la maintenance et la réutilisation du code. Une correction a également été apportée au rôle `podman` pour assurer une configuration correcte des identifiants utilisateur et groupe des conteneurs.

### Évolutions fonctionnelles
- Correction du calcul de `container_uid` et `gid` dans le rôle `podman` pour une configuration correcte des conteneurs. [#20](https://github.com/suitenumerique/st-ansible/issues/20)

### Évolutions techniques
- Refactorisation des rôles `drive`, `messages` et `keycloak` : séparation des tâches principales et importation du fichier `deploy.yml` pour une meilleure organisation et réutilisabilité du code. [#20](https://github.com/suitenumerique/st-ansible/issues/20)
