## Changelog : maestro (30 derniers jours, au 9 juillet 2026)

### Résumé
Cette période a été marquée par de nombreuses améliorations et corrections, touchant à la gestion des analyses, des prélèvements, des documents, ainsi que des aspects techniques de l'application. L'accent a été mis sur l'amélioration de l'expérience utilisateur, notamment en facilitant la sélection des laboratoires, la gestion des erreurs et l'affichage des informations. Des optimisations ont également été apportées à l'export des données et à la gestion des notifications.

### Évolutions fonctionnelles
- Ajout de la gestion de la réception des RAI DAOA. [#1149](https://github.com/betagouv/maestro/issues/1149)
- Amélioration de l'ajout d'options pour les descripteurs dans l'administration. [#1180](https://github.com/betagouv/maestro/issues/1180)
- Utilisation d'un autocomplete pour la sélection du laboratoire lors de la création d'un prélèvement. [#1196](https://github.com/betagouv/maestro/issues/1196)
- Correction de l'affichage des cartes sur le dashboard. [#1179](https://github.com/betagouv/maestro/issues/1179)
- Correction de l'affichage des pourcentages sur le dashboard. [#1189](https://github.com/betagouv/maestro/issues/1189) et [#1177](https://github.com/betagouv/maestro/issues/1177)
- Les utilisateurs 'Suivi national' peuvent maintenant supprimer des documents. [#1114](https://github.com/betagouv/maestro/issues/1114)
- Ajout d'un bandeau d'alerte pour les cas Seves. [#1074](https://github.com/betagouv/maestro/issues/1074)
- Possibilité de repasser des DAI en erreur pour les relancer. [#1063](https://github.com/betagouv/maestro/issues/1063)
- Séparation des emails pour l'EDI Sacha. [#1062](https://github.com/betagouv/maestro/issues/1062)
- Amélioration des libellés dans l'administration. [#1165](https://github.com/betagouv/maestro/issues/1165)
- Repositionnement de l'écran après l'interprétation d'une analyse. [#1164](https://github.com/betagouv/maestro/issues/1164)
- Correction de l'affichage des prélèvements de la région pour les coordinateurs régionaux. [#1184](https://github.com/betagouv/maestro/issues/1184)
- La conclusion du laboratoire est maintenant optionnelle pour le Cereco. [#1183](https://github.com/betagouv/maestro/issues/1183)
- Correction de l'export des informations de conformité. [#1078](https://github.com/betagouv/maestro/issues/1078)
- Correction de l'emplacement de l'adresse des laboratoires sur les étiquettes. [#1093](https://github.com/betagouv/maestro/issues/1093)

### Évolutions techniques
- Mise à jour de plusieurs dépendances (nodemailer, puppeteer-core, @aws-sdk/client-s3, etc.).
- Refactor de la gestion des documents pour séparer les routes des documents de prélèvements et des ressources. [#1123](https://github.com/betagouv/maestro/issues/1123)
- Amélioration de la gestion des backups restic.
- Ajout de la Content Security Policy (CSP) pour Sentry. [#1176](https://github.com/betagouv/maestro/issues/1176)
- Correction de problèmes liés à l'évaluation de code dans Zod.
- Mise à jour de la configuration Dex. [#1163](https://github.com/betagouv/maestro/issues/1163)
- Correction d'un test qui clignotait.
- Suppression d'un warning lors du déploiement sur Scalingo. [#1178](https://github.com/betagouv/maestro/issues/1178)

### Autres changements
- Correction de la gestion des LMR optionnelles. [#1085](https://github.com/betagouv/maestro/issues/1085)
- Correction de la gestion des résidus complexes non quantifiés. [#1113](https://github.com/betagouv/maestro/issues/1113)
- Correction de la gestion des erreurs lors de la mise à jour de la contamination. [#1112](https://github.com/betagouv/maestro/issues/1112)
- Correction de la gestion des DAI avec la date d'édition du DAP. [#1061](https://github.com/betagouv/maestro/issues/1061)
- Correction de la génération des anciennes étiquettes. [#1065](https://github.com/betagouv/maestro/issues/1065)
- Suppression d'un revert de fonctionnalité.
- Correction de l'affichage du tableau des documents. [#1083](https://github.com/betagouv/maestro/issues/1083)
- Correction de la gestion des notifications aux utilisateurs désactivés. [#1144](https://github.com/betagouv/maestro/issues/1144)
- Simplification de la contrainte sur le mode de communication des laboratoires. [#1130](https://github.com/betagouv/maestro/issues/1130)
- Correction de l'affichage des informations de conformité dans l'export. [#1152](https://github.com/betagouv/maestro/issues/1152)
- Correction du menu du filtre des laboratoires agréés. [#1150](https://github.com/betagouv/maestro/issues/1150)
- Implémentation d'un nouveau design pour le tableau de programmation (vue nationale). [#1126](https://github.com/betagouv/maestro/issues/1126)
- Ajout du préfixe sur le donneur d'ordre pour Inovalys. [#1146](https://github.com/betagouv/maestro/issues/1146)
- Correction de la gestion des droits d'accès aux données du labcam pour le bureau des labos. [#1135](https://github.com/betagouv/maestro/issues/1135)
- Correction de l'information de pollution probable remplacée par les sources de contamination dans l'analyse PPV. [#1073](https://github.com/betagouv/maestro/issues/1073)
- Correction de l'affichage des cartes sur le dashboard. [#1179](https://github.com/betagouv/maestro/issues/1179)
- Correction de l'affichage des pourcentages sur le dashboard. [#1189](https://github.com/betagouv/maestro/issues/1189)
- Correction de l'affichage des pourcentages sur le dashboard (suite). [#1177](https://github.com/betagouv/maestro/issues/1177)
- Correction d'un warning lors du déploiement sur Scalingo. [#1178](https://github.com/betagouv/maestro/issues/1178)
- Correction d'un problème de conflit de fichiers Sacha.
- Correction d'un problème de gestion des millisecondes dans les noms de fichiers Sacha. [#1075](https://github.com/betagouv/maestro/issues/1075)
- Correction de l'affichage des cartes sur le dashboard. [#1179](https://github.com/betagouv/maestro/issues/1179)
- Correction de l'affichage des pourcentages sur le dashboard. [#1189](https://github.com/betagouv/maestro/issues/1189)
- Correction de l'affichage des pourcentages sur le dashboard (suite). [#1177](https://github.com/betagouv/maestro/issues/1177)
- Correction d'un warning lors du déploiement sur Scalingo. [#1178](https://github.com/betagouv/maestro/issues/1178)
- Correction de l'affichage des cartes sur le dashboard. [#1179](https://github.com/betagouv/maestro/issues/1179)
- Correction de l'affichage des pourcentages sur le dashboard. [#1189](https://github.com/betagouv/maestro/issues/1189)
- Correction de l'affichage des pourcentages sur le dashboard (suite). [#1177](https://github.com/betagouv/maestro/issues/1177)
- Correction d'un warning lors du déploiement sur Scalingo. [#1178](https://github.com/betagouv/maestro/issues/1178)
