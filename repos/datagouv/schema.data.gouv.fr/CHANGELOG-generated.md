## Changelog : schema.data.gouv.fr (30 derniers jours, au 16 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a enrichi son catalogue avec de nouveaux schémas de données et a bénéficié d'améliorations techniques pour garantir la stabilité et la fiabilité de la génération du site web.

### Évolutions fonctionnelles
- Ajout de nouveaux schémas de données : schémas ACEN et `risques-carto-di` ([#355](https://github.com/datagouv/schema.data.gouv.fr/issues/355)).
- Mise à jour régulière des contenus du site et des recommandations de bonnes pratiques.

### Évolutions techniques
- Résolution des erreurs de dépassement de mémoire (Out Of Memory) lors de la construction du site via l'augmentation de la limite de la pile Node ([#359](https://github.com/datagouv/schema.data.gouv.fr/issues/359)).
- Optimisation de la gestion de la configuration par la consolidation des fichiers de configuration.
- Correction de la syntaxe de certains fichiers de configuration YAML.
