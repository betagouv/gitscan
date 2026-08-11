## Changelog : plusfraichemaville-site (30 derniers jours, au 11 août 2026)

### Résumé
Ce mois a été marqué par une refonte majeure de l'outil d'aide à la décision, qui est désormais pleinement intégré et fonctionnel au sein de l'espace projet. L'expérience utilisateur a été fluidifiée par une meilleure navigation et une gestion plus intelligente des parcours. Parallèlement, le site a renforcé sa visibilité et ses capacités d'échange de données.

### Évolutions fonctionnelles
- **Refonte de l'aide à la décision** : déploiement d'un nouvel arbre de décision opérationnel dans l'espace projet, remplaçant l'ancien module ([#523](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/523), [#522](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/522)).
- **Mise à jour des données** : intégration des informations relatives au budget 2025 ([#519](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/519)) et amélioration de la gestion des données Climadiag (mise à jour possible sans perte des données LCZ).
- **Optimisation de la navigation** : 
    - Affichage des solutions sous forme d'onglets dans l'espace projet pour une meilleure lisibilité.
    - Redirection automatique vers la page de choix de solution si aucun projet n'est encore configuré.
    - Nettoyage du fil d'ariane pour éviter l'affichage de sections vides.

### Évolutions techniques
- **Analyse et suivi** : mise en place de métriques et de tags Matomo pour suivre l'utilisation des nouvelles fonctionnalités ([#518](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/518)).
- **Interopérabilité** : création d'une nouvelle route API permettant à des services tiers (comme PFAT) de consommer les données Climadiag ([#520](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/520)).
- **Référencement (SEO)** : optimisation technique via la gestion des liens canoniques et l'enrichissement des métadonnées pour les pages de retours d'expérience (REX) ([#515](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/515), [#516](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/516)).
- **Architecture** : création d'un store dédié à la gestion de la navigation et amélioration de la robustesse du chargement de l'aide à la décision.

### Autres changements
- **Corrections de contenu** : ajustement de la terminologie dans les modales LCZ et correction de coquilles sur la page "risque santé".
- **Maintenance technique** : résolution de problèmes de build, nettoyage du linter et corrections de sécurité (CodeQL).
