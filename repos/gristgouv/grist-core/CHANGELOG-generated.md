## Changelog : grist-core (30 derniers jours, au 2026-05-05)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de la stabilité et de la robustesse de Grist, notamment grâce à la correction de tests aléatoires et à l'amélioration de la gestion des erreurs. Des efforts ont également été déployés pour améliorer l'expérience utilisateur, en particulier dans la configuration initiale et la gestion des applications OAuth. Enfin, des traductions ont été mises à jour pour plusieurs langues.

### Évolutions fonctionnelles
- Ajout d'un point de terminaison POST `/records/list` permettant de lister les enregistrements. [#2321](https://github.com/gristgouv/grist-core/issues/2321)
- Amélioration de la gestion des autorisations par défaut dans le panneau d'administration. [#2314](https://github.com/gristgouv/grist-core/issues/2314)
- Ajout de la possibilité d'ouvrir le menu contextuel via des raccourcis clavier dans les widgets. [#2226](https://github.com/gristgouv/grist-core/issues/2226)
- Amélioration de la recherche dans les documents pour ignorer la casse des accents. [#2221](https://github.com/gristgouv/grist-core/issues/2221)
- Ajout d'une section de sauvegarde dans le wizard de configuration initiale et le panneau d'administration. [#2283](https://github.com/gristgouv/grist-core/issues/2283)
- Amélioration de l'interface utilisateur pour la gestion des applications OAuth. [#2246](https://github.com/gristgouv/grist-core/issues/2246)
- Ajout d'une section "Serveur" dans le panneau d'administration et le wizard de configuration. [#2280](https://github.com/gristgouv/grist-core/issues/2280)
- Amélioration de la gestion des erreurs lors du blocage de l'accès à la page de configuration rapide pour les utilisateurs non autorisés. [#2323](https://github.com/gristgouv/grist-core/issues/2323)

### Évolutions techniques
- Mise à jour de Pyodide de la version 0.23.4 à la version 0.28.1. [#1754](https://github.com/gristgouv/grist-core/issues/1754)
- Amélioration de la gestion des sessions pour éviter les modifications non autorisées dans le contexte `prefork-as-owner`. [#2297](https://github.com/gristgouv/grist-core/issues/2297)
- Refactorisation des types `ISandbox` pour améliorer la sécurité et la robustesse. [#2211](https://github.com/gristgouv/grist-core/issues/2211)
- Amélioration de la gestion des tests, notamment en corrigeant des tests aléatoires et en améliorant la synchronisation. [#2320](https://github.com/gristgouv/grist-core/issues/2320)
- Amélioration de la gestion des dépendances et des mises à jour de packages.
- Amélioration de la gestion des erreurs et des exceptions.
- Mise à jour de plusieurs dépendances (axios, fast-xml-parser, svgo, flatted, follow-redirects, dompurify, basic-ftp, @xmldom/xmldom, uuid)

### Autres changements
- Mise à jour des traductions pour le suédois, le hongrois, le basque, le portugais brésilien et l'allemand.
- Corrections de bugs mineurs et améliorations de la documentation.
- Nettoyage du code et refactorisation de certaines parties du projet.
- Amélioration de la gestion des tests et de l'intégration continue.
- Ajout de la signature CLA pour certains contributeurs.
- Correction de problèmes de test liés à Chrome.
- Amélioration de la gestion des suggestions.
- Correction de problèmes liés aux widgets et à la gestion des événements.
- Amélioration de la gestion des erreurs dans les tests.
- Ajout d'informations de liaison pour les widgets personnalisés.
