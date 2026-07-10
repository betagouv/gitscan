## Changelog : maestro (30 derniers jours, au 9 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des analyses, des prélèvements et des données associées, notamment concernant l'intégration de nouvelles sources de données (DAOA, Inovalys, Sacha), la gestion des LMR et des résidus, ainsi que des corrections d'erreurs et des optimisations de l'interface utilisateur. Des améliorations de la sécurité et de la conformité ont également été apportées.

### Évolutions fonctionnelles
- Intégration de la réception des données DAOA. [#1149](https://github.com/betagouv/maestro/issues/1149)
- Amélioration de la sélection du laboratoire lors de la création d'un prélèvement avec une fonctionnalité d'auto-complétion. [#1196](https://github.com/betagouv/maestro/issues/1196)
- Possibilité de supprimer des documents pour les utilisateurs du "Suivi national". [#1051](https://github.com/betagouv/maestro/issues/1051)
- Ajout d'un bandeau d'alerte pour les dépassements de LMR (Limites Maximales de Résidus). [#1074](https://github.com/betagouv/maestro/issues/1074)
- Amélioration de la gestion des analyses et de l'affichage des informations de conformité. [#1078](https://github.com/betagouv/maestro/issues/1078)
- Possibilité de repasser des DAI (Demandes d'Analyse Initiale) en erreur pour les relancer. [#1063](https://github.com/betagouv/maestro/issues/1063)
- Amélioration de l'importation des données Inovalys, notamment la gestion du PDF. [#1047](https://github.com/betagouv/maestro/issues/1047)
- Ajout de la possibilité de stocker tous les résidus inconnus dès la réception de l'analyse. [#1169](https://github.com/betagouv/maestro/issues/1169)
- Amélioration des libellés dans l'administration. [#1165](https://github.com/betagouv/maestro/issues/1165)
- Repositionnement de l'écran après l'interprétation d'une analyse. [#1164](https://github.com/betagouv/maestro/issues/1164)
- Correction de l'affichage des prélèvements par région pour les coordinateurs régionaux. [#1184](https://github.com/betagouv/maestro/issues/1184)
- Possibilité de rendre la LMR optionnelle. [#1092](https://github.com/betagouv/maestro/issues/1092)
- Correction de l'ajout d'options pour les descripteurs dans l'administration. [#1180](https://github.com/betagouv/maestro/issues/1180)

### Évolutions techniques
- Refactorisation de l'importation des documents pour séparer les documents de prélèvements et les documents ressources. [#1123](https://github.com/betagouv/maestro/issues/1123)
- Mise à jour de plusieurs dépendances (nodemailer, puppeteer-core, @aws-sdk/client-s3, etc.).
- Amélioration de la gestion des erreurs lors de l'envoi d'emails avec Brevo et ajout d'alertes Mattermost. [#1056](https://github.com/betagouv/maestro/issues/1056)
- Correction d'un problème de CSP (Content Security Policy) pour Sentry. [#1176](https://github.com/betagouv/maestro/issues/1176)
- Mise à jour de la gestion des backups Restic. [#1177](https://github.com/betagouv/maestro/issues/1177)
- Correction de l'ordre de l'onglet agréments laboratoire. [#1145](https://github.com/betagouv/maestro/issues/1145)
- Refactorisation du plan de programmation. [#1007](https://github.com/betagouv/maestro/issues/1007)

### Autres changements
- Correction de plusieurs tests unitaires et d'intégration.
- Amélioration de la documentation et des messages d'erreur.
- Nettoyage du code et correction de petites anomalies.
- Correction de l'affichage des cartes dans le tableau de bord. [#1179](https://github.com/betagouv/maestro/issues/1179)
- Correction d'un warning lors du déploiement sur Scalingo. [#1178](https://github.com/betagouv/maestro/issues/1178)
- Correction d'une erreur dans la console liée à l'évaluation d'un "eval". [#1177](https://github.com/betagouv/maestro/issues/1177)
- Correction du pourcentage affiché dans le dashboard. [#1189](https://github.com/betagouv/maestro/issues/1189) et [#1179](https://github.com/betagouv/maestro/issues/1179)
- Correction d'un warning concernant une substance inconnue. [#1187](https://github.com/betagouv/maestro/issues/1187)
- Correction du type du destinataire du 3ème exemplaire. [#1186](https://github.com/betagouv/maestro/issues/1186)
- Suppression d'un décalage dans l'export de la programmation. [#1185](https://github.com/betagouv/maestro/issues/1185)
- La conclusion du laboratoire est maintenant optionnelle. [#1183](https://github.com/betagouv/maestro/issues/1183)
- Correction de l'affichage des étiquettes. [#1065](https://github.com/betagouv/maestro/issues/1065)
- Correction de l'URL de la page "Quoi de neuf". [#1054](https://github.com/betagouv/maestro/issues/1054)
- Correction de l'affichage des actions prioritaires dans le dashboard. [#1054](https://github.com/betagouv/maestro/issues/1054)
- Correction de l'affichage des informations de conformité dans l'export. [#1052](https://github.com/betagouv/maestro/issues/1052)
- Correction de l'emplacement de l'adresse des laboratoires sur l'étiquette. [#1051](https://github.com/betagouv/maestro/issues/1051)
- Correction de l'affichage de la pollution probable par les sources de contamination. [#1073](https://github.com/betagouv/maestro/issues/1073)
- Suppression d'une erreur dans la console liée à Zod. [#1177](https://github.com/betagouv/maestro/issues/1177)
