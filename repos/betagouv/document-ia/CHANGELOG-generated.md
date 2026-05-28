## Changelog : document-ia (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, le projet document-ia a connu des améliorations significatives en termes de classification de documents, notamment pour les justificatifs de domicile. Des optimisations ont également été apportées à la qualité du code et aux processus de CI/CD, ainsi qu'à l'évaluation des modèles d'extraction de documents. Une nouvelle fonctionnalité de restriction du workflow de classification a été implémentée pour une meilleure gestion des types de documents.

### Évolutions fonctionnelles
- Ajout de la classification des documents de résidence (justificatifs de domicile) [#65](https://github.com/betagouv/document-ia/issues/65).
- Restriction du workflow de classification à des types de documents spécifiques [#54](https://github.com/betagouv/document-ia/issues/54).
- Amélioration de la reconnaissance de l'identité du salarié sur les bulletins de salaire.
- Ajout d'une page de playground pour tester les prompts dans Document IA Evals [#56](https://github.com/betagouv/document-ia/issues/56).

### Évolutions techniques
- Ajout de `gitleaks` comme pre-hook pour la sécurité du code [#67](https://github.com/betagouv/document-ia/issues/67).
- Mise à jour du schéma des fiches de paie pour éviter les erreurs de nom de salaire [#66](https://github.com/betagouv/document-ia/issues/66).
- Amélioration de la configuration de la CI/CD :
    - Déclenchement de la CI pour les branches autres que `main` ou `develop`.
    - Activation de la CI pour `document-ia-evals`.
    - Ajout d'un workflow dispatch.
- Introduction de métriques pour évaluer la qualité des prompts et des modèles d'extraction.
- Refactorisation et amélioration de la structure des modèles d'extraction de documents.
- Ajout d'attributs `examples` aux schémas de types de documents pour améliorer la qualité des prompts.

### Autres changements
- Bump de version à 1.0.4.
- Bump de version à 1.0.3.
- Corrections de linting et amélioration de la qualité du code.
- Mise à jour de `poetry.lock`.
