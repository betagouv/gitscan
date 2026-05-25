## Changelog : archeologia-pipeline (30 derniers jours, au 18 mai 2026)

### Résumé
Cette version majeure (0.2.0) apporte une refonte architecturale complète du pipeline, améliorant significativement sa maintenabilité, sa testabilité et son expérience utilisateur. Les améliorations incluent une nouvelle gestion des configurations, une meilleure validation des paramètres, une interface utilisateur plus réactive et une gestion des logs plus informative.  Le nom du plugin a également été mis à jour en "Archéolog'IA".

### Évolutions fonctionnelles
- **Nom du plugin modifié :** Le plugin s'appelle désormais "Archéolog'IA" dans QGIS. [#2810854](https://github.com/betagouv/archeologia-pipeline/commit/2810854)
- **Gestion des paramètres d'audit :** Amélioration de la coercition, de la traçabilité et de la gestion des avertissements pour les paramètres d'audit. [#bddea2e](https://github.com/betagouv/archeologia-pipeline/commit/bddea2e)
- **Gestion des filtres PDAL :**  Amélioration de la gestion des filtres PDAL vides, avec un retour vers le filtre par défaut en cas de problème et une indication dans l'interface utilisateur. [#d34792a](https://github.com/betagouv/archeologia-pipeline/commit/d34792a)
- **Persistance des préférences UI :** Les préférences de l'interface utilisateur et les classes de détection CV sélectionnées sont maintenant persistantes. [#edf7e7b](https://github.com/betagouv/archeologia-pipeline/commit/edf7e7b)
- **Prise en charge des clusters :** Ajout de la prise en charge des clusters dans le post-processing. [#70cf18a](https://github.com/betagouv/archeologia-pipeline/commit/70cf18a)

### Évolutions techniques
- **Refonte architecturale majeure :**  Refactorisation complète de l'architecture du pipeline pour une meilleure modularité, testabilité et maintenabilité. (10 commits) [#9fbcc89](https://github.com/betagouv/archeologia-pipeline/commit/9fbcc89)
- **Validation centralisée du RunContext :** Mise en place d'une validation centralisée du contexte d'exécution (RunContext) avec des dataclasses typées. [#bf875b8](https://github.com/betagouv/archeologia-pipeline/commit/bf875b8)
- **Gestion des logs améliorée :** Implémentation d'un système de logs dual (UI et fichier) avec différents niveaux de granularité. [#20137ff](https://github.com/betagouv/archeologia-pipeline/commit/20137ff)
- **Refactorisation du module de détection CV :**  Refactorisation importante du module de détection par Computer Vision, avec extraction de composants réutilisables et une meilleure organisation du code. (plusieurs commits) [#f6a944a](https://github.com/betagouv/archeologia-pipeline/commit/f6a944a)
- **Suppression de `tile_splitter` :** Suppression du composant `tile_splitter` pour simplifier le code et améliorer la testabilité. [#91638af](https://github.com/betagouv/archeologia-pipeline/commit/91638af)
- **Amélioration des imports :** Correction des problèmes d'imports circulaires et utilisation d'imports relatifs pour éviter les erreurs dans QGIS. [#72920fe](https://github.com/betagouv/archeologia-pipeline/commit/72920fe)

### Autres changements
- **Documentation mise à jour :** Mise à jour complète de la documentation du projet, incluant un document CLAUDE.md détaillé et une synchronisation avec l'état actuel du code. [#3e06756](https://github.com/betagouv/archeologia-pipeline/commit/3e06756)
- **Linting avec Ruff :** Ajout de linting avec Ruff pour améliorer la qualité du code. [#04ea14b](https://github.com/betagouv/archeologia-pipeline/commit/04ea14b)
- **Mise à jour des checksums Talisman :** Mise à jour des checksums Talisman pour les fichiers modifiés. [#f3b5e05](https://github.com/betagouv/archeologia-pipeline/commit/f3b5e05) et [#a92bb51](https://github.com/betagouv/archeologia-pipeline/commit/a92bb51)
- **Ajout de pyyaml aux dépendances de test :** Ajout de `pyyaml` aux dépendances de test. [#d07e659](https://github.com/betagouv/archeologia-pipeline/commit/d07e659)
