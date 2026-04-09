## Changelog : document-ia (30 derniers jours, au 02 mai 2026)

### Résumé
Ce mois-ci, le projet document-ia a bénéficié d'améliorations significatives concernant la classification des documents, la gestion des dates extraites et la détection de documents 2Ddoc. Une nouvelle version (1.0.2) a été publiée, incluant des corrections et des optimisations.

### Évolutions fonctionnelles

- **Classification des documents :** La classification des documents a été améliorée pour permettre le retour de la catégorie "autre" lorsque la classification automatique n'est pas concluante. [#58](https://github.com/betagouv/document-ia/issues/58)
- **Extraction de dates :** Correction d'un bug concernant les dates invalides après extraction, assurant une meilleure qualité des données. [#57](https://github.com/betagouv/document-ia/issues/57)
- **Détection 2Ddoc :** Amélioration significative de la détection des documents 2Ddoc grâce à l'intégration d'un modèle YOLO. [#51](https://github.com/betagouv/document-ia/issues/51)
- **Schéma de fiche de paie :** Refonte du schéma de la fiche de paie pour une meilleure structuration et une plus grande précision des données extraites. [#53](https://github.com/betagouv/document-ia/issues/53)

### Évolutions techniques

- **Mise à jour des dépendances :**
    - Mise à jour de la librairie `zxing-cpp` dans le worker. [#59](https://github.com/betagouv/document-ia/issues/59)
    - Mise à jour de la librairie `2ddoc-parser` à la version 1.0.5. [#55](https://github.com/betagouv/document-ia/issues/55)
- **Publication des versions :** Publication des versions 1.0.1 et 1.0.2.

### Autres changements

- Correction d'une faute de frappe dans le fichier `workflows.json` et mise à jour du fichier. [#52](https://github.com/betagouv/document-ia/issues/52)
