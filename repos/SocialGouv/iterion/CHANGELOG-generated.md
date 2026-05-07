## Changelog : iterion (30 derniers jours, au 2026-05-06)

### Résumé
Ce mois-ci, iterion a connu une évolution significative, notamment avec l'introduction d'un sous-système de "sandbox" pour l'exécution sécurisée d'agents d'IA, ainsi que des améliorations majeures de l'infrastructure cloud et de l'expérience utilisateur de l'interface web. De nombreuses corrections et optimisations ont également été apportées pour améliorer la stabilité et la performance du projet. L'accent a été mis sur la préparation du déploiement en production et l'amélioration de la robustesse du système.

### Évolutions fonctionnelles
- Ajout d'un système de "sandbox" pour l'exécution d'agents d'IA, avec validation E2E et support de plusieurs versions ([a219e09](https://github.com/SocialGouv/iterion/commit/a219e09)).
- Amélioration de l'interface utilisateur avec l'ajout de panneaux latéraux effondrables, une palette d'éléments et un flux de travail amélioré pour la gestion des fichiers et des commits ([9b8d738](https://github.com/SocialGouv/iterion/commit/9b8d738), [13813ae](https://github.com/SocialGouv/iterion/commit/13813ae), [5ce8b97](https://github.com/SocialGouv/iterion/commit/5ce8b97)).
- Implémentation d'une vue de console d'exécution avec pause, scrubber temporel et affichage en direct des logs ([b69367f](https://github.com/SocialGouv/iterion/commit/b69367f)).
- Possibilité de reprendre une exécution interrompue, avec relecture des événements et synchronisation de l'état ([97b0c03](https://github.com/SocialGouv/iterion/commit/97b0c03), [23dc3ab](https://github.com/SocialGouv/iterion/commit/23dc3ab)).
- Ajout d'une vue "Info" avec des contrôles de fusion et des informations sur l'exécution ([9611ba4](https://github.com/SocialGouv/iterion/commit/9611ba4)).
- Amélioration de l'affichage des différences de fichiers dans l'interface utilisateur ([4d3cd08](https://github.com/SocialGouv/iterion/commit/4d3cd08)).
- Ajout d'une fonctionnalité de recherche dans le panneau des fichiers ([d524700](https://github.com/SocialGouv/iterion/commit/d524700)).
- Ajout d'une vue "Report" affichant les coûts par provider, model et node ([33780bc](https://github.com/SocialGouv/iterion/commit/33780bc)).
- Implémentation d'un système de gestion des coûts et de l'effort pour les agents d'IA ([8cad201](https://github.com/SocialGouv/iterion/commit/8cad201)).
- Ajout d'un SDK TypeScript pour interagir avec l'API iterion ([6c73618](https://github.com/SocialGouv/iterion/commit/6c73618)).

### Évolutions techniques
- Préparation de l'infrastructure pour le déploiement en cloud, incluant la gestion des configurations, des files d'attente et du stockage ([95f0b73](https://github.com/SocialGouv/iterion/commit/95f0b73), [616504f](https://github.com/SocialGouv/iterion/commit/616504f), [feca116](https://github.com/SocialGouv/iterion/commit/feca116)).
- Amélioration de la gestion des erreurs et de la résilience du système ([45678c9](https://github.com/SocialGouv/iterion/commit/45678c9), [d7f40f7](https://github.com/SocialGouv/iterion/commit/d7f40f7)).
- Refactorisation de l'architecture pour une meilleure modularité et maintenabilité ([2df7bc6](https://github.com/SocialGouv/iterion/commit/2df7bc6), [4b695ae](https://github.com/SocialGouv/iterion/commit/4b695ae)).
- Amélioration de la sécurité, notamment en renforçant l'authentification et en corrigeant des vulnérabilités ([78d71a4](https://github.com/SocialGouv/iterion/commit/78d71a4), [50a3208](https://github.com/SocialGouv/iterion/commit/50a3208)).
- Mise en place de tests d'intégration et de couverture de code plus complets ([5fe6879](https://github.com/SocialGouv/iterion/commit/5fe6879), [071b1a1](https://github.com/SocialGouv/iterion/commit/071b1a1)).
- Amélioration du système de logging et de monitoring ([37de569](https://github.com/SocialGouv/iterion/commit/37de569)).
- Utilisation de Docker et Kubernetes pour le déploiement et l'orchestration des conteneurs ([6e1e002](https://github.com/SocialGouv/iterion/commit/6e1e002)).

### Autres changements
- Mise à jour de la documentation et ajout de nouveaux exemples ([b37610f](https://github.com/SocialGouv/iterion/commit/b37610f), [6745c74](https://github.com/SocialGouv/iterion/commit/6745c74)).
- Correction de plusieurs bugs et améliorations mineures de l'interface utilisateur et du code.
- Ajout d'un fichier `.trivyignore` pour exclure certaines vulnérabilités des analyses de sécurité ([3b79731](https://github.com/SocialGouv/iterion/commit/3b79731)).
- Ajout d'un fichier `.gitignore` pour ignorer les fichiers temporaires et les artefacts de build ([1388fed](https://github.com/SocialGouv/iterion/commit/1388fed)).
- Mise à jour des dépendances et des outils de développement.
