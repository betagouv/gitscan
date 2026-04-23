## Changelog : complements-alimentaires (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la maintenance et la mise à jour des dépendances du projet, ainsi que sur la correction de quelques bugs et l'amélioration de la gestion des données. Des améliorations ont été apportées à la gestion des images, des données open data et des statistiques. La suppression de notebooks obsolètes et la mise à jour de la documentation contribuent également à l'amélioration continue du projet.

### Évolutions fonctionnelles
- Correction de l'affichage des images ([#2843](https://github.com/betagouv/complements-alimentaires/pull/2843)).
- Correction d'un problème lié au format des données lors de l'exportation des données ouvertes ([#2855](https://github.com/betagouv/complements-alimentaires/pull/2855)).
- Amélioration de la génération des statistiques et correction de bugs associés ([#2844](https://github.com/betagouv/complements-alimentaires/pull/2844), [#2846](https://github.com/betagouv/complements-alimentaires/pull/2846)).
- Correction d'un problème lié à la gestion des certificats ([#2809](https://github.com/betagouv/complements-alimentaires/pull/2809)).
- Ajout de données de référence pour les ingrédients dans les fixtures.

### Évolutions techniques
- Mise à jour de nombreuses dépendances Python (Django, pypdf, lxml, cryptography, pillow, etc.) vers leurs dernières versions stables.
- Mise à jour des dépendances JavaScript/Node.js (lodash, postcss, vue-dsfr, etc.) dans le frontend.
- Suppression des notebooks obsolètes, le projet s'appuie désormais sur Metabase et la base de données pour l'analyse des données ([#2872](https://github.com/betagouv/complements-alimentaires/pull/2872)).
- Amélioration de la configuration et de la gestion des environnements.

### Autres changements
- Mise à jour de la documentation et du fichier README.
- Mise à jour de la déclaration d'accessibilité ([#2845](https://github.com/betagouv/complements-alimentaires/pull/2845)).
- Nettoyage du code et suppression de fichiers inutiles.
- Ajout d'une clé dans le fichier `.env`.
