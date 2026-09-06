## Changelog : hydra (30 derniers jours, au 04/09/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la fiabilité du processus de collecte (crawler) et l'optimisation de la gestion des fichiers compressés. Le projet renforce également ses capacités de suivi et de mesure de performance pour garantir une meilleure stabilité du pipeline de données.

### Évolutions techniques
- **Robustesse du crawler** : ajout d'un mécanisme de repli (fallback) vers la méthode GET en cas d'expiration (timeout) des requêtes HEAD ([#461](https://github.com/datagouv/hydra/pull/461)).
- **Gestion des formats de données** : refonte du traitement des fichiers Gzip pour permettre un meilleur routage des formats après décompression ([#476](https://github.com/datagouv/hydra/pull/476)) et mise à jour de la détection des fichiers CSV ([#477](https://github.com/datagouv/hydra/pull/477)).
- **Performance et observabilité** : intégration de benchmarks de performance ([#464](https://github.com/datagouv/hydra/pull/464)) et ajout de logs pour tracer les écarts lors de la mise à jour des ressources ([#466](https://github.com/datagouv/hydra/pull/466)).
- **Maintenance** : correction d'un problème d'importation circulaire ([#478](https://github.com/datagouv/hydra/pull/478)).

### Autres changements
- **Documentation** : ajout de commentaires explicatifs concernant le suivi des mises à jour de ressources ([#466](https://github.com/datagouv/hydra/pull/466)).
