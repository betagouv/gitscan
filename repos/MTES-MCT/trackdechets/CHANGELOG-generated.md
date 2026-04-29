## Changelog : trackdechets (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des BSD (Bordereaux de Suivi des Déchets), notamment en facilitant la modification des informations, en corrigeant des bugs bloquants et en ajoutant de nouvelles fonctionnalités pour les utilisateurs ETQ (Établissements Titulaires d'une Exploitation). L'implémentation de l'authentification à double facteur (2FA) renforce également la sécurité de la plateforme. Des améliorations ont été apportées à l'interface utilisateur et à la gestion des codes déchets Bâle.

### Évolutions fonctionnelles
- **BSDD (Bordereau de Suivi des Déchets de Déchets Dangereux):**
    - Possibilité de modifier les intermédiaires jusqu'à la signature de la réception par la destination. [#4741](https://github.com/MTES-MCT/trackdechets/issues/4741)
    - Ajout de la possibilité d'ajouter 2 intermédiaires supplémentaires. [#4738](https://github.com/MTES-MCT/trackdechets/issues/4738)
- **Authentification:**
    - Implémentation de l'authentification à double facteur (2FA) avec possibilité de la désactiver. [#4736](https://github.com/MTES-MCT/trackdechets/issues/4736), [#4739](https://github.com/MTES-MCT/trackdechets/issues/4739), [#4740](https://github.com/MTES-MCT/trackdechets/issues/4740)
- **BSFF (Bordereau de Suivi des Déchets):**
    - Ajout de champs pour l'émetteur, le transporteur et la destination.
    - Sélection du type de BSFF.
- **ETQ:**
    - Possibilité pour les administrateurs ETQ d'anonymiser un utilisateur par son adresse email. [#4722](https://github.com/MTES-MCT/trackdechets/issues/4722)
    - Correction d'un bug empêchant la création d'un BSFF avec un SIRET fermé. [#4717](https://github.com/MTES-MCT/trackdechets/issues/4717)
- **Codes déchets Bâle:**
    - Création d'une liste de codes déchets Bâle. [#4719](https://github.com/MTES-MCT/trackdechets/issues/4719)
- **BSDA:**
    - Récupération des métadonnées du BSDA dans les formulaires front-end. [#4720](https://github.com/MTES-MCT/trackdechets/issues/4720)
    - Correction d'un bug de mise à jour sur le VHU avec plusieurs transporteurs. [#4718](https://github.com/MTES-MCT/trackdechets/issues/4718)
    - La modal de signature transporteur permet désormais de modifier les informations de contact. [#4713](https://github.com/MTES-MCT/trackdechets/issues/4713)
- **BSVHU:**
    - Correction d'un blocage lors de la publication d'un BSVHU si le champ dépassait 250 caractères. [#4728](https://github.com/MTES-MCT/trackdechets/issues/4728)

### Évolutions techniques
- Correction d'un problème d'affichage de CRISP pour les politiques.
- Refactorisation du code pour améliorer la performance et la maintenabilité.
- Correction de problèmes de format et de tests d'intégration.
- Mise en place d'un script pour la modification de la base de données.
- Suppression d'un sélecteur de société inutile dans certains cas.

### Autres changements
- Mise à jour du texte présent dans le bandeau d'information. [#4733](https://github.com/MTES-MCT/trackdechets/issues/4733)
- Préparation de la recette du 28 avril 2026.
- Ajout d'un chatbot IA (en préparation). [#4743](https://github.com/MTES-MCT/trackdechets/issues/4743)
- Diverses corrections de style et de documentation.
