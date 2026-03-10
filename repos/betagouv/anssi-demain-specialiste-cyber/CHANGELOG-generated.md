## Changelog : anssi-demain-specialiste-cyber (30 derniers jours)

### Résumé
Ce changelog présente les récentes mises à jour du site web "DemainSpécialisteCyber". Les changements se concentrent principalement sur la sécurité en mettant à jour plusieurs dépendances pour corriger des vulnérabilités connues. Une correction de bug a également été apportée pour améliorer la gestion des résultats du cache.

### Évolutions fonctionnelles
- Correction d'un bug qui empêchait le renvoi correct des résultats du cache en cas d'erreur avec Grist. [#62d1e8a](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/62d1e8a)

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité :
    - `multer` : versions 2.1.0 et 2.1.1
    - `immutable` : version 5.1.5
    - `minimatch` : versions 3.1.4 et 9.0.7
    - `svelte` : version 5.53.5
    - `ajv` : version 6.14.0
    - `qs` : version 6.14.2
    - `fast-xml-parser` : versions 5.3.6 et 5.3.9
    - `rollup` : version 4.59.0
    - `axios` : version 1.13.5
- Utilisation de révisions pour les dépendances afin d'assurer la reproductibilité des builds. [#511acf0](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/511acf0)
- Correction de vulnérabilités de dépendances. [#1090414](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/1090414)
