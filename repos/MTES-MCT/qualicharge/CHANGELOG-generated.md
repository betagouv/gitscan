## Changelog : qualicharge (30 derniers jours, au 10 août 2026)

### Résumé
Ce mois-ci, le projet s'est enrichi de nouveaux indicateurs de performance (e2 et e3). Un travail important a également été réalisé pour optimiser la rapidité de calcul de ces indicateurs et améliorer l'efficacité du stockage des données de tarification au sein de l'API.

### Évolutions fonctionnelles
- Ajout de nouveaux indicateurs de performance (e2 et e3) pour affiner l'analyse des données de recharge.

### Évolutions techniques
- Optimisation des performances de calcul pour les indicateurs e2 et e3 via Prefect.
- Optimisation du stockage de l'API en ne conservant que les champs de tarification non nuls, afin de réduire l'empreinte des données brutes.
