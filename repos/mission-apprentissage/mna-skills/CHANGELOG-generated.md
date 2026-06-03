## Changelog : mna-skills (30 derniers jours, au 01 juin 2026)

### Résumé
Ce changelog présente les premières versions des skills développées pour la mission apprentissage, axées sur l'automatisation de tâches liées aux issues et pull requests sur GitHub. Les fonctionnalités permettent de créer, assigner et gérer des issues, ainsi que d'initier des audits de sécurité.

### Évolutions fonctionnelles
- Ajout de la skill `lba-issue` avec des étapes de type et de priorité, ainsi qu'une section de mise à jour des issues.
- Implémentation de la résolution de l'assignataire d'une pull request à partir de la mémoire, supprimant ainsi le hardcoding de l'utilisateur "kevbarns" dans la skill `pull-request-lba`.
- La skill `mna-security-audit` permet désormais de spécifier un répertoire de base et de récupérer la branche `main` avant de créer une nouvelle branche pour l'audit.
- Migration de la skill `mna-security-audit` pour utiliser les issues GitHub au lieu de références personnelles.
- Ajout d'un mode de décomposition dans la skill `lba-issue` pour la création d'issues parentes et subordonnées.
- Amélioration de la skill `lba-issue` avec la prise en charge des relations parent/bloqué par, simplification du flux d'assignation et mise à jour de la pile technologique.
- Introduction d'un outil de mise à jour des skills (`skill-updater`) et amélioration du flux d'assignation de la skill `lba-issue`.

### Évolutions techniques
- Initialisation des skills pour la mission apprentissage.
- Refactorisation et simplification du code dans plusieurs skills.

### Autres changements
- Suppression d'un fichier `.gitignore` inutile.
