## Changelog : ecobalyse-method-tooling (30 derniers jours)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration de la gestion des données d'ingrédients, notamment la génération et la mise à jour des fichiers de données pour les ingrédients français et internationaux. Des corrections ont été apportées pour améliorer la classification des aliments et la gestion des suffixes pour distinguer les anciennes et nouvelles versions des données. L'outil a également été optimisé pour gérer les fusions de données et éviter les conflits.

### Évolutions fonctionnelles
- Correction de la classification de certains produits laitiers qui étaient incorrectement classés comme de la viande. [#16db8ef](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/16db8ef)
- Amélioration de la correspondance des groupes de cultures, évitant les erreurs sur les entrées de terres en jachère. [#5b876d5](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/5b876d5)
- Correction des noms des activités ICV. [#de09b79](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/de09b79)
- Mise à jour des fichiers CSV sources pour la France et les ingrédients internationaux. [#b623cba](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/b623cba), [#3ae03d6](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/3ae03d6)
- Régénération des ingrédients OI. [#ebcc4b3](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/ebcc4b3)
- Nouvelle génération FR. [#965b5ab](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/965b5ab)
- Ajout d'un suffixe aux noms de fichiers de sortie pour distinguer les variantes. [#6b241c4](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/6b241c4)
- Renommage du fichier de sortie final en `fichier_final_{variant}.csv`. [#39066c1](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/39066c1)

### Évolutions techniques
- Correction d'une régression suite à un changement de dimension FoodOn pour les légumineuses. [#480fa8b](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/480fa8b)
- Correction pour permettre aux ingrédients ré-exportés de remplacer les existants lors de la fusion. [#7932041](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7932041)
- Amélioration de la gestion des clés dans `feed.json` lors de la suffixation/désuffixation des alias d'activité. [#6f7ba5f](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/6f7ba5f), [#9549c6c](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/9549c6c)
- Modification du marquage des alias, passant d'un préfixe "new-" à un suffixe "-2025" pour les anciens ingrédients. [#feb83b4](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/feb83b4)
- Correction pour ne pas supprimer les suffixes 2025 existants lorsque l'option `--add-old-suffix` n'est pas utilisée. [#171683f](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/171683f)
- Correction pour inclure la colonne de localisation du fil dans les activités générées. [#b01781d](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/b01781d)
- Suppression des activités orphelines. [#29ba1b4](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/29ba1b4)

### Autres changements
- Mise à jour de la documentation README pour refléter le code actuel (dimensions, ordre NOVA, colonnes, flux de données). [#7e33a2d](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7e33a2d)
- Correction de la documentation de la fonction `_extract_ingredient_values`. [#fd78bca](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/fd78bca)
- Ajout du fichier `.envrc` à `.gitignore`. [#3019751](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/3019751)
- Mise à jour de la configuration pour les tournesols. [#0d03056](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/0d03056)
- Correction des choix de processus pour certains ingrédients. [#8ce6d66](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/8ce6d66)
- Ajout d'un nouveau fichier de sortie. [#712709c](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/712709c)
- Finalisation des fichiers. [#141b2f1](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/141b2f1)
