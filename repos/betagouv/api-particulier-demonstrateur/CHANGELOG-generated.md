## Changelog : api-particulier-demonstrateur (30 derniers jours)

### Résumé
Ce démonstrateur d'API a été mis à jour pour supporter la dernière version de Next.js (16) et améliorer la gestion des traductions en anglais. Plusieurs dépendances ont également été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Correction de clés manquantes ou incorrectes dans la localisation anglaise de l'application [#73](https://github.com/betagouv/api-particulier-demonstrateur/pulls/73).
- Adaptation de l'application pour supporter les paramètres asynchrones introduits par Next.js 16.

### Évolutions techniques
- Mise à jour vers Next.js 16, incluant la migration vers la nouvelle configuration ESLint (flat config) pour assurer la compatibilité [#68](https://github.com/betagouv/api-particulier-demonstrateur/pulls/68).
- Amélioration des tests pour les nouvelles fonctionnalités de `next-intl` v4.
- Mise à jour de la version minimale de Node.js à une version LTS (24).
- Refonte de la gestion des types avec TypeScript pour une meilleure compatibilité avec `next-intl` v4 [#72](https://github.com/betagouv/api-particulier-demonstrateur/pulls/72).

### Autres changements
- Mise à jour de nombreuses dépendances : `eslint`, `eslint-config-next`, `micromatch`, `cross-spawn`, `nanoid`, `form-data`, `@babel/runtime`, `minimatch`, `brace-expansion`, `lodash`, `js-yaml`, `braces`, `ws`, `ajv` (mises à jour automatiques via Dependabot). Ces mises à jour visent à améliorer la sécurité et la stabilité de l'application.
