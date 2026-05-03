## Changelog : document-ia (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la précision et de la flexibilité de l'extraction d'informations, notamment pour les bulletins de salaire. De nouvelles fonctionnalités ont été ajoutées pour faciliter l'évaluation des prompts et restreindre le workflow de classification à certains types de documents. Des améliorations techniques ont également été apportées pour optimiser le CI/CD et la gestion des métriques.

### Évolutions fonctionnelles
- Amélioration de l'extraction des informations relatives à l'identité du salarié sur les bulletins de salaire. [#62](https://github.com/betagouv/document-ia/pull/62)
- Ajout de champs `raw_data` et `doc_type` à tous les documents 2D, connus ou non, pour une meilleure gestion des données. [#64](https://github.com/betagouv/document-ia/pull/64)
- Restriction du workflow de classification à des types de documents spécifiques. [#54](https://github.com/betagouv/document-ia/pull/54)
- Ajout d'une nouvelle page "playground" pour tester et évaluer les prompts utilisés par le système. [#56](https://github.com/betagouv/document-ia/pull/56)

### Évolutions techniques
- Amélioration du CI/CD avec l'ajout de workflows dispatch et la déclenchement des tests sur les branches autres que `main` ou `develop`.
- Introduction d'une nouvelle métrique `TOKEN_SET_EQUALITY` pour évaluer la qualité des prompts.
- Refactorisation de la gestion des exemples pour les prompts, avec l'ajout d'un attribut `examples` à `BaseDocumentTypeSchema`.
- Suppression des alias des modèles d'extraction de documents.
- Support d'une liste de `Metric`. [#61](https://github.com/betagouv/document-ia/pull/61)

### Autres changements
- Mise à jour de la version du projet à 1.0.3.
- Corrections de linting et améliorations de la qualité du code.
