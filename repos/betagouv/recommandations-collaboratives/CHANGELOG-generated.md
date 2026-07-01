## Changelog : recommandations-collaboratives (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'ajout d'un système de plugins pour étendre les fonctionnalités de Recoco, l'amélioration de l'authentification avec une nouvelle méthode de connexion par code, et des corrections de bugs et optimisations de performance. Des améliorations ont également été apportées à la gestion des projets et à l'interface utilisateur.

### Évolutions fonctionnelles
- **Plugins :** Introduction d'un système de plugins pour étendre les fonctionnalités de Recoco. Cela inclut la possibilité d'ajouter des composants personnalisés aux conversations et d'utiliser des hooks JavaScript pour interagir avec l'application. [#2188](https://github.com/betagouv/recommandations-collaboratives/pull/2188)
- **Authentification :** Nouvelle méthode de connexion par code, remplaçant l'ancienne méthode "magic link". Cette nouvelle méthode est plus sécurisée et offre une meilleure expérience utilisateur. [#2212](https://github.com/betagouv/recommandations-collaboratives/pull/2212)
- **Gestion des projets :** Ajout d'un filtre "Mes projets" sur la page de la carte pour faciliter la recherche de projets. [#2144](https://github.com/betagouv/recommandations-collaboratives/pull/2144)
- **Interface utilisateur :** Amélioration de l'interface utilisateur de la page de connexion et ajout d'une nouvelle page 403.
- **CRM :** Tri de la liste des utilisateurs CRM par date d'inscription. [#2226](https://github.com/betagouv/recommandations-collaboratives/pull/2226)

### Évolutions techniques
- **Dépendances :** Mise à jour de plusieurs dépendances, notamment Django, pyjwt, et les dépendances frontend (dompurify, vite, form-data, tar, @babel/core).
- **CI/CD :** Ajout de `uv-audit` pour la sécurité des dépendances et suppression de `uv-secure`.
- **Architecture :** Refactorisation du code pour supprimer du code mort et améliorer la structure du projet.
- **Tests :** Ajout et amélioration des tests unitaires et d'intégration.
- **Outils :** Migration de la gestion des dépendances vers `uv` et suppression du fichier `requirements.txt`.
- **Sécurité :** Amélioration de la sécurité en empêchant la fuite du nom du schéma de base de données et en utilisant des échappements SQL appropriés.
- **Docker :** Utilisation de `uv` pour la gestion des dépendances Docker.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les changements apportés au système de plugins.
- **Nettoyage de code :** Suppression de code inutile et amélioration de la lisibilité du code.
- **Corrections :** Correction de plusieurs bugs mineurs et améliorations de la stabilité de l'application.
- **Configuration :** Mise à jour de la configuration pour utiliser les noms de routes au lieu des chemins pour les redirections de connexion.
- **Suppression de code déprécié :** Suppression de code lié à l'ancienne méthode d'authentification "magic link".
