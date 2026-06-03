## Changelog : archeologia-pipeline (30 derniers jours, au 28 mai 2026)

### Résumé
Cette version apporte une refonte majeure de l'interface utilisateur, avec l'introduction d'un nouveau wizard en 4 étapes pour simplifier le processus de traitement des données LiDAR. Des améliorations significatives ont également été apportées à la gestion des annulations de tâches, à la configuration des indices et à la robustesse générale du pipeline.

### Évolutions fonctionnelles
- Ajout d'un dialogue d'information sur les modèles IA programmés dans l'interface utilisateur [#7a6037b](https://github.com/betagouv/archeologia-pipeline/commit/7a6037b).
- Implémentation de seuils de confiance par entité pour la détection d'éléments archéologiques, avec impact sur la symbologie et le filtrage des résultats [#0ceaa4a](https://github.com/betagouv/archeologia-pipeline/commit/0ceaa4a).
- Possibilité de paramétrer le nommage des indices et des cibles dérivées [#075d516](https://github.com/betagouv/archeologia-pipeline/commit/075d516).
- Refonte complète de l'interface utilisateur avec un nouveau wizard en 4 étapes : source, indices, détection et lancement [#d9c3f3d](https://github.com/betagouv/archeologia-pipeline/commit/d9c3f3d).
- Amélioration de la barre de progression pour une meilleure lisibilité [#36696ad](https://github.com/betagouv/archeologia-pipeline/commit/36696ad).
- Ajout de la possibilité de persister les préférences de l'interface utilisateur et les classes de détection sélectionnées [#edf7e7b](https://github.com/betagouv/archeologia-pipeline/commit/edf7e7b).
- Renommage du plugin QGIS en « Archéolog'IA » [#2810854](https://github.com/betagouv/archeologia-pipeline/commit/2810854).

### Évolutions techniques
- Refactorisation majeure de l'architecture du pipeline, notamment au niveau de la gestion des runners, des modèles et des logs [#d427194](https://github.com/betagouv/archeologia-pipeline/commit/d427194).
- Implémentation d'un mécanisme d'annulation de tâches plus précis et flexible, permettant d'annuler des opérations spécifiques comme la conversion de fichiers ou le traitement par dalles [#69ca39d](https://github.com/betagouv/archeologia-pipeline/commit/69ca39d), [#c3939f7](https://github.com/betagouv/archeologia-pipeline/commit/c3939f7), [#de622bc](https://github.com/betagouv/archeologia-pipeline/commit/de622bc).
- Amélioration de la gestion des erreurs et des validations des paramètres d'entrée [#bddea2e](https://github.com/betagouv/archeologia-pipeline/commit/bddea2e).
- Correction de problèmes d'importation circulaire et d'imports absolus qui pouvaient causer des erreurs dans QGIS [#72920fe](https://github.com/betagouv/archeologia-pipeline/commit/72920fe).
- Amélioration de la gestion des fichiers VRT pour éviter les problèmes de régénération d'index [#cc0cc82](https://github.com/betagouv/archeologia-pipeline/commit/cc0cc82).

### Autres changements
- Mise à jour de la documentation (README et CLAUDE.md) pour refléter les changements apportés au pipeline [#74c6c28](https://github.com/betagouv/archeologia-pipeline/commit/74c6c28), [#3e06756](https://github.com/betagouv/archeologia-pipeline/commit/3e06756).
- Mise à jour des checksums Talisman pour corriger les faux positifs et intégrer les nouveaux fichiers [#5ef60e5](https://github.com/betagouv/archeologia-pipeline/commit/5ef60e5), [#8d44677](https://github.com/betagouv/archeologia-pipeline/commit/8d44677), [#393f8d0](https://github.com/betagouv/archeologia-pipeline/commit/393f8d0), [#a756b4f](https://github.com/betagouv/archeologia-pipeline/commit/a756b4f).
- Correction de la version affichée dans le README [#71e1b58](https://github.com/betagouv/archeologia-pipeline/commit/71e1b58).
- Ajout de tests et de linters pour améliorer la qualité du code [#04ea14b](https://github.com/betagouv/archeologia-pipeline/commit/04ea14b).
