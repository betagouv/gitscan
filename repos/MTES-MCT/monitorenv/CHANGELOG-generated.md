## Changelog : monitorenv (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à MonitorEnv au cours du dernier mois. Les principales évolutions concernent l'ajout d'un historique des navires, des optimisations de recherche, des corrections de données et des améliorations techniques de l'infrastructure et des dépendances. Ces changements visent à améliorer l'expérience utilisateur, la performance et la fiabilité de l'application.

### Évolutions fonctionnelles
- Ajout de l'historique des navires sur la page de résumé du navire (#af7c7c1).
- Affichage de la dernière position connue d'un navire sur la page de résumé (#e260f51).
- Amélioration de la recherche des plages en ajoutant la possibilité de rechercher sans accent (#db3962e, #3655ae8).
- Correction du filtre `controlPlan` dans la recherche de couches (#e716c08).
- Correction du flux de régulation pour la publication des données sur data.gouv (#7d69a79).
- Correction de l'affichage des zones réglementaires dans la vue "brief" (#9c73b9d).

### Évolutions techniques
- Mise à jour de la version de Poetry à 3.6.9 (#9a6880d).
- Remplacement de la dépendance `cx_oracle` par `oracledb` (#2d2515f).
- Ajout de volumes pour les certificats Kafka (#95d038f).
- Utilisation de l'extension `unaccent` de PostgreSQL pour améliorer la recherche sans accent (#db3962e, #3655ae8).
- Suppression du code d'infrastructure legacy et des fichiers Dockerfile obsolètes (#aececeb, #03c91be, #2feb5eb, #503e2fe).
- Suppression du dossier `datascience` (#2e32bdd).
- Mise à jour des workflows CI/CD et de la configuration de Dependabot (#cd8fe0c, #f5969b8).
- Mise à jour de la configuration de pre-commit (#f5969b8).
- Mise à jour des actions GitHub utilisées dans les workflows CI/CD (#c3c6080).
- Ajout d'un cache pour la recherche de couches (#fab1715).
- Refactorisation du hook `useSearchLayers` (#ca1f62b).
- Ajout d'une vue matérialisée pour accélérer la recherche de plages (#3655ae8).
- Correction d'un problème empêchant les tests de s'exécuter correctement (#a32c9da).

### Autres changements
- Mise à jour des dépendances : black (25.12.0 -> 26.1.0), css-inline, cypress-io/github-action (6 -> 7) et plusieurs autres dépendances non majeures (#96ab080, #87f4632, #c1805fb, #de9eb8e).
- Mise à jour du fichier `Makefile` (#376dca2, #3036a5d).
- Mise à jour du fichier `.gitignore` (#4d5c3b9).
- Ajout de la documentation pour l'installation du worker Prefect 3 (#e69b967).
- Correction de tests unitaires (#bb39824, #ad78352).
- Correction de bugs et améliorations diverses (#b5016b6, #407d116, #0382dac, #d9655db, #476849b).
- Ajout des codes régionaux Google Places pour Mayotte, Martinique et Guadeloupe (#cfb7a55).
- Correction du hash de ligne pour les zones réglementaires (#b5016b6).
