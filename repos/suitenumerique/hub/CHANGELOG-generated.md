## Changelog : hub (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, le projet Hub a connu une refonte majeure de son interface utilisateur frontend, passant d'une codebase legacy à une nouvelle architecture basée sur Next.js et TypeScript. Cette refonte introduit une nouvelle expérience de chat avec des fonctionnalités telles que les conversations, les threads, les réactions aux messages et un panneau d'outils pour la gestion des documents. L'infrastructure de test a également été modernisée avec l'intégration de Playwright pour les tests end-to-end.

### Évolutions fonctionnelles
- **Chat :** Implémentation complète de l'interface de chat avec affichage des conversations, gestion des messages et chargement initial avec un squelette de chargement. [#928eecf](https://github.com/suitenumerique/hub/commit/928eecf)
- **Threads :** Ajout de la gestion des threads de discussion au sein des conversations, avec une vue liste et une vue détail. [#7e30683](https://github.com/suitenumerique/hub/commit/7e30683)
- **Réactions :** Possibilité de réagir aux messages avec des emojis. [#538a83b](https://github.com/suitenumerique/hub/commit/538a83b)
- **Documents :** Ajout d'un panneau d'outils pour la gestion des documents, incluant la prévisualisation de fichiers (PDF, images, vidéos, audio). [#c3a9df4](https://github.com/suitenumerique/hub/commit/c3a9df4)
- **Interface utilisateur :** Ajout de composants d'interface utilisateur réutilisables tels que l'Avatar et l'AccountSelector. [#7a770db](https://github.com/suitenumerique/hub/commit/7a770db) et [#9d1cd7e](https://github.com/suitenumerique/hub/commit/9d1cd7e)
- **Barre d'outils des messages :** Ajout d'une barre d'outils contextuelle lors du survol des messages. [#195a26d](https://github.com/suitenumerique/hub/commit/195a26d)
- **Bannière de threads non lus :** Affichage d'une bannière indiquant la présence de nouveaux threads non lus. [#2ef00e8](https://github.com/suitenumerique/hub/commit/2ef00e8)

### Évolutions techniques
- **Refonte Frontend :** Migration complète du frontend vers Next.js et TypeScript. [#b138a46](https://github.com/suitenumerique/hub/commit/b138a46)
- **Tests E2E :** Mise à jour et refonte des tests end-to-end avec Playwright. [#7e6e6ae](https://github.com/suitenumerique/hub/commit/7e6e6ae) et [#fc4a041](https://github.com/suitenumerique/hub/commit/fc4a041)
- **Architecture :** Introduction d'une architecture basée sur des "drivers" pour l'accès aux données et des mocks pour le développement. [#38f9904](https://github.com/suitenumerique/hub/commit/38f9904)
- **CI/CD :** Mise à jour des workflows CI/CD pour prendre en compte la nouvelle configuration frontend et les tests E2E. [#fc4a041](https://github.com/suitenumerique/hub/commit/fc4a041)
- **Infrastructure :** Consolidation de la stack Docker et de la base de données pour les tests E2E. [#6aa53a3](https://github.com/suitenumerique/hub/commit/6aa53a3)
- **Internationalisation (i18n) :** Mise à jour de la configuration i18n et des traductions. [#f679e1d](https://github.com/suitenumerique/hub/commit/f679e1d)

### Autres changements
- **Documentation :** Ajout d'informations sur l'utilisation des Architecture Decision Records (ADR). [#3c75b8c](https://github.com/suitenumerique/hub/commit/3c75b8c)
- **README :** Mise à jour du fichier README.md pour refléter les changements récents. [#57adfb6](https://github.com/suitenumerique/hub/commit/57adfb6)
- **Nettoyage du code :** Suppression de l'ancienne codebase frontend et des dépendances inutiles. [#88c31b5](https://github.com/suitenumerique/hub/commit/88c31b5) et [#307582d](https://github.com/suitenumerique/hub/commit/307582d)
