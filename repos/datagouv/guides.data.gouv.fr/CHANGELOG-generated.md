## Changelog : guides.data.gouv.fr (30 derniers jours, au 19/11/2026)

### Résumé
La documentation s'est enrichie de nouveaux guides pratiques (notifications, DOI, cartes.gouv.fr, MCP) et a été affinée pour clarifier les processus de candidature et de gestion des données. Des améliorations de sécurité, notamment l'introduction de l'authentification à deux facteurs, ont également été déployées.

### Évolutions fonctionnelles
- **Nouveaux guides et contenus :**
  - Ajout de documentations sur les notifications ([#95](https://github.com/datagouv/guides.data.gouv.fr/issues/95)), les DOI des jeux de données ([#92](https://github.com/datagouv/guides.data.gouv.fr/issues/92)), la synchronisation avec cartes.gouv.fr ([#91](https://github.com/datagouv/guides.data.gouv.fr/issues/91)) et l'utilisation de MCP (Jan, LM Studio, Open WebUI).
  - Précisions sur les processus de candidature en cours ([#26](https://github.com/datagouv/guides.data.gouv.fr/issues/26), [#55](https://github.com/datagouv/guides.data.gouv.fr/issues/55)) et les candidatures en groupement ([#53](https://github.com/datagouv/guides.data.gouv.fr/issues/53)).
  - Mention explicite des agents publics ([#93](https://github.com/datagouv/guides.data.gouv.fr/issues/93)).
- **Améliorations de la gestion :**
  - Possibilité de modifier la configuration jusqu'à la publication ([#52](https://github.com/datagouv/guides.data.gouv.fr/issues/52)) et gestion des lots sans limitation ([#51](https://github.com/datagouv/guides.data.gouv.fr/issues/51)).
  - Ajout d'instructions relatives à l'authentification à deux facteurs (2FA).
- **Corrections :**
  - Correction de l'affichage du statut "en cours" ([#57](https://github.com/datagouv/guides.data.gouv.fr/issues/57), [#58](https://github.com/datagouv/guides.data.gouv.fr/issues/58)).
  - Correction des scopes manquants pour les subventions aux associations ([#54](https://github.com/datagouv/guides.data.gouv.fr/issues/54)).
  - Suppression de la notion de groupement ([#54](https://github.com/datagouv/guides.data.gouv.fr/issues/54)).

### Évolutions techniques
- **Sécurité et API :**
  - Mise en œuvre de l'authentification à deux facteurs (2FA) via la [PR #35](https://github.com/datagouv/guides.data.gouv.fr/pull/35).
  - Mise à jour de l'API des thématiques ([#90](https://github.com/datagouv/guides.data.gouv.fr/issues/90)).
