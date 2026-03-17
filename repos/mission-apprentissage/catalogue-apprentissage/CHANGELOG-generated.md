## Changelog : catalogue-apprentissage (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées au Catalogue des offres de formations en apprentissage au cours des 30 derniers jours. Les principales évolutions concernent la synchronisation des données, la correction de bugs liés à l'affichage et au traitement des informations, ainsi que des optimisations techniques pour améliorer la performance et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Correction d'un problème empêchant l'affichage du détail des formations pour la Corse. [#f273dff](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/f273dff)
- Correction d'un problème empêchant le recalcul du périmètre. [#68975a6](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/68975a6)
- Ajout d'options de configuration sur une page dédiée. [#8e9e717](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/8e9e717)
- Migration pour correction des statuts après problèmes dans le flux RCO (plusieurs interventions). [#80e366b](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/80e366b), [#9ef934d](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/9ef934d), [#7c4ac0f](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/7c4ac0f), [#ecbb23c](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/ecbb23c)

### Évolutions techniques
- Mise à jour de Mongoose vers la version 9 et réécriture du plugin `diffHistory`. [#d3c7a03](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/d3c7a03)
- Amélioration de la synchronisation avec Elasticsearch. [#5c0429b](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/5c0429b)
- Correction d'un problème empêchant la recréation d'un index Elasticsearch. [#8f4d73e](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/8f4d73e)
- Réactivation des hooks MongooseElastic avant la synchronisation avec Elasticsearch lors des jobs nocturnes. [#621b091](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/621b091)
- Modification du nom des archives du flux RCO et ajout de l'option `pauseHooks` lors de l'exécution uniquement des scripts de synchronisation du flux. [#3d09f9d](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/3d09f9d)
- Ajout d'un serveur Mailpit en local pour les tests SMTP. [#e208de8](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/e208de8)

### Autres changements
- Correction d'un problème avec ESLint. [#d7fd463](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/d7fd463)
- Nettoyage de variables d'environnement obsolètes. [#92d2687](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/92d2687), [#e948991](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/e948991)
- Ajout de Metabase en environnement de développement. [#e948991](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/e948991)
- Correction du format d'un log. [#460f1cd](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/460f1cd)
- Correction de problèmes dans les tests. [#f56d816](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/f56d816), [#51d5a92](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/51d5a92)
- Mise à jour de la version de Yarn. [#3c5d2b4](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/3c5d2b4)
- Correction du fichier `yarn.lock`. [#faeaa6d](https://github.com/mission-apprentissage/catalogue-apprentissage/commit/faeaa6d)
