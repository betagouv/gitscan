## Changelog : monitorfish (30 derniers jours, au 30 octobre 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'expérience utilisateur, notamment via la modernisation de l'interface (passage au design system DSFR) et l'enrichissement des exports de données. Les performances du système ont été boostées avec un démarrage du backend deux fois plus rapide, et un effort important a été consacré à la stabilisation des tests automatisés pour garantir une meilleure fiabilité du logiciel.

### Évolutions fonctionnelles
- **Signalements et Rapports** : 
    - Amélioration des exports CSV incluant désormais les positions et coordonnées des signalements [#5586, #5600, #5580].
    - Ajout du type de cible "Engin" dans les formulaires de signalement INN [#5305].
    - Mise en place de l'archivage automatique des signalements de navires ne possédant pas de photo [#5562].
    - Optimisation de l'interface de la liste des signalements (filtres plus compacts et meilleure ergonomie) [#5112].
- **Gestion des Navires et Missions** :
    - Enrichissement de la fiche navire avec l'affichage des unités et des administrations de contrôles croisés [#5605, #5579, #5558].
    - Amélioration de la saisie des missions avec une validation plus stricte des champs obligatoires (maillage, contrôles Oui/Non) et une meilleure aide visuelle (tooltips) [#5532, #5534].
    - Possibilité d'accepter des espèces à bord sans zone FAO associée [#5603].
- **Cartographie** :
    - Correction du comportement de la carte lors du passage de l'antiméridien pour permettre un tour du globe fluide [#5571].
    - Résolution de problèmes d'affichage liés aux zones possédant des géométries vides [#3300116e].
- **Interface et Accessibilité** :
    - Refonte de la page de connexion pour l'aligner sur le design system de l'État (DSFR) [#5540, #5548].
    - Ajout d'une page dédiée à la déclaration d'accessibilité [#5553].
    - Amélioration de l'affichage des erreurs pour les navigateurs non supportés.
- **Alertes et Infractions** :
    - Mise en place d'alertes par e-mail pour les notifications (NATINF) qui ne sont plus en vigueur [#5607].
    - Correction de l'affichage des infractions en attente [#5582].

### Évolutions techniques
- **Performance Backend** : Accélération du démarrage du backend (deux fois plus rapide) grâce à l'adoption de JDK 25 et l'implémentation d'un cache AOT (Ahead-of-Time) [#5614, 7560a649].
- **Fiabilité des Tests** : 
    - Travail intensif de stabilisation des tests de bout en bout (Cypress) pour éliminer les tests instables ("flaky tests") sur plusieurs modules (vessels, reporting, map) [#5616, 22827f67, 99e1df0d, 8ebc5529].
    - Migration de l'environnement de test vers Cypress 16.
- **Observabilité** : Amélioration de la remontée des erreurs vers Sentry, notamment pour les processus de flux (flows) et les erreurs de threads [#5538, 5539, 5541].
- **Architecture** : 
    - Isolation du service MonitorFish vis-à-vis des pannes potentielles de l'environnement MonitorEnv [#5608, 9a91f98c].
    - Migration progressive vers TypeScript 7 pour le frontend.

### Autres changements
- **Documentation** : Mise à jour de la documentation générale [#5527] et ajout de nouveaux documents d'architecture (ADR) pour documenter les choix techniques [#5549, 3860435b].
