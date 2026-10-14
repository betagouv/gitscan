## Changelog : schema.data.gouv.fr (30 derniers jours, au 14 octobre 2026)

### Résumé
Le projet a connu une activité régulière centrée sur l'enrichissement du catalogue de schémas et la mise à jour de la documentation. Des ajustements techniques ont également été effectués pour garantir la stabilité du processus de génération automatique du site web.

### Évolutions fonctionnelles
- Intégration de nouveaux schémas de données : schémas ACEN et schémas risques-carto-di ([#355](https://github.com/datagouv/schema.data.gouv.fr/pull/355)).

### Évolutions techniques
- Stabilisation du processus de build : augmentation de la limite de mémoire (heap limit) de Node.js pour éviter les erreurs de dépassement de mémoire (OOM) lors de la génération du site avec Vuepress ([#359](https://github.com/datagouv/schema.data.gouv.fr/pull/359)).

### Autres changements
- Maintenance continue du contenu (mises à jour régulières du site web et des recommandations).
- Optimisation de la configuration : consolidation des fichiers de configuration et correction de fichiers YAML.
