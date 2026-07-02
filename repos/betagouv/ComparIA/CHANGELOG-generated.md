## Changelog : ComparIA (30 derniers jours, au 29 juin 2026)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en termes de fonctionnalités et de performance. L'ajout de la recherche web aux comparaisons, l'amélioration de l'interface utilisateur pour le classement des modèles, et l'optimisation de l'export des données sont les points forts de cette période. Des mises à jour de modèles et de traductions ont également été intégrées.

### Évolutions fonctionnelles
- Ajout de la possibilité d'intégrer des résultats de recherche web dans les comparaisons, avec un toggle pour activer/désactiver cette fonctionnalité. [#549](https://github.com/betagouv/ComparIA/pull/549)
- Implémentation d'un contrôle de style sur le classement des modèles, permettant de modifier l'affichage. [#532](https://github.com/betagouv/ComparIA/pull/532)
- Ajout du modèle GLM 5.2 au catalogue. [#540](https://github.com/betagouv/ComparIA/pull/540)
- Ajout du modèle MiniMax M3 au catalogue. [#531](https://github.com/betagouv/ComparIA/pull/531)
- Amélioration de la gestion des modèles Grok : désactivation et archivage des comparaisons associées. [#512](https://github.com/betagouv/ComparIA/pull/512)
- Ajout de nouvelles informations (db_id) aux licences, organisations et LLMs. [#517](https://github.com/betagouv/ComparIA/pull/517)

### Évolutions techniques
- Optimisation de l'export des données pour améliorer les performances, notamment en utilisant un streaming mémoire limité et en évitant la concaténation répétée de dataframes. [#516](https://github.com/betagouv/ComparIA/pull/516)
- Refactorisation du code pour améliorer la réactivité de l'interface utilisateur dans l'arène. [#545](https://github.com/betagouv/ComparIA/pull/545)
- Amélioration de la gestion du cache pour les résultats de recherche web.
- Mise à jour des migrations de la base de données pour une meilleure gestion des données archivées et des comparaisons.
- Correction de bugs liés à la validation des IDs des LLM et au rafraîchissement des tokens Altcha. [#391](https://github.com/betagouv/ComparIA/pull/391), [#463](https://github.com/betagouv/ComparIA/pull/463)
- Amélioration de la gestion des erreurs et des logs, notamment pour la communication avec Loki.
- Mise à jour des dépendances npm et pip.

### Autres changements
- Mise à jour des traductions pour l'italien, le norvégien bokmål, l'espagnol, l'estonien, le suédois, le lituanien, le danois et l'anglais.
- Corrections de bugs mineurs dans l'interface utilisateur (marges, états désactivés des sélecteurs de modèles).
- Amélioration de la documentation et des tests.
- Corrections de problèmes liés à la sélection de la locale et au bug de l'affichage en anglais.
- Ajout de traductions en danois pour MiniMax M3.
- Correction de bugs liés à l'exclusion des cohortes dans l'export des données.
