## Changelog : ComparIA (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en termes de maintenance et de gestion des données. Une fonctionnalité de mode maintenance a été ajoutée pour permettre des opérations de maintenance sans interruption de service pour les utilisateurs. Des corrections ont également été apportées pour gérer plus efficacement les LLM inconnus et améliorer la gestion des messages système. L'interface utilisateur a été améliorée avec une refonte de la page d'accueil et des corrections de liens.

### Évolutions fonctionnelles
- Ajout d'un mode maintenance permettant de mettre le site en maintenance sans affecter les utilisateurs, avec redirection automatique vers la page d'accueil [#570](https://github.com/betagouv/ComparIA/pull/570).
- Amélioration de la page "Datasets" avec correction du lien vers le dataset Hugging Face [#578](https://github.com/betagouv/ComparIA/pull/578).
- Correction de l'affichage des LLM inconnus [#556](https://github.com/betagouv/ComparIA/pull/556).
- Refonte de la page d'accueil avec une nouvelle présentation axée sur le déploiement en propre [#575](https://github.com/betagouv/ComparIA/pull/575).

### Évolutions techniques
- Ajout de commandes `compara-cli` pour la sauvegarde de la base de données et la déconnexion des connexions DB pendant la maintenance [#570](https://github.com/betagouv/ComparIA/pull/570).
- Refactorisation des relations en base de données pour améliorer la suppression en cascade des données [#95d4a539](https://github.com/betagouv/ComparIA/commit/95d4a539).
- Refactorisation du message système pour une meilleure gestion [#555](https://github.com/betagouv/ComparIA/pull/555).
- Diminution du taux d'échantillonnage Sentry pour réduire le volume de traces [#588](https://github.com/betagouv/ComparIA/pull/588).
- Ajout d'une commande pour supprimer les comparaisons avec des LLM inconnus [#aaedca21](https://github.com/betagouv/ComparIA/commit/aaedca21).

### Autres changements
- Mises à jour des traductions pour l'italien, l'espagnol et le norvégien Bokmål.
- Nettoyage de code et suppression de code inutilisé.
- Correction de liens et améliorations de la documentation.
