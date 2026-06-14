## Changelog : messages (30 derniers jours, au 12 juin 2026)

### Résumé
Les 30 derniers jours ont été marqués par des améliorations significatives de l'interface utilisateur, notamment au niveau de la gestion des boîtes de réception et de la composition des messages. Des corrections de bugs ont également été apportées, notamment concernant l'importation de fichiers PST, le traitement des pièces jointes et la gestion des événements de calendrier.  Une refonte technique majeure a eu lieu avec le remplacement de Next.js par Vite et TanStack Router pour une meilleure performance et maintenabilité.

### Évolutions fonctionnelles
- **Boîte de réception :** Amélioration du menu déroulant des boîtes de réception [#705].
- **Paramètres de la boîte de réception :** Regroupement des paramètres de la boîte de réception dans une boîte de dialogue dédiée.
- **Composition de messages :** Amélioration de l'expérience de composition des messages, notamment la gestion des pièces jointes et des statuts de livraison.
- **Liens profonds vers les threads :** Ajout de la possibilité de créer des liens directs vers des threads spécifiques [#664].
- **Assignation de threads :** Possibilité d'assigner des threads à des utilisateurs [#645].
- **Calendrier :** Amélioration de l'affichage des événements récurrents avec exceptions [#686] et ajout d'un lien direct vers une instance CalDAV pour accepter les événements [#584].
- **Illustration de la page d'accueil :** Nouvelle illustration pour la page d'accueil [#702].

### Évolutions techniques
- **Refonte Frontend :** Remplacement de Next.js par Vite et TanStack Router pour une meilleure performance et une architecture plus moderne [#675].
- **Bibliothèque d'emails :** Migration de l'analyseur et du compositeur d'emails vers la nouvelle bibliothèque `jmap-email` [#700].
- **Stockage des blobs :** Implémentation d'un stockage en niveaux et refactorisation des blobs/pièces jointes.
- **Sécurité SMTP :** Renforcement de la configuration de la connexion SMTP et des proxys.
- **Optimisation des performances :** Correction d'un problème de performance lié au nombre élevé de destinataires [#672] et optimisation des requêtes dans l'interface d'administration.
- **Dépendances :** Mise à jour de `django-lasuite` vers la version 0.0.26 [#689].

### Autres changements
- **Documentation :** Ajout de scripts de publication PyPI pour `jmap-email` [#694].
- **Tests :** Ajout de la bibliothèque `defusedxml` pour une meilleure sécurité lors de l'analyse de fichiers XML [#677].
- **Sentry :** Intégration de l'état du selfcheck au système de surveillance Sentry.
- **Nettoyage du code :** Suppression de champs de modèle dépréciés.
- **Configuration :** Amélioration de la gestion des fichiers d'environnement pour les tests.
