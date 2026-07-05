## Changelog : maestro (30 derniers jours, au 2026-07-02)

### Résumé
Les dernières mises à jour de Maestro se concentrent sur l'amélioration de la gestion des analyses et des prélèvements, notamment en intégrant de nouvelles fonctionnalités pour le traitement des résidus, des LMR et des données SEVES. Des corrections et des améliorations ont également été apportées à l'interface utilisateur, aux exports de données et à la gestion des utilisateurs. Enfin, de nombreuses dépendances ont été mises à jour pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité de stocker tous les résidus inconnus dès la réception d'une analyse. [#1169](https://github.com/betagouv/maestro/issues/1169)
- Amélioration des libellés dans la section administrations. [#1165](https://github.com/betagouv/maestro/issues/1165)
- Repositionnement de l'écran d'interprétation d'une analyse en haut de l'écran après son exécution. [#1164](https://github.com/betagouv/maestro/issues/1164)
- Possibilité pour les utilisateurs 'Suivi national' de supprimer des documents. [#1114](https://github.com/betagouv/maestro/issues/1114)
- Ajout d'une API pour l'échange de données avec SEVES. [#900](https://github.com/betagouv/maestro/issues/900)
- Gestion des agréments des laboratoires via le module Labcam. [#871](https://github.com/betagouv/maestro/issues/871)
- Possibilité de repasser des DAI (Demandes d'Analyse Initiale) en erreur pour les relancer. [#1113](https://github.com/betagouv/maestro/issues/1113)
- Ajout d'un bandeau d'alerte SEVES lorsque la LMR (Limite Maximale de Résidus) est dépassée. [#1074](https://github.com/betagouv/maestro/issues/1074)
- Amélioration de la gestion des étiquettes, notamment pour les anciennes. [#1065](https://github.com/betagouv/maestro/issues/1065)
- Correction de l'affichage du menu du filtre laboratoires agréés qui sortait de l'écran. [#1150](https://github.com/betagouv/maestro/issues/1150)
- Correction pour permettre la modification d'un prélèvement par un utilisateur qui n'est pas le préleveur (action volontaire). [#1090](https://github.com/betagouv/maestro/issues/1090)

### Évolutions techniques
- La LMR (Limite Maximale de Résidus) est désormais optionnelle pour certains métabolites. [#1170](https://github.com/betagouv/maestro/issues/1170)
- Correction de la configuration Dex. [#1163](https://github.com/betagouv/maestro/issues/1163)
- Refactor de l'implémentation du nouveau design du tableau de programmation (vue nationale). [#1126](https://github.com/betagouv/maestro/issues/1126)
- Refactor pour séparer les routes des documents de prélèvements et des ressources. [#1123](https://github.com/betagouv/maestro/issues/1123)
- Mise à jour de plusieurs dépendances : React Router, Vite, @mui/material, actions/cache, nodemailer, @aws-sdk/client-s3, etc. (voir commits dependabot)
- Utilisation d'un outil de génération d'URL pour l'export des données Labcam. [#1128](https://github.com/betagouv/maestro/issues/1128)
- Simplification de la contrainte sur le mode de communication dans la table laboratoires. [#1130](https://github.com/betagouv/maestro/issues/1130)
- Correction d'un test clignotant en ajoutant un tri par défaut. [#1121](https://github.com/betagouv/maestro/issues/1121)

### Autres changements
- Correction d'une erreur dans l'export des informations de conformité. [#1152](https://github.com/betagouv/maestro/issues/1152)
- Correction d'un problème où les utilisateurs désactivés recevaient des notifications. [#1144](https://github.com/betagouv/maestro/issues/1144)
- Suppression d'un code spécifique à Maestro dans le module Sacha (revert). [#1154](https://github.com/betagouv/maestro/issues/1154)
- Correction du référentiel des résidus complexes dans SSD2. [#1153](https://github.com/betagouv/maestro/issues/1153)
- Ajout d'un préfixe sur le donneur d'ordre uniquement pour Inovalys. [#1146](https://github.com/betagouv/maestro/issues/1146)
- Correction de l'ordre des onglets dans Labcam. [#1145](https://github.com/betagouv/maestro/issues/1145)
- Correction de l'URL de la page "Quoi de neuf" dans le dashboard. [#1107](https://github.com/betagouv/maestro/issues/1107)
- Mise à jour de la documentation et des exemples de configuration.
