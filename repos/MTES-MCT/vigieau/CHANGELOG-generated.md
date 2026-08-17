## Changelog : vigieau (30 derniers jours, au 16 août 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'accessibilité numérique pour garantir que la plateforme soit utilisable par tous, ainsi que sur la fiabilisation des données de restrictions d'eau. Les corrections apportées assurent une meilleure précision des informations historiques et une synchronisation plus robuste avec les sources officielles (SANDRE, DataGouv).

### Évolutions fonctionnelles
- **Accessibilité numérique (RGAA) :** Amélioration majeure de l'expérience utilisateur pour les personnes en situation de handicap (correction de la navigation, des formulaires, des contrastes, des tableaux de données et de la gestion du focus).
- **Fiabilité des données métier :** Correction de l'affichage de la sévérité des restrictions et de la continuité des dates d'arrêtés pour garantir une information cohérente.

### Évolutions techniques
- **Synchronisation des données :** Résolution de nombreux problèmes de dérive de schéma (*schema drift*) et de réconciliation des données provenant de SANDRE et DataGouv ([#36](https://github.com/MTES-MCT/vigieau/pull/36), [#37](https://github.com/MTES-MCT/vigieau/pull/37), [#38](https://github.com/MTES-MCT/vigieau/pull/38), [#39](https://github.com/MTES-MCT/vigieau/pull/39), [#40](https://github.com/MTES-MCT/vigieau/pull/40), [#41](https://github.com/MTES-MCT/vigieau/pull/41), [#42](https://github.com/MTES-MCT/vigieau/pull/42)).
- **Moteur de statistiques :** Sécurisation de la publication atomique des snapshots et de l'historique départemental pour éviter les données partielles.
- **Infrastructure et CI/CD :** Renforcement de la durabilité des pipelines de tests de production (*smoke tests*) et mise en place de politiques de fraîcheur des données ([#32](https://github.com/MTES-MCT/vigieau/pull/32), [#33](https://github.com/MTES-MCT/vigieau/pull/33), [#35](https://github.com/MTES-MCT/vigieau/pull/35)).
- **Optimisation et stabilité :** Amélioration de la gestion de la mémoire lors de la publication des zones et renforcement de la résilience des processus de rattrapage de données.

### Autres changements
- **Documentation :** Ajout d'un plan de remédiation RGAA et documentation de la branche principale (`master`) ([#34](https://github.com/MTES-MCT/vigieau/pull/34)).
- **Sécurité :** Correction de vulnérabilités identifiées sur des dépendances npm.
