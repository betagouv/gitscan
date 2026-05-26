## Changelog : acces-cible (30 derniers jours, au 25 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la stabilité et de la performance de l'application, notamment lors de l'importation de fichiers CSV et de l'exécution de requêtes SQL. Des améliorations de l'interface utilisateur ont également été apportées avec l'intégration d'un composant de menu latéral du DSFR.

### Évolutions fonctionnelles
- Stabilisation des imports CSV : Le traitement des fichiers CSV a été amélioré en le déplaçant vers une tâche en arrière-plan, améliorant ainsi la réactivité de l'application. [#541](https://github.com/betagouv/acces-cible/issues/541)

### Évolutions techniques
- Optimisation des requêtes SQL : Correction de problèmes de requêtes SQL N+1 pour améliorer les performances. [#538](https://github.com/betagouv/acces-cible/issues/538)
- Refactoring du navigateur : Refactorisation du code lié au navigateur. [#545](https://github.com/betagouv/acces-cible/issues/545)
- Nettoyage du code : Suppression de code mort et de dépendances inutilisées pour simplifier la base de code. [#542](https://github.com/betagouv/acces-cible/issues/542)
- Intégration du composant DSFR Side Menu : Utilisation du composant de menu latéral du Design System des Finances Publiques (DSFR) pour une meilleure cohérence visuelle. [#571](https://github.com/betagouv/acces-cible/issues/571)
- Suppression de la logique `current` : Suppression de la logique liée à `current` dans le code. [#573](https://github.com/betagouv/acces-cible/issues/573)

### Autres changements
- Migration pour compléter les URLs des sites : Ajout et annulation de plusieurs migrations pour compléter les URLs des sites dans la base de données. [#530](https://github.com/betagouv/acces-cible/issues/530), [#553](https://github.com/betagouv/acces-cible/issues/553), [#555](https://github.com/betagouv/acces-cible/issues/555), [#556](https://github.com/betagouv/acces-cible/issues/556), [#557](https://github.com/betagouv/acces-cible/issues/557), [#558](https://github.com/betagouv/acces-cible/issues/558), [#551](https://github.com/betagouv/acces-cible/issues/551), [#554](https://github.com/betagouv/acces-cible/issues/554)
- Correction d'une faute de frappe dans `queue.yml`. [#567](https://github.com/betagouv/acces-cible/issues/567)
