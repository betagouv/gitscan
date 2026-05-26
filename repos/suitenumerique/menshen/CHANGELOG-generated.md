## Changelog : menshen (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de l'expérience de développement et de la robustesse du projet. Des outils ont été ajoutés pour faciliter la mise en place et le test de l'application, notamment un playground et des vérifications de santé pour les conteneurs Docker. Des simplifications de configuration ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un "playground" pour faciliter l'exploration et le test de l'API.
- La création d'un superutilisateur se fait désormais via les variables d'environnement, simplifiant le processus de configuration.

### Évolutions techniques
- Ajout d'une vérification de santé (healthcheck) pour le service Docker, améliorant la résilience de l'application.
- Refonte de l'affichage de l'aide de la commande `make` pour une meilleure lisibilité.
- Renommage du service Docker en `menshen` pour plus de clarté.
- Suppression des paramètres liés à OIDC qui n'étaient plus utilisés.

### Autres changements
- Mise à jour des dépendances Docker (Keycloak, Python, UV, GitHub Actions) vers leurs dernières versions stables.
