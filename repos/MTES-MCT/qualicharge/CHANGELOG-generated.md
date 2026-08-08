## Changelog : qualicharge (30 derniers jours, au 04/08/2026)

### Résumé
Les récentes évolutions se concentrent sur l'enrichissement des indicateurs de performance et la fiabilisation des pipelines de données. Des améliorations ont également été apportées à l'API pour optimiser le stockage et renforcer la validation des données saisies.

### Évolutions fonctionnelles
- **API** : La création d'un tarif nécessite désormais la définition d'au moins une cible pour être valide.

### Évolutions techniques
- **Pipelines de données (Prefect)** :
  - Ajout et amélioration de nouveaux indicateurs de performance (e1-DMR, e2 et e3).
  - Correction de la gestion des plages temporelles lors des requêtes utilisant la table `lateststatus`.
  - Inclusion des points de charge décommissionnés dans les processus d'analyse.
- **API** : Optimisation du stockage des données de tarifs en ne conservant que les champs non nuls en format brut.

### Autres changements
- Mise à jour de la version du projet vers la 0.34.1.
