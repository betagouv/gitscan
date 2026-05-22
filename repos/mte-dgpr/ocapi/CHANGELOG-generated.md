## Changelog : ocapi (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la détection des arrêtés, la gestion des conflits et la consolidation des données, notamment grâce à l'intégration d'un nouveau modèle de langage (LLM) et à des optimisations de la logique de traitement des opérations. Des améliorations significatives ont également été apportées à la documentation et à la gestion des snapshots.

### Évolutions fonctionnelles
- Amélioration de la détection des opérations sur les arrêtés ministériels, qui sont désormais exclues de la détection par le LLM. [#129](https://github.com/mte-dgpr/ocapi/issues/129)
- Gestion améliorée des suppressions complètes en cas de conflits, avec une indication de leur importance réduite. [#116](https://github.com/mte-dgpr/ocapi/issues/116)
- Ajout d'un nœud d'opération "gauche à droite" pour une meilleure représentation des relations entre les opérations. [#128](https://github.com/mte-dgpr/ocapi/issues/128)
- Affichage amélioré des étiquettes dans les diagrammes Mermaid utilisés pour la documentation.
- Suppression de l'affichage du menu déroulant pour les versions non résolues. [#125](https://github.com/mte-dgpr/ocapi/issues/125)
- Gestion des cas où le contenu source d'une opération est manquant. [#95](https://github.com/mte-dgpr/ocapi/issues/95)
- Prise en charge des niveaux romains et alphabétiques dans les identifiants d'articles. [#99](https://github.com/mte-dgpr/ocapi/issues/99)

### Évolutions techniques
- Changement du modèle de langage par défaut et reconstruction des snapshots pour améliorer la performance et la précision. [#123](https://github.com/mte-dgpr/ocapi/issues/123) et [#118](https://github.com/mte-dgpr/ocapi/issues/118)
- Refactorisation du code pour simplifier la gestion des opérations `apply_replace` et `apply_remove`. [#104](https://github.com/mte-dgpr/ocapi/issues/104)
- Mise à jour de la bibliothèque `arretify` vers la version 0.2.0. [#84](https://github.com/mte-dgpr/ocapi/issues/84)
- Amélioration de la gestion des codes d'erreur et refactorisation des helpers. [#100](https://github.com/mte-dgpr/ocapi/issues/100) et [#97](https://github.com/mte-dgpr/ocapi/issues/97)
- Nettoyage du code : suppression de fonctions inutilisées, normalisation des noms de modèles et simplification de la logique. [#124](https://github.com/mte-dgpr/ocapi/issues/124)
- Contournement d'un problème de quarantaine avec le package `mistralai` sur PyPI. [#114](https://github.com/mte-dgpr/ocapi/issues/114)
- Intégration des fichiers annexes dans l'annexe principale. [#98](https://github.com/mte-dgpr/ocapi/issues/98)

### Autres changements
- Amélioration de la documentation et ajout de scénarios de régénération de snapshots. [#131](https://github.com/mte-dgpr/ocapi/issues/131) et [#133](https://github.com/mte-dgpr/ocapi/issues/133) et [#113](https://github.com/mte-dgpr/ocapi/issues/113)
- Suppression du suivi des données de snapshot locales.
- Ajout d'un statut `NOT_AN_OPERATION` pour l'opération `ADD ALL`. [#96](https://github.com/mte-dgpr/ocapi/issues/96)
- Vérification de la cohérence des données de référence (ground truth) avec la version 0.2.0. [#93](https://github.com/mte-dgpr/ocapi/issues/93)
- Ajout d'utilitaires `arretify`. [#87](https://github.com/mte-dgpr/ocapi/issues/87)
