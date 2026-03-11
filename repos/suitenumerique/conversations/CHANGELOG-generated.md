## Changelog : conversations (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à Conversations au cours du dernier mois. Les utilisateurs bénéficieront d'une meilleure expérience grâce à des corrections de bugs, notamment en mode sombre et dans l'affichage des formules mathématiques. Des options de personnalisation ont été ajoutées, comme la possibilité de désactiver la recherche internet automatique. Des optimisations techniques ont également été réalisées pour améliorer la performance et la maintenabilité du code.

### Évolutions fonctionnelles
- Possibilité de désactiver la recherche internet automatique pour l'utilisateur [#4545083](https://github.com/suitenumerique/conversations/commit/4545083)
- Le "waffle" (élément d'interface spécifique) est maintenant masqué si le thème n'est pas français [#96a2963](https://github.com/suitenumerique/conversations/commit/96a2963)
- Correction de l'affichage des messages en mode sombre [#2b81234](https://github.com/suitenumerique/conversations/commit/2b81234)
- Correction de l'affichage des formules mathématiques et des traductions dans la carrousel [#09dceb5](https://github.com/suitenumerique/conversations/commit/09dceb5)
- Gestion des majuscules/minuscules ignorée lors de la bascule vers l'adresse email dans l'authentification OIDC [#3c3eaf3](https://github.com/suitenumerique/conversations/commit/3c3eaf3)
- Correction du type MIME pour les fichiers PPTX [#1088d88](https://github.com/suitenumerique/conversations/commit/1088d88)

### Évolutions techniques
- Refactorisation du service `AIAgentService` pour une meilleure lisibilité et maintenabilité [#ba712af](https://github.com/suitenumerique/conversations/commit/ba712af)
- Mise à jour de plusieurs dépendances : `django-pydantic-field`, `pypdf`, `pillow`, `pydantic-ai` [#8feed1e, #61f86e1, #224e6f8](https://github.com/suitenumerique/conversations/commit/8feed1e, https://github.com/suitenumerique/conversations/commit/61f86e1, https://github.com/suitenumerique/conversations/commit/224e6f8)
- Migration de ESLint vers la version 9 avec une configuration "flat" [#9935335](https://github.com/suitenumerique/conversations/commit/9935335)
- Optimisation du rendu Markdown en streaming grâce à la division en blocs [#af6facf](https://github.com/suitenumerique/conversations/commit/af6facf)
- Utilisation de `uv` au lieu de `pip` pour Crowdin [#e925bff](https://github.com/suitenumerique/conversations/commit/e925bff)
- Inversion de liveness et readiness pour le déploiement backend avec Helm [#e60c938](https://github.com/suitenumerique/conversations/commit/e60c938)
- Vendorisation du fichier `mime.types` pour éviter de le récupérer depuis un serveur Apache distant [#63e0e6c](https://github.com/suitenumerique/conversations/commit/63e0e6c)

### Autres changements
- Mise à jour des chaînes de caractères traduites [#a919d9a](https://github.com/suitenumerique/conversations/commit/a919d9a)
- Bump de la version vers 0.0.13 [#9506df3](https://github.com/suitenumerique/conversations/commit/9506df3)
