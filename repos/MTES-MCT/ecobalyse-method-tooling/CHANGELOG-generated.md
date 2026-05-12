## Changelog : ecobalyse-method-tooling (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des données, notamment l'intégration de nouvelles variantes de données (HUE, NUE, UE), la correction de problèmes liés à la correspondance des données et l'optimisation des processus de transformation et de fusion des données. Plusieurs améliorations ont été apportées à l'outil d'exportation et à la gestion des alias d'activités et d'ingrédients.

### Évolutions fonctionnelles
- Intégration de la variante HUE (High Uncertainty Estimation) pour les ingrédients.
- Ajout de la variante NUE (Nouvelles Unités Énergétiques) et régénération des ingrédients transformés.
- Intégration de la variante UE (Unités Économiques) avec ajout des fichiers CSV sources et des protections contre les erreurs de fusion/orphelins.
- Amélioration de la correspondance des ingrédients et des activités, notamment en pénalisant les références multi-mots bruyantes et en exigeant un chevauchement textuel.
- Correction de problèmes de correspondance pour certains ingrédients spécifiques (mangue, radis, viandes BIO).
- Amélioration de la gestion des noms d'affichage des activités pour garantir leur unicité.
- Ajout d'une colonne `is_byproduct` et actualisation des sorties avec les co-produits d'allocation.
- Ajout d'une colonne `dummy_op` et actualisation des sorties à partir de la descente en couches.
- Possibilité de prédire les métadonnées des ingrédients transformés via le script `predict.py`.

### Évolutions techniques
- Refactorisation du script `export.py` pour unifier la logique des variantes, typifier le flux de données et différer les effets secondaires.
- Amélioration de la fusion du catalogue LCI, préservant l'identité des activités `-2025` et dédupliquant les alias inter-sources.
- Adaptation aux dernières versions de la librairie pyvolca.
- Refactorisation pour adopter les fonctionnalités `include_edges` et de filtrage de VoLCA.
- Extraction des primitives de fusion du catalogue LCI et intégration du générateur d'ingrédients transformés.
- Suppression des ingrédients.json de l'entraînement du prédicteur et de la recherche finale des données.
- Simplification de la gestion des alias d'activités et d'ingrédients en supprimant les marqueurs d'année et les marqueurs `{{archive-alias}}`.
- Utilisation de la transformation des presets côté serveur pour la recherche des consommateurs.
- Correction de la gestion des noms d'activités lors des collisions lors de la fusion.
- Amélioration de la gestion des paramètres de transformation pour les activités transformées.

### Autres changements
- Ajout d'un fichier README pour les scripts `transformed-ingredients`.
- Documentation de la stratégie utilisée pour la gestion des noms d'affichage.
- Conversion de fichiers texte en Markdown.
- Ajout d'un snapshot des ingrédients transformés générés comme base de référence.
- Correction de noms de processus incorrects.
- Mise à jour des fichiers sources.
- Suppression de fichiers inutiles du `.gitignore`.
- Amélioration de la gestion des espaces de noms des ingrédients.
