## Changelog : anssi-recommandations-cyber (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse de l'application, l'ajout de nouvelles fonctionnalités pour faciliter l'accès aux sources des recommandations, et l'intégration d'une nouvelle source de données (Jeopardy). Des corrections de bugs et des améliorations de la gestion des erreurs ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité permettant de récupérer le document source associé à une réponse, via une nouvelle route GET `/source` [#92002bf](https://github.com/betagouv/anssi-recommandations-cyber/commit/92002bf).
- Amélioration de la gestion des erreurs : affichage d'erreurs plus claires et retour d'une erreur HTTP 500 en cas d'échec de communication avec Albert [#a0f01fe](https://github.com/betagouv/anssi-recommandations-cyber/commit/a0f01fe).
- Implémentation de la recherche et de l'intégration de la collection "Jeopardy" [#0ef1536](https://github.com/betagouv/anssi-recommandations-cyber/commit/0ef1536).
- Possibilité de lister les documents d'une collection dans un dataframe via leurs noms [#c6d9763](https://github.com/betagouv/anssi-recommandations-cyber/commit/c6d9763).
- Ajout d'une page FAQ en cours d'initialisation [#1ef2e11](https://github.com/betagouv/anssi-recommandations-cyber/commit/1ef2e11).
- Amélioration de la reformulation des questions pour une meilleure qualité des réponses [#f7faff0](https://github.com/betagouv/anssi-recommandations-cyber/commit/f7faff0).
- Ajout du consentement pour le suivi Matomo [#b2f4e94](https://github.com/betagouv/anssi-recommandations-cyber/commit/b2f4e94).

### Évolutions techniques
- Mise à jour de la version de PostgreSQL à 17 pour l'environnement de développement local [#7c01cd8](https://github.com/betagouv/anssi-recommandations-cyber/commit/7c01cd8).
- Séparation des environnements de développement et de production [#98f19aa](https://github.com/betagouv/anssi-recommandations-cyber/commit/98f19aa).
- Ajout de vérifications de l'existence des variables d'environnement nécessaires au démarrage du serveur [#56b68b9](https://github.com/betagouv/anssi-recommandations-cyber/commit/56b68b9).
- Refactorisation du code pour extraire la logique de gestion des réponses maîtrisées dans une classe dédiée [#ac2f8b6](https://github.com/betagouv/anssi-recommandations-cyber/commit/ac2f8b6).
- Amélioration de la gestion des erreurs et des logs pour faciliter le débogage [#665b9f9](https://github.com/betagouv/anssi-recommandations-cyber/commit/665b9f9).
- Ajout de tests et de configurations pour le déploiement en production [#db4fa63](https://github.com/betagouv/anssi-recommandations-cyber/commit/db4fa63).

### Autres changements
- Correction de typos et amélioration du wording dans l'interface utilisateur [#6b65b01](https://github.com/betagouv/anssi-recommandations-cyber/commit/6b65b01).
- Ajout d'un notebook pour l'analyse des collections d'indexation et Jeopardy [#7868fe7](https://github.com/betagouv/anssi-recommandations-cyber/commit/7868fe7).
- Mise à jour de plusieurs dépendances (cryptography, docker, typescript-eslint, svelte, eslint, etc.) via Renovate Bot. Ces mises à jour visent à améliorer la sécurité et la stabilité de l'application.
- Ajout d'un fichier de configuration pour Renovate Bot [#ebff5a8](https://github.com/betagouv/anssi-recommandations-cyber/commit/ebff5a8).
- Ajout de tracking Matomo sur le bouton de copie de réponse [#bc6a867](https://github.com/betagouv/anssi-recommandations-cyber/commit/bc6a867).
- Suppression du tag `conversation` obsolète [#3469dff](https://github.com/betagouv/anssi-recommandations-cyber/commit/3469dff).
