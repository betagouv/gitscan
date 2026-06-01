## Changelog : ocapi (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la qualité du rendu des permis consolidés, la gestion des conflits et la précision de la détection des opérations réglementaires. Des optimisations ont également été apportées à l'utilisation du modèle de langage (LLM) et à la visualisation des graphes de dépendances.

### Évolutions fonctionnelles
- Correction d'un bug affichant des messages d'opération en double dans les permis générés [#130](https://github.com/mte-dgpr/ocapi/issues/130).
- Amélioration de la gestion des suppressions complètes d'arrêtés en les marquant comme moins importantes en cas de conflit [#116](https://github.com/mte-dgpr/ocapi/issues/116).
- Ajout d'un statut `NOT_AN_OPERATION` pour l'opération "ADD ALL" [#96](https://github.com/mte-dgpr/ocapi/issues/96).
- Gestion améliorée du contenu source manquant pour certaines opérations [#95](https://github.com/mte-dgpr/ocapi/issues/95).
- Suppression de l'affichage du menu déroulant pour les versions non résolues [#125](https://github.com/mte-dgpr/ocapi/issues/125).
- Ajout d'un nœud "gauche à droite" pour les opérations [#128](https://github.com/mte-dgpr/ocapi/issues/128).

### Évolutions techniques
- Exclusion des opérations d'arrêté ministériel de la détection par LLM, améliorant ainsi la précision [#129](https://github.com/mte-dgpr/ocapi/issues/129) et [#123](https://github.com/mte-dgpr/ocapi/issues/123).
- Changement du modèle LLM par défaut et régénération des snapshots pour une meilleure performance et précision [#123](https://github.com/mte-dgpr/ocapi/issues/123).
- Refactorisation du code : nettoyage des noms de modèles, du principal AP, des opérations brutes et des fonctions inutilisées [#124](https://github.com/mte-dgpr/ocapi/issues/124).
- Fusion des branches `apply_replace` et `apply_remove` pour simplifier la logique de consolidation [#104](https://github.com/mte-dgpr/ocapi/issues/104).
- Amélioration de la documentation et des diagrammes Mermaid pour une meilleure lisibilité et compréhension [#113](https://github.com/mte-dgpr/ocapi/issues/113), [#131](https://github.com/mte-dgpr/ocapi/issues/131) et [#133](https://github.com/mte-dgpr/ocapi/issues/133).
- Contournement d'une quarantaine pypi de MistralAI pour assurer la continuité des tests [#114](https://github.com/mte-dgpr/ocapi/issues/114).
- Correction des labels des flèches pointillées dans les diagrammes Mermaid [#113](https://github.com/mte-dgpr/ocapi/issues/113).

### Autres changements
- Intégration de la consolidation d'arrêtés avec arretify [#92](https://github.com/mte-dgpr/ocapi/issues/92).
- Régénération des snapshots après rebasage.
- Correction de messages de warning et gestion des articles en doublon.
