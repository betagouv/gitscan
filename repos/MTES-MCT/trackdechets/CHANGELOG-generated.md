## Changelog : trackdechets (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Trackdéchets se sont concentrées sur la correction de bugs et l'amélioration de l'expérience utilisateur, notamment au niveau des formulaires BSFF et de la gestion des établissements. Des corrections ont été apportées pour permettre une saisie plus complète et précise des informations, ainsi que pour résoudre des problèmes d'accès et de fonctionnalité pour différents profils utilisateurs.

### Évolutions fonctionnelles
- Correction de l'impossibilité de saisir des caractères spéciaux dans le numéro de contenant. [#4786](https://github.com/MTES-MCT/trackdechets/issues/4786)
- Correction de l'affichage de l'onglet BSFF associé et du tableau des conteneurs. [#4788](https://github.com/MTES-MCT/trackdechets/issues/4788) et [#4784](https://github.com/MTES-MCT/trackdechets/issues/4784)
- Correction du retour de la recette aperçu. [#4785](https://github.com/MTES-MCT/trackdechets/issues/4785)
- Correction des labels Réelle & Estimée pour PAOH & VHU.
- Ajout d'un onglet détenteur et des champs manquants.
- Possibilité de modifier le conditionnement sur le BSFF de reconditionnement, regroupement et réexpédition.
- Correction d'un problème empêchant la création de fiches d'intervention en tant qu'opérateur FF avec un autre profil établissement.
- Possibilité de viser un établissement détenteur sur le formulaire BSFF. [#4770](https://github.com/MTES-MCT/trackdechets/issues/4770) et [#4775](https://github.com/MTES-MCT/trackdechets/issues/4775)

### Évolutions techniques
- Refactorisation du composant SecondFactor pour une meilleure clarté.
- Correction de problèmes de linting dans le pipeline CI/CD. [#4798](https://github.com/MTES-MCT/trackdechets/issues/4798)
- Mise à jour de l'URL de l'API.
- Intégration de plusieurs branches de fonctionnalités (TRA-18138, TRA-18029, TRA-18109, TRA-18110, TRA-18313) dans la branche de recette.

### Autres changements
- Ajout de documentation pour la validation Zod pour bsdasri. [#4776](https://github.com/MTES-MCT/trackdechets/issues/4776)
- Mise à jour du changelog et ajout d'un bandeau MEP 2026-06. [#4789](https://github.com/MTES-MCT/trackdechets/issues/4789)
- Suppression temporaire de fonctionnalités liées à MFA (Multi-Factor Authentication) en développement.
