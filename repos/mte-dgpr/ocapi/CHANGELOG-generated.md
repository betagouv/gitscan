## Changelog : ocapi (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse de la détection des opérations, la gestion des conflits et l'amélioration de la qualité des données traitées. Des optimisations ont été apportées à la détection des articles et annexes, ainsi qu'à la gestion des versions des arrêtés. L'intégration avec `arretify` a également été mise à jour.

### Évolutions fonctionnelles
- Amélioration de la détection des opérations : exclusion des opérations liées aux arrêtés ministériels pour une meilleure précision de l'analyse ([#129](https://github.com/mte-dgpr/ocapi/issues/129)).
- Gestion des conflits : amélioration de la gestion des suppressions complètes conflictuelles, en les marquant comme moins importantes ([#116](https://github.com/mte-dgpr/ocapi/issues/116)).
- Interface utilisateur :
    - Suppression du menu déroulant pour les versions non résolues ([#125](https://github.com/mte-dgpr/ocapi/issues/125)).
    - Ajout d'une représentation visuelle des opérations de gauche à droite ([#128](https://github.com/mte-dgpr/ocapi/issues/128)).
- Correction d'un bug affichant des messages de duplication d'opération dans le permis rendu ([#130](https://github.com/mte-dgpr/ocapi/issues/130)).
- Gestion des annexes : fusion des fichiers d'annexe dans l'annexe de base ([#98](https://github.com/mte-dgpr/ocapi/issues/98)).
- Prise en charge des niveaux d'article romains et alphabétiques ([#99](https://github.com/mte-dgpr/ocapi/issues/99)).

### Évolutions techniques
- Mise à jour de `arretify` vers la version 0.2.0 ([#84](https://github.com/mte-dgpr/ocapi/issues/84)).
- Changement du modèle LLM par défaut et reconstruction des snapshots ([#123](https://github.com/mte-dgpr/ocapi/issues/123), [#18](https://github.com/mte-dgpr/ocapi/issues/18)).
- Refactoring et nettoyage du code :
    - Simplification des noms de modèles et des principaux AP ([#124](https://github.com/mte-dgpr/ocapi/issues/124)).
    - Suppression des fonctions inutilisées.
- Amélioration de la gestion des statuts d'opération, avec l'introduction d'un code d'erreur standardisé ([#100](https://github.com/mte-dgpr/ocapi/issues/100)).
- Fusion des opérations `apply_replace` et `apply_remove` ([#104](https://github.com/mte-dgpr/ocapi/issues/104)).
- Ajout d'un statut `NOT_AN_OPERATION` pour les opérations "ADD ALL" ([#96](https://github.com/mte-dgpr/ocapi/issues/96)).
- Gestion des contenus sources manquants pour certaines opérations ([#95](https://github.com/mte-dgpr/ocapi/issues/95)).
- Contournement d'une quarantaine pypi de MistralAI ([#114](https://github.com/mte-dgpr/ocapi/issues/114)).

### Autres changements
- Documentation : amélioration de la documentation et du wiki ([#113](https://github.com/mte-dgpr/ocapi/issues/113)).
- Amélioration de la documentation des scénarios de régénération des snapshots ([#133](https://github.com/mte-dgpr/ocapi/issues/133)).
- Documentation de la section `section_version` ([#131](https://github.com/mte-dgpr/ocapi/issues/131)).
- Suppression du suivi des données de snapshot locales.
- Mise à jour de la licence.
