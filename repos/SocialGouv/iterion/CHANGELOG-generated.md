## Changelog : iterion (30 derniers jours, au 2026-06-22)

### Résumé
Ce mois-ci, iterion a connu une refonte importante de son interface utilisateur studio, avec une attention particulière portée à la performance, l'accessibilité et la clarté. De nouvelles fonctionnalités ont été ajoutées pour faciliter l'intégration de bots avec des outils externes (Forge), améliorer la gestion des organisations et des utilisateurs, et offrir une meilleure visibilité sur les exécutions et les coûts. Des améliorations significatives ont également été apportées à l'architecture interne pour une meilleure maintenabilité et extensibilité.

### Évolutions fonctionnelles
- **Intégrations Forge :** Ajout de la prise en charge de GitHub, GitLab et Forgejo avec authentification OAuth et PAT, permettant de connecter facilement des bots à des dépôts de code.
- **Gestion des organisations :** Nouvelle interface pour gérer les organisations et les utilisateurs, avec des fonctionnalités d'authentification améliorées (SSO, gestion des mots de passe).
- **Interface utilisateur Studio améliorée :**
    - Refonte de l'interface pour une meilleure expérience utilisateur, avec des composants plus modernes et intuitifs.
    - Ajout de filtres et d'options de tri pour les runs.
    - Amélioration de la navigation et de la recherche.
    - Ajout d'une vue "What's Next" pour faciliter le suivi des tâches et des actions à effectuer.
    - Amélioration de l'affichage des logs et des fichiers.
    - Ajout d'une vue pour gérer les labels.
- **Surveillance et analyse :** Ajout d'un tableau de bord pour suivre les coûts et les performances des runs.
- **Gestion des secrets :** Amélioration de la gestion des secrets avec la possibilité de les lier à des bots spécifiques et d'utiliser un stockage chiffré.
- **Edition de métadonnées de bot :** Possibilité de modifier les métadonnées des bots directement dans l'interface utilisateur.
- **Amélioration de la gestion des erreurs :** Affichage plus clair des erreurs et des messages d'alerte.
- **Nouvelles fonctionnalités CLI :** Ajout de commandes pour planifier des runs et gérer les secrets.

### Évolutions techniques
- **Refactoring important du code :** Plusieurs composants ont été refactorés pour améliorer la maintenabilité, la lisibilité et la performance.
- **Amélioration de la gestion des erreurs :** Ajout de mécanismes de gestion des erreurs plus robustes.
- **Optimisation des performances :** Amélioration des performances de l'interface utilisateur et des processus de fond.
- **Sécurité renforcée :** Ajout de mesures de sécurité pour protéger les données et les secrets.
- **Amélioration de la gestion des dépendances :** Mise à jour des dépendances et correction de vulnérabilités.
- **Intégration de nouveaux outils :** Ajout de nouveaux outils pour faciliter le développement et le test.
- **Amélioration de l'architecture :** Refonte de l'architecture pour une meilleure extensibilité et scalabilité.
- **Implémentation de tests unitaires et d'intégration :** Ajout de tests pour garantir la qualité du code.
- **Utilisation de nouvelles technologies :** Adoption de nouvelles technologies pour améliorer les performances et la sécurité.
- **Amélioration de la gestion de la configuration :** Simplification de la configuration et de la gestion des paramètres.
- **Amélioration de la gestion des logs :** Ajout de logs plus détaillés pour faciliter le débogage.

### Autres changements
- **Documentation mise à jour :** La documentation a été mise à jour pour refléter les nouvelles fonctionnalités et les changements apportés au code.
- **Corrections de bugs mineurs :** Plusieurs bugs mineurs ont été corrigés.
- **Amélioration de la gestion des fichiers :** Amélioration de la gestion des fichiers et des répertoires.
- **Amélioration de la gestion des utilisateurs :** Amélioration de la gestion des utilisateurs et des permissions.
- **Nettoyage du code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Ajout de commentaires :** Ajout de commentaires pour faciliter la compréhension du code.
- **Mise à jour des dépendances :** Mise à jour des dépendances pour bénéficier des dernières corrections de bugs et améliorations de sécurité.
