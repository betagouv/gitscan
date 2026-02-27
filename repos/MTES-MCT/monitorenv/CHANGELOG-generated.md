## Changelog : monitorenv (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à monitorenv au cours des 30 derniers jours. Les principales évolutions concernent l'interface utilisateur avec l'ajout d'informations sur l'historique des navires et les signalements, ainsi que des corrections de bugs pour améliorer la stabilité et la fiabilité de l'application. Des mises à jour techniques importantes ont également été effectuées pour moderniser l'infrastructure et les dépendances du projet.

### Évolutions fonctionnelles

- Ajout de l'historique des navires sur la page de résumé du navire. (#7a52b89)
- Affichage de la dernière position connue d'un navire sur la page de résumé. (#e260f51)
- Ajout d'un cercle rouge sur la carte pour indiquer les navires ayant un rapport en cours. (#403a3e4)
- Renommage de "signalement" en "suspicion d'infraction" dans l'interface. (#f54d296)
- Ajout de la géométrie aux rapports créés directement depuis un navire. (#faf1a31)
- Ajout de la source "RAPPORT_NAV" aux sources de missions par défaut. (#389a084)
- Correction pour permettre l'affichage complet des missions. (#65ca6d9)

### Évolutions techniques

- Mise à jour de Poetry vers la version 3.6.9. (#9a6880d)
- Mise à jour de Black vers la version 26.1.0. (#96ab080)
- Remplacement de la dépendance `cx_oracle` par `oracledb`. (#2d2515f)
- Suppression du code d'infrastructure legacy et des fichiers Dockerfile obsolètes. (#aececeb, #203e2fe, #03c91be, #503e2fe)
- Mise à jour des workflows GitHub Actions et du fichier `.gitignore`. (#cd8fe0c, #4d5c3b9)
- Mise à jour des fichiers Makefile. (#376dca2, #3036a5d)
- Mise à jour de la configuration de Coderabbit. (#2feb5eb)
- Suppression du dossier `datascience`. (#2e32bdd)
- Ajout de volumes pour les certificats Kafka. (#95d038f)
- Mise à jour des actions GitHub pour la configuration de Java. (#c3c6080)
- Correction du type `jsonb` dans les modèles. (#044566f)
- Mise à jour de Cypress dans le workflow GitHub Action. (#de9eb8e)

### Autres changements

- Correction de tests unitaires et d'intégration. (#bb39824, #ad78352, #8ff992d)
- Mise à jour de la documentation pour l'installation du worker Prefect 3. (#e69b967)
- Suppression d'une requête inutilisée. (#991ffe1)
- Correction d'un problème empêchant l'ouverture d'une fenêtre latérale lors des tests. (#a32c9da)
- Mise à jour des dépendances non-majeures (plusieurs commits dependabot). (#c1805fb, #ad78352, #9c73b9d)
- Correction d'un bug dans les tests. (#87f4632)
- Mise à jour du fichier `poetry.lock`. (#59ac0dd)
