## Changelog : ecobalyse-method-tooling (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration significative de l'outil `transformed-ingredients`, qui permet de transformer et de gérer les données d'ingrédients pour l'écobilan. Les améliorations incluent une meilleure gestion des alias, une résolution plus précise des données VoLCA, et la génération de rapports CSV pour faciliter la revue des données transformées. Des corrections ont également été apportées pour améliorer la cohérence et la précision des données.

### Évolutions fonctionnelles
- Amélioration de la gestion des alias dans `transformed-ingredients` pour une meilleure correspondance des données. [#221ae9b](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/221ae9b)
- Ajout d'un rapport CSV par variante dans `transformed-ingredients` pour faciliter la revue des données transformées. [#64d555e](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/64d555e)
- Génération de rapports CSV plus concis et backfill ECS depuis le pipeline dans `transformed-ingredients`. [#8c624fe](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/8c624fe)
- Suppression de la soja de la variante BIO. [#0ee7b9b](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/0ee7b9b)

### Évolutions techniques
- Refonte de la génération des ingrédients transformés avec une nouvelle approche en 3 étapes (génération, pipeline, backfill ECS). [#53eef25](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/53eef25) et [#08d2f17](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/08d2f17)
- Amélioration de la résolution VoLCA dans `transformed-ingredients`. [#c174dfa](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/c174dfa)
- Dérivation de tous les inputs du chemin du dépôt Ecobalyse dans `transformed-ingredients`. [#89d9915](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/89d9915)
- Mise à jour de la bibliothèque `transformers` vers la version 5.x. [#e46bea9](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/e46bea9)
- Correction de collisions de `displayName` entre différents lots dans `lci_catalog`. [#39304da](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/39304da)
- Suppression des clés de base de données obsolètes des `generated_activities.json`. [#0888ffb](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/0888ffb)
- Suppression d'une clé de base de données redondante au niveau supérieur. [#27ebf53](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/27ebf53)

### Autres changements
- Mise à jour de la documentation de `transformed-ingredients` pour refléter les changements apportés et l'intégration du dépôt `ecobalyse-data`. [#172190d](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/172190d)
- Mise à jour des chemins dans le README de `transformed-ingredients` suite à la fusion du dépôt `ecobalyse-data`. [#3fa0659](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/3fa0659)
- Correction de vulnérabilités dans les dépendances. [#d90e144](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/d90e144)
- Mise à jour des packages. [#3e7e52d](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/3e7e52d)
