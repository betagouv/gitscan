## Changelog : ocapi (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse du pipeline de traitement des arrêtés préfectoraux, notamment en améliorant la détection des opérations, la gestion des conflits et la qualité des permis générés. Des efforts ont également été faits pour améliorer la documentation et la configuration du projet, ainsi que pour optimiser l'utilisation du modèle de langage (LLM) pour la détection des opérations.

### Évolutions fonctionnelles
- Correction de l'affichage des messages d'opérations en double dans les permis générés [#130](https://github.com/mte-dgpr/ocapi/issues/130).
- Amélioration de la gestion des opérations sur les arrêtés inexistants : elles sont maintenant marquées comme `MISSING_ARRETE` [#149](https://github.com/mte-dgpr/ocapi/issues/149).
- Ajout des coûts PIAG dans la génération des permis [#146](https://github.com/mte-dgpr/ocapi/issues/146).
- Correction des liens dans la documentation [#151](https://github.com/mte-dgpr/ocapi/issues/151).
- Exclusion des opérations d'arrêtés ministériels de la détection par LLM, améliorant ainsi la précision [#129](https://github.com/mte-dgpr/ocapi/issues/129).
- Amélioration de la gestion des suppressions complètes en cas de conflits, en les marquant comme moins importantes [#116](https://github.com/mte-dgpr/ocapi/issues/116).
- Ajout d'un statut `NOT_AN_OPERATION` pour l'opération `ADD ALL` [#96](https://github.com/mte-dgpr/ocapi/issues/96).
- Amélioration de la consolidation des arrêtés avec arretify [#92](https://github.com/mte-dgpr/ocapi/issues/92).

### Évolutions techniques
- Changement du modèle de langage par défaut et reconstruction des snapshots pour améliorer la performance et la précision [#123](https://github.com/mte-dgpr/ocapi/issues/123).
- Refactorisation du code pour standardiser la variable `updated_op`.
- Amélioration de la gestion des erreurs de suppression complète.
- Amélioration de la documentation du graphe LLM et de la régénération des snapshots [#131](https://github.com/mte-dgpr/ocapi/issues/131), [#133](https://github.com/mte-dgpr/ocapi/issues/133).
- Suppression des dropdowns pour les versions non résolues [#125](https://github.com/mte-dgpr/ocapi/issues/125).
- Ajout d'un nœud d'opération de gauche à droite [#128](https://github.com/mte-dgpr/ocapi/issues/128).
- Nettoyage du code (noms de modèles, principal AP, rawop, fonctions inutilisées) [#124](https://github.com/mte-dgpr/ocapi/issues/124).
- Mise en place d'un contournement pour une quarantaine pypi de MistralAI [#114](https://github.com/mte-dgpr/ocapi/issues/114).
- Fusion des opérations `apply_replace` et `apply_remove` avec des modifications mineures [#104](https://github.com/mte-dgpr/ocapi/issues/104).

### Autres changements
- Amélioration de la documentation générale du projet et du wiki [#113](https://github.com/mte-dgpr/ocapi/issues/113).
- Correction des labels Mermaid dans la documentation [#150](https://github.com/mte-dgpr/ocapi/issues/150).
- Correction de liens dans la documentation.
- Amélioration de la docstring.
- Régénération des snapshots après rebasage.
- Correction de la déduplication des messages d'opération sur les sections dupliquées et ajout d'un avertissement et saut de l'historique sur les articles dupliqués.
