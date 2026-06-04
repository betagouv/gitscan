## Changelog : ComparIA (30 derniers jours, au 2026-06-02)

### Résumé
Ce mois-ci, ComparIA a connu des améliorations significatives en termes de gestion des données, de refonte de l'architecture backend et d'optimisations de l'interface utilisateur. Des corrections de bugs et des améliorations de la sécurité ont également été apportées, notamment en matière de détection de spam.  Une préparation est en cours pour supporter plusieurs instances de l'application, notamment pour le danois.

### Évolutions fonctionnelles
- Ajout de nouveaux modèles de langage : Gemini 3.5 Flash et Grok 4.3. [#480](https://github.com/betagouv/ComparIA/pull/480)
- Amélioration de la détection de spam : blocage de modèles de roleplay et de tentatives de jailbreak. [#473](https://github.com/betagouv/ComparIA/pull/473)
- Ajout de la possibilité de configurer le portail par défaut.
- Amélioration de l'interface utilisateur avec de nouvelles animations pour les votes et les révélations.
- Ajout de la gestion du danois (traductions et configuration). [#484](https://github.com/betagouv/ComparIA/pull/484)
- Ajout d'un nouveau groupe de commandes pour la génération de données et de classements.
- Ajout d'une nouvelle modalité de vote et d'annotation.

### Évolutions techniques
- Refonte majeure de l'architecture backend :
    - Remplacement des anciens modèles de données par des modèles SQLModel.
    - Utilisation de types datetime pour les champs de date.
    - Ajout de gestionnaires de session pour la base de données.
    - Amélioration de la gestion du streaming des messages.
    - Optimisation des requêtes de base de données.
- Préparation pour supporter plusieurs instances de l'application (français et danois) :
    - Séparation des configurations et des variables d'environnement.
    - Utilisation de namespaces Redis spécifiques à chaque instance.
    - Mise en place d'un système de gestion des secrets avec Keepass.
- Amélioration des scripts de migration de la base de données : ajout d'un mode incrémental et gestion des erreurs.
- Suppression de l'utilisation de Vertex AI dans Litellm.
- Mise à jour des dépendances : litellm, typescript.
- Amélioration de la gestion des logs et des erreurs.
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.

### Autres changements
- Mise à jour des traductions italiennes et danoises via Weblate.
- Correction de bugs mineurs et améliorations de la documentation.
- Nettoyage du code et suppression de code obsolète.
- Amélioration des tests et de la couverture de code.
- Correction de problèmes de typage dans les jobs de lint.
- Suppression de modèles de langage obsolètes (GPT 5.4, GLM 5, MiniMax M2.5).
- Archivage des modèles Grok.
- Ajout de validations pour les datasets.
- Correction de problèmes liés à la gestion des données corrompues.
- Suppression de la gestion des sessions hash.
- Mise à jour des modèles de confiance pour les classements.
