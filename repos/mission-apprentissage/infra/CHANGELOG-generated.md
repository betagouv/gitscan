## Changelog : infra (30 derniers jours, au 2026-06-02)

### Résumé
Ce changelog présente les améliorations apportées à l'infrastructure au cours du dernier mois. Les changements se concentrent principalement sur la correction de bugs liés à l'exécution des tâches Ansible, la gestion des accès au projet TDB, la sécurité des serveurs et la restauration de la gestion des tags Git.

### Évolutions fonctionnelles
- Correction du script `scheduled-all-servers-password-rotate.sh` pour assurer la rotation des mots de passe sur tous les serveurs. [#219](https://github.com/mission-apprentissage/infra/issues/219)
- Mise en place d'un correctif temporaire pour les vulnérabilités Dirty Frag et Fragnesia, améliorant la sécurité des serveurs. [#216](https://github.com/mission-apprentissage/infra/issues/216)

### Évolutions techniques
- Ajout du tag `always` aux tâches Ansible globales pour garantir leur exécution dans tous les scénarios.
- Restauration des tags Git pour une meilleure gestion des versions et un suivi des modifications.
- Correction d'un problème lié à la restauration des tags Git.

### Autres changements
- Mise à jour des habilitations du projet TDB, améliorant la gestion des accès.
- Désactivation des serveurs sandbox, probablement dans le cadre d'une maintenance ou d'une réorganisation de l'environnement. [#218](https://github.com/mission-apprentissage/infra/issues/218)
