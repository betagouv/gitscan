## Changelog : archeologia-pipeline (30 derniers jours, au 26 mars 2026)

### Résumé
Ce pipeline a été amélioré avec l'ajout d'un nouvel algorithme de clustering spatial (DBSCAN) et une amélioration de la visualisation des clusters. Des corrections ont également été apportées au post-traitement du modèle de détection RF-DETR, et des optimisations de performance ont été réalisées pour le post-traitement, notamment grâce à l'utilisation d'un index spatial STRtree.

### Évolutions fonctionnelles
- Ajout d'un algorithme de clustering spatial DBSCAN avec un style de quadrillage noir pour la visualisation des clusters. [#N/A](https://github.com/betagouv/archeologia-pipeline/commit/d475a02)

### Évolutions techniques
- Correction d'un problème de post-traitement du modèle de détection RF-DETR. [#N/A](https://github.com/betagouv/archeologia-pipeline/commit/05c549a)
- Optimisation du post-traitement avec l'utilisation d'un index spatial STRtree pour améliorer les performances, avec ajout de logs de temps d'exécution. [#N/A](https://github.com/betagouv/archeologia-pipeline/commit/2ba5f0d)
