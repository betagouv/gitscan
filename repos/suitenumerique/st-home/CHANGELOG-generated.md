## Changelog : st-home (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette nouvelle version apporte des améliorations significatives à la robustesse de l'application, notamment dans le traitement des données SIRENE et la gestion des erreurs du proxy Caddy. L'interface utilisateur a également été améliorée, avec des corrections d'affichage et l'ajout de fonctionnalités au blog (pagination, catégories, partage). Enfin, l'architecture interne a été modernisée avec le remplacement de Celery par Dramatiq pour la gestion des tâches asynchrones.

### Évolutions fonctionnelles
- **Blog :** Amélioration du blog avec l'ajout de la pagination, des catégories et des liens de partage. [#70](https://github.com/suitenumerique/st-home/pull/70)
- **Carte de conformité :** Correction de l'affichage des boutons de commune. [#73](https://github.com/suitenumerique/st-home/issues/73)
- **Données SIRENE :** Amélioration de la robustesse du téléchargement des données SIRENE et du rapprochement avec les données SIRET de DILA.
- **RPNT :** Correction de certaines classifications erronées SIRENE et améliorations de l'interface utilisateur.

### Évolutions techniques
- **Architecture :** Remplacement de Celery par Dramatiq pour la gestion des tâches asynchrones, améliorant la performance et la maintenabilité. [#70](https://github.com/suitenumerique/st-home/pull/70)
- **Proxy Caddy :** Correction d'un contournement de la blocklist et gestion des erreurs de géolocalisation pour éviter les blocages. [#72](https://github.com/suitenumerique/st-home/issues/72)
- **Worker :** Adaptation des mécanismes de retries et mise à niveau du dashboard.
- **Worker :** Mise à niveau du dashboard.

### Autres changements
- Amélioration de la gestion des erreurs et de la robustesse générale de l'application.
- Ajout d'une nouvelle version du changelog pour la version 0.2.1.
