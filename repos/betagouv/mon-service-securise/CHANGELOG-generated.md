## Changelog : mon-service-securise (30 derniers jours, au 02 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur avec l'adoption des composants du Design System de la République Française (DSFR), améliorant ainsi l'accessibilité et la cohérence visuelle. Des fonctionnalités d'administration des utilisateurs et de gestion des risques ont été ajoutées ou améliorées, notamment la gestion des rôles d'administration et la visualisation des risques V2. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Implémentation de l'attribution de rôles (admin, superviseur) aux utilisateurs : permet de gérer les permissions d'accès aux fonctionnalités d'administration.
- Affichage des actions de retrait d'accès aux services d'un utilisateur administré.
- Amélioration de l'affichage des risques V2 : affichage de la description des risques, des badges, et intégration d'identifiants numériques.
- Ajout d'une recherche textuelle sur les responsables de mesures.
- Affichage des risques spécifiques dans les matrices.
- Possibilité de surcharger la gravité d'un risque général V2.
- Ajout d'une indication de fichier généré lors de la sélection des vecteurs et des matrices.
- Amélioration de l'affichage des entités et des utilisateurs administrés dans l'interface d'administration.
- Ajout d'une page dédiée à la gestion des administrateurs supervisés par un superviseur.
- Affichage d'une alerte lors de l'attribution d'un rôle à un utilisateur.
- Ajout d'un bandeau d'information remplaçant l'ancien, utilisant des tuiles DSFR.

### Évolutions techniques
- Migration vers les composants DSFR pour l'interface utilisateur : amélioration de l'accessibilité et de la cohérence visuelle (tableaux, boutons, liens, etc.).
- Refonte de la gestion des configurations de risques.
- Amélioration de la gestion des événements et des journaux d'audit.
- Mise à jour des dépendances : plusieurs dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.
- Amélioration de la configuration et des tests d'accessibilité.
- Utilisation d'un singleton pour la connexion Knex.
- Ajout de tests d'accessibilité pour les pages d'administration et les tiroirs.
- Suppression de code obsolète et factorisation du code.
- Amélioration de la gestion des secrets et des configurations.
- Ajout d'un script pour faciliter la mise à jour de l'UI Kit.

### Autres changements
- Ajout d'un fichier `robots.txt` pour améliorer le référencement.
- Ajout d'un sitemap pour faciliter l'indexation par les moteurs de recherche.
- Ajout de documentation et de commentaires pour améliorer la maintenabilité du code.
- Corrections de typos et d'erreurs de style.
- Amélioration des messages d'erreur et des notifications.
- Ajout de badges "bêta" pour les nouvelles fonctionnalités en phase de test.
- Ajout de tests unitaires et d'intégration.
