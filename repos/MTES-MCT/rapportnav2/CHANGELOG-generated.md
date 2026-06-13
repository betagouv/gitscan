## Changelog : rapportnav2 (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les évolutions de rapportnav2 se concentrent sur l'amélioration de l'expérience utilisateur avec l'intégration de Metabase pour l'affichage de rapports, des corrections de bugs pour une meilleure stabilité et l'ajout de nouvelles fonctionnalités pour la gestion des ressources et des actions liées aux missions. Des améliorations de sécurité et des optimisations techniques ont également été apportées.

### Évolutions fonctionnelles
- Intégration d'un iframe Metabase pour l'affichage de rapports directement dans l'application ([335da44](https://github.com/MTES-MCT/rapportnav2/commit/335da44f3a3fde0e0af055f8d1d97eb584458155)).
- Ajout de la gestion des ressources et des actions liées aux missions, incluant une nouvelle table `mission_action_resource` ([afed9d0](https://github.com/MTES-MCT/rapportnav2/commit/afed9d064cca5e7ddeb9a9ef4d1d5b3f74099204)).
- Amélioration de l'interface utilisateur avec l'implémentation d'un dialogue personnalisé et l'application de styles spécifiques ([ce5ac4a](https://github.com/MTES-MCT/rapportnav2/commit/ce5ac4aaa8501642d23db2c28314976d3a04adf9)).
- Correction de l'affichage des erreurs 400 dans l'interface utilisateur.
- Ajout de la possibilité de plonger (diving) pour les contrôles de navigation.
- Amélioration de la gestion des types de ressources pour les unités de contrôle environnemental (Env).
- Ajout d'une zone de texte au lieu d'un champ texte pour les observations des contrôles environnementaux.

### Évolutions techniques
- Mise à jour des dépendances frontend ([38d3888](https://github.com/MTES-MCT/rapportnav2/commit/38d3888989a39576429c538116f1637f680a9727)).
- Correction de problèmes de validation des données côté backend et ajout d'un générateur de documentation pour les règles de validation ([fd12ba8](https://github.com/MTES-MCT/rapportnav2/commit/fd12ba83612bd5fd0a44d96daf17ed85743ba008)).
- Refactorisation du code frontend pour la gestion des administrateurs et ajout d'une page de gestion ([5522538](https://github.com/MTES-MCT/rapportnav2/commit/55225384a554b5c91f84f26877b164f96683f35c)).
- Mise à jour de la configuration backend pour exclure le code de la couverture de test.
- Correction de vulnérabilités de sécurité en forçant l'utilisation de versions spécifiques de `org.apache.tomcat.embed`.
- Correction de problèmes liés au cache et à la récupération des données.

### Autres changements
- Correction d'un bug lié au type de localisation GPS des contrôles.
- Mise à jour de la documentation et des snapshots de tests.
- Corrections de bugs mineurs et améliorations de la stabilité générale.
- Mise à jour du playbook de déploiement.
- Ajout de tests pour les snapshots frontend.
- Correction de bugs liés aux importations de tests.
