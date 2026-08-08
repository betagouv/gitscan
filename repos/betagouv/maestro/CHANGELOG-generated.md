## Changelog : maestro (30 derniers jours, au 06/08/2026)

### Résumé
Les récentes évolutions de Maestro se concentrent sur l'enrichissement des outils de pilotage et la fiabilisation des données d'analyse. De nouvelles capacités statistiques et de filtrage ont été intégrées, tandis que des corrections ciblées améliorent la précision des résultats pour plusieurs partenaires de laboratoire. Des optimisations techniques ont également été réalisées pour améliorer la stabilité du système.

### Évolutions fonctionnelles

**Nouvelles fonctionnalités**
- Ajout de statistiques détaillées sur le tableau de bord [#949](https://github.com/betagouv/maestro/issues/949).
- Intégration d'un nouveau filtre basé sur la date d'envoi de la DAI pour les prélèvements [#1231](https://github.com/betagouv/maestro/issues/1231).
- Prise en charge de la réception des RAI DAOA [#1149](https://github.com/betagouv/maestro/issues/1149).
- Enrichissement du référentiel avec l'ajout de la substance active cyprosulfamide [#1246](https://github.com/betagouv/maestro/issues/1246).

**Améliorations et corrections**
- **Expérience utilisateur :** l'accordéon des détails d'un échantillon s'ouvre désormais par défaut pour un accès plus rapide à l'information [#1229](https://github.com/betagouv/maestro/issues/1229).
- **Fiabilité des données :** corrections importantes sur la gestion des analyses et des codes matrices pour les partenaires Inovalys, Girpa, Cereco et Labcam [#1276](https://github.com/betagouv/maestro/issues/1276), [#1275](https://github.com/betagouv/maestro/issues/1275), [#1265](https://github.com/betagouv/maestro/issues/1265), [#1264](https://github.com/betagouv/maestro/issues/1264), [#1213](https://github.com/betagouv/maestro/issues/1213).
- **Gestion des prélèvements :** mise à jour automatique du laboratoire destinataire lors d'un changement de matrice [#1274](https://github.com/betagouv/maestro/issues/1274).
- **Affichage et rapports :** correction de l'affichage des noms de documents dans les tableaux [#1232](https://github.com/betagouv/maestro/issues/1232), de la récupération des conformités dans le dashboard [#1262](https://github.com/betagouv/maestro/issues/1262) et de l'historique des documents pour les rapports multiples [#1230](https://github.com/betagouv/maestro/issues/1230).

### Évolutions techniques

- **Performance :** passage de la mise à jour des départements en mode non automatique afin de réduire la consommation de mémoire vive (RAM) du système [#1260](https://github.com/betagouv/maestro/issues/1260).
- **Refactoring :** centralisation du code d'extraction de la référence Maestro pour l'ensemble des laboratoires [#1247](https://github.com/betagouv/maestro/issues/1247).
