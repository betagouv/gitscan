## Changelog : infra (30 derniers jours, au 18 juin 2026)

### Résumé
Ce changelog résume les opérations de migration de serveurs et de gestion des accès récentes. L'infrastructure a été mise à jour avec la migration de plusieurs serveurs (API, LBA, TDB, BAL) entre les environnements recette et production. Des ajustements ont également été effectués concernant les habilitations des utilisateurs sur différents projets. Enfin, des améliorations ont été apportées à l'organisation des tâches Ansible et à la rotation des mots de passe.

### Évolutions fonctionnelles
- Correction d'un problème avec SOPS dans le workflow `all-servers-unban-ip.yml`.
- Amélioration de la rotation des mots de passe sur tous les serveurs via le script `scheduled-all-servers-password-rotate.sh` [#219](https://github.com/mission-apprentissage/infra/issues/219).

### Évolutions techniques
- Migration des serveurs `api-production`, `lba-production`, `tdb-production` et `bal-production`.
- Migration des serveurs `lba-preview` et `tdb-recette`.
- Suppression des sous-modules `authorizations` et `inventories`.
- Réorganisation des tâches Ansible pour une meilleure structure.
- Ajout du tag `always` aux tâches Ansible globales pour garantir leur exécution.
- Suppression de Rémy des habilitations des projets mongodb, lba, api et bal.

### Autres changements
- Migration du serveur `bal-recette`.
- Migration du serveur `api-recette` (deux commits successifs).
- Mise à jour des habilitations du projet `tdb`.
