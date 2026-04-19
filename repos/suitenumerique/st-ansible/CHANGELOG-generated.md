## Changelog : st-ansible (30 derniers jours, au 2026-04-17)

### Résumé
Cette mise à jour apporte des corrections et des améliorations concernant la gestion des droits sur les fichiers déployés par Podman, ainsi qu'une restructuration des tâches Ansible pour les rôles drive, messages et keycloak afin d'améliorer la lisibilité et la maintenabilité.

### Évolutions fonctionnelles
- Correction d'un problème de gestion des droits sur les fichiers déployés par l'application Podman. Cela assure un fonctionnement correct des applications déployées. [#20](https://github.com/suitenumerique/st-ansible/issues/20)

### Évolutions techniques
- Restructuration des tâches Ansible pour les rôles `drive`, `messages` et `keycloak` en séparant la logique principale et le déploiement dans un fichier `deploy.yml` dédié. Cela améliore l'organisation du code et facilite sa maintenance. [#20](https://github.com/suitenumerique/st-ansible/issues/20)
