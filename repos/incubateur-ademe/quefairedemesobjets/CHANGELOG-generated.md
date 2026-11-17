## Changelog : quefairedemesobjets (30 derniers jours, au 17/11/2026)

### Résumé
Ce mois a été marqué par le passage en version finale de l'Assistant (V2), offrant une expérience utilisateur plus fluide et complète, ainsi que par une modernisation profonde des outils de gestion de données et de l'infrastructure de déploiement pour gagner en rapidité et en sécurité.

### Évolutions fonctionnelles
- **Lancement de l'Assistant V2** : Fin de la phase bêta avec un nouveau parcours utilisateur complet (accueil, fiches, solutions, carte) et une intégration généralisée des iframes [#3655](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3655).
- **Amélioration de l'expérience Assistant** : Optimisation de la fluidité de la carte, ajout de la géolocalisation, affichage des gestes supportés par les lieux et amélioration de l'ergonomie visuelle [#3645](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3645) [#3640](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3640) [#3669](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3669).
- **Expansion de l'Open Data** : Mise à disposition des données de lieux, de produits et de consignes de tri via l'API v1 et sur S3 [#3517](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3517) [#3444](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3444).
- **Nouveau système d'administration des Suggestions** : Implémentation d'une interface moderne (Django + React) permettant la validation par ligne, les actions de masse et la gestion par cohortes [#3488](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3488) [#3492](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3492) [#3493](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3493).
- **Accessibilité et UI** : Correction de l'affichage des iframes sur mobile et amélioration de l'accessibilité des modales [#3635](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3635) [#3590](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3590).

### Évolutions techniques
- **Optimisation de la CI/CD** : Refonte majeure des pipelines pour accélérer les déploiements (parallélisation des tests, meilleur usage du cache Docker, workflows par application et exécution différenciée selon les changements) [#3593](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3593) [#3587](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3587) [#3586](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3586).
- **Renforcement de la sécurité** : Mise en place de scans automatiques des images Docker avec Trivy et correction de plusieurs vulnérabilités (CVE) [#3665](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3665) [#3692](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3692).
- **Architecture et Infrastructure** : Déploiement d'un Nginx serverless devant Metabase et Airflow, et migration de la gestion des suggestions vers une nouvelle architecture technique [#3446](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3446) [#3488](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3488).
- **Data & Machine Learning** : Lancement d'un projet de déduplication des acteurs par approche Machine Learning et fiabilisation des pipelines d'enrichissement de données (DBT/Airflow) [#3176](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3176) [#3532](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3532).

### Autres changements
- **Documentation** : Ajout de la documentation pour le nouveau module d'administration des suggestions [#3494](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3494).
- **Maintenance** : Renommage de composants pour une meilleure clarté du code et nettoyage des comportements hérités (legacy) [#3574](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3574) [#3662](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3662).
