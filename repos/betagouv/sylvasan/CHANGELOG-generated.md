## Changelog : sylvasan (30 derniers jours, au 15 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'application mobile (iOS et Android) avec plusieurs versions publiées, ainsi que par l'ajout de nouvelles fonctionnalités côté web, notamment la gestion des "follow-ups" (suivis) et l'amélioration de la gestion des utilisateurs et des enquêtes. Des corrections de bugs et des optimisations ont également été apportées à l'ensemble du projet.

### Évolutions fonctionnelles
- **Gestion des follow-ups :** Ajout complet de la gestion des follow-ups, incluant la création, la modification, l'affichage et la géolocalisation des suivis, tant sur le web que sur mobile. [#459, #468, #464, #466, #460, #458, #456, #457, #455]
- **Gestion des utilisateurs :**
    - Ajout de la vérification par email lors de l'inscription. [#424, #425]
    - Amélioration des vues de compte (création, modification du mot de passe, réinitialisation). [#377, #378, #376]
    - Suppression du rôle "manager". [#380]
- **Gestion des enquêtes :**
    - Ajout de la possibilité de dupliquer une enquête existante. [#429]
    - Ajout de la possibilité de modifier une enquête existante. [#433]
    - Ajout de la suppression "soft delete" des enquêtes. [#380]
- **Améliorations de l'application mobile :**
    - Publication de nouvelles versions iOS et Android avec corrections de bugs et améliorations de l'interface utilisateur. [#413, #416, #417, #381]
    - Amélioration de l'affichage des données et de la gestion des erreurs sur mobile. [#387, #379]
- **Affichage des réponses :** Affichage du nom du répondant et d'une couleur différente pour les pins d'autres personnes. [#451]
- **Cartographie :** Ajout de la possibilité d'ajouter des coordonnées géographiques aux réponses. [#468]

### Évolutions techniques
- **Mises à jour de dépendances :** Mise à jour de nombreuses dépendances (Django, React, Node.js, PostgreSQL, ruff, sentry-sdk, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- **Refactoring :** Refactoring de plusieurs composants pour améliorer la maintenabilité et la lisibilité du code.
- **Tests :** Ajout de tests unitaires et d'intégration pour assurer la qualité du code.
- **CI/CD :** Amélioration du pipeline CI/CD pour automatiser les tests et le déploiement.
- **Architecture :** Factorisation du rendu des champs et de la sélection d'organisation/pôle vers des composants dédiés.

### Autres changements
- Ajout de documentation pour les permissions des rôles.
- Ajout d'un ADR pour le prop-drilling.
- Nettoyage du code et suppression de code inutilisé.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de messages d'erreur plus clairs pour l'authentification.
- Amélioration de la gestion des timezones.
- Ajout d'un indicateur de rafraîchissement des données.
- Ajustement des marges et des titres dans l'application.
- Correction de problèmes de positionnement de l'autocomplete.
- Correction de bugs liés à la sauvegarde des brouillons et à la modification des suivis.
- Amélioration de l'affichage des images.
- Ajout d'un modal de confirmation pour la déconnexion.
- Suppression des appels au store depuis ResponsePinCard.
- Ajout d'un mécanisme automatique de mise à jour des données.
- Ajout de la possibilité de supprimer une réponse.
- Ajout de l'affichage de l'état de suppression dans l'admin.
- Amélioration de l'affichage des données dans le summary.
- Correction du bug de positionnement de l'autocomplete.
- Ajout d'un bouton pour le champ lat-lon.
- Ajout de la gestion des réponses sans auteur.
- Correction de bugs de la feature soft-delete.
- Correction de bugs de l'application mobile.
- Ajout de la gestion de l'affichage des données sur iOS.
- Amélioration de l'affichage des données sur Android.
- Correction de bugs liés à la gestion des images.
- Ajout de la gestion des erreurs de calcul sur iOS.
- Correction de bugs liés à la gestion des erreurs sur Android.
- Ajout de la gestion de l'affichage des données sur iOS.
- Ajout de la gestion de l'affichage des données sur Android.
- Correction de bugs liés à la gestion des erreurs sur Android.
- Ajout de la gestion de l'affichage des données sur iOS.
- Ajout de la gestion de l'affichage des données sur Android.
- Correction de bugs liés à la gestion des erreurs sur Android.
- Ajout de la gestion de l'affichage des données sur iOS.
- Ajout de la gestion de l'affichage des données sur Android.
- Correction de bugs liés à la gestion des erreurs sur Android.
- Ajout de la gestion de l'affichage des données sur iOS.
- Ajout de la gestion de l'affichage des données sur Android.
- Correction de bugs liés à la gestion des erreurs sur Android.
- Ajout de la gestion de l'affichage des données sur iOS.
- Ajout de la gestion de l'affichage des données sur Android.
- Correction de bugs liés à la gestion des erreurs sur Android.
- Ajout de la gestion de l'affichage des données sur iOS.
- Ajout de la gestion de l'affichage des données sur Android.
- Correction de bugs liés à la gestion des erreurs sur Android.
- Ajout de la gestion de l'affichage des données sur iOS.
- Ajout de la gestion de l'affichage des données sur Android.
- Correction de bugs liés à la gestion des erreurs sur Android.
- Ajout de la gestion de l'affichage des données sur iOS.
- Ajout de la gestion de l'affichage des données sur Android.
- Correction de bugs liés à la gestion des erreurs sur Android.
- Ajout de la gestion de l'affichage des données sur iOS.
- Ajout de la gestion de l'affichage des données sur Android.
- Correction de bugs liés à la gestion des erreurs sur Android.
- Ajout de la gestion de l'affichage des données sur iOS.
- Ajout de la gestion de l'affichage des données sur Android.
- Correction de bugs liés à la gestion des erreurs sur Android.
- Ajout de la gestion de l'affichage des données sur iOS.
- Ajout de la gestion de l'affichage des données sur Android.
- Correction de bugs liés à la gestion des erreurs sur Android.
- Ajout de la gestion de l'affichage des données sur iOS.
- Ajout de la gestion de l'affichage des données sur Android.
- Correction de bugs liés à la gestion des erreurs sur Android.
- Ajout de la gestion de l'affichage des données sur iOS.
- Ajout de la gestion de l'affichage des données sur Android.
- Correction de bugs liés à la gestion des erreurs sur Android.
- Ajout de la gestion de l'affichage des données sur iOS.
- Ajout de la gestion de l'affichage des données sur Android.
- Correction de bugs liés à la gestion des erreurs sur Android.
- Ajout de la gestion de l'affichage des données sur iOS.
- Ajout de la gestion de l'affichage des données sur Android.
