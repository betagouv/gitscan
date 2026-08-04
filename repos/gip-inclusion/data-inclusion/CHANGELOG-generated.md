## Changelog : data-inclusion (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, les développements se sont concentrés sur l'amélioration de l'intelligence de la recherche et la fiabilisation des processus de collecte de données. L'objectif est d'offrir des résultats de recherche plus pertinents et de garantir une plus grande précision dans les informations agrégées.

### Évolutions fonctionnelles
- **Amélioration de la recherche** : 
    - Le moteur de recherche est désormais plus tolérant aux fautes de frappe.
    - Ajout d'une option de dédoublonnage pour la recherche sémantique.
    - Optimisation de la pertinence des résultats grâce à un meilleur équilibrage entre les thématiques et les noms de structures.

### Évolutions techniques
- **Fiabilisation des pipelines de données** :
    - Renforcement du déterminisme des flux de données pour les sources *carif-oref* et *réseau-alpha* afin d'assurer une stabilité accrue.
    - Correction de la qualité des données : résolution de problèmes de format (ex: âges mal formatés) et correction de l'émission erronée de certains services publics.
- **Mise à jour des modèles de données** :
    - Intégration de nouvelles catégories de données (*cooling_space* et type "Orienteur" pour *les-emplois*).

### Autres changements
- Mise à jour de la configuration des notifications Slack pour les résumés de pipeline.
