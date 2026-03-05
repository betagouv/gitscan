## Changelog : monitorenv (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à monitorenv au cours des 30 derniers jours. Les principales évolutions concernent l'interface utilisateur, notamment l'amélioration de la gestion des informations sur les navires et des signalements, ainsi que des optimisations techniques pour améliorer la performance et la stabilité de l'application. Des mises à jour de l'infrastructure et des dépendances ont également été réalisées.

### Évolutions fonctionnelles
- Ajout de l'historique des positions des navires sur la page de résumé du navire. [#2345](https://github.com/MTES-MCT/monitorenv/issues/2345)
- Affichage de la dernière position connue d'un navire sur sa page de résumé.
- Renommage de "signalement" en "suspicion d'infraction".
- Ajout d'un cercle rouge sur la carte pour indiquer les navires ayant un signalement en cours.
- Amélioration de l'affichage des zones réglementaires et des AMP dans le "brief" et le document éditable.
- Correction de l'affichage du sélecteur d'unité de contrôle.
- Ajout de toutes les positions filtrées à la carte et au résumé du navire.
- Ajout des plannings sur les zones localisées.
- Affichage des informations du navire même si seul le nom est renseigné.
- Ajout de la source de mission "RAPPORT_NAV" pour récupérer toutes les missions complètes.
- Ajout de la géométrie au reporting lors de sa création à partir d'un navire.

### Évolutions techniques
- Utilisation du client Oracle "heavy" lors de l'utilisation de FMC.
- Augmentation de la taille de la mémoire partagée de la base de données à 256 Mo.
- Mise à jour de Poetry vers la version 3.6.9.
- Refonte de l'infrastructure : suppression du code infra legacy, des fichiers Dockerfile et des workflows GitHub obsolètes.
- Mise à jour de la configuration d'environnement et de pre-commit.
- Ajout de tests unitaires pour l'historique des navires.
- Remplacement de la dépendance `cx_oracle` par `oracledb`.
- Ajout de volumes pour les certificats Kafka.
- Correction de types JSONB dans les modèles.

### Autres changements
- Mise à jour de plusieurs dépendances (black, css-inline, cypress-io/github-action, kotlin, etc.).
- Correction de tests unitaires.
- Mise à jour des actions CI/CD (actions/setup-java).
- Mise à jour de la documentation (ajout de l'installation du worker Prefect 3).
- Nettoyage du code et des fichiers de configuration.
