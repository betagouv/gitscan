## Changelog : simplifions (30 derniers jours, au 23 août 2026)

### Résumé
Ce mois a marqué le lancement de l'application Rails autonome de Simplifions. Les efforts se sont concentrés sur la mise en place d'une interface conforme au Design System de l'État (DSFR), l'automatisation complète des déploiements et la simplification de l'environnement de développement pour les contributeurs.

### Évolutions fonctionnelles
- **Identité visuelle** : Mise en conformité de l'interface avec la production (page d'accueil, page "À propos", favicon et logo).
- **Design System** : Intégration du DSFR pour assurer une expérience utilisateur cohérente avec les standards de l'État.
- **Gestion de contenu** : Nouveau système de gestion des articles permettant de publier du contenu via des fichiers YAML, évitant ainsi des modifications directes dans le code source.

### Évolutions techniques
- **Déploiement & CI/CD** : 
    - Automatisation des déploiements vers les environnements de sandbox, staging et production via GitHub Actions [#6](https://github.com/datagouv/simplifions/pull/6).
    - Amélioration de la stabilité de la CI (gestion des schémas de base de données et des processus de publication Brakeman).
- **Développement local** : Simplification de l'installation et du lancement du projet grâce à Docker et `make`.
- **Architecture & Optimisation** :
    - Initialisation de l'application Rails en mode autonome.
    - Refonte de la section articles utilisant `ViewComponent` et `importmap` pour une meilleure gestion du JavaScript et des composants.
    - Allègement de l'application par la suppression de dépendances inutilisées (`solid_queue`, `solid_cable`, `image_processing`).
- **Maintenance** : Correction des processus d'installation (`make install`) suite à des changements de dépendances [#11](https://github.com/datagouv/simplifions/pull/11).

### Autres changements
- **Qualité du code** : Adoption des conventions de tests et de style (RSpec et RuboCop) de l'équipe.
- **Nettoyage** : Suppression des notes de travail locales du dépôt.
