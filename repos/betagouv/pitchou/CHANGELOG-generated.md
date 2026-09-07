## Changelog : pitchou (30 derniers jours, au 06/09/2026)

### Résumé
Ce mois-ci, Pitchou a principalement évolué pour offrir de meilleurs outils d'administration, notamment via des capacités d'exportation de données enrichies et la possibilité de déclencher manuellement les synchronisations. La gestion des espèces protégées a également été fluidifiée grâce à des améliorations de l'interface utilisateur et une meilleure cohérence dans l'affichage des anomalies.

### Évolutions fonctionnelles
- **Administration & Dossiers** :
    - Amélioration des capacités d'exportation : téléchargement des tableaux d'avis d'experts, inclusion de la date de phase et possibilité d'exporter l'historique complet des dossiers (au lieu de l'année en cours) [#684](https://github.com/betagouv/pitchou/issues/684), [#689](https://github.com/betagouv/pitchou/issues/689).
    - Ajout de la possibilité de déclencher manuellement la synchronisation avec Démarche Numérique [#687](https://github.com/betagouv/pitchou/issues/687).
- **Gestion des espèces & Projets** :
    - Amélioration de l'interface utilisateur pour la gestion des espèces impactées et la visualisation de leurs anomalies [#691](https://github.com/betagouv/pitchou/issues/691).
    - Meilleure cohérence de l'affichage des anomalies entre les logs de synchronisation et l'interface du projet.
    - Ajout de liens vers le référentiel des types d'impact pour faciliter la consultation lors de la saisie.
- **Nouvelles fonctionnalités** :
    - Ajout de l'activité "carrière alluviale" [#696](https://github.com/betagouv/pitchou/issues/696) et de nouvelles catégories d'activités [#688](https://github.com/betagouv/pitchou/issues/688).
    - Envoi d'e-mails CNPN directement depuis l'application instructeur [#692](https://github.com/betagouv/pitchou/issues/692).

### Évolutions techniques
- **Données & Architecture** :
    - Optimisation de la gestion des données d'impact des espèces en s'appuyant exclusivement sur les données de la base de données [#691](https://github.com/betagouv/pitchou/issues/691).
    - Automatisation du peuplement de la base de données pour les fichiers d'espèces impactées lors de leur création [#683](https://github.com/betagouv/pitchou/issues/683).
    - Refactorisation du nommage de la phase de recevabilité pour plus de clarté [#690](https://github.com/betagouv/pitchou/issues/690).

### Autres changements
- Mise en place d'un système de changelog pour le projet [#686](https://github.com/betagouv/pitchou/issues/686).
- Documentation : ajout de la première ADR (Architecture Decision Record) concernant la structuration des données d'espèces protégées.
- Maintenance : suppression d'outils obsolètes [#682](https://github.com/betagouv/pitchou/issues/682) et application de nouvelles règles de qualité de code (limite de 200 lignes par fichier) [#680](https://github.com/betagouv/pitchou/issues/680).
