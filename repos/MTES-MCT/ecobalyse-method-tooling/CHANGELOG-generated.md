## Changelog : ecobalyse-method-tooling (30 derniers jours)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration du processus de fusion des données d'ingrédients, notamment en gérant les anciens et nouveaux identifiants, et en affinant la classification des produits agricoles. Des corrections de bugs ont également été apportées pour améliorer la précision de la classification et la gestion des données.

### Évolutions fonctionnelles
- Amélioration de la prédiction du groupe de cultures (cropGroup) grâce à des données de référence RPG 28. (#1f98e12)
- Correction d'une classification erronée des produits laitiers comme étant de la viande. (#16db8ef)
- Correction d'un problème empêchant la correspondance correcte des groupes de cultures sur les entrées de terres de jachère. (#5b876d5)
- Correction de l'attribution de la colonne de localisation des cultures à partir du CSV dans les activités générées. (#b01781d)
- Les ingrédients exportés remplacent désormais les ingrédients existants lors de la fusion. (#7932041)
- Préservation des métadonnées non alimentaires (textiles, etc.) lors de la fusion. (#316dfd9)

### Évolutions techniques
- Refactorisation de la fonction `merge_activities` pour utiliser des dictionnaires plats et des clés de fusion basées sur l'UUID. (#b8f6acd)
- Simplification de la gestion des variables d'environnement en utilisant des chemins de base `ECOBALYSE_DATA` et `ECOBALYSE`. (#c70285e)
- Mise à jour de la gestion des suffixes pour les anciens ingrédients, passant d'un préfixe "new-" à un suffixe "-2025". (#feb83b4)
- Modification de la manière dont les clés sont renommées dans `feed.json` pour utiliser les alias des ingrédients au lieu des alias des activités. (#99c27ad)
- Correction du renommage des clés dans `feed.json` et remplacement de l'option `--remove-old-suffix` par la commande `remove-old`. (#9549c6c)
- Mise à jour des clés dans `feed.json` lors de l'ajout de suffixes/suppression de suffixes aux alias d'activités. (#6f7ba5f)
- Ajout du fichier `.envrc` à `.gitignore`. (#3019751)

### Autres changements
- Mise à jour des fichiers CSV sources. (#3ae03d6)
- Mise à jour du fichier `README` avec les variables d'environnement actuelles et l'utilisation de l'interface en ligne de commande. (#7348048)
- Renommage du fichier de sortie final en `fichier_final_{variant}.csv`. (#39066c1)
- Ajout d'un suffixe de variante aux noms des fichiers de sortie générés. (#6b241c4)
- Correction de l'absence de suppression des suffixes 2025 existants lorsque l'option `--add-old-suffix` n'est pas utilisée. (#171683f)
- Mention dans la documentation de n'utiliser l'option `--add-old-suffix` que sur la première variante. (#2dd151f)
- Correction des choix de processus pour certains ingrédients. (#8ce6d66)
- Nouvelle sortie. (#712709c)
- Suppression des doublons d'ingrédients par `displayName` entre les fichiers lors de la fusion. (#b88dfe2)
- Consolidation des activités par `activityName` lors de la fusion. (#ff61dfc)
- Mise à jour des données de tournesol. (#0d03056)
