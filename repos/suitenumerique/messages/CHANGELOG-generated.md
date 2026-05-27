## Changelog : messages (30 derniers jours, au 26 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment l'intégration de liens directs vers les threads, l'amélioration du compositeur de messages, et la possibilité d'inviter des utilisateurs qui ne se sont pas encore connectés. Des optimisations de performance ont également été apportées, en particulier pour la gestion des pièces jointes et l'indexation des recherches. La sécurité a été renforcée avec des mesures pour prévenir les vulnérabilités liées à l'envoi d'emails et à la génération de mots de passe.

### Évolutions fonctionnelles
- Ajout de liens directs vers les threads pour une navigation plus rapide et précise [#664].
- Amélioration du compositeur de messages pour une meilleure expérience utilisateur.
- Possibilité d'inviter des utilisateurs qui ne se sont pas encore connectés [#644].
- Ajout d'un lien vers une instance CalDAV pour accepter les événements directement [#584].
- Possibilité d'assigner des threads à des utilisateurs [#645].
- Ajout d'actions de lecture/non-lecture sur la barre d'actions des threads [#659].
- Ajout d'un champ TOTP obligatoire et d'un champ de recherche dans l'interface d'administration [#667].
- Possibilité de supprimer les messages internes à tout moment [#669].
- Ajout d'informations sur le délai de propagation DNS [#654].
- Possibilité de spécifier un identifiant de canal pour le widget de feedback sur la page d'accueil [#655].
- Sections de panneau redimensionnables dans l'interface utilisateur [#655].

### Évolutions techniques
- Refactorisation du stockage des pièces jointes avec implémentation d'un stockage en niveaux [#667].
- Optimisation des requêtes dans l'interface d'administration pour éviter les problèmes de performance liés au N+1 [#672].
- Amélioration de la logique d'importation des fichiers PST.
- Utilisation de la bibliothèque standard Python pour la composition des emails.
- Amélioration de la gestion du cache des requêtes de threads [#642].
- Remplacement de `delete_by_query` par une suppression en masse par ID pour améliorer les performances d'indexation.
- Gestion des erreurs de transport OpenSearch avec des tentatives de relance.
- Déplacement des tâches d'importation et d'indexation des files d'attente vers des conteneurs dédiés [#643].
- Optimisation de la charge utile en masse pour `search_reindex`.
- Décalage des tâches d'indexation pour une meilleure performance.

### Autres changements
- Correction de problèmes de parsing d'emails avec des caractères UTF-8 [#656].
- Correction d'un bug empêchant la suppression des accès aux threads [#668].
- Correction d'un bug lié à l'affichage de l'en-tête du panneau de thread avec des labels imbriqués [#658].
- Correction d'un bug lié à l'ordre des threads [#617].
- Correction d'un bug lié aux requêtes doubles et au scintillement lors de la recherche [#596].
- Correction d'un bug empêchant la marque d'un thread comme lu lors de l'envoi d'une réponse automatique [#594].
- Correction d'un bug lié à la logique de widget et à la compatibilité ascendante [#650, #649].
- Correction d'un bug lié à la localisation du séparateur de pièces jointes.
- Correction d'un bug lié au langage par défaut de l'interface utilisateur.
- Correction d'un bug lié à la gestion des erreurs Celery.
- Amélioration de la sécurité en empêchant le marquage des emails avec `From=To` comme expéditeur [#652].
- Renforcement de la sécurité lors de la génération des mots de passe en forçant l'inclusion de caractères spéciaux [#640].
- Correction d'un problème de nommage des processus dans le fichier Procfile.
- Suppression d'une assignation de thread précédemment implémentée et réintroduite par erreur.
