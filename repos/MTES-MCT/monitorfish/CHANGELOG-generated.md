## Changelog : monitorfish (30 derniers jours, au 18 juin 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations concernant le suivi des navires, notamment l'intégration des données AIS (Automatic Identification System) pour afficher la position des navires sur la carte. Des corrections et des améliorations ont également été apportées aux formulaires de contrôle en mer et à terre, ainsi qu'à la gestion des signalements INN et des préavis. Des optimisations techniques et des corrections de bugs ont également été réalisées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **AIS :** Affichage des navires équipés d'un système AIS sur la carte, avec des informations sur leur type, leur destination et leur position récente.
- **Contrôles en mer et à terre :** Modifications des formulaires pour l'e-ISR (échange électronique d'informations sur les contrôles) v1.2, incluant la gestion des espèces, des quantités et des zones de pêche.
- **Signalements INN :** Amélioration des filtres dans la liste des signalements INN pour faciliter la recherche et la gestion. Possibilité pour le pôle INN de mettre à jour les signalements liés aux fiches Navpro.
- **Préavis :** Affichage de la raison pour laquelle un préavis est "à vérifier" (note, signalement, port état tiers).
- **Unités :** Ajout d'une recherche par type et base lors de la création d'une nouvelle unité.
- **NATINF :** Ajout des NATINF 4789 et 30013.
- **Gestion des engins :** Ajout d'un engin pour les navires auxiliaires à la campagne BFT (Thon Rouge).

### Évolutions techniques
- **Backend :** Mise à jour de plusieurs dépendances backend (Spring Boot, Security, Flyway, Ktor).
- **Frontend :** Mise à jour de plusieurs dépendances frontend (uuid, TS-ESLint, styled-components, monitor-ui, ol, fuse.js).
- **Kafka :** Ajout de la gestion de Kafka pour l'intégration des données AIS. Configuration et gestion des variables d'environnement associées.
- **Tests :** Correction de tests Cypress et amélioration de la stabilité des tests e2e.
- **Base de données :** Ajout d'index pour optimiser les performances des requêtes sur les notes de vente dans le data warehouse.
- **Architecture :** Refactorisation du code pour séparer les espèces embarquées et les rejets dans les contrôles.

### Autres changements
- Amélioration de la documentation pour la génération du fichier .p12.
- Correction de problèmes de linting et de style de code.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Correction de problèmes d'affichage et de comportement des formulaires.
- Ajout de logs et d'informations de débogage pour faciliter la résolution des problèmes.
- Correction de problèmes de sérialisation des données.
- Amélioration de la gestion des erreurs et des exceptions.
