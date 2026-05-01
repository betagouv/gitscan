## Changelog : ocapi (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse et la précision du pipeline de traitement des arrêtés préfectoraux. Des améliorations ont été apportées à la détection des abrogations, à la gestion des identifiants d'articles, et à la consolidation des documents. L'intégration avec la librairie `arretify` a été mise à jour, et des tests ont été ajoutés pour garantir la qualité du code.

### Évolutions fonctionnelles
- Amélioration de la détection des dates limites et ajout de prompts de secours pour une meilleure précision.
- Gestion améliorée des identifiants d'articles non standard dans le rendu des documents [#61](https://github.com/mte-dgpr/ocapi/issues/61).
- Prise en charge des identifiants d'articles utilisant des niveaux romains et alphabétiques [#99](https://github.com/mte-dgpr/ocapi/issues/99).
- Affichage des résultats des opérations directement dans les articles sources [#73](https://github.com/mte-dgpr/ocapi/issues/73) et [#442](https://github.com/mte-dgpr/ocapi/issues/442).
- Amélioration de la détection des doublons [#55](https://github.com/mte-dgpr/ocapi/issues/55).
- Suppression des titres de section redondants lors de la consolidation des documents [#53](https://github.com/mte-dgpr/ocapi/issues/53).
- Prise en charge du fournisseur Google/Gemini pour les appels LLM [#74](https://github.com/mte-dgpr/ocapi/issues/74).

### Évolutions techniques
- Mise à jour de la dépendance `arretify` vers la version 0.2.0 [#84](https://github.com/mte-dgpr/ocapi/issues/84).
- Refonte du code pour utiliser `ErrorCode` au lieu de `status_code` [#100](https://github.com/mte-dgpr/ocapi/issues/100) et [#97](https://github.com/mte-dgpr/ocapi/issues/97).
- Amélioration des règles de détection d'abrogation [#85](https://github.com/mte-dgpr/ocapi/issues/85).
- Remplacement des exemples de tests par des snapshots pour une meilleure fiabilité [#62](https://github.com/mte-dgpr/ocapi/issues/62) et [#67](https://github.com/mte-dgpr/ocapi/issues/67).
- Utilisation de comparaisons HTML exactes dans les tests de snapshot.
- Suppression des fichiers `.vscode` du suivi Git [#65](https://github.com/mte-dgpr/ocapi/issues/65).
- Modification de `REPLACE ALL` en `REMOVE` pour la détection [#66](https://github.com/mte-dgpr/ocapi/issues/66).
- Ajout de tests et amélioration de la couverture de code.
- Exigence de Python 3.12 pour l'exécution [#70](https://github.com/mte-dgpr/ocapi/issues/70).

### Autres changements
- Documentation mise à jour pour refléter la prise en charge du fournisseur Google/Gemini.
- Amélioration de la lisibilité du code et correction de petites erreurs de style.
- Ajout de configurations pour le fournisseur Google.
- Suppression de données de snapshot locales non suivies.
- Correction de noms de tests et suppression d'erreurs mypy.
