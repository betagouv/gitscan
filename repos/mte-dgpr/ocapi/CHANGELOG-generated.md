## Changelog : ocapi (30 derniers jours, au 8 avril 2026)

### Résumé
Ce mois-ci, ocapi a bénéficié d'améliorations significatives en matière de gestion des arrêts préfectoraux, notamment dans la résolution des opérations complexes, la gestion des doublons et la détection des erreurs. Des améliorations ont également été apportées à l'infrastructure de test et au déploiement, ainsi qu'à la documentation et à la qualité du code.

### Évolutions fonctionnelles
- Amélioration de la gestion des opérations complexes via l'utilisation de LLM (Large Language Models) [#368](https://github.com/mte-dgpr/ocapi/issues/368).
- Gestion des doublons d'arrêtés préfectoraux [#55](https://github.com/mte-dgpr/ocapi/issues/55).
- Amélioration du score de détection des informations pertinentes dans les arrêtés [#57](https://github.com/mte-dgpr/ocapi/issues/57).
- Gestion des opérations d'ajout (ADD) dans les arrêtés [#48](https://github.com/mte-dgpr/ocapi/issues/48).
- Affichage des codes de statut avec leur raison explicative [#363](https://github.com/mte-dgpr/ocapi/issues/363).
- Gestion des erreurs lors de l'extraction de la cible et du sous-cible [#324](https://github.com/mte-dgpr/ocapi/issues/324).
- Amélioration de la gestion des codes d'erreur liés aux sous-cibles [#42](https://github.com/mte-dgpr/ocapi/issues/42).
- Publication des exemples sur GitHub Pages pour une meilleure accessibilité [#345](https://github.com/mte-dgpr/ocapi/issues/345).
- Mise à jour des arrêtés préfectoraux à partir du dépôt arretify [#38](https://github.com/mte-dgpr/ocapi/issues/38).
- Prise en charge du format de date YYYY-MM-DD pour les fichiers d'entrée [#37](https://github.com/mte-dgpr/ocapi/issues/37).

### Évolutions techniques
- Implémentation de tests de snapshot pour garantir la stabilité de l'application [#39](https://github.com/mte-dgpr/ocapi/issues/39).
- Refonte de l'architecture de l'API (AP Refonte) [#40](https://github.com/mte-dgpr/ocapi/issues/40).
- Ajout de tests de couverture pour améliorer la qualité du code.
- Amélioration de la gestion des exceptions.
- Centralisation des noms pour une meilleure cohérence du code [#34](https://github.com/mte-dgpr/ocapi/issues/34).
- Refactorisation des étapes du pipeline [#32](https://github.com/mte-dgpr/ocapi/issues/32).
- Mise à jour des dépendances et amélioration de la configuration du projet (pyproject.toml).
- Ajout de linters pour améliorer la qualité du code.

### Autres changements
- Traduction des commentaires, des docstrings et des messages en anglais.
- Mise à jour de la documentation.
- Nettoyage du code et suppression d'artefacts inutiles.
- Ajout de logs pour faciliter le débogage.
- Mise à jour des fichiers ground truth pour les tests.
- Suppression de code obsolète.
