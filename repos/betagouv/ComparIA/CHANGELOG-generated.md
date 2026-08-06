## Changelog : ComparIA (30 derniers jours, au 04 août 2026)

### Résumé
Ce mois-ci, ComparIA a franchi une étape importante dans sa gestion opérationnelle avec l'introduction d'un mode maintenance pour faciliter les interventions techniques. L'outil en ligne de commande a été enrichi pour simplifier l'administration de la base de données, tandis que l'expérience utilisateur a été affinée par la correction de liens et la mise à jour du catalogue de modèles.

### Évolutions fonctionnelles
- **Mode maintenance** : Ajout d'une fonctionnalité permettant de suspendre l'accès au service et de rediriger automatiquement les utilisateurs vers la page d'accueil une fois la maintenance terminée [#570](https://github.com/betagouv/ComparIA/pull/570).
- **Gestion des modèles** : Mise à jour du catalogue des modèles disponibles et optimisation de la gestion des artefacts de modèles.
- **Corrections d'interface** : 
    - Correction du lien vers les datasets Hugging Face sur la page dédiée [#575](https://github.com/betagouv/ComparIA/pull/575).
    - Résolution d'un problème d'identification des modèles de langage (LLM) inconnus [#556](https://github.com/betagouv/ComparIA/pull/556).

### Évolutions techniques
- **Amélioration de la CLI** : L'outil `comparia-cli` propose désormais de nouvelles commandes pour la gestion de la base de données, notamment la création de sauvegardes et la déconnexion des sessions actives pour sécuriser les opérations de maintenance.
- **Refactorisation** : Optimisation de la gestion des messages système [#555](https://github.com/betagouv/ComparIA/pull/555).
- **Observabilité et configuration** :
    - Réduction du volume de traces envoyées à Sentry pour optimiser le monitoring [#588](https://github.com/betagouv/ComparIA/pull/588).
    - Ajustement des limites de débit (rate limits) par adresse IP.

### Autres changements
- **Documentation** : Refonte complète du fichier README pour mieux orienter les utilisateurs souhaitant déployer leur propre instance [#578](https://github.com/betagouv/ComparIA/pull/578).
- **Internationalisation** : Mise à jour des traductions pour l'anglais, l'espagnol, l'italien et le norvégien bokmål via Weblate [#557](https://github.com/betagouv/ComparIA/pull/557).
