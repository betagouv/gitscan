## Changelog : trackdechets (30 derniers jours, au 19 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des déchets, notamment via la fonctionnalité BSDD (Bon de Suivi des Déchets) et BSFF (Bordereau de Suivi des Flux de Déchets). Des corrections et des améliorations ont été apportées pour répondre aux retours de recette et améliorer l'expérience utilisateur, en particulier concernant les formulaires et les workflows de validation. La sécurité a également été renforcée avec l'implémentation de l'authentification à double facteur.

### Évolutions fonctionnelles
- **BSDD :**
  - Possibilité de modifier les intermédiaires jusqu'à la signature de la réception par la destination [#4741](https://github.com/MTES-MCT/trackdechets/issues/4741).
  - Ajout de la possibilité d'ajouter deux intermédiaires supplémentaires [#4738](https://github.com/MTES-MCT/trackdechets/issues/4738).
- **BSFF :**
  - Implémentation de la fonctionnalité BSFF au DSFR (Dépôt Simplifié des Formalités des Déchets) avec l'ajout des champs émetteur, transporteur et détenteur [#4735](https://github.com/MTES-MCT/trackdechets/issues/4735).
  - Correction de l'impossibilité de viser un établissement détenteur sur le formulaire BSFF [#4770](https://github.com/MTES-MCT/trackdechets/issues/4770).
  - Correction de l'impossibilité de renseigner ou modifier les informations de contact de l'installation TTR du regroupement BSFF [#4767](https://github.com/MTES-MCT/trackdechets/issues/4767).
  - Correction des retours de la démo BSFF [#4750](https://github.com/MTES-MCT/trackdechets/issues/4750).
- **Authentification :**
  - Implémentation de l'authentification à double facteur (2FA) [#4736](https://github.com/MTES-MCT/trackdechets/issues/4736) et [#4739](https://github.com/MTES-MCT/trackdechets/issues/4739).
  - Possibilité de désactiver la double authentification [#4740](https://github.com/MTES-MCT/trackdechets/issues/4740).
- **Registre :**
  - Permettre à un établissement ayant le profil "Installation de valorisation de terres et sédiments" d’accéder à l’export du registre réglementaire entrant et sortant [#4748](https://github.com/MTES-MCT/trackdechets/issues/4748).
- **Divers :**
  - Ajout d'un chatbot IA (en préparation de recette) [#4743](https://github.com/MTES-MCT/trackdechets/issues/4743).
  - Modification du script de la base de données [#4744](https://github.com/MTES-MCT/trackdechets/issues/4744) et [#4737](https://github.com/MTES-MCT/trackdechets/issues/4737).

### Évolutions techniques
- Correction de bugs liés au packagin et au reconditionnement [#4762](https://github.com/MTES-MCT/trackdechets/issues/4762).
- Correction de problèmes d'affichage avec Crisp (outil de support client) [#4745](https://github.com/MTES-MCT/trackdechets/issues/4745).
- Amélioration des conditions de verrouillage des champs dans les formulaires [#4751](https://github.com/MTES-MCT/trackdechets/issues/4751).
- Ajout de documentation pour la validation Zod [#4776](https://github.com/MTES-MCT/trackdechets/issues/4776).
- Suppression de code obsolète et nettoyage de l'interface utilisateur pour la recette MEP [#4761](https://github.com/MTES-MCT/trackdechets/issues/4761).

### Autres changements
- Mise à jour de la description du footer.
- Correction de l'espacement entre les colonnes.
- Corrections de typographie.
- Diverses corrections et améliorations de l'interface utilisateur.
