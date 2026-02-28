## Changelog : api-particulier-demonstrateur (30 derniers jours)

### Résumé
Ce démonstrateur d'API a été mis à jour pour supporter la dernière version de Next.js (16) et améliorer la gestion de l'internationalisation. Des corrections ont été apportées pour assurer la cohérence des traductions en anglais et des améliorations ont été faites pour la compatibilité avec TypeScript 5. De nombreuses dépendances ont également été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Correction de clés manquantes ou incorrectes dans les traductions anglaises (#73).
- Adaptation de l'application pour supporter les paramètres asynchrones introduits dans Next.js 16.

### Évolutions techniques
- Mise à jour vers Next.js 16 (#68).
- Migration vers la nouvelle configuration ESLint 9 flat config pour la compatibilité avec Next.js 16 (#4ff54a3).
- Mise à jour de la version minimale de Node.js à la version LTS 24 (#1acf513).
- Amélioration de la compatibilité avec TypeScript 5 (#1b6a20f).
- Mise à jour des tests pour les nouvelles branches de repli de next-intl v4 (#e427485).

### Autres changements
- Mise à jour de nombreuses dépendances : `eslint`, `eslint-config-next`, `micromatch`, `cross-spawn`, `nanoid`, `form-data`, `@babel/runtime`, `minimatch`, `brace-expansion`, `lodash`, `js-yaml`, `braces`, `ws` et `ajv`. Ces mises à jour sont gérées par Dependabot (#63, #72, #71, #70, #69, #67, #66, #65, #64, #61, #59, #53, #52, #406d18d, #e6fa971, #cc7ac0d, #749111c, #84ee258).
