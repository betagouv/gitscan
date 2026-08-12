## Changelog : sylvasan (30 derniers jours, au 07/08/2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de la précision des données géographiques, l'enrichissement des exports de données et l'optimisation de l'expérience de saisie sur le terrain. L'interface a été affinée pour rendre les formulaires plus lisibles et les actions plus explicites pour les agents.

### Évolutions fonctionnelles
- **Exports de données** : Amélioration de la richesse des exports qui incluent désormais le titre de l'enquête, les suivis (*follow-ups*) et l'identifiant externe des répondants [#516](https://github.com/betagouv/sylvasan/pull/516).
- **Cartographie et Géolocalisation** :
    - Ajout d'indicateurs de précision GPS (cercle de précision et échelle) pour une meilleure fiabilité des relevés [#497](https://github.com/betagouv/sylvasan/pull/497).
    - Amélioration de la carte avec l'ajout du clustering et de la visibilité des suivis sur l'observation [#515](https://github.com/betagouv/sylvasan/pull/515).
    - Le bouton de géolocalisation est désormais disponible sur l'ensemble des cartes.
- **Saisie et Formulaires** :
    - Amélioration de la visibilité des champs obligatoires (ajustement des labels, des icônes et des styles) [#514](https://github.com/betagouv/sylvasan/pull/514).
    - Optimisation de la gestion des images (affichage en plein écran et nouveau composant dédié sur le web).
    - Clarification des libellés pour les actions de sauvegarde en brouillon et d'envoi d'enquête [#499](https://github.com/betagouv/sylvasan/pull/499), [#496](https://github.com/betagouv/sylvasan/pull/496).
- **Gestion des données** :
    - Ajout de filtres (notamment par organisation) et de la pagination pour la liste des enquêtes [#494](https://github.com/betagouv/sylvasan/pull/494).
    - Mise en place de mécanismes de prévention pour éviter les doublons d'observations et dans les modales de sous-enquêtes [#517](https://github.com/betagouv/sylvasan/pull/517).
- **Application Mobile** : Correction de l'ordre d'affichage des champs dans les formulaires mobiles [#500](https://github.com/betagouv/sylvasan/pull/500).

### Évolutions techniques
- **Optimisation du stockage** : Passage d'un stockage en Base64 à un stockage par ID pour les champs de type tableau (*array fields*), améliorant la performance.
- **Qualité et Accessibilité** :
    - Renforcement de l'accessibilité numérique via l'ajout d'attributs ARIA.
    - Augmentation de la couverture de tests, notamment sur la gestion des adhésions (*memberships*) [#469](https://github.com/betagouv/sylvasan/pull/469).
- **Déploiement Mobile** : Nouvelles versions et releases de l'application Android (environnements de test et préproduction).
