## Changelog : ocapi (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse et la précision du pipeline de traitement des arrêtés préfectoraux. Des améliorations significatives ont été apportées à la détection des abrogations, à la résolution des conflits, et à la gestion des opérations complexes grâce à l'intégration de modèles de langage (LLM). L'expérience utilisateur est également améliorée par une meilleure gestion des erreurs et des informations de statut.

### Évolutions fonctionnelles
- Amélioration de la détection des abrogations grâce à des règles plus strictes [#85](https://github.com/mte-dgpr/ocapi/issues/85).
- Gestion améliorée des opérations complexes (ADD, REPLACE) grâce à l'utilisation de modèles de langage pour la résolution de conflits [#368](https://github.com/mte-dgpr/ocapi/issues/368).
- Affichage des résultats des opérations directement dans les articles sources [#73](https://github.com/mte-dgpr/ocapi/issues/73), [#48](https://github.com/mte-dgpr/ocapi/issues/48).
- Gestion des identifiants d'articles non standard lors du rendu HTML [#61](https://github.com/mte-dgpr/ocapi/issues/61).
- Amélioration de la détection des dates limites et des prompts de secours associés [#72](https://github.com/mte-dgpr/ocapi/issues/72).
- Prise en charge de l'affichage des codes de statut et de leurs raisons pour une meilleure gestion des erreurs [#363](https://github.com/mte-dgpr/ocapi/issues/363).
- Amélioration de la gestion des doublons [#55](https://github.com/mte-dgpr/ocapi/issues/55).
- Ajout d'un score de confiance pour la détection des opérations [#43](https://github.com/mte-dgpr/ocapi/issues/43).
- Publication d'exemples ICPE sur GitHub Pages pour une meilleure documentation et accessibilité [#345](https://github.com/mte-dgpr/ocapi/issues/345).

### Évolutions techniques
- Refonte de la gestion des autorisations initiales (AP_AUTORISATION) pour privilégier la dernière autorisation trouvée [#76](https://github.com/mte-dgpr/ocapi/issues/76).
- Amélioration de la résolution des branches de taille 2 [#71](https://github.com/mte-dgpr/ocapi/issues/71).
- Suppression des wrappers de section inutiles dans le contenu HTML [#69](https://github.com/mte-dgpr/ocapi/issues/69).
- Remplacement des mocks LLM par un statut `DISABLED_LLM_CALL` pour une meilleure gestion des tests [#79](https://github.com/mte-dgpr/ocapi/issues/79).
- Validation du sous-cible pour toutes les opérations cibles [#81](https://github.com/mte-dgpr/ocapi/issues/81).
- Utilisation de snapshots pour les tests HTML, améliorant la fiabilité et la maintenabilité [#67](https://github.com/mte-dgpr/ocapi/issues/67).
- Déclaration de la dépendance `arretify` et exigence de Python 3.12 [#70](https://github.com/mte-dgpr/ocapi/issues/70).
- Suppression des fichiers `.vscode` du suivi Git [#65](https://github.com/mte-dgpr/ocapi/issues/65).
- Amélioration de la gestion des erreurs lors de l'extraction de la cible [#57](https://github.com/mte-dgpr/ocapi/issues/57).
- Centralisation des noms pour une meilleure cohérence du code [#44](https://github.com/mte-dgpr/ocapi/issues/44).
- Ajout de la prise en charge du fournisseur Google/Gemini [#52](https://github.com/mte-dgpr/ocapi/issues/52).
- Amélioration des tests et de la couverture du code.

### Autres changements
- Mise à jour de la documentation et des exemples.
- Corrections de linting et de style de code.
- Suppression de fichiers inutiles.
- Amélioration des messages de log.
- Diverses corrections de bugs et améliorations de la maintenabilité.
