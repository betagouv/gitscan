## Changelog : dockerfiles (30 derniers jours, au 16 octobre 2026)

### Résumé
Ce mois-ci, le projet a enrichi sa collection d'outils avec une nouvelle image dédiée à l'infrastructure (OpenTofu) et a optimisé ses processus d'automatisation pour garantir que seuls les changements validés déclenchent la création de nouvelles images.

### Évolutions fonctionnelles
- Ajout d'une nouvelle image Docker dédiée aux déploiements avec OpenTofu.

### Évolutions techniques
- Optimisation des pipelines CI/CD pour restreindre l'exécution des builds aux seules Pull Requests validées et fusionnées dans la branche principale (`main`).
