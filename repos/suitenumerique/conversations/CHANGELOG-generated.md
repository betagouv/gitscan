## Changelog : conversations (30 derniers jours, au 29 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse et la surveillance de la santé des modèles d'IA, l'amélioration de l'expérience utilisateur avec des messages d'erreur plus clairs et une interface plus conviviale, ainsi que des optimisations techniques pour la gestion des tâches en arrière-plan et l'indexation des documents. Des améliorations de sécurité et de gestion des accès ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un mode maintenance pour la plateforme.
- Affichage de messages d'erreur plus spécifiques en cas de problème avec le fournisseur de LLM ou lors de l'analyse de documents.
- Amélioration de l'interface utilisateur :
    - Le bouton d'aide a été remplacé par un menu déroulant.
    - Le nom par défaut du produit est maintenant "L'Assistant".
    - Amélioration de la taille de la fenêtre modale des paramètres.
    - Utilisation d'une couleur d'avertissement sémantique pour l'icône de la bannière.
- Amélioration du filtrage et de l'affichage des chats dans l'administration.
- Possibilité de modifier le statut de santé du modèle directement dans l'interface d'administration.
- Affichage de la taille maximale des pièces jointes en cas d'échec du téléchargement.

### Évolutions techniques
- Mise en place de Celery pour la gestion des tâches asynchrones, incluant le déploiement des workers et beat via Helm.
- Ajout d'un mécanisme de fallback pour les modèles.
- Implémentation d'un système de surveillance de la santé des modèles Albert avec un job Cron et une intégration dans l'interface utilisateur.
- Refonte de la gestion des rôles et des accès avec une liste de contournement pour une flexibilité accrue.
- Mise à jour de la version de Python à 3.14 et des dépendances.
- Ajout d'un processeur d'historique à fenêtre glissante pour le backend.
- Suppression de l'endpoint de liste des utilisateurs.
- Amélioration de la gestion de l'indexation des documents :
    - Désindexation des collections inactives et réindexation dans les conversations.
    - Gestion des erreurs 404 lors de la suppression comme succès de désindexation.
- Ajout d'un cooldown basé sur la santé du modèle pour limiter le taux de requêtes.
- Correction d'un problème de redirection OIDC qui exposait le port interne.

### Autres changements
- Mise à jour des chaînes de traduction.
- Bump de la version à 0.0.19 et 0.0.18.
- Amélioration de la configuration du chart Helm.
- Correction de problèmes liés aux pods de job et au budget de perturbation du backend.
- Correction de l'utilisation de la langue du navigateur pour l'interface utilisateur par défaut.
