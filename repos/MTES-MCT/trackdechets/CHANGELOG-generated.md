## Changelog : trackdechets (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des déchets, notamment avec l'implémentation de fonctionnalités liées au BSFF (Bordereau de Suivi des Déchets) et au BSDD (Bordereau de Suivi des Déchets Dangereux). Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées, ainsi que l'ajout de la double authentification pour une sécurité renforcée.

### Évolutions fonctionnelles
- **BSFF/DSFR :** Implémentation de la gestion des déchets BSFF au sein du DSFR, incluant l'ajout d'informations sur l'émetteur, le transporteur et la destination. [#4735](https://github.com/MTES-MCT/trackdechets/issues/4735)
- **BSDD :** Possibilité de modifier les intermédiaires sur un BSDD jusqu'à la signature de la réception par la destination. [#4741](https://github.com/MTES-MCT/trackdechets/issues/4741)
- **BSDD :** Ajout de la possibilité d'ajouter deux intermédiaires supplémentaires sur un BSDD. [#4738](https://github.com/MTES-MCT/trackdechets/issues/4738)
- **Codes déchets :** Création d'une liste de Codes déchets Bâle, similaire à la liste des codes déchets existante. [#4737](https://github.com/MTES-MCT/trackdechets/issues/4737)
- **Authentification :** Ajout de la double authentification (2FA) pour une sécurité accrue. [#4736](https://github.com/MTES-MCT/trackdechets/issues/4736) et [#4739](https://github.com/MTES-MCT/trackdechets/issues/4739)
- **Registre :** Permettre à un établissement ayant le profil "Installation de valorisation de terres et sédiments" d’accéder à l’export du registre réglementaire entrant et sortant. [#4748](https://github.com/MTES-MCT/trackdechets/issues/4748)
- **Correction :** Correction d'une régression empêchant l'ajout/modification d'une installation d'entreposage provisoire (TTR) après signature de l'entreprise de travaux. [#4734](https://github.com/MTES-MCT/trackdechets/issues/4734)
- **Correction :** Correction des conditions de verrouillage des champs selon les cas. [#4751](https://github.com/MTES-MCT/trackdechets/issues/4751)
- **Correction :** Correction des retours de la BSFF. [#4750](https://github.com/MTES-MCT/trackdechets/issues/4750)

### Évolutions techniques
- **Préparation recette :** Préparation de l'environnement pour la recette du 28 avril 2026. [#4742](https://github.com/MTES-MCT/trackdechets/issues/4742)
- **Refactoring :** Refactorisation du code pour améliorer la structure et la maintenabilité.
- **Scripts de modification BD :** Ajout de scripts pour effectuer des modifications sur la base de données. [#4744](https://github.com/MTES-MCT/trackdechets/issues/4744)
- **Sonar :** Correction des problèmes signalés par SonarQube.

### Autres changements
- **Documentation :** Mise à jour de la documentation.
- **Interface utilisateur :** Améliorations de l'interface utilisateur, notamment pour l'affichage des tableaux et des filtres.
- **Configuration :** Modifications de la configuration pour masquer certaines fonctionnalités en production et en sandbox. [#4756](https://github.com/MTES-MCT/trackdechets/issues/4756)
- **Chatbot IA :** Implémentation d'un chatbot IA. [#4743](https://github.com/MTES-MCT/trackdechets/issues/4743)
- **Revert :** Annulation de certaines modifications suite à des problèmes rencontrés. [#4761](https://github.com/MTES-MCT/trackdechets/issues/4761)
