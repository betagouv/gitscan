## Changelog : vue-dsfr (30 derniers jours, au 11/08/2026)

### Résumé
Ce mois-ci, la bibliothèque a considérablement amélioré la gestion des icônes, notamment pour faciliter leur utilisation en mode hors-ligne et lors de rendus côté serveur (SSR/SSG). Parallèlement, l'infrastructure de développement a été stabilisée via des mises à jour de la chaîne de build et de la CI/CD, tandis que la documentation a été enrichie pour mieux accompagner l'usage avec Nuxt et l'assistance par agents IA.

### Évolutions fonctionnelles
- **Gestion des icônes** : 
    - Ajout de l'option `preferOffline` pour privilégier l'utilisation des collections d'icônes locales [#1383](https://github.com/dnum-mi/vue-dsfr/issues/1383).
    - Support du format `prefixe-nom` pour la résolution des icônes hors-ligne [#1386](https://github.com/dnum-mi/vue-dsfr/issues/1386).
    - Support du rendu local des icônes pour les environnements SSG et SSR [#1369](https://github.com/dnum-mi/vue-dsfr/issues/1369).
    - Correction du `viewBox` invalide pour le composant `VIconOffline` lorsque les positions sont absentes [#1372](https://github.com/dnum-mi/vue-dsfr/issues/1372).
- **Composants UI** : Correction des erreurs liées à l'utilisation du presse-papier dans le composant `DsfrDataTable` [#1352](https://github.com/dnum-mi/vue-dsfr/issues/1352).

### Évolutions techniques
- **CI/CD et Build** : 
    - Correction des workflows de release pour assurer la compatibilité avec Node 24 [#1375](https://github.com/dnum-mi/vue-dsfr/issues/1375).
    - Stabilisation des builds Storybook sur Netlify et gestion de l'isolation avec Vite 7.
    - Mise à jour de l'environnement de build vers pnpm v11.
    - Correction des noms d'événements Vue dans les processus de build.
- **Refactoring** : Modernisation de la gestion des chemins de fichiers via l'utilisation de `import.meta.dirname`.

### Autres changements
- **Documentation** : 
    - Clarification de l'usage combiné des plugins d'icônes dans le guide Nuxt [#1380](https://github.com/dnum-mi/vue-dsfr/issues/1380).
    - Mise à jour des guides concernant l'assistance par agents IA (conventions et sécurisation des commandes personnalisées).
    - Correction de la branche cible par défaut pour les Pull Requests [#1358](https://github.com/dnum-mi/vue-dsfr/issues/1358).
