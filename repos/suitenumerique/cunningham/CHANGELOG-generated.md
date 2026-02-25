## Changelog : cunningham (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations significatives aux composants de formulaires, en introduisant un nouveau style "classique" pour plusieurs d'entre eux. Cette nouvelle variante offre une apparence plus traditionnelle tout en conservant les principes d'accessibilité et de personnalisation de Cunningham. Des corrections et des ajustements ont également été apportés pour améliorer la stabilité et la cohérence du projet.

### Évolutions fonctionnelles
- Ajout d'une variante "classique" aux composants `TextArea`, `Select`, `Input` et `DatePicker`, offrant ainsi plus de flexibilité en termes de style. (#367958c, #1dfd2ac, #2a39c8e, #c2a0013, #e94ddc9, #fb0c8c0)
- Possibilité de masquer le label sur les composants `Input`, `DatePicker` et `TextArea` dans la nouvelle variante classique. (#2a39c8e, #fb0c8c0)
- Ajout du support du placeholder dans la variante classique du composant `Select`. (#e94ddc9)
- Ajout d'une variante classique au composant `LabelledBox`. (#367958c)

### Évolutions techniques
- Introduction d'un enum `FieldVariant` pour gérer les différentes variantes de champs, facilitant l'ajout de nouvelles variantes à l'avenir. (#1dfd2ac, #5b522e3)
- Export de l'enum `FieldVariant` pour une utilisation plus large dans le projet. (#1dfd2ac)
- Suppression du fichier `openspec` du suivi Git et ajout au fichier `.gitignore`. (#964dc94)
- Mise à jour des types de tests pour le composant `Input`. (#51834ae)

### Autres changements
- Publication d'une nouvelle version des packages. (#3aeacdd)
- Ajout d'artefacts de changement pour la variante "classique" dans `openspec`. (#1468973)
