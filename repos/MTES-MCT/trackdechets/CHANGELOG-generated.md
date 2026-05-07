## Changelog : trackdechets (30 derniers jours, au 06 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des déchets dangereux (BSFF/BSDA), avec l'ajout de fonctionnalités pour la gestion des intermédiaires, des installations d'entreposage provisoires et l'intégration avec le DSFR. L'authentification a également été renforcée avec l'implémentation de la double authentification. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- **BSFF/BSDA :** Ajout de la possibilité de modifier les intermédiaires jusqu'à la signature de la réception par la destination. [#4741](https://github.com/MTES-MCT/trackdechets/issues/4741)
- **BSFF/BSDA :** Correction d'une régression empêchant l'ajout/modification d'une installation d'entreposage provisoire (TTR) après signature de l’entreprise de travaux. [#4734](https://github.com/MTES-MCT/trackdechets/issues/4734)
- **BSFF :** Implémentation de l'ajout d'émetteur, transporteur et destination dans le formulaire BSFF.
- **BSFF :** Ajout d'un sélecteur de type de déchets Bâle. [#4737](https://github.com/MTES-MCT/trackdechets/issues/4737)
- **Authentification :** Implémentation de la double authentification (2FA) avec la possibilité de la désactiver. [#4739](https://github.com/MTES-MCT/trackdechets/issues/4739), [#4736](https://github.com/MTES-MCT/trackdechets/issues/4736), [#4740](https://github.com/MTES-MCT/trackdechets/issues/4740)
- **Interface utilisateur :** Correction de problèmes d'affichage de CRISP pour les politiques. [#4745](https://github.com/MTES-MCT/trackdechets/issues/4745)
- **Interface utilisateur :** Correction de l'espacement entre les colonnes.
- **Interface utilisateur :** Ajout d'un bandeau avec un texte mis à jour. [#4733](https://github.com/MTES-MCT/trackdechets/issues/4733)
- **Registre :** Permettre à un établissement ayant le profil "Installation de valorisation de terres et sédiments" d’accéder à l’export du registre réglementaire entrant et sortant. [#4748](https://github.com/MTES-MCT/trackdechets/issues/4748)

### Évolutions techniques
- Préparation de la recette et du déploiement en production (plusieurs commits de préparation).
- Ajout d'un script pour la modification de la base de données.
- Refactoring et corrections de code diverses.
- Amélioration des tests d'intégration.
- Correction d'un problème de découpage de la liste des codes Bâle.

### Autres changements
- Mise à jour de la documentation.
- Corrections de SonarQube.
- Nettoyage de code et améliorations de la structure du projet.
- Ajout d'un chatbot IA (en préparation de recette). [#4743](https://github.com/MTES-MCT/trackdechets/issues/4743)
- Modification de la description du footer.
- Ajout de styles CSS pour le modal.
