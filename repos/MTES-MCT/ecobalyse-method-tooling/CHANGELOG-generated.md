## Changelog : ecobalyse-method-tooling (30 derniers jours, au 9 juillet 2026)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration des outils d'analyse comparative (Brightway vs VoLCA) et l'automatisation du traitement des ingrédients transformés pour l'écobilan. Des outils de diagnostic et de caractérisation des flux ont également été ajoutés.

### Évolutions fonctionnelles
- Ajout d'un outil de diagnostic de caractérisation des flux pour BAFU. [#9eb6835](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/9eb6835)
- Ajout d'un outil de comparaison Brightway vs VoLCA pour la base BAFU, incluant une option pour exclure les impacts à long terme (`--exclude-long-term`). [#242b45a](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/242b45a)
- Amélioration du processus de génération et de backfill des ingrédients transformés, avec l'ajout de rapports CSV pour la revue des variantes. [#64d555e](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/64d555e) et [#8c624fe](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/8c624fe)
- Extraction des recettes Agribalyse et ajout de fichiers README pour une meilleure documentation. [#e85b591](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/e85b591)

### Évolutions techniques
- Refactorisation de la structure des outils Brightway vs VoLCA, les déplaçant sous les répertoires `bafu/` et `food/`. [#8b4eff0](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/8b4eff0) et [#1a6ffe8](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/1a6ffe8)
- Amélioration de la gestion des alias et du tri des clés lors de la fusion du catalogue LCI. [#221ae9b](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/221ae9b)
- Suppression des clés de base de données obsolètes dans les activités générées pour les ingrédients transformés. [#0888ffb](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/0888ffb)

### Autres changements
- Mise à jour et maintenance des fichiers README. [#431771f](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/431771f)
- Documentation du workflow en 3 étapes pour la génération des ingrédients transformés. [#08d2f17](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/08d2f17)
- Enregistrement des résultats de la comparaison Brightway/VoLCA concernant la parité et un problème spécifique lié aux eaux souterraines dans VoLCA. [#ad308c1](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/ad308c1)
