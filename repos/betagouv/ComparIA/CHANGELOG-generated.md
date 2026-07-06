## Changelog : ComparIA (30 derniers jours, au 29 juin 2026)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en termes de performance, notamment pour l'export de données, et de nouvelles fonctionnalités comme l'ajout d'un contrôle de style pour le classement des modèles et la prise en charge de LaTeX. Des corrections de bugs et des mises à jour de sécurité ont également été implémentées, ainsi que des traductions mises à jour grâce à la communauté Weblate.

### Évolutions fonctionnelles
- Ajout d'un contrôle de style pour le classement des modèles, permettant de personnaliser l'affichage des résultats [#532](https://github.com/betagouv/ComparIA/pull/532).
- Prise en charge de LaTeX pour une meilleure présentation des données [#549](https://github.com/betagouv/ComparIA/pull/549).
- Ajout du modèle GLM 5.2 au catalogue de modèles disponibles [#540](https://github.com/betagouv/ComparIA/pull/540).
- Ajout du modèle MiniMax M3 au catalogue de modèles disponibles [#531](https://github.com/betagouv/ComparIA/pull/531).
- Amélioration de la gestion des erreurs et du rafraîchissement du token Captcha pour une meilleure expérience utilisateur [#539](https://github.com/betagouv/ComparIA/pull/539).
- Ajout du suivi du temps nécessaire pour obtenir une réponse des modèles et horodatage des conversations dans les ensembles de données [#524](https://github.com/betagouv/ComparIA/pull/524).
- Ajout d'informations sur les LLM (Large Language Models) [#517](https://github.com/betagouv/ComparIA/pull/517).
- Amélioration de la gestion des données PII (Personally Identifiable Information) et du spam dans les ensembles de données [#527](https://github.com/betagouv/ComparIA/pull/527).

### Évolutions techniques
- Optimisation de la performance de l'export des ensembles de données en utilisant la mise en cache et le streaming [#516](https://github.com/betagouv/ComparIA/pull/516).
- Refactorisation du code pour améliorer la réactivité de l'interface utilisateur dans l'arène [#545](https://github.com/betagouv/ComparIA/pull/545).
- Mise à jour des migrations de la base de données pour améliorer la cohérence et la performance.
- Amélioration de la gestion des logs avec l'utilisation de LokiQueueHandler pour éviter les blocages.
- Correction de bugs liés à la validation des IDs des LLM [#391](https://github.com/betagouv/ComparIA/pull/391).
- Correction de bugs liés au rafraîchissement du token Altcha [#463](https://github.com/betagouv/ComparIA/pull/463).
- Correction d'un bug lié à la locale "en" [#533](https://github.com/betagouv/ComparIA/pull/533).

### Autres changements
- Mise à jour des traductions pour l'italien, l'espagnol, le norvégien bokmål, l'estonien, le suédois, le lituanien, le danois et l'anglais grâce à la communauté Weblate.
- Mise à jour des dépendances du projet.
- Amélioration de la configuration et de la documentation.
- Nettoyage du code et suppression de fichiers inutiles.
