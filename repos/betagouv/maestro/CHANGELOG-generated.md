## Changelog : maestro (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'interface utilisateur, notamment au niveau des tableaux de programmation, de la gestion des prélèvements et de l'affichage des analyses. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant l'affichage des données et la gestion des filtres. Enfin, des évolutions ont été apportées pour faciliter l'intégration avec des partenaires comme DAOA et Inovalys.

### Évolutions fonctionnelles
- Ajout d'un filtre sur la date d'envoi de la DAI pour les prélèvements [#1231](https://github.com/betagouv/maestro/issues/1231).
- Amélioration de l'affichage de l'historique des documents associés aux analyses, même en cas de multiples rapports [#1230](https://github.com/betagouv/maestro/issues/1230).
- Ouverture par défaut de l'accordéon "détails" pour les échantillons [#1229](https://github.com/betagouv/maestro/issues/1229).
- Correction de l'affichage du nom du document dans la vue tableau des ressources [#1232](https://github.com/betagouv/maestro/issues/1232).
- Implémentation d'un nouveau design pour le tableau de programmation, vue nationale [#1155](https://github.com/betagouv/maestro/issues/1155) et [#1126](https://github.com/betagouv/maestro/issues/1126).
- Ajout de statistiques sur le dashboard [#949](https://github.com/betagouv/maestro/issues/949).
- Utilisation d'un autocomplete pour la sélection du laboratoire lors de la création d'un prélèvement [#1196](https://github.com/betagouv/maestro/issues/1196).
- Gestion de la réception des RAI DAOA [#1149](https://github.com/betagouv/maestro/issues/1149).
- Amélioration des libellés dans l'administration [#1165](https://github.com/betagouv/maestro/issues/1165).
- Repositionnement de l'écran après l'interprétation d'une analyse [#1164](https://github.com/betagouv/maestro/issues/1164).
- Ajout du préfixe sur le donneur d'ordre uniquement pour Inovalys [#1146](https://github.com/betagouv/maestro/issues/1146).

### Évolutions techniques
- Correction des codes matrices pour LabCam [#1213](https://github.com/betagouv/maestro/issues/1213).
- Correction de l'ajout d'options pour les descripteurs dans l'administration [#1180](https://github.com/betagouv/maestro/issues/1180).
- Correction du calcul des pourcentages sur le dashboard [#1189](https://github.com/betagouv/maestro/issues/1189), [#1188](https://github.com/betagouv/maestro/issues/1188) et [#1179](https://github.com/betagouv/maestro/issues/1179).
- Correction d'un warning lié à l'évaluation d'un "eval" dans Zod [#1177](https://github.com/betagouv/maestro/issues/1177).
- Ajout de la CSP pour Sentry [#1176](https://github.com/betagouv/maestro/issues/1176).
- Correction du nettoyage des backups Restic [#1175](https://github.com/betagouv/maestro/issues/1175).
- Correction d'un test instable [#1174](https://github.com/betagouv/maestro/issues/1174).
- Mise à jour de diverses dépendances (Knex, uuid, Puppeteer, Playwright, i18next, etc.).

### Autres changements
- Correction d'un bug où le menu du filtre "laboratoires agréés" sortait de l'écran [#1150](https://github.com/betagouv/maestro/issues/1150).
- Correction du référentiel des résidues complexes pour SSD2 [#1153](https://github.com/betagouv/maestro/issues/1153).
- Correction des informations de conformité dans l'export [#1152](https://github.com/betagouv/maestro/issues/1152).
- Correction de l'affichage des prélèvements de la région pour les coordinateurs régionaux [#1184](https://github.com/betagouv/maestro/issues/1184).
- La conclusion du laboratoire est maintenant optionnelle pour CEReco [#1183](https://github.com/betagouv/maestro/issues/1183).
- Le type du destinataire du 3ème exemplaire est déduit du 2ème [#1186](https://github.com/betagouv/maestro/issues/1186).
- Suppression du décalage sur la ligne "Total" de l'export de la programmation [#1185](https://github.com/betagouv/maestro/issues/1185).
- Un warning n'est plus émis qu'une seule fois pour une substance inconnue [#1187](https://github.com/betagouv/maestro/issues/1187).
- Le LMR de 3 métabolites est maintenant optionnel [#1170](https://github.com/betagouv/maestro/issues/1170).
- Tous les résidus inconnus sont stockés dès la réception [#1169](https://github.com/betagouv/maestro/issues/1169).
- Revert d'une fonctionnalité liée à Sacha [#1154](https://github.com/betagouv/maestro/issues/1154).
- Correction de l'exemple de configuration Dex [#1163](https://github.com/betagouv/maestro/issues/1163).
