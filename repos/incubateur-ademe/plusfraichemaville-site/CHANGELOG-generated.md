## Changelog : plusfraichemaville-site (30 derniers jours, au 02/09/2026)

### Résumé
Ce mois-ci, le site a franchi une étape majeure en s'ouvrant aux entreprises privées et en modernisant son infrastructure technique avec le passage à Strapi 5. L'outil d'aide à la décision a été entièrement repensé pour être plus fluide, plus complet et directement intégré au sein de l'espace projet.

### Évolutions fonctionnelles
- **Élargissement de l'audience** : Ouverture du site aux entreprises privées avec une identification automatique du profil utilisateur (agent public vs privé) [#527](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/527).
- **Refonte de l'aide à la décision** : L'outil est désormais pleinement fonctionnel dans l'espace projet, incluant l'ajout de bannières d'incitation et une meilleure gestion des filtres [#522](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/522).
- **Optimisation de l'expérience utilisateur** :
    - Amélioration de la navigation : redirection automatique vers le choix de solution si aucun projet n'est configuré et gestion plus fine du fil d'ariane.
    - Ajustements de l'interface : plusieurs améliorations de la clarté des textes (wording) sur les parcours de diagnostic, la climatisation et les pages d'urgence.
- **Suivi et analyse** : Mise en place de nouveaux indicateurs de performance (metrics) et de suivi Matomo pour analyser l'utilisation des fonctionnalités et le parcours utilisateur.

### Évolutions techniques
- **Migration Backend** : Passage réussi à Strapi v5 et nettoyage approfondi des modèles de données associés [#528](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/528) [#529](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/529).
- **Optimisation de la base de données** : Nettoyage du schéma, suppression de tables obsolètes (`estimation_aides`) et passage à une récupération dynamique des identifiants de documents.
- **SEO et Navigation** : Correction de la gestion des URLs canoniques pour améliorer le référencement et résoudre des problèmes de défilement (scroll) sur les fiches solutions [#525](https://github.com/incubateur-ademe/plusfraichemaville-site/pull/525).

### Autres changements
- **Maintenance du code** : Corrections de linter, de build et de sécurité (CodeQL) pour stabiliser l'environnement de développement.
- **Fiabilité** : Amélioration de la gestion des erreurs lors du chargement des modules de l'aide à la décision.
