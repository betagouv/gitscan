## Changelog : trackdechets (30 derniers jours, au 3 juin 2026)

### Résumé
Cette période a été marquée par une série de corrections et d'améliorations concernant principalement le module BSFF (Bordereau de Suivi des Déchets), ainsi que des ajustements sur les formulaires et la gestion des établissements. Des corrections ont également été apportées pour améliorer l'expérience utilisateur et la conformité du système. Une recette a été préparée et déployée.

### Évolutions fonctionnelles
- Correction de l'impossibilité de saisir des caractères spéciaux dans le numéro de contenant. [#4cb314bc](https://github.com/MTES-MCT/trackdechets/commit/4cb314bc)
- Correction de l'affichage de l'onglet BSFF associé et du tableau des conteneurs. [#bf1cf393](https://github.com/MTES-MCT/trackdechets/commit/bf1cf393) et [#4a799e26](https://github.com/MTES-MCT/trackdechets/commit/4a799e26)
- Correction du retour de la recette aperçu. [#90073557](https://github.com/MTES-MCT/trackdechets/commit/90073557) et [#1d1d18cc](https://github.com/MTES-MCT/trackdechets/commit/1d1d18cc)
- Correction des labels Réelle & Estimée pour PAOH & VHU. [#b605920f](https://github.com/MTES-MCT/trackdechets/commit/b605920f)
- Ajout d'un onglet détenteur et des champs manquants. [#e4670f1e](https://github.com/MTES-MCT/trackdechets/commit/e4670f1e)
- Possibilité de modifier le conditionnement sur le BSFF de reconditionnement, regroupement et réexpédition. [#347e974d](https://github.com/MTES-MCT/trackdechets/commit/347e974d)
- Correction permettant de viser un établissement détenteur sur le formulaire BSFF. [#25bbbf93](https://github.com/MTES-MCT/trackdechets/commit/25bbbf93) et [#4770](https://github.com/MTES-MCT/trackdechets/pull/4770)
- Correction pour permettre la création de fiches d'intervention en tant qu'opérateur FF, même avec un autre profil établissement. [#5a14d33a](https://github.com/MTES-MCT/trackdechets/commit/5a14d33a)
- Mise à jour de l'URL de l'API. [#0f8a6e07](https://github.com/MTES-MCT/trackdechets/commit/0f8a6e07)

### Évolutions techniques
- Refactorisation du composant SecondFactor pour une meilleure clarté. [#6978edfc](https://github.com/MTES-MCT/trackdechets/commit/6978edfc)
- Ajout de documentation pour la validation Zod pour bsdasri. [#779f59bf](https://github.com/MTES-MCT/trackdechets/commit/779f59bf) et [#9755f2d8](https://github.com/MTES-MCT/trackdechets/commit/9755f2d8)
- Hotfixes pour TRA-18313, TRA-18273 et TRA-18314. [#d04f9d81](https://github.com/MTES-MCT/trackdechets/commit/d04f9d81) et [#290a033e](https://github.com/MTES-MCT/trackdechets/commit/290a033e)
- Préparation et déploiement de la recette 2026-05. [#fc350e87](https://github.com/MTES-MCT/trackdechets/commit/fc350e87)

### Autres changements
- Ajout d'un bandeau et mise à jour du changelog pour le mois de juin 2026. [#c64b030c](https://github.com/MTES-MCT/trackdechets/commit/c64b030c) et [#1b742d0b](https://github.com/MTES-MCT/trackdechets/commit/1b742d0b)
- Initialisation de l'aperçu DSFR. [#906e04a4](https://github.com/MTES-MCT/trackdechets/commit/906e04a4)
- Revert de modifications liées à la gestion de l'authentification multi-facteurs (MFA) en développement. [#307be8b3](https://github.com/MTES-MCT/trackdechets/commit/307be8b3) et [#9435cc89](https://github.com/MTES-MCT/trackdechets/commit/9435cc89)
