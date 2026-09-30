## Changelog : potentiel (30 derniers jours, au 29/09/2026)

### Résumé
Ce mois a été marqué par l'intégration de plusieurs cycles de versions (3.87, 3.88 et 3.89), apportant des améliorations significatives à l'expérience utilisateur et de nouvelles capacités métier. Les évolutions majeures incluent l'ajout de statistiques publiques, la visualisation cartographique des sites de production et un renforcement de l'accessibilité. Le projet a également bénéficié de mises à jour de sécurité et d'une optimisation de l'infrastructure de stockage et d'authentification.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** :
    - Ajout de statistiques publiques et amélioration de leur affichage ([#4575](https://github.com/MTES-MCT/potentiel/issues/4575)).
    - Intégration d'une carte des sites de production sur la page projet ([#4634](https://github.com/MTES-MCT/potentiel/issues/4634)).
    - Création de nouvelles tâches pour les attestations de constitution ([#4631](https://github.com/MTES-MCT/potentiel/issues/4631)).
    - Possibilité d'importer et de modifier de nouveaux fournisseurs "Sol" ([#4564](https://github.com/MTES-MCT/potentiel/issues/4564)).
    - Disponibilité de l'attestation d'actionnariat dans les documents du projet ([#4540](https://github.com/MTES-MCT/potentiel/issues/4540)).
- **Expérience utilisateur et interface** :
    - Amélioration du tri dans la liste des projets ([#4623](https://github.com/MTES-MCT/potentiel/issues/4623)).
    - Optimisation des modèles d'emails (invitations et variables complexes) ([#4608](https://github.com/MTES-MCT/potentiel/issues/4608), [#4632](https://github.com/MTES-MCT/potentiel/issues/4632)).
    - Mise à jour de la signalétique (badges de statut, renommage d'onglets, correction de typos) ([#4601](https://github.com/MTES-MCT/potentiel/issues/4601), [#4617](https://github.com/MTES-MCT/potentiel/issues/4617), [#4636](https://github.com/MTES-MCT/potentiel/issues/4636)).
    - Amélioration de la clarté des messages (avis de rejet, erreurs de doublons) ([#4629](https://github.com/MTES-MCT/potentiel/issues/4629), [#4548](https://github.com/MTES-MCT/potentiel/issues/4548)).
- **Accessibilité** :
    - Optimisation de la navigation pour les lecteurs d'écran, notamment pour les liens "ouvrir dans un nouvel onglet" ([#4624](https://github.com/MTES-MCT/potentiel/issues/4624), [#4596](https://github.com/MTES-MCT/potentiel/issues/4596), [#4578](https://github.com/MTES-MCT/potentiel/issues/4578)).
- **Gestion des droits et corrections** :
    - Affinement des permissions sur l'historique ([#4607](https://github.com/MTES-MCT/potentiel/issues/4607)), les formulaires de modification ([#4589](https://github.com/MTES-MCT/potentiel/issues/4589)) et l'accès aux détails de changement de puissance ([#4590](https://github.com/MTES-MCT/potentiel/issues/4590)).
    - Corrections de bugs sur les fonctions de recherche ([#4625](https://github.com/MTES-MCT/potentiel/issues/4625), [#4595](https://github.com/MTES-MCT/potentiel/issues/4595)), les filtres de listes ([#4620](https://github.com/MTES-MCT/potentiel/issues/4620)) et la validation des champs requis ([#4581](https://github.com/MTES-MCT/potentiel/issues/4581)).

### Évolutions techniques
- **Infrastructure et CI/CD** :
    - Mise à jour de l'environnement de déploiement (passage à Node 24 pour la CI/CD) ([#4637](https://github.com/MTES-MCT/potentiel/issues/4637)).
    - Évolutions sur le stockage et l'authentification (utilisation de nouveaux dépôts MinIO et mise à jour de Keycloak) ([#4638](https://github.com/MTES-MCT/potentiel/issues/4638), [#4591](https://github.com/MTES-MCT/potentiel/issues/4591), [#4609](https://github.com/MTES-MCT/potentiel/issues/4609), [#4551](https://github.com/MTES-MCT/potentiel/issues/4551)).
- **Sécurité** :
    - Implémentation de tags d'authentification pour le chiffrement de l'ID projet ([#4588](https://github.com/MTES-MCT/potentiel/issues/4588)).
    - Mise à jour des correctifs de sécurité des packages ([#4568](https://github.com/MTES-MCT/potentiel/issues/4568)).
- **Architecture et Performance** :
    - Refactoring des templates de pages vers un système de sections ([#4557](https://github.com/MTES-MCT/potentiel/issues/4557)).
    - Optimisation de la gestion des connexions et des projections PostgreSQL ([#4613](https://github.com/MTES-MCT/potentiel/issues/4613), [#4618](https://github.com/MTES-MCT/potentiel/issues/4618), [#4583](https://github.com/MTES-MCT/potentiel/issues/4583)).
    - Intégration des releases 3.87, 3.88 et 3.89.

### Autres changements
- **Tests et Documentation** :
    - Ajout de nouveaux fichiers de tests pour les API ([#4604](https://github.com/MTES-MCT/potentiel/issues/4604), [#4599](https://github.com/MTES-MCT/potentiel/issues/4599)).
    - Mise à jour du Storybook ([#4537](https://github.com/MTES-MCT/potentiel/issues/4537)).
