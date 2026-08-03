## Changelog : infra (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'observabilité de l'infrastructure avec l'ajout de métriques MongoDB exposées au monitoring, ainsi que sur l'amélioration de la lisibilité des logs via Fluentd. Des corrections mineures et des tâches de maintenance ont également été effectuées.

### Évolutions fonctionnelles
- Ajout de l'exposition du port de métriques MongoDB (9946) vers le monitoring pour le cluster LBA. [#225](https://github.com/mission-apprentissage/infra/issues/225)
- Amélioration de la lisibilité des logs Fluentd en mappant les niveaux de log numériques à leurs noms correspondants. [#224](https://github.com/mission-apprentissage/infra/issues/224)
- Correction d'un problème lié à la hauteur du terminal dans tmux. [#226](https://github.com/mission-apprentissage/infra/issues/226)

### Évolutions techniques
- Mise à jour des habilitations.
- Rotation du secret principal SOPS.

### Autres changements
- Correction d'une faute de frappe. [#43648b6](https://github.com/mission-apprentissage/infra/commit/43648b6)
