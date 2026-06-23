## Changelog : conversations (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse du système, la gestion de la santé des modèles d'IA, l'expérience utilisateur et la sécurité. Des indicateurs de santé des modèles sont désormais disponibles, des erreurs sont mieux gérées et affichées, et l'accès est plus finement contrôlé. L'interface utilisateur a également été améliorée avec des ajustements visuels et fonctionnels.

### Évolutions fonctionnelles
- Affichage d'une erreur spécifique lorsque l'analyse d'un document échoue [#2ffffae](https://github.com/suitenumerique/conversations/commit/2ffffae)
- Affichage d'une erreur spécifique lorsque le fournisseur LLM est indisponible.
- Indication de la taille maximale des pièces jointes en cas d'échec de l'upload.
- Ajout d'un mode maintenance pour la plateforme.
- Amélioration du filtrage et de l'affichage des chats dans l'interface d'administration [#db7bf6d](https://github.com/suitenumerique/conversations/commit/db7bf6d)
- Nouvelle interface de gestion des paramètres (settings modal) avec une taille ajustée.
- Possibilité d'éditer le statut de santé des modèles depuis l'interface d'administration.
- Ajout de bannières dynamiques indiquant l'état de santé des assistants IA.
- Menu déroulant remplaçant le bouton d'aide sur l'onboarding.

### Évolutions techniques
- Implémentation d'un système de limitation du débit (rate limiting) basé sur l'état de santé du modèle.
- Ajout d'un processeur d'historique en fenêtre glissante (sliding window history processor) pour améliorer les performances.
- Mise en place d'un job Cron pour surveiller l'état de santé des modèles Albert et l'intégrer dans l'application.
- Refactorisation de la gestion des statuts de santé des modèles (renommage de "orange" en "yellow").
- Amélioration de la gestion des pods Helm pour éviter les conflits avec le budget de perturbation du backend.
- Mise à jour des dépendances backend et frontend.
- Amélioration de la sécurité avec l'ajout d'un filtrage d'accès basé sur les rôles avec une liste de contournement.
- Correction d'une fuite d'informations de port interne lors des redirections OIDC.
- Suppression du point de terminaison de la liste des utilisateurs (user list endpoint).
- Correction d'un bug empêchant l'ouverture des liens sources dans un nouvel onglet.

### Autres changements
- Mise à jour des chaînes de traduction (i18n).
- Mise à jour de la documentation.
- Mise à jour de la version du chart Helm à v0.0.6.
- Désactivation des scripts d'installation Yarn dans le build Docker pour renforcer la sécurité.
- Correction de l'affichage de la langue du navigateur lors du premier chargement de l'interface utilisateur.
- Correction de la mise en page et de l'apparence de certains éléments de l'interface utilisateur.
- Suppression de l'instruction `prevent_url_hallucination` dans l'agent de conversation.
- Amélioration de la gestion des fichiers de projet pour la recherche RAG.
- Ajout de la possibilité de configurer des bannières avec différents niveaux, titres et contenus.
