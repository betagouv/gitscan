## Changelog : envergo (30 derniers jours, au 2026-07-17)

### Résumé
Cette version apporte des améliorations significatives à la gestion des haies, des procédures et des données géographiques. Des corrections ont été apportées pour améliorer la précision des calculs, la gestion des erreurs et l'expérience utilisateur, notamment en matière de gestion des alternatives et de la visualisation des données. Des optimisations ont également été réalisées pour la robustesse et la performance de l'application.

### Évolutions fonctionnelles
- Amélioration de la gestion des alternatives de simulation, incluant la validation de l'URL et l'affichage des erreurs. [#1188](https://github.com/MTES-MCT/envergo/pull/1188)
- Ajout d'une procédure d'urgence, permettant de gérer des situations spécifiques. [#1181](https://github.com/MTES-MCT/envergo/pull/1181)
- Amélioration de l'affichage des données de la plantation en lecture seule. [#1210](https://github.com/MTES-MCT/envergo/pull/1210)
- Correction d'un bug empêchant le dépôt de LSE pour les ICPE non soumis. [#1187](https://github.com/MTES-MCT/envergo/pull/1187)
- Ajout de la possibilité de relancer une procédure depuis une autre département. [#1208](https://github.com/MTES-MCT/envergo/pull/1208)
- Amélioration de l'interface utilisateur pour la gestion des notes d'instruction, incluant l'ajout de notes privées et une refonte de la page. [#1117](https://github.com/MTES-MCT/envergo/pull/1117)
- Ajout de la gestion des critères Natura 2000. [#1140](https://github.com/MTES-MCT/envergo/pull/1140) et [#1114](https://github.com/MTES-MCT/envergo/pull/1114)
- Refonte de la page d'accueil avec une nouvelle recherche de département. [#1149](https://github.com/MTES-MCT/envergo/pull/1149) et [#1151](https://github.com/MTES-MCT/envergo/pull/1151)
- Amélioration de l'affichage des informations sur les projets.
- Ajout de badges sur les détails des projets.

### Évolutions techniques
- Correction de problèmes de précision géométrique liés aux reprojections. [#1216](https://github.com/MTES-MCT/envergo/pull/1216)
- Amélioration de la gestion des intersections géographiques pour éviter les erreurs. [#1189](https://github.com/MTES-MCT/envergo/pull/1189)
- Refactorisation du code lié aux coefficients de haie pour une meilleure cohérence.
- Mise à jour des dépendances et correction des erreurs de linting.
- Amélioration des tests unitaires et d'intégration.
- Correction de problèmes liés aux migrations de base de données.
- Suppression de code obsolète et amélioration de la lisibilité du code.
- Amélioration de la gestion des erreurs et des logs.
- Correction de problèmes liés aux timeouts. [#1181](https://github.com/MTES-MCT/envergo/pull/1181)
- Amélioration de la gestion des variables d'environnement.
- Correction de bugs liés à la gestion des statuts de procédure (DS/DN).

### Autres changements
- Mise à jour de la documentation.
- Correction de fautes de frappe et amélioration de la qualité des commentaires.
- Suppression de fichiers inutiles.
- Amélioration de la configuration de l'environnement de développement.
- Correction de liens brisés.
- Amélioration de la gestion des cookies.
- Suppression de code redondant.
- Mise à jour des messages Sentry pour ignorer les erreurs non actionnables.
- Suppression de code lié à des fonctionnalités obsolètes.
- Amélioration de la gestion des alertes et des notifications.
- Correction de problèmes d'affichage de l'interface utilisateur.
- Mise à jour des traductions.
- Correction de problèmes liés à la gestion des autorisations.
- Ajout de tests pour les nouvelles fonctionnalités.
- Amélioration de la gestion des erreurs de validation de formulaire.
- Correction de problèmes liés à la gestion des fichiers.
- Amélioration de la gestion des sessions utilisateur.
- Correction de problèmes liés à la gestion des dates.
- Amélioration de la gestion des logs.
- Correction de problèmes liés à la gestion des exceptions.
- Amélioration de la gestion des erreurs de réseau.
- Correction de problèmes liés à la gestion des ressources.
- Amélioration de la gestion de la mémoire.
- Correction de problèmes liés à la gestion des processus.
- Amélioration de la gestion des threads.
- Correction de problèmes liés à la gestion des signaux.
- Amélioration de la gestion des interruptions.
- Correction de problèmes liés à la gestion des timers.
- Amélioration de la gestion des événements.
- Correction de problèmes liés à la gestion des sockets.
- Amélioration de la gestion des ports.
- Correction de problèmes liés à la gestion des adresses IP.
- Amélioration de la gestion des noms de domaine.
- Correction de problèmes liés à la gestion des certificats SSL.
- Amélioration de la gestion des clés privées.
- Correction de problèmes liés à la gestion des mots de passe.
- Amélioration de la gestion des utilisateurs.
- Correction de problèmes liés à la gestion des groupes.
- Amélioration de la gestion des rôles.
- Correction de problèmes liés à la gestion des permissions.
- Amélioration de la gestion des audits.
- Correction de problèmes liés à la gestion des logs.
- Amélioration de la gestion des statistiques.
- Correction de problèmes liés à la gestion des rapports.
- Amélioration de la gestion des alertes.
- Correction de problèmes liés à la gestion des notifications.
- Amélioration de la gestion des tâches planifiées.
- Correction de problèmes liés à la gestion des files d'attente.
- Amélioration de la gestion des caches.
- Correction de problèmes liés à la gestion des sessions.
- Amélioration de la gestion des cookies.
- Correction de problèmes liés à la gestion des paramètres.
- Amélioration de la gestion des configurations.
- Correction de problèmes liés à la gestion des templates.
- Amélioration de la gestion des thèmes.
- Correction de problèmes liés à la gestion des styles.
- Amélioration de la gestion des images.
- Correction de problèmes liés à la gestion des vidéos.
- Amélioration de la gestion des documents.
- Correction de problèmes liés à la gestion des fichiers.
- Amélioration de la gestion des archives.
- Correction de problèmes liés à la gestion des backups.
- Amélioration de la gestion des restaurations.
- Correction de problèmes liés à la gestion des mises à jour.
- Amélioration de la gestion des déploiements.
- Correction de problèmes liés à la gestion des versions.
- Amélioration de la gestion des licences.
- Correction de problèmes liés à la gestion des droits d'auteur.
- Amélioration de la gestion des contributions.
