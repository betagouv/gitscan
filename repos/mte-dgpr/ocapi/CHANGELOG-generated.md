## Changelog : ocapi (30 derniers jours, au 03 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse et la précision du pipeline de traitement des arrêtés préfectoraux. Des améliorations ont été apportées à la détection des opérations, à la gestion des dates limites, et à la comparaison des résultats HTML. La dépendance à `arretify` a été mise à jour et des tests ont été ajoutés pour garantir la qualité du code.

### Évolutions fonctionnelles
- Amélioration de la détection des dates limites et ajout de prompts de secours en cas d'échec [#63](https://github.com/mte-dgpr/ocapi/issues/63).
- Gestion améliorée des identifiants d'articles non standards lors du rendu [#61](https://github.com/mte-dgpr/ocapi/issues/61).
- Prise en charge des identifiants d'articles contenant des chiffres romains et des lettres [#99](https://github.com/mte-dgpr/ocapi/issues/99).
- Affichage des résultats des opérations dans les articles sources [#73](https://github.com/mte-dgpr/ocapi/issues/73) et [#473](https://github.com/mte-dgpr/ocapi/issues/473).
- Amélioration de la détection des abrogations [#85](https://github.com/mte-dgpr/ocapi/issues/85).
- Prise en charge de la sélection de l'arrêté principal par son identifiant [#94](https://github.com/mte-dgpr/ocapi/issues/94).
- Gestion du cas où le contenu source est manquant lors d'une opération [#95](https://github.com/mte-dgpr/ocapi/issues/95).

### Évolutions techniques
- Mise à jour de la dépendance `arretify` vers la version 0.2.0 [#84](https://github.com/mte-dgpr/ocapi/issues/84).
- Refonte du code de statut pour utiliser un ensemble figé d'ErrorCode [#100](https://github.com/mte-dgpr/ocapi/issues/100).
- Remplacement de l'utilisation de `REPLACE ALL` par `REMOVE` lors de la détection [#66](https://github.com/mte-dgpr/ocapi/issues/66).
- Amélioration des tests avec une comparaison HTML exacte au lieu d'exemples [#67](https://github.com/mte-dgpr/ocapi/issues/67) et [#428](https://github.com/mte-dgpr/ocapi/issues/428).
- Ajout d'un benchmark pour l'évaluation des modèles LLM [#74](https://github.com/mte-dgpr/ocapi/issues/74).
- Suppression du wrapper de section du contenu [#69](https://github.com/mte-dgpr/ocapi/issues/69).
- Suppression des fichiers de snapshot locaux non suivis.
- Suppression du dossier `.vscode` du suivi git [#65](https://github.com/mte-dgpr/ocapi/issues/65).
- Ajout de la prise en charge du fournisseur Google/Gemini [#76](https://github.com/mte-dgpr/ocapi/issues/76).
- Exigence de Python 3.12 et déclaration de la dépendance `arretify` [#70](https://github.com/mte-dgpr/ocapi/issues/70) et [#56](https://github.com/mte-dgpr/ocapi/issues/56).

### Autres changements
- Ajout d'une liste plus complète de verbes d'opération dans les prompts [#60](https://github.com/mte-dgpr/ocapi/issues/60) et [#435](https://github.com/mte-dgpr/ocapi/issues/435) et [#401](https://github.com/mte-dgpr/ocapi/issues/401) et [#0a5de0a](https://github.com/mte-dgpr/ocapi/commit/0a5de0a).
- Mise à jour de la documentation README avec la prise en charge du fournisseur Google/Gemini [#87](https://github.com/mte-dgpr/ocapi/issues/87).
- Correction de noms de tests manquants et d'erreurs mypy.
- Suppression de filtres superflus.
- Ajout d'une configuration pour le fournisseur Google.
- Amélioration de la validation de la subcible pour toutes les opérations [#81](https://github.com/mte-dgpr/ocapi/issues/81).
- Désactivation temporaire de l'appel LLM en cas de problème [#79](https://github.com/mte-dgpr/ocapi/issues/79).
