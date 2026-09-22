## Changelog : conversations (30 derniers jours, au 21 septembre 2026)

### Résumé
Ce mois-ci, conversations a considérablement enrichi ses capacités avec l'arrivée d'un connecteur data.gouv et d'un outil de génération de présentations. L'expérience de chat a été stabilisée pour offrir une interaction plus fluide, tandis que l'infrastructure de test et de déploiement a été renforcée pour garantir une meilleure fiabilité et sécurité des réponses de l'IA.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** : ajout d'un connecteur pour data.gouv et d'un outil de génération de présentations (slide decks).
- **Amélioration de l'interface utilisateur** :
    - Nouveau menu déroulant "+" pour les actions de saisie.
    - Interface d'administration optimisée (affichage de la taille des conversations et augmentation du nombre d'éléments par page).
    - Suppression de la barrière du code d'activation pour simplifier l'accès.
- **Expérience de chat améliorée** :
    - Meilleure gestion de la stabilité (prévention des doubles envois, gestion robuste de l'historique et des échecs de chargement).
    - Fluidité visuelle accrue lors du streaming des réponses.
    - Messages d'explication clairs lorsqu'une limite de création est atteinte.
- **Corrections** : résolution de problèmes d'affichage liés aux traductions.

### Évolutions techniques
- **Intelligence Artificielle** : migration vers le SDK Vercel AI v5 et mise à jour du format de stockage des messages en conséquence.
- **Qualité et Tests** :
    - Implémentation d'un framework d'évaluation comportementale pour mesurer la qualité des réponses de l'IA.
    - Optimisation de la CI/CD avec la parallélisation et le découpage (sharding) des tests E2E.
- **Sécurité et Performance** :
    - Mise en place de limitations de débit (throttling) pour la création de projets et de conversations.
    - Sécurisation des workflows GitHub Actions contre les risques de corruption de la chaîne d'approvisionnement.
    - Optimisation des requêtes de la liste des projets pour garantir un tri stable.
- **Maintenance** : refactoring du module de configuration et nettoyage des logs (ASGI).

### Autres changements
- **Internationalisation** : mises à jour des chaînes de traduction ([#717](https://github.com/suitenumerique/conversations/pull/717), [#711](https://github.com/suitenumerique/conversations/pull/711)).
- **Documentation** : révision de la procédure de release et de la documentation des paramètres de limitation de l'API.
