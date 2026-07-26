## Changelog : maestro (30 derniers jours, au 16 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'interface utilisateur, notamment sur les tableaux de bord et la gestion des laboratoires. Des corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité de la plateforme, en particulier concernant l'affichage des données et la gestion des utilisateurs. De nouvelles fonctionnalités ont également été implémentées pour faciliter la gestion des prélèvements et des analyses, notamment l'ajout d'une autocomplétion pour la sélection des laboratoires et la gestion des données RAI DAOA.

### Évolutions fonctionnelles
- Ajout de statistiques sur le tableau de bord. [#949](https://github.com/betagouv/maestro/issues/949)
- Amélioration de l'affichage du tableau de programmation (vue nationale) avec un nouveau design. [#1126](https://github.com/betagouv/maestro/issues/1126)
- Implémentation d'une autocomplétion pour la sélection du laboratoire lors de la création d'un prélèvement. [#1196](https://github.com/betagouv/maestro/issues/1196)
- Gestion de la réception des RAI DAOA. [#1149](https://github.com/betagouv/maestro/issues/1149)
- Correction de l'affichage des cartes sur le tableau de bord. [#1179](https://github.com/betagouv/maestro/issues/1179)
- Correction de l'ordre de l'onglet "agréments laboratoire" dans LabCam. [#1145](https://github.com/betagouv/maestro/issues/1145)
- Correction de l'affichage des prélèvements de la région pour les coordinateurs régionaux. [#1184](https://github.com/betagouv/maestro/issues/1184)
- Correction de l'affichage des informations de conformité dans l'export. [#1152](https://github.com/betagouv/maestro/issues/1152)
- Correction du menu du filtre laboratoires agrées qui sortait de l'écran. [#1150](https://github.com/betagouv/maestro/issues/1150)
- Ajout de libellés améliorés dans l'administration. [#1165](https://github.com/betagouv/maestro/issues/1165)
- Repositionnement de l'écran après l'interprétation d'une analyse. [#1164](https://github.com/betagouv/maestro/issues/1164)
- Correction des codes matrices dans LabCam. [#1213](https://github.com/betagouv/maestro/issues/1213)

### Évolutions techniques
- Mise à jour de plusieurs dépendances (Knex, uuid, puppeteer-core, etc.).
- Correction de la configuration Dex. [#1163](https://github.com/betagouv/maestro/issues/1163)
- Ajout de la CSP pour Sentry. [#1176](https://github.com/betagouv/maestro/issues/1176)
- Suppression d'un warning lors du déploiement sur Scalingo. [#1178](https://github.com/betagouv/maestro/issues/1178)
- Correction du nettoyage des backups restic. [#1169](https://github.com/betagouv/maestro/issues/1169)

### Autres changements
- Correction de bugs mineurs et améliorations de la stabilité.
- Correction d'un test qui clignotait. [#1172](https://github.com/betagouv/maestro/issues/1172)
- Suppression d'une erreur dans la console liée à l'évaluation d'un « eval ». [#1177](https://github.com/betagouv/maestro/issues/1177)
- Correction du pourcentage affiché sur le tableau de bord (plusieurs itérations). [#1188](https://github.com/betagouv/maestro/issues/1188), [#1189](https://github.com/betagouv/maestro/issues/1189)
- Correction du type du destinataire du 3ème exemplaire. [#1186](https://github.com/betagouv/maestro/issues/1186)
- Suppression du décalage sur la ligne Total de l'export. [#1185](https://github.com/betagouv/maestro/issues/1185)
- La conclusion du laboratoire est maintenant optionnelle. [#1183](https://github.com/betagouv/maestro/issues/1183)
- Le préfixe sur le donneur d'ordre est ajouté uniquement pour Inovalys. [#1146](https://github.com/betagouv/maestro/issues/1146)
- Arrêt de l'envoi de notifications aux utilisateurs désactivés. [#1144](https://github.com/betagouv/maestro/issues/1144)
- Simplification de la contrainte sur le mode de communication dans la table laboratoires. [#1130](https://github.com/betagouv/maestro/issues/1130)
- Correction d'un revert d'une fonctionnalité précédente.
- Stockage de tous les résidus inconnus dès la réception. [#1169](https://github.com/betagouv/maestro/issues/1169)
- La LMR de 3 métabolites est maintenant optionnelle. [#1170](https://github.com/betagouv/maestro/issues/1170)
- Correction d'un warning pour une substance inconnue qui était émis plusieurs fois. [#1187](https://github.com/betagouv/maestro/issues/1187)
