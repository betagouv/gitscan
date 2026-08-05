## Changelog : mirai-mesreunions (30 derniers jours, au 04 août 2026)

### Résumé
Les récentes évolutions se sont concentrées sur l'amélioration de la fiabilité de l'importation de contenus multimédias et sur l'optimisation majeure du processus de construction (build) du logiciel, désormais plus intégré et performant.

### Évolutions fonctionnelles
- **Amélioration de l'importation YouTube** : Le système est désormais plus résilient face aux mécanismes anti-bot ; en cas de blocage, l'importation tente automatiquement une nouvelle tentative au lieu de s'interrompre brutalement.

### Évolutions techniques
- **Optimisation de la CI/CD** : Migration du processus de construction vers un modèle "in-cluster" utilisant BuildKit (mode rootless). Cette évolution permet de supprimer la dépendance aux machines virtuelles (VM) externes pour les builds.
- **Corrections du processus de build** : Résolution de bugs liés à l'identification du cluster et à des erreurs de variables lors de la phase de construction des images.
