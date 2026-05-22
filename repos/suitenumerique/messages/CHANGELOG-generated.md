## Changelog : messages (30 derniers jours, au 21 mai 2026)

### Résumé
Les dernières mises à jour de Messages se concentrent sur l'amélioration des performances, la correction de bugs et l'ajout de nouvelles fonctionnalités pour faciliter la gestion des messages et des threads. Des améliorations significatives ont été apportées à l'importation de fichiers PST, à la gestion des pièces jointes, à l'interface utilisateur et à la sécurité.

### Évolutions fonctionnelles
- Possibilité de supprimer les messages internes à tout moment. [#669](https://github.com/suitenumerique/messages/issues/669)
- Amélioration du composant de rédaction de messages (message composer).
- Lien direct vers un thread spécifique. [#664](https://github.com/suitenumerique/messages/issues/664)
- Ajout d'un champ TOTP obligatoire et d'un champ de recherche dans l'interface d'administration. [#667](https://github.com/suitenumerique/messages/issues/667)
- Possibilité d'assigner un thread. [#645](https://github.com/suitenumerique/messages/issues/645)
- Ajout d'actions de lecture/non-lu sur la barre d'actions d'un thread. [#659](https://github.com/suitenumerique/messages/issues/659)
- Possibilité d'inviter des utilisateurs qui ne se sont pas encore connectés. [#644](https://github.com/suitenumerique/messages/issues/644)
- Localisation du séparateur de pièces jointes.
- Amélioration de la gestion des panneaux redimensionnables.
- Affichage d'un info-bulle pour confirmer l'actualisation de la boîte de réception.
- Support des widgets hérités et nouveaux. [#650](https://github.com/suitenumerique/messages/issues/650)

### Évolutions techniques
- Refonte du stockage des pièces jointes (blobs) avec implémentation d'un stockage en plusieurs niveaux.
- Optimisation des requêtes N+1 dans l'interface d'administration.
- Correction d'un problème de performance lié au nombre élevé de destinataires. [#672](https://github.com/suitenumerique/messages/issues/672)
- Amélioration de la logique d'importation des fichiers PST.
- Refactorisation de la gestion du cache des requêtes de threads. [#642](https://github.com/suitenumerique/messages/issues/642)
- Utilisation de la bibliothèque standard Python pour la composition des emails.
- Amélioration de la gestion des erreurs de transport OpenSearch.
- Optimisation de la gestion des requêtes de réindexation.
- Suppression de l'utilisation de `delete_by_query` au profit d'une suppression en masse par ID.
- Amélioration du payload en masse pour la réindexation de la recherche.
- Déport des tâches d'indexation pour améliorer les performances.
- Correction de problèmes de parsing d'emails avec des caractères UTF8. [#656](https://github.com/suitenumerique/messages/issues/656)
- Mise en place de conteneurs dédiés pour les files d'attente des workers d'import et de réindexation.
- Correction du nom des processus dans le fichier Procfile.
- Correction de l'affichage des en-têtes avec des labels imbriqués. [#658](https://github.com/suitenumerique/messages/issues/658)

### Autres changements
- Correction de la création des fichiers d'environnement avant l'appel à compose.
- Préservation de l'ID "obs-id-left" In-Reply-To via UnstructuredHeader.
- Ajout d'informations sur le délai de propagation DNS. [#654](https://github.com/suitenumerique/messages/issues/654)
- Empêchement du marquage des emails "From=To" comme expéditeur. [#652](https://github.com/suitenumerique/messages/issues/652)
- Ajout d'un bouton d'aide configurable dans l'en-tête.
- Renforcement de la sécurité des mots de passe générés en forçant l'inclusion de caractères spéciaux. [#640](https://github.com/suitenumerique/messages/issues/640)
- Forçage de la langue par défaut. [#647](https://github.com/suitenumerique/messages/issues/647)
- Ajout d'un widget pour le feedback sur la page d'accueil avec un ID de canal spécifique. [#655](https://github.com/suitenumerique/messages/issues/655)
