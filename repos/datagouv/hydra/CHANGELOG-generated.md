## Changelog : hydra (30 derniers jours, au 16 avril 2026)

### Résumé
Cette version apporte des améliorations significatives en termes de performance et de fonctionnalités, notamment l'optimisation de la génération de données Parquet, l'ajout du support pour l'analyse WMS (Web Map Service) et une meilleure gestion des fichiers temporaires. Des corrections de bugs et des améliorations techniques ont également été apportées pour une plus grande stabilité et maintenabilité du projet.

### Évolutions fonctionnelles
- Ajout du support pour l'analyse des services WMS (Web Map Service) [#401](https://github.com/datagouv/hydra/pull/401).
- Amélioration de la génération de données Parquet en lisant directement depuis la base de données PostgreSQL au lieu de relire les fichiers CSV [#402](https://github.com/datagouv/hydra/pull/402).
- Ajout de métriques de temps détaillées pour les étapes de conversion GeoJSON et PMTiles, facilitant l'identification des goulots d'étranglement [#403](https://github.com/datagouv/hydra/pull/403).
- Gestion améliorée de la taille maximale des fichiers pour les formats inconnus, avec une valeur par défaut définie [#414](https://github.com/datagouv/hydra/pull/414).
- Correction de l'utilisation du nom de fichier de base dans les jobs [#416](https://github.com/datagouv/hydra/pull/416).

### Évolutions techniques
- Refactorisation des endpoints de statistiques pour une meilleure clarté et organisation [#387](https://github.com/datagouv/hydra/pull/387).
- Ajout de vérification de type intégrée pour améliorer la qualité du code [#391](https://github.com/datagouv/hydra/pull/391).
- Utilisation d'un dossier temporaire configurable pour les téléchargements et nettoyage des fichiers temporaires [#400](https://github.com/datagouv/hydra/pull/400).
- Correction de la gestion des erreurs `FileNotFoundError` dans les workers d'analyse [#395](https://github.com/datagouv/hydra/pull/395).
- Suppression des avertissements de log inutiles pour les fonctionnalités OGC [#399](https://github.com/datagouv/hydra/pull/399).

### Autres changements
- Mise à jour de la dépendance `csv-detective` vers la version 0.11.2 [#407](https://github.com/datagouv/hydra/pull/407).
- Correction d'une URL incorrecte dans les vérifications [#406](https://github.com/datagouv/hydra/pull/406).
- Suppression d'une importation inutilisée [#10481b1](https://github.com/datagouv/hydra/commit/10481b1).
