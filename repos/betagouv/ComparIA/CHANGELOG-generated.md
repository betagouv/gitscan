## Changelog : ComparIA (30 derniers jours, au 9 juillet 2026)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en termes de fonctionnalités et de stabilité. L'ajout d'un mode maintenance permet de réaliser des opérations techniques sans perturber les utilisateurs. De nouvelles fonctionnalités ont été implémentées pour la gestion des modèles de langage, notamment l'ajout de GLM 5.2 et MiniMax M3, ainsi que des améliorations de l'interface utilisateur pour le classement des modèles. Des corrections de bugs et des refactorings ont également été réalisés pour améliorer la qualité du code et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'un mode maintenance permettant de mettre la plateforme hors ligne pour des opérations techniques [#570](https://github.com/betagouv/ComparIA/pull/570).
- Possibilité de créer une sauvegarde de la base de données via la ligne de commande `compara-cli` [#572](https://github.com/betagouv/ComparIA/pull/572).
- Ajout de GLM 5.2 au catalogue de modèles [#540](https://github.com/betagouv/ComparIA/pull/540).
- Ajout de MiniMax M3 au catalogue de modèles [#531](https://github.com/betagouv/ComparIA/pull/531) et [#538](https://github.com/betagouv/ComparIA/pull/538).
- Ajout d'un contrôle de style pour le classement des modèles, permettant de filtrer les résultats en fonction de critères spécifiques [#532](https://github.com/betagouv/ComparIA/pull/532).
- Ajout du support LaTeX pour la saisie de texte [#549](https://github.com/betagouv/ComparIA/pull/549).
- Consolidation de la page des datasets en une seule page [#539](https://github.com/betagouv/ComparIA/pull/539).

### Évolutions techniques
- Refactor de la gestion des messages système pour simplifier le code et améliorer la performance [#555](https://github.com/betagouv/ComparIA/pull/555).
- Refactor des relations en base de données pour améliorer l'intégrité des données et simplifier les suppressions [#95d4a539](https://github.com/betagouv/ComparIA/commit/95d4a539).
- Mise en place d'un guardrail de sécurité de contenu pour les prompts utilisateurs afin de limiter les réponses inappropriées [#542](https://github.com/betagouv/ComparIA/pull/542).
- Correction de bugs liés à la validation des IDs des modèles de langage [#391](https://github.com/betagouv/ComparIA/pull/391).
- Correction de bugs liés au rafraîchissement des tokens Altcha [#463](https://github.com/betagouv/ComparIA/pull/463).
- Correction d'un bug lié à la sélection de la locale sur le frontend [#533](https://github.com/betagouv/ComparIA/pull/533).
- Amélioration de la réactivité de l'interface de l'arène et correction de bugs d'affichage [#545](https://github.com/betagouv/ComparIA/pull/545).

### Autres changements
- Mise à jour des traductions italiennes via Weblate [#552](https://github.com/betagouv/ComparIA/pull/552), [#546](https://github.com/betagouv/ComparIA/pull/546), [#490](https://github.com/betagouv/ComparIA/pull/490).
- Ajout de la traduction danoise pour MiniMax M3 [#538](https://github.com/betagouv/ComparIA/pull/538).
- Suppression de code inutilisé.
- Corrections mineures et améliorations de la documentation.
- Limitation temporaire des limites de débit par IP pour résoudre un problème de performance [#45f5b018](https://github.com/betagouv/ComparIA/commit/45f5b018).
