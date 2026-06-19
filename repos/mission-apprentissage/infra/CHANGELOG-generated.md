## Changelog : infra (30 derniers jours, au 18 juin 2026)

### Résumé
Ce changelog fait état d'une période de migration importante des serveurs de production et de recette vers une nouvelle infrastructure. Des ajustements ont été apportés aux habilitations utilisateurs et à l'organisation des tâches Ansible pour faciliter ces migrations et améliorer la gestion du projet. Une correction concernant la rotation des mots de passe a également été implémentée.

### Évolutions fonctionnelles
- Correction d'un problème concernant la rotation des mots de passe des serveurs via le script `scheduled-all-servers-password-rotate.sh` [#219](https://github.com/mission-apprentissage/infra/issues/219).

### Évolutions techniques
- **Migrations de serveurs:** Migration des serveurs `api-production`, `lba-production`, `tdb-production`, `bal-production`, `lba-preview`, `tdb-recette`, `lba-recette`, `bal-recette` et `api-recette`.
- **Refactoring Ansible:** Réorganisation des tâches Ansible pour une meilleure gestion et efficacité.
- Ajout du tag `always` aux tâches Ansible globales pour garantir leur exécution dans tous les contextes.
- Suppression des sous-modules `authorizations` et `inventories`.

### Autres changements
- Suppression de Rémy des habilitations des projets `mongodb`, `lba`, `api` et `bal`.
- Mise à jour des habilitations du projet `tdb`.
- Correction de la configuration SOPS pour le workflow `all-servers-unban-ip.yml`.
