## Changelog : conversations (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse du système, la surveillance de la santé des modèles d'IA, et l'expérience utilisateur. Des correctifs ont été apportés pour améliorer la stabilité, notamment en lien avec la gestion des pods et la configuration des dépendances. L'interface utilisateur a été améliorée avec de nouvelles fonctionnalités comme le mode maintenance et des indicateurs de santé des modèles.

### Évolutions fonctionnelles
- Ajout d'un mode maintenance pour permettre des opérations de maintenance planifiées.
- Affichage d'indicateurs de santé dynamiques pour les assistants IA, informant l'utilisateur de leur disponibilité.
- Amélioration du filtrage et de l'affichage des conversations dans l'interface d'administration.
- Possibilité de continuer à taper pendant que l'IA génère une réponse.
- Affichage d'un message d'erreur spécifique lorsque le fournisseur de LLM est indisponible.
- Amélioration de la gestion des fichiers et de la recherche documentaire.
- Ajout d'un menu déroulant pour l'aide à la place du bouton d'aide précédent.
- Possibilité d'éditer le statut de santé des modèles directement dans l'interface d'administration.

### Évolutions techniques
- Mise en place d'un système de surveillance de la santé des modèles Albert via un job Cron et une intégration Helm.
- Refonte de la gestion des collections de données pour optimiser les performances (désindexation des collections inactives et réindexation à la demande).
- Implémentation d'un système de limitation du débit (rate limiting) basé sur la santé du modèle.
- Amélioration de la gestion des erreurs et des redirections OIDC pour éviter les fuites d'informations sensibles.
- Mise à jour des dépendances du backend et du frontend.
- Optimisation de la gestion des pods Helm pour éviter les conflits de disruption budget.
- Renommage du statut "orange" de santé du modèle en "yellow" pour plus de clarté.
- Ajout d'un processeur d'historique à fenêtre glissante pour améliorer la gestion du contexte des conversations.
- Suppression du point de terminaison de liste d'utilisateurs pour des raisons de sécurité.

### Autres changements
- Mise à jour des chaînes de caractères pour la traduction (i18n).
- Amélioration de la documentation et des tests unitaires.
- Correction de problèmes de style et de mise en page dans l'interface utilisateur.
- Désactivation des scripts d'installation Yarn dans les builds Docker pour plus de sécurité.
- Correction de la langue par défaut de l'interface utilisateur lors du premier chargement.
- Amélioration de l'instruction pour éviter les hallucinations d'URL.
- Correction de bugs liés à l'ouverture de liens dans de nouveaux onglets.
- Correction d'un crash lié au streaming avec les APIs compatibles OpenAI.
