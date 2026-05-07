## Changelog : ocapi (30 derniers jours, au 3 mai 2026)

### Résumé
Ce mois-ci, les évolutions d'ocapi se concentrent sur l'amélioration de la précision de la détection des informations clés dans les arrêtés préfectoraux, notamment les dates limites et les opérations effectuées. Des améliorations ont également été apportées à la gestion des annexes et des identifiants d'arrêtés, ainsi qu'à l'infrastructure de test et à la configuration du projet.

### Évolutions fonctionnelles
- Amélioration de la détection des dates limites et ajout de prompts de secours pour une meilleure robustesse. [#63](https://github.com/mte-dgpr/ocapi/issues/63)
- Prise en charge des identifiants d'articles non standard dans le rendu des arrêtés. [#61](https://github.com/mte-dgpr/ocapi/issues/61)
- Affichage des résultats des opérations directement dans les articles sources pour une meilleure traçabilité. [#73](https://github.com/mte-dgpr/ocapi/issues/73)
- Gestion améliorée des annexes, avec fusion des fichiers annexe dans l'annexe principale. [#98](https://github.com/mte-dgpr/ocapi/issues/98)
- Prise en charge des niveaux romains et alphabétiques dans les identifiants d'articles. [#99](https://github.com/mte-dgpr/ocapi/issues/99)
- Amélioration de la sélection de l'arrêté principal par son identifiant. [#94](https://github.com/mte-dgpr/ocapi/issues/94)
- Prise en compte de la dernière autorisation (AP_AUTORISATION) comme initiale. [#76](https://github.com/mte-dgpr/ocapi/issues/76) et [#266045b](https://github.com/mte-dgpr/ocapi/commit/266045b)

### Évolutions techniques
- Mise à jour de la dépendance `arretify` vers la version 0.2.0. [#84](https://github.com/mte-dgpr/ocapi/issues/84)
- Refonte du code de gestion des codes de statut pour utiliser un ensemble figé d'ErrorCode. [#100](https://github.com/mte-dgpr/ocapi/issues/100) et [#97](https://github.com/mte-dgpr/ocapi/issues/97)
- Amélioration des règles de détection d'abrogation. [#85](https://github.com/mte-dgpr/ocapi/issues/85)
- Remplacement des exemples par des snapshots pour les tests, améliorant ainsi la fiabilité et la maintenabilité. [#62](https://github.com/mte-dgpr/ocapi/issues/62)
- Utilisation de comparaisons HTML exactes dans les tests de snapshot. [#67](https://github.com/mte-dgpr/ocapi/issues/67)
- Suppression du wrapper de section du contenu. [#69](https://github.com/mte-dgpr/ocapi/issues/69)
- Ajout de la prise en charge du fournisseur Google/Gemini et exécution de benchmarks LLM. [#74](https://github.com/mte-dgpr/ocapi/issues/74)
- Déclaration de la dépendance `arretify` et exigence de Python 3.12. [#70](https://github.com/mte-dgpr/ocapi/issues/70) et [#ffaab34](https://github.com/mte-dgpr/ocapi/commit/ffaab34)
- Suppression des fichiers `.vscode` du suivi git. [#65](https://github.com/mte-dgpr/ocapi/issues/65)

### Autres changements
- Ajout d'une liste plus complète de verbes d'opération pour améliorer la qualité des prompts. [#60](https://github.com/mte-dgpr/ocapi/issues/60) et [#0a5de0a](https://github.com/mte-dgpr/ocapi/commit/0a5de0a)
- Correction de fautes de frappe et amélioration de la lisibilité du code.
- Mise à jour de la documentation README avec la prise en charge du fournisseur Google.
- Suppression de données de snapshot locales non suivies.
- Correction de problèmes mypy dans les tests.
- Amélioration du score de détection. [#57](https://github.com/mte-dgpr/ocapi/issues/57)
