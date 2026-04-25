## Changelog : ocapi (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, ocapi a bénéficié d'améliorations significatives dans la résolution des conflits et la gestion des opérations sur les arrêtés préfectoraux. L'intégration de nouveaux modèles de langage et l'amélioration des règles de détection d'abrogation contribuent à une plus grande automatisation et précision du pipeline. Des optimisations ont également été apportées à la gestion des doublons et à la présentation des résultats.

### Évolutions fonctionnelles
- Amélioration de la détection des abrogations grâce à des règles plus précises [#85](https://github.com/mte-dgpr/ocapi/issues/85).
- Gestion améliorée des opérations complexes (ADD, REPLACE) grâce à l'intégration de modèles de langage (LLM) pour la résolution de conflits [#376](https://github.com/mte-dgpr/ocapi/issues/376).
- Prise en charge de nouveaux modèles de langage, notamment Google Gemini [#74](https://github.com/mte-dgpr/ocapi/issues/74).
- Amélioration de la détection des dates limites et gestion des prompts de repli [#63](https://github.com/mte-dgpr/ocapi/issues/63).
- Gestion des doublons améliorée [#55](https://github.com/mte-dgpr/ocapi/issues/55).
- Affichage des résultats des opérations dans les articles sources [#73](https://github.com/mte-dgpr/ocapi/issues/73).
- Prise en charge d'identifiants d'articles non standard lors du rendu HTML [#61](https://github.com/mte-dgpr/ocapi/issues/61).
- Publication d'exemples d'utilisation sur GitHub Pages [#345](https://github.com/mte-dgpr/ocapi/issues/345).
- Amélioration du score de confiance pour la détection [#43](https://github.com/mte-dgpr/ocapi/issues/43).

### Évolutions techniques
- Mise à jour de la dépendance `arretify` vers la version 0.2.0 [#84](https://github.com/mte-dgpr/ocapi/issues/84).
- Refonte de la chaîne de résolution pour les branches de taille 2 [#71](https://github.com/mte-dgpr/ocapi/issues/71).
- Suppression du wrapper de section du contenu [#69](https://github.com/mte-dgpr/ocapi/issues/69).
- Remplacement des mocks LLM par un statut `DISABLED_LLM_CALL` [#79](https://github.com/mte-dgpr/ocapi/issues/79).
- Validation du sous-cible pour toutes les opérations cibles [#81](https://github.com/mte-dgpr/ocapi/issues/81).
- Amélioration des tests avec l'utilisation de snapshots pour la comparaison HTML [#67](https://github.com/mte-dgpr/ocapi/issues/67).
- Ajout de tests unitaires et de couverture de code.
- Amélioration de la structure du code et suppression de fichiers inutiles (.vscode, uv.lock).
- Utilisation de Python 3.12 et déclaration de la dépendance `arretify` [#70](https://github.com/mte-dgpr/ocapi/issues/70).

### Autres changements
- Mise à jour de la documentation et des exemples.
- Correction de petites erreurs et améliorations de la lisibilité du code.
- Ajout de logs pour faciliter le débogage.
- Suppression de code obsolète.
- Amélioration des messages d'erreur et des informations de débogage.
- Mise à jour des snapshots de tests.
- Correction de problèmes de typage avec mypy.
- Suppression de filtres superflus [#58](https://github.com/mte-dgpr/ocapi/issues/58).
