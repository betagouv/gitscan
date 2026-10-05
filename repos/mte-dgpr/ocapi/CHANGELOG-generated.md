## Changelog : ocapi (30 derniers jours, au 02/10/2026)

### Résumé
Ce mois-ci, le projet a principalement renforcé ses capacités d'intelligence artificielle en intégrant de nouveaux modèles de langage et en améliorant la fiabilité du traitement des données et de la gestion de l'historique.

### Évolutions fonctionnelles
- Amélioration de la stabilité du marquage des opérations et de la gestion de l'historique [#165](https://github.com/mte-dgpr/ocapi/issues/165)
- Correction du traitement des cibles secondaires (passage automatique de `None` à `ALL`) [#172](https://github.com/mte-dgpr/ocapi/issues/172)

### Évolutions techniques
- Extension du support des modèles d'IA avec l'intégration de l'API Albert et de nouveaux modèles récents [#176](https://github.com/mte-dgpr/ocapi/issues/176) [#174](https://github.com/mte-dgpr/ocapi/issues/174)
- Optimisation de la gestion des appels API : ajout de clés pour l'évaluation des coûts et augmentation du timeout à 150s [#176](https://github.com/mte-dgpr/ocapi/issues/176)
- Audit du code et corrections liées à l'intégration de Claude [#170](https://github.com/mte-dgpr/ocapi/issues/170)
- Amélioration de la gestion des erreurs lors de l'application des opérations via l'ajout de codes d'erreur
- Refactorisation du code pour supprimer des vérifications redondantes dans le bloc `apply_ops`

### Autres changements
- Mise à jour de la documentation concernant l'utilisation des LLM et les procédures d'ajout de nouveaux modèles [#174](https://github.com/mte-dgpr/ocapi/issues/174)
