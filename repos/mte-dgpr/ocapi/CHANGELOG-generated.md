## Changelog : ocapi (30 derniers jours, au 2026-04-19)

### Résumé
Les dernières mises à jour d'ocapi se concentrent sur l'amélioration de la robustesse du pipeline de traitement des arrêtés préfectoraux, notamment en gérant mieux les cas complexes et les erreurs. Des améliorations ont été apportées à la détection des opérations, à la gestion des doublons et à la présentation des résultats. L'intégration de nouveaux modèles de langage (LLM) et l'ajout de tests automatisés renforcent également la qualité et la fiabilité du projet.

### Évolutions fonctionnelles
- Amélioration de la détection des opérations complexes grâce à l'intégration de LLM pour la résolution ([#368](https://github.com/mte-dgpr/ocapi/issues/368)).
- Gestion améliorée des doublons lors du traitement des arrêtés ([#410](https://github.com/mte-dgpr/ocapi/issues/410)).
- Affichage des résultats des opérations directement dans les articles sources pour une meilleure traçabilité ([#73](https://github.com/mte-dgpr/ocapi/issues/73), [#386](https://github.com/mte-dgpr/ocapi/issues/386)).
- Prise en charge de l'opération "ADD" pour l'ajout d'informations aux arrêtés ([#376](https://github.com/mte-dgpr/ocapi/issues/376)).
- Gestion des erreurs lors de l'extraction de la cible, avec affichage de codes d'erreur et de raisons ([#324](https://github.com/mte-dgpr/ocapi/issues/324)).
- Amélioration de la détection des dates limites et gestion des cas de fallback ([#442](https://github.com/mte-dgpr/ocapi/issues/442)).
- Prise en charge de l'affichage des codes de statut avec une raison ([#363](https://github.com/mte-dgpr/ocapi/issues/363)).
- Amélioration de la gestion des identifiants d'articles non standard ([#61](https://github.com/mte-dgpr/ocapi/issues/61)).
- Préférence pour le dernier arrêté "AP_AUTORISATION" comme initial ([#76](https://github.com/mte-dgpr/ocapi/issues/76)).

### Évolutions techniques
- Mise à jour de la dépendance `arretify` et exigence de Python 3.12 ([#70](https://github.com/mte-dgpr/ocapi/issues/70)).
- Remplacement des mocks LLM par un statut `DISABLED_LLM_CALL` pour une meilleure gestion des tests et de l'environnement ([#79](https://github.com/mte-dgpr/ocapi/issues/79)).
- Ajout de tests snapshot pour une comparaison HTML plus précise ([#67](https://github.com/mte-dgpr/ocapi/issues/67), [#428](https://github.com/mte-dgpr/ocapi/issues/428)).
- Intégration de Google/Gemini comme fournisseur de LLM et ajout des résultats de benchmark ([#74](https://github.com/mte-dgpr/ocapi/issues/74)).
- Validation du sous-cible pour toutes les opérations cibles ([#81](https://github.com/mte-dgpr/ocapi/issues/81)).
- Refonte de la configuration des tests et ajout d'un workflow CI pour les tests snapshot ([#39](https://github.com/mte-dgpr/ocapi/issues/39)).
- Suppression des fichiers `.vscode` du suivi Git ([#65](https://github.com/mte-dgpr/ocapi/issues/65)).
- Amélioration de la structure du code et suppression de code redondant ([#58](https://github.com/mte-dgpr/ocapi/issues/58)).

### Autres changements
- Mise à jour de la documentation README avec la prise en charge de Google/Gemini.
- Suppression de sections wrapper inutiles dans le contenu HTML ([#69](https://github.com/mte-dgpr/ocapi/issues/69)).
- Ajout de logs pour faciliter le débogage.
- Suppression de fichiers de sortie inutiles (xlsx) du `.gitignore`.
- Ajout de la publication des exemples sur GitHub Pages ([#345](https://github.com/mte-dgpr/ocapi/issues/345)).
- Centralisation des noms pour une meilleure cohérence du code ([#44](https://github.com/mte-dgpr/ocapi/issues/44)).
- Amélioration de la lisibilité du code avec des corrections de linting.
