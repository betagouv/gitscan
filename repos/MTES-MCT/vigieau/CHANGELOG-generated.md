## Changelog : vigieau (30 derniers jours, au 16 août 2026)

### Résumé
Ce mois a été principalement consacré à la mise en conformité de la plateforme avec les normes d'accessibilité numérique (RGAA) et à la fiabilisation des flux de données. Les efforts ont porté sur la correction des erreurs de synchronisation avec les sources officielles (SANDRE, DataGouv) et sur la stabilisation des processus de publication des statistiques et des zones de restriction, garantissant ainsi une information plus précise et inclusive pour tous les utilisateurs.

### Évolutions fonctionnelles
- **Accessibilité (RGAA) :** Amélioration majeure de l'expérience utilisateur pour les personnes en situation de handicap, incluant la navigation, la gestion du focus, la sémantique des formulaires, la lisibilité des tableaux de données et des cartes, ainsi que les contrastes visuels.
- **Fiabilité des données :** Correction de l'historique des restrictions par commune et amélioration de la précision des données de zones de restriction.
- **Suivi de service :** Ajout d'un indicateur de santé pour la synchronisation des publications.

### Évolutions techniques
- **Synchronisation et intégrité des données :**
    - Résolution des dérives de schémas (schema drift) lors de la synchronisation avec le SANDRE [#36](https://github.com/MTES-MCT/vigieau/pull/36) [#37](https://github.com/MTES-MCT/vigieau/pull/37).
    - Sécurisation et atomisation des processus de publication des zones et des statistiques pour éviter toute corruption de données.
    - Amélioration de la gestion des preuves et des délais de synchronisation MDM (Master Data Management) [#41](https://github.com/MTES-MCT/vigieau/pull/41) [#42](https://github.com/MTES-MCT/vigieau/pull/42).
- **Infrastructure et CI/CD :**
    - Mise en place de tests de fumée ("smoke tests") en production pour garantir la disponibilité et la fraîcheur des données [#32](https://github.com/MTES-MCT/vigieau/pull/32) [#33](https://github.com/MTES-MCT/vigieau/pull/33).
    - Renforcement de la robustesse et de la durabilité des pipelines de déploiement.
- **Performance et stabilité :**
    - Optimisation de la reprise d'historique par département et gestion de la mémoire lors de la publication des zones.
    - Correction de vulnérabilités de sécurité sur les dépendances npm.

### Autres changements
- **Documentation :** Définition de la branche `master` comme branche canonique [#34](https://github.com/MTES-MCT/vigieau/pull/34) et établissement d'un plan de remédiation pour l'accessibilité.
