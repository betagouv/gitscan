## Changelog : monitor-ui (30 derniers jours, au 27/10/2026)

### Résumé
Les évolutions récentes se concentrent sur l'amélioration de la flexibilité des composants d'interface, notamment pour les boutons et la prévisualisation de fichiers, tout en affinant le processus automatisé de déploiement des versions.

### Évolutions fonctionnelles
- **Composants UI :**
    - Introduction d'une nouvelle taille pour le composant `LinkButton`. Notez que l'ajout d'une icône est désormais obligatoire lorsque la taille "Large" est sélectionnée ([af7df50](https://github.com/MTES-MCT/monitor-ui/commit/af7df50)).
    - Le composant `FilePreview` permet désormais de rendre la fonction de suppression (`onDelete`) optionnelle lorsqu'il est utilisé en mode lecture seule ([a71d93e](https://github.com/MTES-MCT/monitor-ui/commit/a71d93e)).

### Évolutions techniques
- **CI/CD :**
    - Optimisation de la configuration de release avec l'ajout du paramètre `breaking` dans le fichier `.releaserc` ([751992c](https://github.com/MTES-MCT/monitor-ui/commit/751992c)).
    - Publication des versions 24.60.2 et 24.61.0.
