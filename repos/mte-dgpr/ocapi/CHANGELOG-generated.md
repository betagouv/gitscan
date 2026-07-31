## Changelog : ocapi (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette version apporte des améliorations à la génération des permis, notamment dans la logique de rendu. Des corrections ont été apportées au tri de l'historique des articles et à la détermination du répertoire racine du projet. L'ajout d'un nouveau fournisseur Deepseek et des corrections de typage améliorent la robustesse et les capacités du système.

### Évolutions fonctionnelles
- Amélioration de la logique de rendu des permis consolidés. [#163](https://github.com/mte-dgpr/ocapi/issues/163)
- Correction du tri de l'historique des articles. [#162](https://github.com/mte-dgpr/ocapi/issues/162)
- Ajout du fournisseur Deepseek pour l'évaluation et le traitement du langage naturel. [#153](https://github.com/mte-dgpr/ocapi/issues/153)

### Évolutions techniques
- Refactorisation de la détermination du répertoire racine du projet pour une meilleure gestion des configurations et des templates inclus dans la construction du wheel. [#157](https://github.com/mte-dgpr/ocapi/issues/157) & [d133872](https://github.com/mte-dgpr/ocapi/commit/d133872)
- Correction de problèmes de typage.
- Amélioration de la gestion des erreurs lors de l'évaluation.

### Autres changements
- Mise à jour de la documentation README.
- Ajout d'un fichier `.gitattributes`.
- Suppression de fonctions inutilisées.
