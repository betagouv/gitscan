## Changelog : api-engagement (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des règles de diffusion des missions, l'intégration avec Demarches Simplifiées, et l'amélioration de l'expérience utilisateur sur la plateforme, notamment en termes d'accessibilité et d'ergonomie. Des corrections et optimisations techniques ont également été apportées pour améliorer la performance et la stabilité de l'API et des applications associées.

### Évolutions fonctionnelles

- **Intégration Demarches Simplifiées:** Ajout de l'intégration avec Demarches Simplifiées pour une meilleure diffusion des missions. [#1154](https://github.com/betagouv/api-engagement/issues/1154)
- **Règles de diffusion:**
    - Affichage des règles de diffusion dans le tableau de bord de l'éditeur. [#1151](https://github.com/betagouv/api-engagement/issues/1151)
    - Amélioration de la gestion des règles de diffusion, notamment en stockant les informations au niveau de l'organisation éditrice. [#1183](https://github.com/betagouv/api-engagement/issues/1183)
    - Possibilité de filtrer les diffuseurs par valeur de champ dans les règles de diffusion. [#1111](https://github.com/betagouv/api-engagement/issues/1111)
    - Suppression de l'ancienne table `publisher_diffusion` et utilisation des nouvelles règles de diffusion. [#1135](https://github.com/betagouv/api-engagement/issues/1135)
- **Plateforme:**
    - Améliorations de l'accessibilité (RGAA) sur la plateforme, notamment pour les formulaires et la page d'accueil. [#1179](https://github.com/betagouv/api-engagement/issues/1179) et [#1128](https://github.com/betagouv/api-engagement/issues/1128)
    - Redesign de la page des résultats et de la page de détails des missions sur la plateforme. [#1060](https://github.com/betagouv/api-engagement/issues/1060) et [#1081](https://github.com/betagouv/api-engagement/issues/1081)
    - Ajout d'un paramètre de débogage pour afficher un bouton de débogage sur la plateforme. [#1126](https://github.com/betagouv/api-engagement/issues/1126)
    - Amélioration de l'affichage des badges de compensation. [#1173](https://github.com/betagouv/api-engagement/issues/1173)
- **API:**
    - Ajout d'un "gate" `openToMinor` pour contrôler l'accès à certaines fonctionnalités. [#1185](https://github.com/betagouv/api-engagement/issues/1185)
    - Amélioration de la prise en charge du HTML dans l'endpoint `v2/mission`. [#1149](https://github.com/betagouv/api-engagement/issues/1149)
    - Amélioration de la prise en charge de `does_not_contain` dans l'endpoint `mission-browse`. [#1148](https://github.com/betagouv/api-engagement/issues/1148)
    - Ajout de valeurs par défaut pour les champs "places". [#1155](https://github.com/betagouv/api-engagement/issues/1155)

### Évolutions techniques

- **Refactoring:** Refactorisation de la gestion des accès des éditeurs et de la résolution des règles de diffusion. [#1157](https://github.com/betagouv/api-engagement/issues/1157) et [#1187](https://github.com/betagouv/api-engagement/issues/1187)
- **CI/CD:** Mise à jour des dépendances et configuration du workspace npm pour les jobs analytics et widget. [#1172](https://github.com/betagouv/api-engagement/issues/1172)
- **Analytics:**
    - Ajout d'un job pour rejouer les queues de lettres mortes. [#1116](https://github.com/betagouv/api-engagement/issues/1116)
    - Amélioration des jobs d'analytics pour la plateforme. [#1127](https://github.com/betagouv/api-engagement/issues/1127)
    - Ajout d'un mart quotidien pour l'enrichissement des missions. [#1123](https://github.com/betagouv/api-engagement/issues/1123)
- **Sécurité:** Protection contre les injections dans l'endpoint d'enrichissement des missions. [#1141](https://github.com/betagouv/api-engagement/issues/1141)
- **Infrastructure:** Limitation du taux de requêtes sur les routes de l'API de la plateforme. [#1075](https://github.com/betagouv/api-engagement/issues/1075)

### Autres changements

- Amélioration de la documentation des règles de diffusion. [#1142](https://github.com/betagouv/api-engagement/issues/1142) et [#1177](https://github.com/betagouv/api-engagement/issues/1177)
- Suppression des URLs de rapport. [#1191](https://github.com/betagouv/api-engagement/issues/1191)
- Ajout d'une extension Chrome pour faciliter le développement. [#1178](https://github.com/betagouv/api-engagement/issues/1178)
- Corrections diverses et améliorations de la qualité du code.
