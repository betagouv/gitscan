## Changelog : conversations (30 derniers jours, au 21 septembre 2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes avec l'ajout de nouvelles capacités, notamment un connecteur pour data.gouv et un outil de génération de présentations. L'expérience utilisateur a été considérablement fluidifiée, particulièrement lors des échanges avec l'IA, tandis que la robustesse technique a été renforcée par une mise à jour majeure de l'infrastructure IA et l'implémentation de nouveaux outils d'évaluation de la qualité des réponses.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** :
    - Ajout d'un connecteur pour les données de data.gouv.
    - Introduction d'un outil de génération de présentations (slide decks).
- **Interface utilisateur (UI/UX)** :
    - Refonte de la zone de saisie avec un nouveau menu déroulant "+" pour les actions.
    - Amélioration de la fluidité du chat : meilleure gestion de l'affichage des questions pendant le streaming de la réponse et gestion plus intuitive des erreurs de saisie ou de l'historique.
    - Ajout de messages d'information pour expliquer les délais en cas de limitation de débit (rate limiting).
- **Administration** :
    - Amélioration de la gestion des conversations : affichage de leur taille et augmentation du nombre de conversations visibles par page pour faciliter les actions groupées.

### Évolutions techniques
- **Intelligence Artificielle** :
    - Migration vers la version 5 du Vercel AI SDK et mise à jour du format de stockage des messages.
    - Mise en place d'un nouveau framework d'évaluation comportementale pour tester la fiabilité des réponses de l'IA.
- **Sécurité et Performance** :
    - Implémentation de limitations de débit (throttling) sur la création de projets et de conversations pour protéger le système.
    - Optimisation des requêtes de la liste des projets pour garantir un ordre de tri stable.
- **Infrastructure et CI/CD** :
    - Audit de sécurité des workflows GitHub Actions.
    - Optimisation de la CI : correction des vérifications de changelog et modification de la source des images MinIO.
    - Résolution de problèmes liés à l'environnement de développement (Vite/Dev Container).

### Autres changements
- **Documentation** : Refonte de la procédure de release et documentation des paramètres de limitation de débit de l'API.
- **Internationalisation** : Mise à jour des chaînes de traduction ([#717](https://github.com/suitenumerique/conversations/pull/717), [#711](https://github.com/suitenumerique/conversations/pull/711)).
