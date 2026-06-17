## Changelog : mon-service-securise (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'administration des utilisateurs et des organisations, avec une refonte de l'interface pour les administrateurs et superviseurs. Des améliorations d'accessibilité et des corrections de bugs ont également été apportées à l'ensemble de l'application. L'ajout de nouveaux ACR pour Proconnect renforce la sécurité du service.

### Évolutions fonctionnelles
- Ajout d'une page dédiée aux administrateurs supervisés par un superviseur. [#86f8ea0](https://github.com/betagouv/mon-service-securise/issues/86f8ea0)
- Les administrateurs et superviseurs ont maintenant une navigation spécifique.
- Un libellé spécifique est affiché pour les administrateurs dans le fil d'ariane des mesures.
- Les superviseurs sont redirigés vers la page `/admin/entites`.
- L'encart des statistiques est masqué sur le tableau de bord si le *feature flag* est désactivé.
- Affichage de l'état actif des items du menu d'administration.
- Le menu d'administration est caché derrière un *feature flag*.
- Ajout d'une action permettant de retirer les accès d'un utilisateur administré à des services.
- Possibilité d'attribuer un rôle à un utilisateur administré.
- Affichage des cartes résumé sur la page admin/utilisateurs.
- Affichage des administrateurs d'une entité sur la page des superviseurs.
- Ajout d'une fonctionnalité permettant de nommer un administrateur sur un périmètre complet.
- Ajout d'une fonctionnalité permettant de retirer un administrateur d'une entité.
- Ajout d'une fonctionnalité permettant de supprimer un administrateur.
- Affichage du nombre d'entités et de services par utilisateur administré.
- Affichage d'un badge "Admin" sur la liste des utilisateurs.
- Ajout d'une page d'invitation d'administrateurs.
- Amélioration de l'affichage des actions du tiroir.
- Correction de l'affichage des actions du tiroir au-dessus des tableaux DSFR.
- Correction de l'affichage de la hauteur des tuiles.
- Correction de l'affichage du cartouche thématique pour éviter le passage à la ligne.
- Affichage d'une modale listant les entités d'un utilisateur administré.
- Empêche la redirection vers une URL qui ne commence pas par l'URL de base de MSS.
- Ajout de la possibilité de passer des données supplémentaires lors de l'audit.
- Ajout de la possibilité de nommer un administrateur en tant que superviseur.

### Évolutions techniques
- Épinglage des versions des dépendances des GitHub Actions pour une meilleure stabilité. [74bb5f1](https://github.com/betagouv/mon-service-securise/commit/74bb5f1)
- Ajout de nouveaux ACR garantissant l'usage d'un MFA de Proconnect. [f4f72c1](https://github.com/betagouv/mon-service-securise/commit/f4f72c1)
- Refactorisation du code pour l'administration des organisations, avec migration vers un nouveau dépôt de données.
- Suppression de code obsolète et simplification de certaines fonctions.
- Amélioration de la gestion des erreurs et des types.
- Ajout d'un singleton pour la connexion Knex.
- Suppression de la duplication de configuration Knex.
- Ajout d'un script pour la mise à jour de l'UI Kit.
- Mise à jour de l'UI Kit.
- Ajout d'un abonné pour tracer l'attribution d'un rôle.
- Ajout d'un adaptateur d'audit.
- Ajout de tests unitaires et d'intégration.
- Mise à jour de la dépendance `axios` vers la version 1.16.0.

### Autres changements
- Amélioration de l'accessibilité de plusieurs pages (conseils cyber, statistiques, CGU, mentions légales, accessibilité, inscription, connexion, création de service).
- Correction de problèmes de contraste et d'accessibilité sur différentes pages.
- Ajout d'articles Crisp aux pages testées pour l'accessibilité.
- Correction de liens et d'éléments d'interface.
- Amélioration de la documentation et des commentaires.
- Corrections de bugs mineurs et améliorations de la qualité du code.
- Ajout de rapports d'audit pour les actions d'administration.
- Correction de l'affichage des badges de mesure.
- Ajout d'un message d'alerte lors de l'attribution de rôle.
- Correction de la procédure d'initialisation des sels.
- Correction de l'affichage des services "seul propriétaire".
- Correction de l'affichage des administrateurs sur plusieurs lignes.
- Correction de l'affichage des indicateurs "seul propriétaire".
- Correction de l'affichage des entités supervisées.
- Correction de l'affichage des services par entité supervisée.
- Ajout d'un message d'alerte si le tableau est vide.
- Amélioration de la gestion des erreurs et des exceptions.
- Correction de problèmes de typage.
- Suppression de code inutile.
- Amélioration de la lisibilité du code.
- Ajout de commentaires pour faciliter la maintenance.
