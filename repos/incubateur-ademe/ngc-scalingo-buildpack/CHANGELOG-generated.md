## Changelog : ngc-scalingo-buildpack (30 derniers jours, au 2 juin 2026)

### Résumé
Ce buildpack a connu des améliorations significatives pour le déploiement de monorepos pnpm sur Scalingo. Les changements se concentrent sur la correction de problèmes liés à la copie des fichiers de build, à la compatibilité avec différentes versions de pnpm et à l'optimisation du processus de déploiement pour une meilleure fiabilité et performance.

### Évolutions fonctionnelles
- Correction d'un problème de copie des fichiers de build `.next/` qui pouvaient être corrompus à cause de liens symboliques. [#66f7381](https://github.com/incubateur-ademe/ngc-scalingo-buildpack/commit/66f7381)
- Amélioration de la compatibilité avec différentes versions de pnpm en utilisant le mode `--legacy` pour le déploiement. [#268dad9](https://github.com/incubateur-ademe/ngc-scalingo-buildpack/commit/268dad9)
- Correction de l'injection des packages de l'espace de travail lors du déploiement avec pnpm. [#0290326](https://github.com/incubateur-ademe/ngc-scalingo-buildpack/commit/0290326)
- Correction de la correspondance entre la taille de l'image et la version de Node.js. [#f1784fd](https://github.com/incubateur-ademe/ngc-scalingo-buildpack/commit/f1784fd)

### Évolutions techniques
- Refonte du processus de déploiement pour utiliser `pnpm deploy` de manière universelle, remplaçant le mode "standalone". [#a1a1aae](https://github.com/incubateur-ademe/ngc-scalingo-buildpack/commit/a1a1aae)
- Utilisation de l'option `--config.shamefully-hoist=true` au lieu d'une variable d'environnement pour activer le hoisting. [#ddc1ae6](https://github.com/incubateur-ademe/ngc-scalingo-buildpack/commit/ddc1ae6)
- Amélioration de la vérification des dépendances transitives après le déploiement. [#e3c39ea](https://github.com/incubateur-ademe/ngc-scalingo-buildpack/commit/e3c39ea)
- Utilisation de `grep` au lieu de `node` pour lire le nom du package, améliorant ainsi la robustesse. [#3cb1be7](https://github.com/incubateur-ademe/ngc-scalingo-buildpack/commit/3cb1be7)

### Autres changements
- Suppression des logs de débogage inutiles. [#d072218](https://github.com/incubateur-ademe/ngc-scalingo-buildpack/commit/d072218)
- Ajout de logs pour les arguments de déploiement et la décision de hoisting. [#82ad0f9](https://github.com/incubateur-ademe/ngc-scalingo-buildpack/commit/82ad0f9)
- Initialisation du buildpack pour le déploiement de monorepos pnpm. [#0c27415](https://github.com/incubateur-ademe/ngc-scalingo-buildpack/commit/0c27415)
