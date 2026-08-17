## Changelog : vue-dsfr (30 derniers jours, au 11 août 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de la gestion des icônes (support du rendu local pour le SSG/SSR et nouvelles options de résolution) et sur la stabilisation de l'environnement de développement et de déploiement (correction des workflows CI/CD et optimisation des builds).

### Évolutions fonctionnelles
- **Gestion des icônes** :
    - Ajout du support du rendu local pour les environnements SSG et SSR avec le composant `VIconOffline` [#1369](https://github.com/dnum-mi/vue-dsfr/pull/1369).
    - Ajout de l'option `preferOffline` dans le plugin d'icônes pour privilégier la résolution depuis les collections locales [#1383](https://github.com/dnum-mi/vue-dsfr/pull/1383).
    - Support du format de nommage `prefixe-nom` pour la résolution des icônes hors ligne [#1386](https://github.com/dnum-mi/vue-dsfr/pull/1386).
    - Correction d'un bug de `viewBox` invalide sur le composant `VIconOffline` lorsque les propriétés `left` et `top` sont absentes [#1372](https://github.com/dnum-mi/vue-dsfr/pull/1372).
- **Composants** :
    - Correction des erreurs de copie dans le composant `DsfrDataTable` [#1352](https://github.com/dnum-mi/vue-dsfr/pull/1352).

### Évolutions techniques
- **CI/CD et Build** :
    - Stabilisation des workflows de release en utilisant Node 24 [#1375](https://github.com/dnum-mi/vue-dsfr/pull/1375).
    - Amélioration de la robustesse du build : correction de l'isolation de Storybook, mise à jour de `pnpm` (v11) et correction des noms d'événements Vue.
    - Correction de l'échec du build Storybook sur Netlify via l'épinglage de la version Node.
- **Refactoring** :
    - Simplification de la gestion des chemins en remplaçant `fileURLToPath/URL` par `import.meta.dirname`.
    - Durcissement des prérequis de version Node.js dans la configuration du projet.

### Autres changements
- **Documentation** :
    - Clarification de l'usage combiné de `addCollection` et `createVueDsfrIconPlugin` dans le guide Nuxt [#1380](https://github.com/dnum-mi/vue-dsfr/pull/1380).
    - Mise à jour des guides concernant l'assistance par agents IA (conventions, commandes et workflows) [#1337](https://github.com/dnum-mi/vue-dsfr/pull/1337), [#1364](https://github.com/dnum-mi/vue-dsfr/pull/1364), [#1366](https://github.com/dnum-mi/vue-dsfr/pull/1366).
    - Correction de la branche cible par défaut lors de la création de pull requests [#1358](https://github.com/dnum-mi/vue-dsfr/pull/1358).
