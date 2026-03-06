## Changelog : api-particulier-demonstrateur (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'application, notamment une migration vers Next.js 16 et une correction de clés manquantes ou incorrectes dans la localisation anglaise. De nombreuses dépendances ont également été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Correction de clés manquantes et incorrectes dans la localisation anglaise, améliorant l'expérience utilisateur pour les utilisateurs anglophones. [#73](https://github.com/betagouv/api-particulier-demonstrateur/pulls/73)
- Adaptation des layouts et des pages pour la gestion des paramètres asynchrones introduits par Next.js 16.
- Correction de problèmes de typage liés à l'utilisation de Next-intl v4 et TypeScript 5.

### Évolutions techniques
- Migration vers Next.js 16, incluant la mise à jour de la configuration et des dépendances associées.
- Mise à jour vers ESLint 9 avec la configuration `eslint-config-next` pour une meilleure qualité du code.
- Mise à jour de la version minimale de Node.js à la version LTS 24.
- Migration vers la nouvelle configuration "flat" d'ESLint pour la compatibilité avec `eslint-config-next` 16.
- Mise à jour des tests pour prendre en compte les nouvelles fonctionnalités de Next-intl v4 concernant les branches de repli (fallback branches).

### Autres changements
- Mise à jour de nombreuses dépendances : `eslint`, `eslint-config-next`, `micromatch`, `cross-spawn`, `nanoid`, `form-data`, `@babel/runtime`, `minimatch`, `brace-expansion`, `lodash`, `js-yaml`, `braces`, `ws`, `ajv`. Ces mises à jour visent à améliorer la sécurité et la stabilité de l'application.
