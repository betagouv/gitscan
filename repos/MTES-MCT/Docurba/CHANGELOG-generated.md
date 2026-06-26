## Changelog : Docurba (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, Docurba a bénéficié d'améliorations significatives tant au niveau de l'interface utilisateur (Nuxt) que du backend (Django). Les modifications incluent une meilleure gestion des événements et des procédures, des optimisations de l'administration, et une refonte de l'authentification avec l'intégration de Supabase. Des améliorations de performance et de sécurité ont également été apportées.

### Évolutions fonctionnelles
- L'affichage des dates de procédure a été ajouté sur les pages des procédures et des collectivités. [#3319000](https://github.com/MTES-MCT/Docurba/issues/3319000)
- L'ID de la procédure est maintenant affiché dans l'onglet Procédures et Validations.
- Amélioration de l'affichage sur les écrans étroits pour la page "Mes collectivités". [#acca044](https://github.com/MTES-MCT/Docurba/issues/acca044)
- Possibilité de modifier les événements depuis l'interface d'administration.
- Ajout de la possibilité de rechercher des événements de prescription.
- Les événements liés à un lancement de procédure utilisent maintenant le nom et l'email de l'utilisateur comme auteur lors de la mise à jour du PAC.
- Amélioration de la détection des événements de lancement et message d'erreur plus clair.
- Les événements sont maintenant liés à un projet.
- Possibilité de filtrer les collectivités par département, région et type via une nouvelle API interne.
- Pagination des résultats de l'API interne pour les collectivités.
- Ajout de catégories PAC.
- Ajout d'une catégorie d'événement.
- L'interface d'administration permet maintenant de rechercher des utilisateurs par email et de mettre à jour leur mot de passe.
- Les procédures peuvent être listées en fonction des communes incluses dans leur périmètre.
- Amélioration de l'affichage des événements sur la page des procédures.

### Évolutions techniques
- Intégration de Supabase pour l'authentification et la gestion des sessions.
- Refonte de l'authentification avec ajout de la gestion des sessions et du header Supabase-Authorization.
- Remplacement de `wget` par `curl` dans les scripts.
- Utilisation de Nginx pour servir les fichiers statiques et suppression de la dépendance `whitenoise`.
- Configuration de Nginx pour limiter le taux de requêtes (rate limiting).
- Suppression de la dépendance `django-revproxy`.
- Amélioration des tests Django : ajout d'un client staff, regroupement des tests par modèle, et amélioration des performances.
- Harmonisation de la gestion des paramètres de requête dupliqués dans l'API interne.
- Suppression de paramètres obsolètes et de code commenté.
- Mise à jour de plusieurs dépendances : `pytest`, `ruff`, `cryptography`, `pyjwt`, `django-filter`, `supabase`, `django`.
- Amélioration de l'intégration de `pg_history` pour la traçabilité des modifications.
- Utilisation de `format_html` pour des raisons de sécurité dans l'administration Django.
- Amélioration de la gestion des variables d'environnement pour l'URL de l'API.
- Utilisation de l'API Django pour récupérer les procédures et les collectivités au lieu de l'API Node.

### Autres changements
- Ajout d'une alerte Slack lors du lancement d'un déploiement.
- Ajout d'un champ `last_sign_in_at` au modèle User.
- Documentation et commentaires améliorés.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout d'un champ `owner_id` au modèle Procedure.
- Historisation de toutes les modifications d'événement.
- Limitation des champs envoyés dans les payloads des webhooks.
- Correction de la configuration des templates.
- Suppression de la vue publique `collectivite-detail`.
- Amélioration de la configuration des applications de revue (review apps).
- Ajout de la gestion des événements non gérés par Sudocuh.
- Ajout d'une vérification quotidienne des mises à jour des dépendances.
