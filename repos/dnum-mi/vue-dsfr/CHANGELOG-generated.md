## Changelog : vue-dsfr (30 derniers jours, au 11/08/2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de la gestion des icônes, notamment via un meilleur support du mode hors-ligne et du rendu côté serveur (SSR/SSG). Le projet a également bénéficié d'une stabilisation importante de son infrastructure de build et de ses processus de déploiement.

### Évolutions fonctionnelles
- **Amélioration de la gestion des icônes** :
    - Ajout de l'option `preferOffline` pour permettre l'utilisation de collections d'icônes locales [#1384](https://github.com/dnum-mi/vue-dsfr/pull/1384).
    - Support du rendu local des icônes pour les environnements SSG et SSR [#1370](https://github.com/dnum-mi/vue-dsfr/pull/1370).
    - Correction du format des noms (gestion des tirets) lors de la résolution des icônes hors-ligne [#1387](https://github.com/dnum-mi/vue-dsfr/pull/1387).
    - Correction d'un problème de `viewBox` invalide dans le composant `VIconOffline` lorsque les coordonnées sont absentes [#1373](https://github.com/dnum-mi/vue-dsfr/pull/1373).
- **Composants UI** :
    - Correction du composant `DsfrDataTable` pour éviter les erreurs lors de l'utilisation de la fonction de copie dans le presse-papier [#1360](https://github.com/dnum-mi/vue-dsfr/pull/1360).

### Évolutions techniques
- **Infrastructure et Build** :
    - Mise à jour de l'environnement de gestion de paquets vers `pnpm` v11.21.0 et ajustement de la configuration de build [#1377](https://github.com/dnum-mi/vue-dsfr/pull/1377).
    - Stabilisation des workflows de release en utilisant Node 24 [#1376](https://github.com/dnum-mi/vue-dsfr/pull/1376).
    - Amélioration de l'isolation du build Storybook (Vite 7) et correction des builds sur Netlify.
- **Refactoring** :
    - Simplification de la gestion des chemins avec l'utilisation de `import.meta.dirname`.
    - Correction de la nomenclature de certains événements Vue dans le processus de build.

### Autres changements
- **Documentation** :
    - Clarification de l'utilisation combinée des fonctions `addCollection` et `createVueDsfrIconPlugin` dans le guide Nuxt [#1381](https://github.com/dnum-mi/vue-dsfr/pull/1381).
    - Mise à jour importante du guide des contributeurs concernant l'usage, la sécurisation et les conventions liées aux agents d'assistance IA [#1367](https://github.com/dnum-mi/vue-dsfr/pull/1367) [#1365](https://github.com/dnum-mi/vue-dsfr/pull/1365).
    - Correction de la branche cible par défaut pour les Pull Requests dans la documentation [#1359](https://github.com/dnum-mi/vue-dsfr/pull/1359).
