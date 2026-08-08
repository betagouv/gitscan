## Changelog : simplifions (30 derniers jours, au 05 août 2026)

### Résumé
Ce mois a été consacré à l'initialisation de l'application en tant que projet autonome et à la mise en place de son infrastructure de déploiement. L'accent a été mis sur la synchronisation de l'interface utilisateur avec la version de production et sur l'automatisation des processus de test et de mise en ligne.

### Évolutions fonctionnelles
- **Identité visuelle** : Mise en conformité de l'interface avec la version de production (utilisation du logo Simplifions.data, du favicon officiel et intégration du Design System de l'État - DSFR).
- **Contenu** : Alignement des pages d'accueil et "À propos" sur le modèle de la version de production.

### Évolutions techniques
- **CI/CD et Déploiement** : 
    - Automatisation des déploiements vers les environnements de sandbox, staging et production via GitHub Actions [#6](https://github.com/datagouv/simplifions/pull/6).
    - Possibilité de déclencher manuellement les cycles d'intégration continue (CI).
- **Optimisation et Architecture** :
    - Allègement de l'application par la suppression de composants inutilisés (`solid_queue`, `solid_cable` et `image_processing`).
    - Initialisation de l'application Rails standalone.
    - Mise en place d'une gestion multi-environnements pour les identifiants et les configurations.
- **Expérience de développement** :
    - Simplification du lancement de l'application en local grâce à Docker et `make`.
    - Adoption des standards de qualité et de test (RSpec, RuboCop) basés sur les conventions de l'équipe.
    - Servage local des assets du DSFR pour plus d'autonomie.

### Autres changements
- **Nettoyage** : Suppression des notes de projet locales du dépôt pour garantir la propreté du code.
