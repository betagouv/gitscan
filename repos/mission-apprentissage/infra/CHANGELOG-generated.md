## Changelog : infra (30 derniers jours, au 30 juin 2026)

### Résumé
Ce changelog fait état d'une période de migrations de serveurs et de réorganisation de l'infrastructure. Les serveurs de production et de recette ont été migrés, et les habilitations d'accès ont été mises à jour. Des améliorations ont également été apportées à la configuration Ansible pour une meilleure gestion des tâches.

### Évolutions fonctionnelles
- Correction de la variable `PRODUCT_OPENPGP_KEY` dans le playbook `all-servers-unban-ip.yml` pour assurer le bon fonctionnement du déblocage d'adresses IP. [#222](https://github.com/mission-apprentissage/infra/issues/222)
- Correction de la configuration SOPS pour le playbook `all-servers-unban-ip.yml` afin de garantir la sécurité des secrets.

### Évolutions techniques
- Migration des serveurs `api-production`, `lba-production`, `tdb-production` et `bal-production`.
- Migration des serveurs `lba-preview`, `tdb-recette`, `lba-recette`, `bal-recette` et `api-recette`.
- Suppression des sous-modules `authorizations` et `inventories` pour simplifier la structure du dépôt.
- Réorganisation des tâches Ansible pour une meilleure organisation et maintenabilité.
- Ajout du tag `always` aux tâches Ansible globales pour garantir leur exécution dans tous les contextes.
- Mise à jour des habilitations du projet `tdb`.

### Autres changements
- Suppression de Rémy des habilitations des projets `mongodb`, `lba`, `api` et `bal`.
- Remplacement d'une ancienne adresse IP.
