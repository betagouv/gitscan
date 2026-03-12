## Changelog : class-validator (30 derniers jours)

### Résumé
Les 30 derniers jours ont été marqués par une série d'améliorations et d'ajouts à la librairie class-validator. Plusieurs nouveaux validateurs ont été implémentés pour gérer des formats de données spécifiques (IBAN, codes ISO de langues et pays, UUID), offrant ainsi une validation plus complète. Des options de validation plus flexibles ont également été introduites, et des vulnérabilités de dépendances ont été corrigées.

### Évolutions fonctionnelles
- Ajout du validateur `IsIBAN` avec des options de configuration pour une validation plus précise des numéros IBAN [#2618](https://github.com/proconnect-gouv/class-validator/pull/2618).
- Ajout du validateur `IsISO6391` pour valider les codes de langue ISO 639-1 [#2626](https://github.com/proconnect-gouv/class-validator/pull/2626).
- Ajout du validateur `IsISO31661Numeric` pour valider les codes de pays ISO 3166-1 numériques [#2657](https://github.com/proconnect-gouv/class-validator/pull/2657).
- Amélioration du validateur `IsUUID` pour supporter les versions 1 à 8, nil et max, ainsi que tous les formats [#2647](https://github.com/proconnect-gouv/class-validator/pull/2647).
- Introduction de l'option `validateIf` pour une validation conditionnelle plus flexible [#1579](https://github.com/proconnect-gouv/class-validator/pull/1579).

### Évolutions techniques
- Mise à jour des dépendances vulnérables pour améliorer la sécurité [#2669](https://github.com/proconnect-gouv/class-validator/pull/2669).
- Publication des versions 0.15.0 et 0.15.1 [#2670](https://github.com/proconnect-gouv/class-validator/pull/2670), [#2671](https://github.com/proconnect-gouv/class-validator/pull/2671), [#2672](https://github.com/proconnect-gouv/class-validator/pull/2672).

### Autres changements
- Correction d'une erreur grammaticale mineure dans le fichier README.md [#2596](https://github.com/proconnect-gouv/class-validator/pull/2596).
