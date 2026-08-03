## Changelog : formulaire-qf (30 derniers jours, au 30 juillet 2026)

### Résumé
Les récentes mises à jour de formulaire-qf se concentrent sur l'amélioration de la journalisation, la gestion des notifications et la mise à jour des dépendances du projet pour assurer sa stabilité et sa sécurité.

### Évolutions fonctionnelles
- Correction d'un problème de suppression de notifications : Seules les notifications créées par l'application formulaire-qf sont désormais supprimées, évitant des suppressions accidentelles.  [#360](https://github.com/etalab/formulaire-qf/pull/360)

### Évolutions techniques
- **Journalisation:** Implémentation de la journalisation au format JSON via `logstasher` pour faciliter l'analyse et le suivi des événements. [#368](https://github.com/etalab/formulaire-qf/pull/368)
- Mise à jour de plusieurs dépendances :  Plusieurs dépendances ont été mises à jour vers leurs dernières versions stables, incluant `simplecov`, `websocket-driver`, `rubocop-rails`, `activerecord-session_store` et `net-imap`. Ces mises à jour visent à améliorer la sécurité et la performance de l'application.

### Autres changements
- Mise à jour des dépendances de développement : Les dépendances de développement ont été mises à jour pour assurer la compatibilité et la stabilité de l'environnement de développement.
