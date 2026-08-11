## Changelog : qualicharge (30 derniers jours, au 10 août 2026)

### Résumé
Les récentes évolutions se concentrent sur l'enrichissement des capacités d'analyse avec l'ajout de nouveaux indicateurs de performance et sur l'amélioration de la fiabilité des données via l'API. Des optimisations techniques ont également été réalisées pour accélérer les calculs et optimiser le stockage.

### Évolutions fonctionnelles
- Ajout de nouveaux indicateurs de performance (e2 et e3).
- Renforcement de la validation de l'API : l'ajout d'au moins une cible est désormais obligatoire lors de la création d'un tarif.

### Évolutions techniques
- **Optimisation des performances** : Amélioration de la vitesse de calcul des indicateurs e2 et e3 via Prefect.
- **Optimisation du stockage** : L'API ne stocke désormais que les champs de tarifs non nuls en format brut pour réduire l'empreinte des données.
- **Correction de bug** : Rectification de la définition de la plage temporelle pour les requêtes utilisant la table `lateststatus`.
