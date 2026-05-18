## Changelog : document-ia (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la qualité de l'extraction d'informations, notamment sur les bulletins de salaire, ainsi que sur l'ajout d'outils pour faciliter l'évaluation et le débogage des prompts utilisés par le système. Des restrictions ont également été ajoutées pour affiner le workflow de classification des documents.

### Évolutions fonctionnelles
- Amélioration de l'extraction de l'identité du salarié sur les bulletins de salaire, notamment pour éviter les erreurs de nom de salaire. [#66](https://github.com/betagouv/document-ia/issues/66)
- Ajout de données brutes et du type de document à chaque document 2D, connu ou non. [#64](https://github.com/betagouv/document-ia/issues/64)
- Restriction du workflow de classification aux types de documents spécifiques. [#54](https://github.com/betagouv/document-ia/issues/54)
- Ajout d'une page de playground pour les prompts dans Document IA Evals, facilitant les tests et l'expérimentation. [#56](https://github.com/betagouv/document-ia/issues/56)

### Évolutions techniques
- Introduction d'une nouvelle métrique `TOKEN_SET_EQUALITY` pour évaluer la similarité des ensembles de tokens.
- Support d'une liste de métriques.
- Refonte des exemples pour les prompts, améliorant la clarté et la précision.
- Suppression des alias des modèles d'extraction de documents.
- Amélioration de la configuration du CI/CD, incluant le déclenchement sur les branches autres que `main` ou `develop` et l'ajout de workflows dispatch.
- Mise à jour de la version vers 1.0.3 puis 1.0.4.

### Autres changements
- Ajout d'attributs `examples` à `BaseDocumentTypeSchema` pour améliorer la documentation et la compréhension des schémas.
- Correction de linting et amélioration de la cohérence du code.
