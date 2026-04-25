## Changelog : document-ia (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la précision de l'identification des informations sur les bulletins de salaire, l'ajout de nouvelles métriques pour évaluer les performances du système, et l'amélioration de la flexibilité du workflow de classification des documents. Une nouvelle page de playground pour les prompts a également été ajoutée à l'outil d'évaluation. Enfin, une version 1.0.2 a été publiée.

### Évolutions fonctionnelles
- Amélioration de l'identification des informations relatives à l'identité salariale sur les bulletins de salaire. [#62](https://github.com/betagouv/document-ia/pull/62)
- Ajout d'une page de playground pour les prompts dans l'outil d'évaluation Document IA Evals, permettant de tester et d'affiner les prompts utilisés. [#56](https://github.com/betagouv/document-ia/issues/56)
- Le workflow de classification des documents est désormais restreint à des types de documents spécifiques. [#54](https://github.com/betagouv/document-ia/issues/54)
- Correction d'un bug permettant au workflow de classification de retourner la valeur "autre". [#58](https://github.com/betagouv/document-ia/issues/58)
- Correction d'un bug lié aux dates invalides après l'extraction. [#57](https://github.com/betagouv/document-ia/issues/57)

### Évolutions techniques
- Ajout d'une nouvelle métrique `TOKEN_SET_EQUALITY` pour évaluer la similarité des tokens. [#61](https://github.com/betagouv/document-ia/pull/61)
- Possibilité de définir une liste de métriques. [#59](https://github.com/betagouv/document-ia/pull/59)
- Amélioration de la configuration du CI/CD, notamment l'ajout d'un workflow dispatch et la vérification des prompts rendus. [#60](https://github.com/betagouv/document-ia/pull/60)
- Refactorisation des modèles d'extraction de documents pour supprimer les alias. [#60](https://github.com/betagouv/document-ia/pull/60)
- Mise à jour de la librairie `zxing-cpp` dans le worker. [#59](https://github.com/betagouv/document-ia/pull/59)
- Mise à jour de la librairie `2ddoc-parser`. [#55](https://github.com/betagouv/document-ia/pull/55)

### Autres changements
- Publication de la version 1.0.2.
- Ajout d'exemples et correction de types de champs pour les schémas de documents.
- Ajout de l'attribut `examples` aux schémas `BaseDocumentTypeSchema`.
- Amélioration de la configuration du CI pour `document-ia-evals`.
- Correction de linting.
- Bump de `poetry.lock`.
