## Changelog : trackdechets (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des déchets, notamment avec l'implémentation de nouvelles fonctionnalités pour les BSDD (Bon de Suivi Déchet Dangereux) et les BSFF (Bordereau de Suivi des Flux de Déchets). L'authentification a également été renforcée avec l'ajout de l'authentification à deux facteurs. Des corrections de bugs ont été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- **BSDD :** Possibilité de modifier les intermédiaires jusqu'à la signature de la réception par la destination. [#4741](https://github.com/MTES-MCT/trackdechets/pull/4741)
- **BSDD :** Ajout de la possibilité d'ajouter 2 intermédiaires supplémentaires sur un BSDD. [#4738](https://github.com/MTES-MCT/trackdechets/pull/4738)
- **Authentification :** Implémentation de l'authentification à deux facteurs (2FA) avec possibilité de l'activer et de la désactiver. [#4736](https://github.com/MTES-MCT/trackdechets/pull/4736), [#4739](https://github.com/MTES-MCT/trackdechets/pull/4739), [#4740](https://github.com/MTES-MCT/trackdechets/pull/4740)
- **BSFF :** Implémentation de l'ajout de l'émetteur, du transporteur et de la destination sur les BSFF.
- **BSFF :** Ajout d'un sélecteur de type BSFF.
- **Codes déchets Bâle :** Création d'une liste de Codes déchets Bâle sur le même principe que la liste des codes déchets. [#4737](https://github.com/MTES-MCT/trackdechets/pull/4737)
- **Interface utilisateur :** Correction de l'espacement entre les colonnes.
- **Chatbot IA :** Implémentation d'un chatbot IA. [#4743](https://github.com/MTES-MCT/trackdechets/pull/4743)
- **Bandeau :** Mise à jour du texte présent dans le bandeau. [#4733](https://github.com/MTES-MCT/trackdechets/pull/4733)

### Évolutions techniques
- **BSFF :** Intégration des règles BSFF au DSFR.
- **BSFF :** Refactoring de la sauvegarde des données BSFF.
- **Tests :** Ajout et correction de tests d'intégration.
- **CodeQL :** Correction d'un problème potentiel de sécurité identifié par CodeQL.
- **Modification BD :** Ajout de scripts pour modification de la base de données. [#4744](https://github.com/MTES-MCT/trackdechets/pull/4744)

### Autres changements
- Correction d'une régression empêchant la modification des installations d'entreposage provisoire (TTR) après signature de l'entreprise de travaux. [#4734](https://github.com/MTES-MCT/trackdechets/pull/4734)
- Correction de bugs d'affichage liés à CRISP pour les politiques.
- Modifications diverses de l'interface utilisateur et du code pour améliorer la qualité et la maintenabilité.
- Préparation de la recette du 28 avril 2026 et de la MEP du 07 avril 2026.
