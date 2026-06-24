## Changelog : Docurba (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Docurba se concentrent sur l'amélioration de l'administration des données, notamment des procédures, des événements et des utilisateurs. Des corrections et des améliorations ont été apportées à l'interface utilisateur Nuxt3, ainsi que des optimisations techniques pour la sécurité et la performance. L'authentification via Supabase a été implémentée.

### Évolutions fonctionnelles
- Ajout de l'ID de la procédure dans l'onglet Procédures et Validations.
- Amélioration de la recherche et de la sélection des événements, notamment en affichant si une procédure est antérieure ou postérieure à la loi Huwart.
- Possibilité de mettre à jour les événements directement depuis la page de la procédure.
- Ajout de la possibilité de rechercher des utilisateurs par email dans l'interface d'administration Django.
- Mise à jour du mot de passe utilisateur via l'interface d'administration Django.
- Liste des procédures incluant la commune courante dans l'interface d'administration Django.
- Historisation de toutes les modifications d'événements.
- Limitation des champs envoyés dans les payloads des webhooks pour optimiser les performances.
- Ajout d'une alerte Slack lors du lancement d'un déploiement.
- Amélioration de la détection des événements de lancement et des messages d'erreur associés.
- Ajout d'un champ `last_sign_in_at` au modèle User.
- Implémentation de l'authentification via Supabase.

### Évolutions techniques
- Refactorisation des tests Django pour une meilleure organisation et couverture.
- Mise à jour des dépendances : pytest, ruff, cryptography, pyjwt, django-filter, supabase, django.
- Amélioration de la configuration des templates.
- Suppression de dépendances obsolètes (whitenoise, django-revproxy).
- Utilisation de Nginx pour servir les fichiers statiques et mise en place d'un rate limiting.
- Utilisation de curl au lieu de wget.
- Mise en place d'un pipeline CI/CD plus robuste avec une vérification quotidienne des mises à jour des dépendances.
- Utilisation de l'API Django pour récupérer les procédures et collectivités dans Nuxt3.
- Correction de problèmes liés à la configuration CORS en environnement local.
- Amélioration de la performance des requêtes et des modèles Django.

### Autres changements
- Documentation mise à jour.
- Nettoyage du code et suppression de code commenté.
- Ajout de commentaires pour améliorer la lisibilité du code.
- Configuration de l'URL de l'API Docurba via une variable d'environnement.
- Ajout de nouvelles catégories de PAC (Prescription, Autorisation de Construire).
- Ajout d'une nouvelle catégorie d'événements.
- Amélioration de l'intégration de pg_history.
- Ajout de commentaires et de documentation pour les nouvelles fonctionnalités.
- Correction de bugs mineurs et améliorations de la stabilité.
