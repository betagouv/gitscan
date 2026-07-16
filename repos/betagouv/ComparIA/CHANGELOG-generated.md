## Changelog : ComparIA (30 derniers jours, au 15 juillet 2026)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en termes de fonctionnalités et de stabilité. L'ajout d'un mode maintenance permet des opérations de maintenance sans interruption de service pour les utilisateurs. Des améliorations ont été apportées à l'interface utilisateur, notamment pour la visualisation des classements et la gestion des datasets. La sécurité a également été renforcée avec l'ajout d'un système de modération du contenu.

### Évolutions fonctionnelles
- Ajout d'un mode maintenance pour permettre des opérations de maintenance sans affecter l'expérience utilisateur. [#572](https://github.com/betagouv/ComparIA/issues/572)
- Possibilité de basculer entre un classement standard et un classement contrôlé par un style, offrant plus de flexibilité dans l'analyse des résultats. [#532](https://github.com/betagouv/ComparIA/issues/532)
- Ajout du modèle GLM 5.2 au catalogue de modèles disponibles. [#540](https://github.com/betagouv/ComparIA/issues/540)
- Support du format LaTeX pour une meilleure présentation des contenus. [#549](https://github.com/betagouv/ComparIA/issues/549)
- Amélioration de la page des datasets, consolidée en une seule vue. [#578](https://github.com/betagouv/ComparIA/issues/578)
- Ajout d'une fonctionnalité permettant de créer une copie de sauvegarde de la base de données via la ligne de commande. [#570](https://github.com/betagouv/ComparIA/issues/570)
- Ajout d'une commande pour déconnecter les connexions à la base de données pendant la maintenance. [#570](https://github.com/betagouv/ComparIA/issues/570)
- Correction de l'affichage du lien vers le dataset Hugging Face sur la page Datasets. [#555](https://github.com/betagouv/ComparIA/issues/555)

### Évolutions techniques
- Refactorisation de la gestion des messages système pour une meilleure maintenabilité. [#555](https://github.com/betagouv/ComparIA/issues/555)
- Amélioration de la gestion des relations en base de données avec l'ajout de suppressions en cascade. [#556](https://github.com/betagouv/ComparIA/issues/556)
- Mise en place d'un système de modération du contenu pour les prompts utilisateurs. [#542](https://github.com/betagouv/ComparIA/issues/542)
- Correction de la validation des identifiants des LLM. [#391](https://github.com/betagouv/ComparIA/issues/391)
- Correction du rafraîchissement du token Altcha. [#463](https://github.com/betagouv/ComparIA/issues/463)
- Refactorisation du code pour améliorer la réactivité de l'arène sur mobile. [#545](https://github.com/betagouv/ComparIA/issues/545)
- Mise à jour des dépendances et des configurations.

### Autres changements
- Mise à jour des traductions italiennes via Weblate.
- Corrections mineures de l'interface utilisateur.
- Amélioration de la documentation et des commentaires dans le code.
- Corrections de bugs et améliorations de la stabilité générale.
