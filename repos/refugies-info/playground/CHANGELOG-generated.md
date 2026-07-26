## Changelog : playground (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment au niveau des pop-ups de publication, de la gestion des traductions et de l'historique des actions sur les fiches. Des améliorations techniques ont également été apportées pour optimiser les logs, la gestion des états et l'intégration de nouveaux filtres.

### Évolutions fonctionnelles
- **Publication :** Amélioration de l'UX/UI des pop-ups de publication [#305](https://github.com/refugies-info/playground/pull/305).
- **Conformité :** Suppression de la restriction du changement de conformité pour faciliter la gestion des fiches [#298](https://github.com/refugies-info/playground/pull/298).
- **Notifications :** Ajout d'une notification Slack lors de la publication d'une fiche [#303](https://github.com/refugies-info/playground/pull/303).
- **Archivage :** Affichage d'une pop-up informant qu'une fiche a été archivée [#303](https://github.com/refugies-info/playground/pull/303).
- **Traduction :**
    - Amélioration de l'UX/UI de la page de traduction [#294](https://github.com/refugies-info/playground/pull/294) et de la liste des traductions [#282](https://github.com/refugies-info/playground/pull/282), [#286](https://github.com/refugies-info/playground/pull/286).
    - Ajout d'un système de notes pour les traductions [#292](https://github.com/refugies-info/playground/pull/292).
    - Possibilité d'assigner un traducteur à une traduction.
    - Ajout d'une sauvegarde automatique pour les traductions.
- **Recherche :** Ajout d'un filtre pour la barre de recherche permettant de spécifier le champ à rechercher [#300](https://github.com/refugies-info/playground/pull/300).
- **Import :**
    - Tri de la liste des éléments importés par date d'import [#299](https://github.com/refugies-info/playground/pull/299).
    - Ajout de filtres dans l'onglet d'import [#291](https://github.com/refugies-info/playground/pull/291).
- **Workflow :** Ajout d'un onglet "Journal d'activités" pour suivre l'historique des actions sur les fiches [#269](https://github.com/refugies-info/playground/pull/269).
- **État de traitement :** Amélioration de la gestion de l'état de traitement des fiches [#293](https://github.com/refugies-info/playground/pull/293).
- **Gestion des utilisateurs :** Centralisation des données utilisateurs dans le backend [#289](https://github.com/refugies-info/playground/pull/289).

### Évolutions techniques
- **Logs :** Ajout de logs pour diverses opérations, notamment l'archivage et les traductions [#297](https://github.com/refugies-info/playground/pull/297).
- **Base de données :** Suppression d'une requête inutile et migration pour le type de valeur archivage [#298](https://github.com/refugies-info/playground/pull/298).
- **Performance :** Réduction du nombre d'éléments traités par défaut dans l'ingestion de données [#275](https://github.com/refugies-info/playground/pull/275).
- **Architecture :** Refactorisation du code et suppression de fichiers inutiles.
- **Intégration :** Amélioration de l'intégration avec Letta (gestion des tokens et des logs).

### Autres changements
- Ajout d'un SVG personnalisé [#303](https://github.com/refugies-info/playground/pull/303).
- Mise à jour de la documentation.
- Corrections de bugs et améliorations de la qualité du code.
- Amélioration de la gestion des erreurs et des messages d'information.
- Correction de conflits de branche.
