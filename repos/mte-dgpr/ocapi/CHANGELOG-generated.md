## Changelog : ocapi (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse du pipeline de traitement des arrêtés préfectoraux, notamment en améliorant la détection des opérations (abrogation, remplacement), la gestion des identifiants d'arrêtés, et la précision de l'extraction d'informations clés comme les dates limites. Des efforts ont également été faits pour améliorer la qualité des tests et la documentation.

### Évolutions fonctionnelles
- Amélioration de la détection des abrogations et des remplacements d'articles d'arrêtés.
- Gestion améliorée des identifiants d'arrêtés, avec la possibilité de sélectionner l'arrêté principal. [#94](https://github.com/mte-dgpr/ocapi/issues/94)
- Prise en charge des identifiants d'articles au format romain ou alphabétique. [#99](https://github.com/mte-dgpr/ocapi/issues/99)
- Affichage des résultats des opérations directement dans les articles sources pour une meilleure traçabilité. [#73](https://github.com/mte-dgpr/ocapi/issues/73)
- Amélioration de la détection des dates limites et gestion des cas où l'information est manquante. [#63](https://github.com/mte-dgpr/ocapi/issues/63)
- Prise en charge de l'ajout de fichiers annexes aux arrêtés. [#98](https://github.com/mte-dgpr/ocapi/issues/98)
- Amélioration de la sélection de l'autorisation initiale (AP_AUTORISATION). [#76](https://github.com/mte-dgpr/ocapi/issues/76)

### Évolutions techniques
- Mise à jour de la dépendance `arretify` vers la version 0.2.0. [#84](https://github.com/mte-dgpr/ocapi/issues/84)
- Refactorisation du code pour améliorer la gestion des codes d'erreur et des statuts des opérations. [#100](https://github.com/mte-dgpr/ocapi/issues/100) et [#97](https://github.com/mte-dgpr/ocapi/issues/97)
- Amélioration des tests avec l'utilisation de snapshots pour la comparaison HTML. [#67](https://github.com/mte-dgpr/ocapi/issues/67) et [#62](https://github.com/mte-dgpr/ocapi/issues/62)
- Suppression de code inutile et amélioration de la lisibilité du code.
- Ajout d'un mécanisme pour désactiver les appels à un modèle de langage (LLM) pour les tests et le débogage. [#79](https://github.com/mte-dgpr/ocapi/issues/79)
- Amélioration de la chaîne de résolution pour les branches de taille 2. [#71](https://github.com/mte-dgpr/ocapi/issues/71)
- Remplacement de l'opération "REPLACE ALL" par "REMOVE". [#66](https://github.com/mte-dgpr/ocapi/issues/66)

### Autres changements
- Mise à jour de la documentation et du fichier README.
- Ajout de la prise en charge du fournisseur Google/Gemini pour les modèles de langage. [#74](https://github.com/mte-dgpr/ocapi/issues/74)
- Suppression des fichiers `.vscode` du suivi Git. [#65](https://github.com/mte-dgpr/ocapi/issues/65)
- Correction de labels mermaid dans la documentation. [#113](https://github.com/mte-dgpr/ocapi/issues/113)
- Ajout de configurations pour le fournisseur Google.
- Suppression de données de snapshot locales non suivies.
- Correction de noms de tests manquants.
- Correction d'erreurs mypy dans les tests.
- Amélioration de la section filtre dans le README.
- Ajout d'un benchmark LLM.
- Déclaration de la dépendance `arretify` et exigence de Python 3.12. [#70](https://github.com/mte-dgpr/ocapi/issues/70) et [#102](https://github.com/mte-dgpr/ocapi/issues/102)
