## Changelog : hub (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, le projet Hub a connu une refonte majeure de son interface utilisateur frontend, passant à une nouvelle architecture basée sur React et Next.js. Les principales nouveautés concernent l'implémentation d'une fonctionnalité de chat avec gestion des conversations, des threads, des réactions et un panneau d'outils pour la gestion des documents. L'infrastructure de test a également été revue et modernisée.

### Évolutions fonctionnelles
- **Chat :** Implémentation d'une interface de chat complète avec :
    - Affichage des conversations et gestion du chargement initial [#928eecf](https://github.com/suitenumerique/hub/commit/928eecf)
    - Gestion des threads de messages avec affichage et actions associées [#1f344b8](https://github.com/suitenumerique/hub/commit/1f344b8)
    - Possibilité de réagir aux messages avec des emojis [#538a83b](https://github.com/suitenumerique/hub/commit/538a83b)
    - Barre d'outils pour les messages avec options (à venir) [#195a26d](https://github.com/suitenumerique/hub/commit/195a26d)
- **Documents :** Ajout d'un panneau d'outils pour la gestion des documents avec :
    - Affichage de la liste des documents [#e8b1ad0](https://github.com/suitenumerique/hub/commit/e8b1ad0)
    - Prévisualisation des fichiers (PDF, image, vidéo, audio) [#c3a9df4](https://github.com/suitenumerique/hub/commit/c3a9df4)
- **Interface utilisateur :**
    - Ajout de composants d'interface utilisateur réutilisables (Avatar, etc.) [#7a770db](https://github.com/suitenumerique/hub/commit/7a770db)
    - Amélioration de l'affichage avec des fonds contextuels et transparents [#4058a28](https://github.com/suitenumerique/hub/commit/4058a28)
    - Ajout d'un sélecteur de compte utilisateur [#9d1cd7e](https://github.com/suitenumerique/hub/commit/9d1cd7e)

### Évolutions techniques
- **Frontend :** Refonte complète du frontend avec :
    - Migration vers React et Next.js [#f1b318e](https://github.com/suitenumerique/hub/commit/f1b318e)
    - Restructuration du code et ajout de hooks personnalisés [#c5d2ab1](https://github.com/suitenumerique/hub/commit/c5d2ab1)
    - Mise en place d'une architecture "driver" pour l'accès aux données [#38f9904](https://github.com/suitenumerique/hub/commit/38f9904)
- **Tests :**
    - Mise à jour de la configuration de Playwright pour les tests E2E [#7e6e6ae](https://github.com/suitenumerique/hub/commit/7e6e6ae)
    - Réécriture des tests E2E pour la page d'accueil et les nouvelles fonctionnalités [#afe89a6](https://github.com/suitenumerique/hub/commit/afe89a6)
    - Suppression des anciens tests E2E [#f679994](https://github.com/suitenumerique/hub/commit/f679994)
- **Infrastructure :**
    - Consolidation de la stack Docker Compose et de la base de données pour les tests E2E [#6aa53a3](https://github.com/suitenumerique/hub/commit/6aa53a3)
    - Mise à jour des workflows CI/CD [#fc4a041](https://github.com/suitenumerique/hub/commit/fc4a041)

### Autres changements
- Mise à jour de la documentation pour l'utilisation d'Architecture Decision Records [#3c75b8c](https://github.com/suitenumerique/hub/commit/3c75b8c)
- Mise à jour des dépendances et du fichier `.gitignore` [#669fa10](https://github.com/suitenumerique/hub/commit/669fa10)
- Synchronisation de l'attribut `lang` des balises HTML avec la langue active [#57fce10](https://github.com/suitenumerique/hub/commit/57fce10)
- Ajout de fichiers d'assets publics [#da95319](https://github.com/suitenumerique/hub/commit/da95319)
- Correction d'un problème de routage Nginx pour l'export statique [#48f818b](https://github.com/suitenumerique/hub/commit/48f818b)
- Initialisation du projet frontend [#c7ca997](https://github.com/suitenumerique/hub/commit/c7ca997)
