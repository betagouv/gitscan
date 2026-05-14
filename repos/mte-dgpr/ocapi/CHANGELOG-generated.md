## Changelog : ocapi (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement sur ocapi se sont concentrés sur l'amélioration de la gestion des arrêtés, notamment la consolidation et la résolution des conflits. Des améliorations ont été apportées à la détection des abrogations, à la gestion des annexes et à l'intégration d'arretify. L'expérience utilisateur a également été améliorée avec l'affichage des résultats des opérations directement dans les articles sources.

### Évolutions fonctionnelles
- Amélioration de la détection des abrogations pour une meilleure précision. [#85](https://github.com/mte-dgpr/ocapi/issues/85)
- Gestion améliorée des annexes, avec la fusion des fichiers annexes dans l'appendice principal. [#98](https://github.com/mte-dgpr/ocapi/issues/98)
- Acceptation des niveaux d'article romains et alphabétiques (ex: I, A). [#99](https://github.com/mte-dgpr/ocapi/issues/99)
- Affichage des résultats des opérations directement dans les articles sources pour une meilleure traçabilité. [#73](https://github.com/mte-dgpr/ocapi/issues/73)
- Prise en charge de la sélection de l'arrêté principal par son identifiant. [#94](https://github.com/mte-dgpr/ocapi/issues/94)
- Amélioration de la consolidation des arrêtés avec arretify. [#92](https://github.com/mte-dgpr/ocapi/issues/92)
- Gestion des cas où le contenu source est manquant lors d'une opération. [#95](https://github.com/mte-dgpr/ocapi/issues/95)

### Évolutions techniques
- Mise à jour de la dépendance `arretify` vers la version 0.2.0. [#84](https://github.com/mte-dgpr/ocapi/issues/84)
- Refonte du code de statut pour utiliser un ensemble figé de codes d'erreur (`ErrorCode`). [#100](https://github.com/mte-dgpr/ocapi/issues/100)
- Fusion des opérations `apply_replace` et `apply_remove`. [#104](https://github.com/mte-dgpr/ocapi/issues/104)
- Ajout d'un statut `NOT_AN_OPERATION` pour l'opération "ADD ALL". [#96](https://github.com/mte-dgpr/ocapi/issues/96)
- Amélioration de la chaîne de résolution pour les branches de taille 2. [#71](https://github.com/mte-dgpr/ocapi/issues/71)
- Suppression de l'enveloppe de section du contenu. [#69](https://github.com/mte-dgpr/ocapi/issues/69)
- Remplacement du mock LLM par un statut `DISABLED_LLM_CALL`. [#79](https://github.com/mte-dgpr/ocapi/issues/79)
- Validation du sous-cible pour les opérations ciblant "ALL". [#81](https://github.com/mte-dgpr/ocapi/issues/81)
- Amélioration des règles de détection d'abrogation. [#85](https://github.com/mte-dgpr/ocapi/issues/85)
- Propagation du `status_code` aux opérations. [#68](https://github.com/mte-dgpr/ocapi/issues/68)
- Ajout de la prise en charge du fournisseur Google/Gemini et des benchmarks LLM. [#74](https://github.com/mte-dgpr/ocapi/issues/74)

### Autres changements
- Mise à jour de la documentation wiki. [#113](https://github.com/mte-dgpr/ocapi/issues/113)
- Correction d'étiquettes de flèches pointillées dans Mermaid.
- Correction d'étiquettes Mermaid dans la documentation.
- Contournement d'une quarantaine pypi pour MistralAI. [#114](https://github.com/mte-dgpr/ocapi/issues/114)
- Suppression des répertoires de données de snapshot locaux non suivis.
- Amélioration des tests et des snapshots.
- Ajout de la déclaration de la dépendance `arretify` et exigence de Python 3.12. [#70](https://github.com/mte-dgpr/ocapi/issues/70)
- Mise à jour de la section README et ajout de la prise en charge du fournisseur Google/Gemini.
- Amélioration de la comparaison HTML exacte dans les tests de snapshot. [#67](https://github.com/mte-dgpr/ocapi/issues/67)
- Suppression de fichiers xlsx de sortie d'évaluation du gitignore.
- Correction de noms de tests manquants dans les underscores.
- Correction d'erreurs mypy dans `make_other_test`.
- Suppression de filtres superflus. [#58](https://github.com/mte-dgpr/ocapi/issues/58)
