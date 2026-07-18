## Changelog : monitorfish (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives sur le formulaire de contrôle, notamment pour l'intégration de la version 1.3 de l'e-ISR, avec des ajustements des champs affichés et de la logique de remplissage. Des efforts ont également été déployés pour améliorer la gestion des groupes de navires prioritaires, tant au niveau de l'interface utilisateur que de l'API. Enfin, des corrections de bugs et des optimisations techniques ont été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Formulaire de contrôle (CR de contrôle) :**
    - Correction de l'affichage du champ INN dans le formulaire de contrôle, notamment pour les contrôles en Outre-Mer. [#5289](https://github.com/MTES-MCT/monitorfish/issues/5289)
    - Correction du troncage du calendrier de fin de mission. [#5269](https://github.com/MTES-MCT/monitorfish/issues/5269)
    - Amélioration de l'affichage des groupes de navires et des signalements associés dans le formulaire de contrôle. [#5270](https://github.com/MTES-MCT/monitorfish/issues/5270)
    - Possibilité de sauvegarder une infraction en attente.
    - Correction de la logique d'affichage des zones FAO lors de l'ajout d'une espèce.
- **e-ISR :**
    - Mise à jour des champs facultatifs et de la logique d'application pour la version 1.3. [#5257](https://github.com/MTES-MCT/monitorfish/issues/5257)
    - Adaptation des APIs publiques pour l'intégration de l'e-ISR v1.3. [#5170](https://github.com/MTES-MCT/monitorfish/issues/5170)
    - Modifications des contrôles en mer et à la débarque pour l'e-ISR v1.2. [#5175](https://github.com/MTES-MCT/monitorfish/issues/5175)
- **Groupes de navires prioritaires :**
    - Ajout de la description des groupes prioritaires dans les nouvelles fonctionnalités. [#5231](https://github.com/MTES-MCT/monitorfish/issues/5231)
    - Affichage des groupes prioritaires avec des icônes de ciblage et réorganisation de l'affichage.
    - Ajout de données codées en dur pour les groupes prioritaires.
    - Amélioration de l'API pour récupérer les groupes de navires avec leurs vaisseaux associés.
- **Préavis :** Affichage des messages manuels dans la marée du navire. [#5222](https://github.com/MTES-MCT/monitorfish/issues/5222)
- **Propriétaire du navire :** Récupération des données du propriétaire du navire depuis Navpro.

### Évolutions techniques
- **Linting :**
    - Migration du linter frontend vers OxLint (hybride avec ESLint). [#5258](https://github.com/MTES-MCT/monitorfish/issues/5258)
    - Passage à ESLint 9 avec suppressions natives. [#5259](https://github.com/MTES-MCT/monitorfish/issues/5259)
    - Restauration de la parité Airbnb et accélération des hooks commit/push.
    - Correction des violations de linting.
    - Mise en place de hooks Git pour le linting backend via ktlint.
- **Backend :**
    - Amélioration de la performance de la fonction `GetAllVesselGroupsWithVessels`.
    - Correction de la logique `effectiveControlPriorityLevel`.
    - Ajout de tests backend pour les groupes de navires prioritaires.
    - Utilisation de `updateMany` au lieu de spread-mapping pour optimiser les performances.
- **Tests :**
    - Amélioration de la stabilité des tests Cypress (correction de flakiness).
    - Ajout de tests Cypress sur des données réelles pour l'affichage des groupes de navires.
    - Ajout de tests pour les nouveaux champs et fonctionnalités.
- **Dépendances :** Mise à jour de certaines dépendances. [#5255](https://github.com/MTES-MCT/monitorfish/issues/5255)

### Autres changements
- Correction du bug sur le champ `position_type` de la table `last_positions`. [#5229](https://github.com/MTES-MCT/monitorfish/issues/5229)
- Mise à jour de la REG UE pour les avaries VMS. [#5241](https://github.com/MTES-MCT/monitorfish/issues/5241)
- Ajout de l'opérateur à l'API publique. [#5259](https://github.com/MTES-MCT/monitorfish/issues/5259)
- Suppression de la baseline ktlint. [#5261](https://github.com/MTES-MCT/monitorfish/issues/5261)
- Amélioration de la documentation et des commentaires.
