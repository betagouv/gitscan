## Changelog : conversations (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à Conversations au cours des 30 derniers jours. Les principales évolutions concernent l'expérience utilisateur avec l'ajout d'une recherche améliorée, la possibilité de désactiver la recherche internet automatique et des corrections de bugs liés à l'interface et au mode sombre. Des optimisations techniques et des mises à jour de dépendances ont également été réalisées.

### Évolutions fonctionnelles
- Ajout d'une recherche avec une modale dédiée et une meilleure expérience utilisateur. [#1234](https://github.com/suitenumerique/conversations/issues/1234)
- Possibilité pour l'utilisateur de désactiver la recherche internet automatique.
- Correction de l'affichage inversé des messages toast pour les bascules de paramètres.
- Correction du style du mode sombre sur les messages du chat.
- Amélioration de la gestion des cas d'insensibilité lors de la restauration sur l'adresse email pour l'authentification OIDC.
- Masquage du "waffle" (fonctionnalité expérimentale) si le thème n'est pas français.

### Évolutions techniques
- Mise à jour de Django et de Pydantic.
- Migration de ESLint vers la version 9 avec une configuration "flat".
- Refactorisation du service `AIAgentService` pour une meilleure lisibilité et maintenabilité.
- Optimisation du rendu Markdown en streaming avec une division en blocs pour améliorer la performance.
- Utilisation de `uv` au lieu de `pip` pour Crowdin.
- Inversion des probes liveness et readiness pour le déploiement backend avec Helm.
- Mise à jour de Pydantic AI.
- Mise à jour de Pillow et django-pydantic-field.

### Autres changements
- Mise à jour des chaînes de traduction (i18n).
- Correction du type MIME pour les fichiers PPTX.
- Ajustement temporaire du tableau (array).
- Correction d'un bug lié à l'affichage des formules mathématiques et des traductions de la carrousel.
