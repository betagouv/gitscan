## Changelog : st-home (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à la robustesse de l'application, notamment dans le traitement des données SIRENE et DILA SIRET. L'interface utilisateur a également été améliorée, avec des corrections d'affichage et l'ajout de fonctionnalités pour le blog (pagination, catégories, partage). Enfin, l'architecture interne a été optimisée avec le remplacement de Celery par Dramatiq pour la gestion des tâches asynchrones.

### Évolutions fonctionnelles
- Amélioration du blog avec pagination, catégories et liens de partage. [#70](https://github.com/suitenumerique/st-home/issues/70)
- Correction de l'affichage du bouton de commune sur la carte de conformité. [#73](https://github.com/suitenumerique/st-home/issues/73)
- Amélioration de la classification SIRENE et corrections d'interface utilisateur pour le RPNT.
- Ajout d'une migration pour la table d'historique des RCPNT.

### Évolutions techniques
- Remplacement de Celery par Dramatiq pour la gestion des tâches asynchrones, améliorant la fiabilité et la performance. [#70](https://github.com/suitenumerique/st-home/issues/70)
- Amélioration de la robustesse du téléchargement SIRENE et de la correspondance DILA SIRET.
- Correction d'un contournement de la liste noire et gestion des erreurs de géolocalisation dans Caddy. [#72](https://github.com/suitenumerique/st-home/issues/72)
- Mise à jour du dashboard du worker.

### Autres changements
- Nouvelle version du changelog pour le RPNT (0.2.1).
- Adaptation des tentatives et mise à niveau du dashboard du worker.
