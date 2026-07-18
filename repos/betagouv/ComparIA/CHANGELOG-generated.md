## Changelog : ComparIA (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en termes de stabilité, de fonctionnalités et d'expérience utilisateur. L'ajout d'un mode maintenance, la gestion améliorée des erreurs, et l'intégration de nouveaux modèles de langage sont les points forts de cette période. Des corrections ont également été apportées pour améliorer la réactivité de l'interface et la validation des identifiants des modèles.

### Évolutions fonctionnelles
- Ajout d'un mode maintenance permettant de mettre le site hors ligne pour des opérations de maintenance planifiées [#572](https://github.com/betagouv/ComparIA/pull/572).
- Intégration du modèle GLM 5.2 au catalogue de modèles disponibles [#540](https://github.com/betagouv/ComparIA/pull/540).
- Possibilité d'activer/désactiver un contrôle de style dans le classement des modèles [#532](https://github.com/betagouv/ComparIA/pull/532).
- Ajout du support LaTeX pour une meilleure présentation des contenus [#549](https://github.com/betagouv/ComparIA/pull/549).
- Amélioration de la gestion des erreurs lors de l'envoi de prompts dans l'arène [#545](https://github.com/betagouv/ComparIA/pull/545).
- Correction du lien vers le dataset Hugging Face sur la page Datasets [#575](https://github.com/betagouv/ComparIA/pull/575).
- Mise en place d'un "guardrail" de sécurité de contenu pour filtrer les prompts utilisateurs [#542](https://github.com/betagouv/ComparIA/pull/542).

### Évolutions techniques
- Refactor de la gestion des messages système pour simplifier la configuration et améliorer la cohérence [#555](https://github.com/betagouv/ComparIA/pull/555).
- Refactor des relations en base de données pour améliorer la suppression en cascade et l'intégrité des données [#95d4a539](https://github.com/betagouv/ComparIA/commit/95d4a539).
- Ajout de commandes `compara-cli` pour la sauvegarde de la base de données et la déconnexion des connexions DB en mode maintenance [#570](https://github.com/betagouv/ComparIA/pull/570), [#568](https://github.com/betagouv/ComparIA/pull/568).
- Correction de la validation des identifiants des modèles de langage [#391](https://github.com/betagouv/ComparIA/pull/391).
- Correction d'un problème de rafraîchissement du token Altcha [#463](https://github.com/betagouv/ComparIA/pull/463).
- Réduction du taux d'échantillonnage Sentry pour limiter le volume de traces [#588](https://github.com/betagouv/ComparIA/pull/588).
- Amélioration de la réactivité de l'arène sur mobile [#545](https://github.com/betagouv/ComparIA/pull/545).

### Autres changements
- Mise à jour des traductions pour plusieurs langues via Weblate (Norvégien Bokmål, Espagnol, Anglais, Italien, Estonien, Suédois, Lituanien, Danois).
- Refonte de la page README pour mettre l'accent sur le déploiement autonome [#578](https://github.com/betagouv/ComparIA/pull/578).
- Corrections mineures de l'interface utilisateur (marges, états désactivés).
- Mise à jour des dépendances et des configurations.
