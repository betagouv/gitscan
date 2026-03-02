## Changelog : dsfr-form-builder (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à la gem dsfr-form-builder au cours des 30 derniers jours. Les principales évolutions concernent la correction de bugs, l'amélioration de la gestion des champs de formulaire, et la mise en place d'une documentation et d'un site de démonstration pour faciliter l'utilisation de la gem. Plusieurs versions ont été publiées pour intégrer ces changements.

### Évolutions fonctionnelles
- Correction du passage de l'option `data` aux champs input textuels [#73](https://github.com/betagouv/dsfr-form-builder/issues/73)
- Correction du comportement de l'attribut `value` sur les inputs, qui n'affecte plus le `for` du label [#66](https://github.com/betagouv/dsfr-form-builder/issues/66)
- Support du `disabled` pour les champs `select` [#58](https://github.com/betagouv/dsfr-form-builder/issues/58)
- Suppression de l'ajout automatique d'une étoile pour les champs `required` [#70](https://github.com/betagouv/dsfr-form-builder/issues/70)
- Correction du double rendu de `dsfr_input_group` [#64](https://github.com/betagouv/dsfr-form-builder/issues/64)

### Évolutions techniques
- Ajout d'un `Rakefile` pour faciliter la création de releases [#62](https://github.com/betagouv/dsfr-form-builder/issues/62)
- Correction des specs en local via la variable d'environnement `RACK_TEST` [#69](https://github.com/betagouv/dsfr-form-builder/issues/69)
- Correction pour `rack-env` et les `permitted hosts` du guide [#71](https://github.com/betagouv/dsfr-form-builder/issues/71)
- Ajout d'un site de documentation et de démonstration [#55](https://github.com/betagouv/dsfr-form-builder/issues/55)
- Amélioration des instructions de déploiement [#63](https://github.com/betagouv/dsfr-form-builder/issues/63)
- Améliorations du `Makefile` et de `Guard` pour faciliter le développement [#59](https://github.com/betagouv/dsfr-form-builder/issues/59)

### Autres changements
- Corrections et améliorations du `README` [#61](https://github.com/betagouv/dsfr-form-builder/issues/61), [#68](https://github.com/betagouv/dsfr-form-builder/issues/68)
- Publication des versions v0.0.10, v0.0.11, v0.0.12 et v0.0.13 [#60](https://github.com/betagouv/dsfr-form-builder/issues/60), [#65](https://github.com/betagouv/dsfr-form-builder/issues/65), [#67](https://github.com/betagouv/dsfr-form-builder/issues/67), [#72](https://github.com/betagouv/dsfr-form-builder/issues/72)
