## Changelog : maestro (30 derniers jours, au 2026-07-16)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment au niveau des tableaux de bord et de la gestion des laboratoires. Des corrections ont été apportées pour améliorer la précision des données affichées et la gestion des documents. Plusieurs optimisations et corrections de bugs ont été implémentées pour améliorer la stabilité et la fiabilité de l'application.

### Évolutions fonctionnelles
- Ajout de statistiques sur le tableau de bord [#949].
- Amélioration de l'affichage et de la navigation dans le tableau de programmation (vue nationale) [#1126, #1155].
- Implémentation d'un autocomplete pour la sélection du laboratoire lors de la création d'un prélèvement [#1196].
- Gestion de la réception des RAI DAOA [#1149].
- Possibilité de supprimer des documents pour les utilisateurs "Suivi national" [#1114].
- Ajout d'un bandeau d'alerte pour les cas SEVES [#1074].
- Amélioration des libellés dans l'administration [#1165].
- Repositionnement de l'écran après l'interprétation d'une analyse [#1164].
- Correction de l'affichage des cartes sur le tableau de bord [#1179].
- Correction de l'affichage des pourcentages sur le tableau de bord [#1189, #1177].
- Correction de l'affichage des prélèvements par région pour les coordinateurs régionaux [#1184].
- Correction de l'ajout d'options pour les descripteurs [#1180].
- Correction des codes matrices dans LabCam [#1213].
- Correction des droits d'accès aux données LabCam pour le bureau des laboratoires [#1145].
- Correction de l'emplacement de l'adresse des laboratoires sur les étiquettes [#1093].
- Correction de l'export des informations de conformité [#1152].
- Correction de l'affichage des informations de conformité [#1078].
- Possibilité de modifier un prélèvement même si l'utilisateur n'est pas le préleveur (action volontaire) [#1090].

### Évolutions techniques
- Refactorisation de la gestion des routes des documents pour une meilleure organisation [#1123].
- Utilisation d'un outil de génération d'URL pour l'export dans LabCam [#1128].
- Mise à jour de plusieurs dépendances (nodemailer, puppeteer-core, @sentry/node, etc.).
- Amélioration de la gestion des backups Restic [#1156].
- Correction de la configuration DEX [#1163].
- Ajout de la Content Security Policy (CSP) pour Sentry [#1176].
- Mise à jour de la gestion des LMR (Limites Maximales de Résidus) pour plus de flexibilité [#1085].
- Correction de la gestion des erreurs et des avertissements dans divers modules.

### Autres changements
- Correction de tests unitaires pour éviter les faux positifs [#1153, #1157].
- Nettoyage de code et suppression de warnings [#1178, #1175].
- Amélioration de la documentation interne.
- Correction de la gestion des millisecondes dans les noms de fichiers pour éviter les conflits [#1075].
- Suppression d'un revert précédent [#1054].
- Correction de l'affichage de la conclusion du laboratoire Cereco [#1183].
- Correction de la gestion des résidus complexes dans les analyses [#1113].
- Correction de la gestion des analyses PPV (Pollution Potentielle des Volailles) [#1073].
- Correction de la gestion des 0 dans les résultats d'analyse [#1180].
- Correction de l'affichage des informations de conformité dans l'export [#1152].
- Correction de la gestion des utilisateurs désactivés pour les notifications [#1144].
- Correction de la contrainte sur le mode de communication des laboratoires [#1130].
- Correction de l'affichage des cartes sur le tableau de bord [#1179].
- Correction de l'affichage des pourcentages sur le tableau de bord [#1189, #1177].
- Correction de l'affichage des prélèvements par région pour les coordinateurs régionaux [#1184].
- Correction de l'ajout d'options pour les descripteurs [#1180].
- Correction des codes matrices dans LabCam [#1213].
- Correction des droits d'accès aux données LabCam pour le bureau des laboratoires [#1145].
- Correction de l'emplacement de l'adresse des laboratoires sur les étiquettes [#1093].
- Correction de l'export des informations de conformité [#1152].
- Correction de l'affichage des informations de conformité [#1078].
- Possibilité de modifier un prélèvement même si l'utilisateur n'est pas le préleveur (action volontaire) [#1090].
