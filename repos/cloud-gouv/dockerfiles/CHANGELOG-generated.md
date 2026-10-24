## Changelog : dockerfiles (30 derniers jours, au 21 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec l'introduction d'une nouvelle image dédiée aux déploiements OpenTofu. Parallèlement, les processus d'automatisation ont été renforcés pour garantir une meilleure stabilité et un contrôle accru sur la production des images.

### Évolutions fonctionnelles
- Ajout d'une nouvelle image Docker spécifiquement conçue pour les déploiements OpenTofu.

### Évolutions techniques
- **Amélioration de l'image OpenTofu** :
  - Intégration de `git` pour faciliter les opérations liées aux dépôts.
  - Ajout de l'outil `syft` pour permettre la génération de SBOM (Software Bill of Materials) directement lors de l'utilisation de l'image.
- **Optimisation de la CI/CD** :
  - Restriction des déclenchements de pipelines pour ne construire des images qu'après la fusion de Pull Requests validées dans la branche principale.
  - Mise en place de déclenchements automatiques lors de la création de nouveaux tags.
