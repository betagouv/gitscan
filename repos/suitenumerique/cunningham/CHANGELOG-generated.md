## Changelog : cunningham (30 derniers jours)

### Résumé
Cette mise à jour apporte une nouvelle option de style "classique" pour plusieurs composants de formulaires, offrant ainsi plus de flexibilité pour l'apparence de vos interfaces. Des améliorations ont également été apportées pour mieux gérer l'affichage des labels et des espaces réservés. Enfin, un fichier temporaire inutilisé a été retiré du suivi Git.

### Évolutions fonctionnelles
- Ajout d'une variante "classique" pour les composants `TextArea`, `Select`, `Input` et `DatePicker` [#1234](https://github.com/suitenumerique/cunningham/issues/1234).
- Possibilité de masquer le label pour les composants `Input`, `DatePicker` et `TextArea`.
- Ajout du support de placeholder pour le composant `Select`.
- Ajout d'une variante "classique" pour le composant `LabelledBox`.

### Évolutions techniques
- Introduction d'un enum `FieldVariant` pour gérer les différentes variantes de champs de formulaire.
- Export de l'enum `FieldVariant` pour une utilisation plus facile.
- Suppression du fichier `openspec` du suivi Git et ajout au fichier `.gitignore`.
- Mise à jour des types de tests pour le composant `Input`.
- Publication d'une nouvelle version des packages.

### Autres changements
- Ajout d'artefacts de changement pour la variante "classique" dans `openspec`.
