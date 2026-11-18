## Changelog : dialog-integrations (30 derniers jours, au 17 novembre 2026)

### Résumé
Ce mois-ci, le projet a connu une refonte majeure de son moteur de règles. Cette évolution permet d'améliorer significativement la qualité des données d'arrêtés de circulation en filtrant automatiquement les informations incomplètes ou non pertinentes (ex: mesures uniquement cyclables, tonnages extrêmes). La stabilité des processus de synchronisation et l'intégration de nouvelles données (Limoges, Paris) ont également été renforcées.

### Évolutions fonctionnelles
- **Amélioration de la qualité des données** : Mise en place de nouveaux critères de validation pour exclure automatiquement les données peu pertinentes, telles que les mesures ciblant uniquement les piétons/cycles, les limitations de tonnage hors normes, ou les réglementations temporaires expirées ou incomplètes.
- **Optimisation de l'intégration de Paris** : Amélioration du filtrage des champs textuels et de la gestion des sens uniques pour les données parisiennes [#37, #43, #44].
- **Nouvelle intégration** : Ajout des limites de tonnage pour la ville de Limoges.

### Évolutions techniques
- **Refonte de l'architecture des règles** : Passage d'un système de simple filtrage à un système de validation robuste, permettant d'appliquer des règles communes à toutes les sources de données [#41].
- **Restructuration du pipeline de données** : Découpage du processus d'organisation en étapes modulaires et déplacement du moteur central pour une meilleure maintenance [#39, #40].
- **Fiabilisation des échanges externes** : Standardisation des appels vers les services tiers avec l'ajout systématique de délais d'attente (timeouts) et de tentatives de reconnexion automatiques.
- **Sécurisation des synchronisations** : Renforcement de la stabilité des synchronisations nocturnes via une gestion par source et de nouveaux mécanismes de contrôle [#38].
- **Nouveau connecteur** : Capacité de lecture unifiée pour les exports Opendatasoft et les couches ArcGIS.

### Autres changements
- **Nettoyage du code** : Suppression d'utilitaires inutilisés, simplification des messages de log et des commentaires pour plus de clarté.
- **Maintenance CI/CD** : Retrait de l'intégration de Rennes dans les tests automatisés.
