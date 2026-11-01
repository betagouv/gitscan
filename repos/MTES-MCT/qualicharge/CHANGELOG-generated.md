## Changelog : qualicharge (30 derniers jours, au 24 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante dans l'ouverture des données avec l'automatisation de l'export des tarifs vers les services OpenData. Nous avons également renforcé la fiabilité des indicateurs de performance et consolidé la sécurité de l'ensemble de l'application.

### Évolutions fonctionnelles
- **Ouverture des données** : Mise en place de l'exportation automatique des tarifs vers le service OpenData via l'outil Data7.

### Évolutions techniques
- **Fiabilité des données** : Correction de la logique de calcul des indicateurs (e2, e3 et e6) pour assurer une prise en compte correcte des statuts manquants.
- **Sécurité** : Résolution de plusieurs vulnérabilités et mise à jour des dépendances transitatives non sécurisées.
- **Infrastructure & CI/CD** : Correction du processus d'initialisation (seeding) de la base de données au sein des workflows Prefect.
- **Maintenance** : Passage de la version de l'API à 0.35.1.
