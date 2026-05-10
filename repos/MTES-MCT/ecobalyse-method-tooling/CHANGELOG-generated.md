## Changelog : ecobalyse-method-tooling (30 derniers jours, au 8 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des données d'ingrédients transformés, notamment en intégrant de nouvelles variantes (NUE, HUE, UE) et en affinant les processus de correspondance et de fusion des données. Des corrections et améliorations ont également été apportées à la gestion des alias, des noms d'activités et des données sources.

### Évolutions fonctionnelles
- Ajout de la prise en charge de la variante UE (Unités Économiques) avec des fichiers CSV sources et des mécanismes de fusion/orphelins pour garantir l'intégrité des données.
- Intégration de la variante HUE (Human Use Efficiency) et régénération des ingrédients transformés.
- Amélioration de la correspondance des groupes de cultures (cropGroup matcher) pour une meilleure précision et une meilleure information sur la confiance.
- Ajout de la possibilité d'exporter les données sources à partir de Google Sheets via le script `export.py`.
- Ajout d'une colonne `is_byproduct` et actualisation des sorties avec les co-produits d'allocation.
- Ajout d'une colonne `dummy_op` et actualisation des sorties à partir de la descente en couches.
- Ajout de noms d'affichage en français pour les ingrédients, en utilisant un modèle de traduction.
- Prédiction des métadonnées des ingrédients transformés via le script `predict.py`.

### Évolutions techniques
- Refactorisation pour adopter les fonctionnalités `include_edges` et de filtrage de VoLCA.
- Amélioration de la gestion des alias d'activités et d'ingrédients, avec suppression des marqueurs d'année et des suffixes inutiles.
- Correction de la logique de fusion du catalogue LCI pour préserver l'identité des activités et dédupliquer les alias.
- Adaptation à la dernière version de pyvolca.
- Extraction des paramètres de transformation pour toutes les activités du preset transformé.
- Amélioration de la gestion des collisions de noms d'affichage lors de la fusion des activités.
- Correction de bugs liés à la gestion des noms d'activités et d'ingrédients (radis, mangue, viandes BIO).
- Amélioration de la gestion des noms d'affichage pour éviter les doublons.
- Modification de la stratégie de remplacement des mixes de consommation.
- Utilisation des paramètres transformés côté serveur pour la recherche des consommateurs.

### Autres changements
- Ajout d'un fichier README pour les scripts `transformed-ingredients`.
- Documentation de la stratégie utilisée pour la gestion des données.
- Conversion de fichiers texte en Markdown.
- Ajout d'un fichier `.gitignore`.
- Mise à jour du fichier README.
- Correction de processus mal nommés.
- Suppression d'ingrédients.json de l'entraînement du prédicteur et de la recherche finale des données.
