## Changelog : ComparIA (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, ComparIA a connu des améliorations significatives en termes de fonctionnalités et de performance. L'ajout de la recherche web intégrée aux comparaisons, l'amélioration de la gestion des modèles (ajout, archivage, informations) et l'optimisation de l'export des données sont les évolutions les plus notables. Des corrections de bugs et des mises à jour de traductions ont également été apportées pour améliorer l'expérience utilisateur.

### Évolutions fonctionnelles
- **Recherche web intégrée :** Ajout de la possibilité d'intégrer des résultats de recherche web directement dans les comparaisons, avec un toggle pour activer/désactiver cette fonctionnalité. [#549](https://github.com/betagouv/ComparIA/issues/549)
- **Nouveaux modèles :** Ajout du modèle GLM 5.2 et MiniMax M3 au catalogue. [#540](https://github.com/betagouv/ComparIA/issues/540), [#531](https://github.com/betagouv/ComparIA/issues/531)
- **Gestion des modèles :** Archivage des modèles GPT 5.4, GLM 5 et MiniMax M2.5.
- **Amélioration de l'interface utilisateur :**
    - Correction de bugs d'affichage et de comportement sur mobile. [#545](https://github.com/betagouv/ComparIA/issues/545)
    - Amélioration de la réactivité de l'arène.
    - Correction de l'état désactivé du sélecteur de modèle.
    - Ajout d'un contrôle de style sur le classement (leaderboard). [#532](https://github.com/betagouv/ComparIA/issues/532)
- **Gestion des datasets :** Simplification de la page des datasets pour n'afficher qu'un seul dataset. [#517](https://github.com/betagouv/ComparIA/issues/517)
- **Gestion des utilisateurs :** Ajout d'informations sur les organisations, licences et LLMs. [#512](https://github.com/betagouv/ComparIA/issues/512)

### Évolutions techniques
- **Performance :** Optimisation de l'export des datasets pour réduire la consommation de mémoire et améliorer la vitesse. [#516](https://github.com/betagouv/ComparIA/issues/516)
- **Base de données :**
    - Ajout de migrations pour gérer les nouvelles fonctionnalités et les corrections de bugs.
    - Correction de problèmes liés aux migrations et à la gestion des données archivées.
- **Cache :** Implémentation d'un cache pour les résultats de recherche web.
- **Sécurité :**
    - Mise en place d'un "guardrail" de sécurité de contenu pour les prompts utilisateurs. [#542](https://github.com/betagouv/ComparIA/issues/542)
    - Correction de vulnérabilités potentielles liées à la gestion des jetons Altcha. [#463](https://github.com/betagouv/ComparIA/issues/463)
- **Logging :** Utilisation de LokiQueueHandler pour éviter les blocages lors de l'envoi de logs.
- **Dépendances :** Mises à jour de certaines dépendances.

### Autres changements
- **Documentation :** Mise à jour de la documentation et du fichier README.
- **Traductions :** Mise à jour des traductions dans plusieurs langues (italien, espagnol, estonien, suédois, lituanien, danois, anglais, etc.).
- **Nettoyage de code :** Suppression de code inutile et refactoring de certaines parties du code.
- **Configuration :** Ajout de la variable d'environnement `LINKUP_API_KEY` pour la configuration de l'API Linkup.
- **Tests :** Ajout et mise à jour de tests unitaires et d'intégration.
