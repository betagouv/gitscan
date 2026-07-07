## Changelog : conversations (30 derniers jours, au 6 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité, la gestion de la santé des modèles d'IA, et l'expérience utilisateur. Des correctifs ont été apportés pour gérer les erreurs de chargement de documents, les problèmes d'authentification et l'affichage d'informations pertinentes sur l'état du système. L'interface utilisateur a également été améliorée avec des ajustements visuels et des messages d'erreur plus clairs.

### Évolutions fonctionnelles
- Amélioration de la gestion des erreurs lors de la suppression de documents, qui est maintenant considérée comme un succès même si un indexage échoue.
- Affichage d'un message d'erreur spécifique lorsque le fournisseur de LLM est indisponible.
- Affichage d'un message d'erreur spécifique lors d'échecs de parsing de documents.
- L'interface utilisateur permet maintenant de gérer les utilisateurs sans nom complet.
- Ajout de bannières dynamiques indiquant l'état de santé de l'assistant IA.
- Amélioration de l'expérience utilisateur avec un menu déroulant pour le bouton d'aide.
- L'application utilise maintenant la langue du navigateur pour l'interface utilisateur par défaut au premier chargement.
- Amélioration de l'affichage des erreurs lors du téléchargement de fichiers (limite de taille).

### Évolutions techniques
- Implémentation de tâches asynchrones avec Celery pour améliorer la performance et la réactivité.
- Ajout d'un mécanisme de fallback pour les modèles d'IA.
- Mise à jour de la version de Python à 3.14 et des dépendances.
- Refactorisation du module de vues de chat et utilisation de constantes partagées.
- Ajout d'un processeur d'historique à fenêtre glissante pour la gestion des conversations.
- Implémentation d'un refroidissement (cooldown) basé sur l'état de santé du modèle pour limiter le taux de requêtes.
- Ajout de filtres d'accès basés sur les rôles avec une liste de contournement.
- Modification du statut "orange" de la santé du modèle en "yellow".
- Ajout de la possibilité de modifier le statut de santé du modèle dans l'interface d'administration.
- Ajout d'un mécanisme de désindexation et de réindexation des collections inactives.

### Autres changements
- Mise à jour des chaînes de traduction.
- Mise à jour des logos et des icônes.
- Correction de liens brisés et amélioration de la cible des liens.
- Modification de l'illustration de la page 404.
- Bump de la version à 0.0.19.
