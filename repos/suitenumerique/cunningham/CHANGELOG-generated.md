## Changelog : cunningham (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à l'apparence et à la flexibilité des champs de formulaires. Une nouvelle variante "classique" a été ajoutée aux composants Input, TextArea, Select et DatePicker, offrant ainsi un style plus traditionnel. Des options pour masquer les labels ont également été introduites pour une personnalisation accrue.

### Évolutions fonctionnelles
- Ajout d'une variante "classique" aux composants Input, TextArea, Select et DatePicker.
- Possibilité de masquer les labels sur les composants Input, TextArea et DatePicker.
- Le composant Select prend désormais en charge un placeholder dans sa variante classique.
- Ajout d'une variante classique au composant LabelledBox.

### Évolutions techniques
- Introduction d'un enum `FieldVariant` pour gérer les différentes variantes de champs de formulaire.
- Ajout de tokens de design pour la variante "classique" des champs de formulaire.
- Export de l'enum `FieldVariant` pour une utilisation plus large.
- Suppression du fichier `openspec` du suivi Git et ajout au fichier `.gitignore`.
- Mise à jour des types de tests pour le composant Input.
- Nouvelle version des packages (#3aeacdd).
