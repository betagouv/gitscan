## Changelog : ngc-scalingo-buildpack (30 derniers jours, au 6 mai 2026)

### Résumé
Ce buildpack a été initialement créé pour faciliter le déploiement d'applications utilisant des monorepos gérés avec pnpm sur Scalingo. Les récentes améliorations se concentrent sur la correction de problèmes liés à la taille de l'image Docker générée et à la compatibilité de la version de Node.js utilisée, ainsi que sur la robustesse de la détection du nom du package.

### Évolutions fonctionnelles
- Correction d'un problème où la taille de l'image Docker générée était incorrecte. [#1](https://github.com/incubateur-ademe/ngc-scalingo-buildpack/issues/1)
- Amélioration de la compatibilité avec différentes versions de Node.js. [#1](https://github.com/incubateur-ademe/ngc-scalingo-buildpack/issues/1)

### Évolutions techniques
- Utilisation de `grep` au lieu de `node` pour lire le nom du package, améliorant la robustesse et la performance. [#2](https://github.com/incubateur-ademe/ngc-scalingo-buildpack/issues/2)
- Initialisation du buildpack pour le déploiement de monorepos pnpm. [#3](https://github.com/incubateur-ademe/ngc-scalingo-buildpack/issues/3)
