## Changelog : trackdechets (30 derniers jours, au 03 juin 2026)

### Résumé
Ce mois-ci, les évolutions de trackdechets se sont concentrées sur la correction de bugs et l'amélioration de l'expérience utilisateur, notamment sur les formulaires BSFF et les fonctionnalités liées aux établissements détenteurs. Des travaux ont également été réalisés sur l'intégration de l'aperçu DSFR et la gestion des signatures.

### Évolutions fonctionnelles
- Correction de l'impossibilité de saisir des caractères spéciaux dans le numéro de contenant. [#4786](https://github.com/MTES-MCT/trackdechets/issues/4786)
- Correction de l'affichage de l'onglet BSFF associé et du tableau des conteneurs. [#4788](https://github.com/MTES-MCT/trackdechets/issues/4788) et [#4784](https://github.com/MTES-MCT/trackdechets/issues/4784)
- Correction du retour recette aperçu. [#4785](https://github.com/MTES-MCT/trackdechets/issues/4785)
- Correction des labels Réelle & Estimée pour PAOH & VHU.
- Ajout d'un onglet détenteur et des champs manquants. [#4770](https://github.com/MTES-MCT/trackdechets/issues/4770)
- Possibilité de modifier le conditionnement sur le BSFF de reconditionnement, regroupement et réexpédition. [#4775](https://github.com/MTES-MCT/trackdechets/issues/4775)
- Correction de l'impossibilité de viser un établissement détenteur sur le formulaire BSFF. [#4770](https://github.com/MTES-MCT/trackdechets/issues/4770) et [#4767](https://github.com/MTES-MCT/trackdechets/issues/4767)
- Correction de l'impossibilité de renseigner ou modifier les informations de contact de l'installation TTR du regroupement sur le BSFF. [#4769](https://github.com/MTES-MCT/trackdechets/issues/4769)
- Initialisation des écrans de signature et de gestion des contenants.
- Intégration de l'aperçu DSFR.

### Évolutions techniques
- Refactorisation du composant SecondFactor pour une meilleure clarté.
- Mise à jour de l'URL de l'API.
- Ajout de documentation pour la validation Zod pour bsdasri. [#4776](https://github.com/MTES-MCT/trackdechets/issues/4776)

### Autres changements
- Préparation du bandeau et du changelog pour la version MEP 2026-06. [#4789](https://github.com/MTES-MCT/trackdechets/issues/4789)
- Corrections et réversions liées à la gestion de l'authentification multi-facteurs (MFA).
- Intégration des branches `TRA-18138`, `TRA-18029-TRA-18109-TRA-18110` et `TRA-18313`.
- Corrections diverses sur le formulaire BSFF pour améliorer son fonctionnement et sa convivialité.
