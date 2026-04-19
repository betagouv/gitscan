## Changelog : ocapi (30 derniers jours, au 2026-04-17)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse du pipeline de traitement des arrêtés préfectoraux, notamment en améliorant la détection des dates limites, la gestion des opérations complexes et la gestion des erreurs. Des tests plus précis ont été ajoutés, ainsi qu'un support pour l'affichage de pages d'exemple et l'intégration de nouveaux modèles de langage (Google Gemini).

### Évolutions fonctionnelles
- Amélioration de la détection des dates limites et ajout de prompts de secours en cas d'échec [#76](https://github.com/mte-dgpr/ocapi/issues/76).
- Gestion améliorée des identifiants d'articles non standard lors du rendu des documents [#61](https://github.com/mte-dgpr/ocapi/issues/61).
- Affichage des résultats des opérations sur les articles sources [#73](https://github.com/mte-dgpr/ocapi/issues/73).
- Gestion des opérations complexes via l'utilisation de modèles de langage (LLM) [#368](https://github.com/mte-dgpr/ocapi/issues/368).
- Gestion des opérations d'ajout (ADD) via LLM [#376](https://github.com/mte-dgpr/ocapi/issues/376).
- Remplacement des exemples par des tests de snapshots pour une meilleure fiabilité [#428](https://github.com/mte-dgpr/ocapi/issues/428).
- Ajout de pages d'exemple accessibles via GitHub Pages pour faciliter la compréhension et l'utilisation [#345](https://github.com/mte-dgpr/ocapi/issues/345).
- Gestion des codes de statut d'erreur lors de l'extraction de la cible [#324](https://github.com/mte-dgpr/ocapi/issues/324).
- Amélioration du score de détection et ajout de scores de confiance [#43](https://github.com/mte-dgpr/ocapi/issues/43).
- Gestion des doublons [#55](https://github.com/mte-dgpr/ocapi/issues/55).
- Élimination des titres de section redondants lors de la consolidation [#53](https://github.com/mte-dgpr/ocapi/issues/53).

### Évolutions techniques
- Déclaration de la dépendance `arretify` et exigence de Python 3.12 [#70](https://github.com/mte-dgpr/ocapi/issues/70).
- Utilisation de tests de snapshots pour une comparaison HTML plus précise [#67](https://github.com/mte-dgpr/ocapi/issues/67).
- Refonte de l'approche de test avec l'ajout d'un workflow CI/CD et de tests de snapshots [#39](https://github.com/mte-dgpr/ocapi/issues/39).
- Ajout du support pour le modèle Google Gemini [#52](https://github.com/mte-dgpr/ocapi/issues/52).
- Amélioration de la gestion des erreurs et ajout de logs.
- Suppression de fichiers inutiles du suivi Git (.vscode).
- Mise à jour des modèles de langage utilisés.
- Centralisation des noms pour une meilleure cohérence du code [#44](https://github.com/mte-dgpr/ocapi/issues/44).

### Autres changements
- Correction de fautes de frappe et amélioration de la documentation.
- Amélioration de la lisibilité du code et refactoring de certaines parties.
- Suppression de configurations locales inutiles.
- Correction de problèmes mineurs dans les tests.
- Ajout de commentaires pour faciliter la compréhension du code.
- Mise à jour de la section filtres dans le README.
- Correction de problèmes liés à l'imbrication des articles lors de l'application d'opérations d'ajout.
- Amélioration de la gestion des payloads envoyés à OpenAI.
