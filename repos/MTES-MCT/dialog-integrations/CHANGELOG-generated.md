## Changelog : dialog-integrations (30 derniers jours, au 2026-05-12)

### Résumé
Ce mois-ci, le projet dialog-integrations a progressé sur l'intégration de nouvelles sources de données, notamment pour les préfectures de Nantes et Rennes. Des améliorations ont été apportées à l'infrastructure CI/CD pour optimiser le processus d'intégration et de déploiement, ainsi que des corrections et améliorations générales du code.

### Évolutions fonctionnelles
- Intégration des données de la préfecture de Rennes : la source de données de Rennes est maintenant prête à être intégrée. [#10](https://github.com/MTES-MCT/dialog-integrations/pull/10)
- Intégration des données de la préfecture de Nantes : la source de données de Nantes est en phase de test et a été temporairement désactivée puis remise en brouillon. [#11](https://github.com/MTES-MCT/dialog-integrations/pull/11)

### Évolutions techniques
- Amélioration de la gestion des environnements et ajout de notifications.
- Optimisation du workflow CI/CD : l'intégration n'est plus déclenchée à chaque push pour éviter des exécutions inutiles.
- Amélioration de la capture des sorties des processus.
- Refonte de la gestion des identifiants pour une meilleure persistance.
- Amélioration du linting et ajout de typage pour une meilleure qualité du code.
- Mise à jour de certaines dépendances.

### Autres changements
- Correction de formatage et améliorations générales du code.
- Nettoyage du code et amélioration de la lisibilité.
