## Changelog : trackdechets (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la fonctionnalité BSDD (Bon de Suivi Déchet Dangereux) et BSFF (Bon de Suivi Formulaire Facilité), avec des corrections de bugs et l'ajout de nouvelles fonctionnalités pour répondre aux besoins des utilisateurs et aux retours de la recette. L'implémentation de l'authentification à double facteur (2FA) a également été avancée.

### Évolutions fonctionnelles
- **BSDD :**
  - Possibilité de modifier les intermédiaires jusqu'à la signature de la réception par la destination. [#4741](https://github.com/MTES-MCT/trackdechets/issues/4741)
  - Ajout de la possibilité d'ajouter deux intermédiaires supplémentaires sur un BSDD. [#4738](https://github.com/MTES-MCT/trackdechets/issues/4738)
- **BSFF :**
  - Correction de bugs empêchant la saisie ou la modification des informations de l'installation TTR du regroupement. [#4767](https://github.com/MTES-MCT/trackdechets/issues/4767)
  - Correction de l'impossibilité de viser un établissement détenteur sur le formulaire. [#4770](https://github.com/MTES-MCT/trackdechets/issues/4770) et [#4762](https://github.com/MTES-MCT/trackdechets/issues/4762)
  - Ajout de la gestion du décochage et du bouton de suppression.
  - Implémentation de la fonctionnalité BSFF au DSFR (Dépôt Simplifié des Formalités des Déchets).
  - Ajout des champs émetteur, transporteur et destination au formulaire BSFF.
  - Ajout de la sélection du type de BSFF.
  - Mise en place du schéma Zod pour le formulaire BSFF.
- **Authentification :**
  - Implémentation de l'activation de la double authentification (2FA). [#4736](https://github.com/MTES-MCT/trackdechets/issues/4736)
  - Possibilité de désactiver la double authentification. [#4740](https://github.com/MTES-MCT/trackdechets/issues/4740)
  - Amélioration de la connexion avec la 2FA activée. [#4739](https://github.com/MTES-MCT/trackdechets/issues/4739)
- **Autres :**
  - Ajout d'une liste de Codes déchets Bâle sur le même principe que la liste des codes déchets. [#4737](https://github.com/MTES-MCT/trackdechets/issues/4737)
  - Modification du lien Géorisque vers Trackdéchets. [#4749](https://github.com/MTES-MCT/trackdechets/issues/4749)
  - Permettre à un établissement ayant le profil "Installation de valorisation de terres et sédiments" d’accéder à l’export du registre réglementaire entrant et sortant. [#4748](https://github.com/MTES-MCT/trackdechets/issues/4748)

### Évolutions techniques
- Préparation pour la recette du 28 avril 2026. [#4742](https://github.com/MTES-MCT/trackdechets/issues/4742)
- Ajout d'un script pour la modification de la base de données. [#4744](https://github.com/MTES-MCT/trackdechets/issues/4744)
- Correction de l'espacement entre les colonnes.
- Rebase depuis une ancienne branche fork pour la recette TRA-17387.
- Correction de bugs et refactoring du code BSFF.
- Suppression de code caché entre recette et MEP.
- Correction de conditions de verrouillage des champs.
- Retours de la démo implémentés.
- Correction de l'affichage CRISP pour la policy.

### Autres changements
- Ajout d'un chatbot IA (en préparation de recette). [#4743](https://github.com/MTES-MCT/trackdechets/issues/4743)
- Modifications du footer (bannière, description, CSS).
- Corrections Sonar.
- Découpage de la liste des codes bales.
- Amélioration des tests d'intégration.
- Correction d'un problème potentiel de génération de nombres aléatoires non sécurisés.
