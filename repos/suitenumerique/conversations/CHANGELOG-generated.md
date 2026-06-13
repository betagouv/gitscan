## Changelog : conversations (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité, la surveillance de la santé des modèles d'IA, l'expérience utilisateur et la sécurité. Des indicateurs de santé des modèles sont désormais disponibles, des corrections de bugs améliorent la fiabilité, et des ajustements de l'interface utilisateur rendent l'application plus intuitive. Des améliorations de sécurité ont également été apportées pour restreindre l'accès et protéger les données.

### Évolutions fonctionnelles
- Ajout d'une bannière dynamique affichant l'état de santé des assistants IA. [#1234](https://github.com/suitenumerique/conversations/issues/1234)
- Possibilité de taper pendant que l'IA génère une réponse.
- Mode maintenance configurable pour l'application.
- Amélioration du filtrage et de l'affichage des conversations dans l'administration.
- Affichage d'un message d'erreur spécifique lorsque le fournisseur de LLM est indisponible.
- Remplacement du bouton d'aide par un menu déroulant pour une meilleure organisation.
- La taille maximale des pièces jointes est maintenant affichée en cas d'échec de l'upload.

### Évolutions techniques
- Implémentation d'un système de surveillance de la santé des modèles Albert via une tâche Cron et une intégration Helm.
- Refonte de la gestion des collections de données, avec désindexation des collections inactives et réindexation lors des conversations.
- Ajout d'un "sliding window history processor" pour la gestion de l'historique des conversations.
- Mise en place d'un refroidissement (cooldown) du taux de requêtes basé sur l'état de santé du modèle.
- Amélioration de la sécurité avec un filtrage d'accès basé sur les rôles et une liste de contournement.
- Correction d'un problème de redirection OIDC qui exposait le port interne.
- Suppression du point de terminaison de la liste des utilisateurs.
- Amélioration de l'instruction pour éviter les hallucinations d'URL.
- Correction d'un bug empêchant l'arrêt correct des pods lors de la maintenance.

### Autres changements
- Mise à jour des traductions.
- Mise à jour des dépendances du backend et du frontend.
- Désactivation des scripts d'installation Yarn dans les builds Docker pour des raisons de sécurité.
- Amélioration de la documentation et des tests.
- Correction de problèmes d'affichage et de style dans l'interface utilisateur.
- Ajustement de la taille de la fenêtre modale des paramètres.
- Correction du comportement de l'application lors du chargement initial, en utilisant la langue du navigateur.
- Restriction de l'outil d'auto-documentation aux questions concernant les métadonnées.
