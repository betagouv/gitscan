## Changelog : sites-conformes-easy-deploy (30 derniers jours, au 19 novembre 2026)

### Résumé
Ce mois a été consacré au lancement du projet et à la mise en place de l'automatisation des déploiements. Les efforts se sont concentrés sur la création et l'optimisation des workflows GitHub Actions pour garantir une gestion fiable des versions et des processus de déploiement.

### Évolutions fonctionnelles
- Ajout d'une nouvelle GitHub Action pour automatiser les processus de déploiement.

### Évolutions techniques
- Amélioration du workflow `check-tags` :
  - Optimisation de la détection des tags, incluant désormais le support dans les branches de Pull Request.
  - Refactorisation pour utiliser des variables dynamiques au lieu de noms de branches codés en dur.
  - Ajout d'un filtre pour ignorer les tags de type "release candidate" provenant de l'amont (upstream).

### Autres changements
- Initialisation du dépôt et ajout de la documentation (README).
