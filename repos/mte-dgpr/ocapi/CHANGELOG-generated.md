## Changelog : ocapi (30 derniers jours, au 2026-05-19)

### Résumé
Les dernières mises à jour d'ocapi se concentrent sur l'amélioration de la consolidation des arrêtés préfectoraux, notamment en gérant mieux les conflits et les opérations d'abrogation. Des améliorations ont également été apportées à la gestion des annexes, à la reconnaissance des identifiants d'articles et à l'intégration avec la librairie arretify. Des corrections et des optimisations diverses ont été implémentées pour améliorer la robustesse et la précision du pipeline.

### Évolutions fonctionnelles
- Amélioration de la gestion des conflits lors de la consolidation des arrêtés, en marquant les suppressions complètes conflictuelles comme moins importantes [#116](https://github.com/mte-dgpr/ocapi/issues/116).
- Gestion améliorée des opérations d'ajout de tous les éléments, avec l'ajout d'un statut `NOT_AN_OPERATION` [#96](https://github.com/mte-dgpr/ocapi/issues/96).
- Prise en charge des identifiants d'articles contenant des chiffres romains et des lettres [#99](https://github.com/mte-dgpr/ocapi/issues/99).
- Gestion du contenu source manquant pour certaines opérations [#95](https://github.com/mte-dgpr/ocapi/issues/95).
- Intégration des fichiers d'annexe dans l'appendice de base [#98](https://github.com/mte-dgpr/ocapi/issues/98).
- Amélioration de la détection des abrogations [#85](https://github.com/mte-dgpr/ocapi/issues/85).
- Consolidation des arrêtés via arretify [#92](https://github.com/mte-dgpr/ocapi/issues/92).

### Évolutions techniques
- Refactorisation et nettoyage du code, incluant les noms de modèles, l'AP principal, rawop et les fonctions inutilisées [#124](https://github.com/mte-dgpr/ocapi/issues/124).
- Fusion des fonctions `apply_replace` et `apply_remove` avec des modifications mineures [#104](https://github.com/mte-dgpr/ocapi/issues/104).
- Mise à jour de la librairie `arretify` vers la version 0.2.0 [#84](https://github.com/mte-dgpr/ocapi/issues/84).
- Amélioration de la propagation du code de statut (`status_code`) aux opérations et autres [#68](https://github.com/mte-dgpr/ocapi/issues/68).
- Refonte du `status_code` en `ErrorCode` (frozenset) [#100](https://github.com/mte-dgpr/ocapi/issues/100).
- Amélioration de la résolution en chaîne pour les branches de taille 2 [#71](https://github.com/mte-dgpr/ocapi/issues/71).
- Correction des labels des flèches pointillées dans Mermaid et des labels dans la documentation [#113](https://github.com/mte-dgpr/ocapi/issues/113).
- Correction d'un problème lié à la quarantaine de pypi pour MistralAI [#114](https://github.com/mte-dgpr/ocapi/issues/114).

### Autres changements
- Mise à jour de la licence et renommage de certaines fonctions helpers [#97](https://github.com/mte-dgpr/ocapi/issues/97).
- Ajout d'un appendice dans "other" [#102](https://github.com/mte-dgpr/ocapi/issues/102).
- Suppression du suivi des données de snapshot locales [#103059](https://github.com/mte-dgpr/ocapi/commit/0103059).
- Amélioration des utilitaires arretify [#87](https://github.com/mte-dgpr/ocapi/issues/87).
- Vérification de la vérité terrain 0.2.0 [#93](https://github.com/mte-dgpr/ocapi/issues/93).
- Sélection de l'identifiant de l'arrêté principal [#94](https://github.com/mte-dgpr/ocapi/issues/94).
- Correction de la configuration du LLM et des tests [#126](https://github.com/mte-dgpr/ocapi/issues/126).
