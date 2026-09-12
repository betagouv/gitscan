## Changelog : pitchou (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration des outils d'administration, notamment via des exports de données plus complets et flexibles. La gestion des espèces impactées a été simplifiée et fiabilisée, tandis que de nouvelles fonctionnalités d'envoi d'emails et de gestion des activités ont été intégrées pour faciliter le travail des agents.

### Évolutions fonctionnelles
- **Administration et exports de données**
  - Amélioration des téléchargements de dossiers : possibilité d'exporter l'historique complet (au lieu de l'année en cours) [#684], ajout de la colonne liée à l'AE et intégration de la date de phase.
  - Nouvel export disponible : téléchargement de la table des avis experts.
  - Possibilité de déclencher manuellement la synchronisation avec la Démarche Numérique [#687].
  - Améliorations diverses de l'interface d'administration [#689].
- **Gestion des dossiers et des espèces**
  - Ajout de la recherche et du filtrage par espèce impactée dans la liste des dossiers [#695].
  - Amélioration de l'interface utilisateur pour les espèces impactées et la gestion des anomalies (harmonisation entre les logs de synchronisation et l'onglet projet).
  - Affichage du lien vers le référentiel du type d'impact pour les fichiers d'espèces.
- **Activités et communications**
  - Ajout de nouvelles catégories d'activités et de l'activité "carrière alluviale" [#696, #688].
  - Envoi d'emails CNPN directement depuis l'application instructeur [#692], avec affichage d'informations spécifiques lors de l'envoi.
- **Divers**
  - Intégration d'une fonctionnalité de changelog [#686].

### Évolutions techniques
- **Architecture et données**
  - Refonte du nommage de la phase de recevabilité [#690].
  - Optimisation de l'affichage des données d'espèces impactées via un accès direct en base de données [#691].
  - Automatisation du peuplement de la base de données pour les nouvelles données d'espèces impactées [#683].
- **Corrections**
  - Correction de la gestion des redirections d'authentification dans l'administration [#702].

### Autres changements
- **Documentation**
  - Ajout de la première ADR concernant la structuration des espèces protégées et de leurs impacts en base de données.
