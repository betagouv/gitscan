## Changelog : egapro (30 derniers jours, au 08 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur une mise en conformité majeure avec les normes d'accessibilité (RGAA) et une clarification globale des parcours de déclaration. La sécurité de l'interface d'administration a été renforcée, tandis que la précision des données exportées et la robustesse de l'infrastructure ont été améliorées pour offrir une expérience plus fiable aux entreprises et aux administrateurs.

### Évolutions fonctionnelles
- **Accessibilité (RGAA) :** Améliorations massives pour faciliter la navigation au clavier, la gestion du zoom (200%), la lecture des tableaux de données et l'annonce des messages de statut par les lecteurs d'écran.
- **Parcours de déclaration et CSE :** Clarification des libellés (effectifs, rémunérations, avis du CSE), gestion des erreurs de saisie non numériques et ajustement des règles d'affichage des indicateurs pour éviter les informations superflues.
- **Espace Utilisateur ("Mon espace") :** Mise à jour de l'interface avec de nouveaux badges de statut pour les déclarations, nettoyage des informations de profil et simplification de l'affichage des entreprises.
- **Administration et Export :** Ajout de filtres par tranche d'effectifs dans le tableau des déclarations [#4498] et amélioration de la précision des données exportées (API SUIT et fichiers), notamment sur les effectifs par quartile et les écarts de rémunération.
- **Aide et Notifications :** Mise à jour de la FAQ et suppression de liens vers des modèles ou fichiers indisponibles.

### Évolutions techniques
- **Sécurité :** Implémentation de la double authentification (2FA) pour l'accès à l'espace administrateur [#4482] et anonymisation des journaux d'activité utilisateur pour la conformité [#4526].
- **Infrastructure et CI/CD :** Sécurisation des emails d'administration via des *sealed-secrets* [#4705] et optimisation des tests de bout en bout (E2E) avec un parallélisme accru dans la CI [#4556].
- **Architecture et Refactoring :** Centralisation des routes statiques, des utilitaires de formatage et des schémas de validation (Zod) pour améliorer la maintenabilité. Uniformisation des scripts de projet en TypeScript.
- **API :** Optimisation des contrôles de verrouillage et amélioration de la couverture des routes auditées.

### Autres changements
- **Documentation :** Génération automatique de la documentation de l'API SUIT à partir du code [#4527].
- **Outils :** Ajout d'un kit de reprise de données (V1) pour faciliter les migrations [#4469].
