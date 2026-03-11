## Changelog : monitorenv (30 derniers jours)

### Résumé
Les dernières mises à jour de monitorenv se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des navires et des signalements. Des optimisations techniques ont également été apportées pour améliorer la performance et la stabilité de l'application, ainsi que pour moderniser l'infrastructure et les outils de développement.

### Évolutions fonctionnelles
- Ajout de l'historique des positions d'un navire sur sa fiche récapitulative ([#7a52b89](https://github.com/MTES-MCT/monitorenv/commit/7a52b89)).
- Affichage de la dernière position connue d'un navire sur sa fiche récapitulative.
- Possibilité d'ajouter toutes les positions filtrées à la fiche récapitulative d'un navire.
- Renommage de "signalement" en "suspicion d'infraction".
- Ajout d'un cercle rouge sur la carte pour indiquer les navires ayant un signalement en cours.
- Amélioration de la sélection de l'unité de contrôle ([#10eb5ff](https://github.com/MTES-MCT/monitorenv/commit/10eb5ff)).
- Ajout de plannings aux zones localisées ([#9363bfa](https://github.com/MTES-MCT/monitorenv/commit/9363bfa)).
- Correction de l'affichage des zones AMP et réglementaires liées aux vigilances dans le résumé et le document éditable ([#740caf2](https://github.com/MTES-MCT/monitorenv/commit/740caf2)).
- Affichage des informations du navire même si seul le nom est renseigné.
- Amélioration de la formulation de l'historique du navire.
- Ajout de la source de mission "RAPPORT_NAV" pour l'utilisation complète des missions.
- Ajout de la géométrie au signalement lors de sa création à partir d'un navire.
- Correction d'un bug empêchant le déplacement du résumé du navire lors de la création d'un rapport en mer ([#2da4d68](https://github.com/MTES-MCT/monitorenv/commit/2da4d68)).

### Évolutions techniques
- Utilisation du client Oracle "heavy" lorsque FMC est activé.
- Augmentation de la taille de la mémoire partagée de la base de données à 256 Mo.
- Mise à jour de Poetry vers la version 3.6.9.
- Mise à jour de Black vers la version 26.1.0.
- Modernisation de l'infrastructure : suppression du code infra legacy, des workflows Github legacy, des fichiers Dockerfile legacy, et des dossiers inutilisés (datascience).
- Mise à jour de la configuration de l'environnement et de pre-commit.
- Ajout de tests pour l'historique des navires.
- Ajout de tracking sur la recherche de navires et la création de rapports à partir du résumé du navire ([#66229c4](https://github.com/MTES-MCT/monitorenv/commit/66229c4)).
- Remplacement de la dépendance `cx_oracle` par `oracledb`.
- Ajout de volumes pour les certificats Kafka.

### Autres changements
- Mise à jour de la documentation pour l'installation du worker Prefect 3.
- Mise à jour du fichier Makefile.
- Mise à jour de Coderabbit.
- Suppression d'une requête inutilisée.
- Mise à jour du fichier contributing.
- Mise à jour du fichier gitignore.
- Mise à jour de la configuration de Dependabot.
- Bump de plusieurs dépendances mineures (css-inline).
