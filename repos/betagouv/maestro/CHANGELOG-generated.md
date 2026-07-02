## Changelog : maestro (30 derniers jours, au 01 juillet 2026)

### Résumé
Cette période a été marquée par de nombreuses améliorations et corrections, notamment autour de l'intégration avec des partenaires comme Inovalys et Sèves, de la gestion des documents et des analyses, ainsi que par des optimisations de l'interface utilisateur et de la sécurité. Des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la sécurité de l'application.

### Évolutions fonctionnelles
- Amélioration de l'affichage des analyses après interprétation, les repositionnant en haut de l'écran. [#1164](https://github.com/betagouv/maestro/issues/1164)
- Amélioration des libellés dans l'administration. [#1165](https://github.com/betagouv/maestro/issues/1165)
- Possibilité pour les utilisateurs 'Suivi national' de supprimer des documents. [#1114](https://github.com/betagouv/maestro/issues/1114)
- Ajout d'une API pour l'intégration avec SEVES. [#900](https://github.com/betagouv/maestro/issues/900)
- Ajout de la gestion des agréments des laboratoires (Labcam). [#871](https://github.com/betagouv/maestro/issues/871)
- Les utilisateurs désactivés ne reçoivent plus de notifications. [#1144](https://github.com/betagouv/maestro/issues/1144)
- Possibilité de repasser des DAI en erreur pour pouvoir les relancer. [#1113](https://github.com/betagouv/maestro/issues/1113)
- Ajout d'un bandeau d'alerte pour les dépassements de LMR (Limites de Maximum de Résidus). [#1074](https://github.com/betagouv/maestro/issues/1074)
- Possibilité d'imprimer un formulaire vierge pour les DAOA après sélection de l'abattoir. [#1011](https://github.com/betagouv/maestro/issues/1011)
- Amélioration de la gestion des LMR optionnelles. [#1013](https://github.com/betagouv/maestro/issues/1013)
- Ajout de nouveaux types de ressources (réglementation et modèle) pour les documents. [#988](https://github.com/betagouv/maestro/issues/988)
- Correction de l'affichage du menu des laboratoires agréés qui sortait de l'écran. [#1150](https://github.com/betagouv/maestro/issues/1150)
- Correction pour permettre la modification d'un prélèvement par un utilisateur non préleveur (sur action volontaire). [#1090](https://github.com/betagouv/maestro/issues/1090)
- Correction des droits d'accès aux données du Labcam pour le bureau des labos. [#1135](https://github.com/betagouv/maestro/issues/1135)
- Correction des informations de conformité lors de l'export. [#1152](https://github.com/betagouv/maestro/issues/1152)
- Correction de l'emplacement de l'adresse des laboratoires sur les étiquettes, privilégiant l'adresse de facturation. [#1093](https://github.com/betagouv/maestro/issues/1093)
- Correction de l'affichage du dashboard quand il n'y a pas d'actions prioritaires. [#1054](https://github.com/betagouv/maestro/issues/1054)
- Correction pour ne plus envoyer d'erreurs lors de la mise à jour de la contamination. [#1112](https://github.com/betagouv/maestro/issues/1112)
- Correction pour autoriser le dépôt de documents pour le suivi national. [#1051](https://github.com/betagouv/maestro/issues/1051)

### Évolutions techniques
- Refactor de l'implémentation du nouveau design du tableau de programmation (vue nationale). [#1126](https://github.com/betagouv/maestro/issues/1126)
- Refactor pour utiliser un outil de génération d'URL pour l'export des données. [#1128](https://github.com/betagouv/maestro/issues/1128)
- Séparation des routes des documents de prélèvements et des documents ressources. [#1123](https://github.com/betagouv/maestro/issues/1123)
- Refactor pour implémenter une notion de sous-plans au lieu des kinds. [#1007](https://github.com/betagouv/maestro/issues/1007)
- Amélioration du typage des réponses de l'API. [#1006](https://github.com/betagouv/maestro/issues/1006)
- Mise à jour de plusieurs dépendances (nodemailer, @sentry/node, @aws-sdk/client-s3, etc.).
- Correction de l'exemple de configuration Dex. [#1163](https://github.com/betagouv/maestro/issues/1163)
- Mise à jour de la gestion des emails Brevo (utilisation du relai SMTP). [#991](https://github.com/betagouv/maestro/issues/991)

### Autres changements
- Ajout d'un autocomplete pour le filtre des laboratoires. [#1136](https://github.com/betagouv/maestro/issues/1136)
- Ajout de tests pour éviter les tests clignotants. [#1121](https://github.com/betagouv/maestro/issues/1121)
- Suppression d'un revert de fonctionnalité.
- Nettoyage et simplification du code.
- Correction de la largeur de la colonne "référence" et du tableau des documents. [#1083](https://github.com/betagouv/maestro/issues/1083)
- Ajout de la gestion des millisecondes dans le nom des fichiers pour éviter les conflits. [#1075](https://github.com/betagouv/maestro/issues/1075)
- Mise à jour de la documentation et de la configuration.
