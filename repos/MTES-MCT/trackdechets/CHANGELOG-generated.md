## Changelog : trackdechets (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la préparation et le déploiement de la recette de mai 2026, avec des corrections de bugs et des ajustements de l'interface utilisateur pour améliorer l'expérience utilisateur, notamment concernant la gestion des conteneurs, des détenteurs et des recettes. Des corrections liées à l'authentification multi-facteurs (MFA) ont également été apportées.

### Évolutions fonctionnelles
- Correction de l'affichage des labels "Réelle" et "Estimée" pour les PAOH et VHU.
- Ajout d'un onglet "détenteur" avec les champs manquants. [#4784](https://github.com/MTES-MCT/trackdechets/issues/4784)
- Correction permettant de saisir des caractères spéciaux dans le numéro de conteneur. [#4786](https://github.com/MTES-MCT/trackdechets/issues/4786)
- Correction de l'affichage de l'onglet BSFF associé et du tableau des conteneurs. [#4788](https://github.com/MTES-MCT/trackdechets/issues/4788)
- Correction du retour à l'aperçu de la recette. [#4785](https://github.com/MTES-MCT/trackdechets/issues/4785)
- Intégration des modifications liées aux fonctionnalités TRA-18138, TRA-18029, TRA-18109 et TRA-18110.
- Corrections liées aux incidents BSFF-18273 et BSFF-18314.
- Correction liée à l'incident TRA-18302.
- Hotfix pour l'incident TRA-18313. [#4781](https://github.com/MTES-MCT/trackdechets/issues/4781)

### Évolutions techniques
- Refactorisation du composant `SecondFactor` pour une meilleure clarté.
- Préparation du bandeau et du changelog pour la recette MEP 2026-06. [#4789](https://github.com/MTES-MCT/trackdechets/issues/4789)
- Préparation de la recette 2026-05. [#4783](https://github.com/MTES-MCT/trackdechets/issues/4783)
- Correction du pipeline lint. [#4798](https://github.com/MTES-MCT/trackdechets/issues/4798)

### Autres changements
- Revert de la suppression du développement MFA.
- Nettoyage et suppression de code lié au développement MFA.
