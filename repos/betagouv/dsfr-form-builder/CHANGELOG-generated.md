## Changelog : dsfr-form-builder (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à la gem dsfr-form-builder au cours des 30 derniers jours. Les changements incluent des corrections de bugs, des améliorations de l'interface, l'ajout d'un site de documentation et de démo, ainsi que des améliorations des outils de développement et de déploiement.

### Évolutions fonctionnelles
- Correction : Le champ `value` des inputs n'affecte plus le `for` du label associé (#66).
- Correction : Suppression de l'ajout automatique d'une étoile pour les champs requis (#70).
- Amélioration : Support du `disabled` pour les champs `select` (#58).
- Correction : Correction du double rendu de `dsfr_input_group` (#64).
- Correction : Signature de `dsfr_input_group` rétablie à son état précédent (#56).

### Évolutions techniques
- Ajout d'un site de documentation et de démo pour la gem (#55).
- Ajout d'un `Rakefile` pour faciliter la création des releases (#62).
- Amélioration des instructions de déploiement (#63).
- Amélioration du `Makefile` et de `Guard` pour faciliter le développement (#59).
- Correction des specs en local via la variable d'environnement `RACK_TEST` (#69).
- Correction pour `rack-env` et les `permitted hosts` du guide (#71).

### Autres changements
- Correction d'un lien dans le `README` pour la création d'une release (#68).
- Amélioration du `README` (#61).
- Releases : v0.0.13 (#72), v0.0.12 (#67), v0.0.11 (#65), v0.0.10 (#60) ont été publiées.
