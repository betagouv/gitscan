## Changelog : conversations (30 derniers jours, au 10 septembre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec l'amélioration de l'expérience de chat et l'ajout de nouveaux outils, comme la génération de présentations et un panneau de sources pour plus de transparence. Nous avons également renforcé la robustesse technique du système, notamment via une mise à jour majeure de la gestion de l'IA et une optimisation des processus de test et de sécurité.

### Évolutions fonctionnelles
- **Nouveaux outils et fonctionnalités** :
    - Ajout d'un outil de génération de présentations (slide decks).
    - Introduction d'un panneau de sources pour améliorer la transparence des réponses de l'IA.
    - Amélioration des capacités de l'assistant DINUM via l'optimisation des instructions (prompts).
- **Amélioration de l'expérience utilisateur (UX)** :
    - Optimisation de l'interface de chat : meilleure gestion du streaming des réponses, prévention des doubles envois de messages et gestion plus fluide des erreurs de chargement de l'historique.
    - Ajout d'explications claires pour l'utilisateur lorsqu'une limite de création est atteinte.
    - Suppression de la page et de la barrière du code d'activation.
- **Administration et Analytics** :
    - Amélioration de la gestion administrative : affichage de la taille des conversations et augmentation du nombre d'éléments par page pour les actions groupées.
    - Mise en place du suivi analytique (projets, export de documents, résumé et empreinte CO2).

### Évolutions techniques
- **Intelligence Artificielle** :
    - Migration vers le Vercel AI SDK v5 et mise à jour du format de stockage des messages.
    - Mise en place d'un nouveau framework d'évaluation comportementale pour tester la qualité des réponses de l'IA.
- **Infrastructure et CI/CD** :
    - Optimisation des tests E2E : parallélisation des tests sur plusieurs navigateurs et réduction du temps de build.
    - Renforcement de la sécurité de la chaîne d'approvisionnement par le verrouillage des versions des actions GitHub.
    - Audit de sécurité des workflows GitHub Actions.
- **Backend et Performance** :
    - Renforcement de la sécurité via l'implémentation de limitations de débit (throttling) sur la création de projets et de conversations.
    - Refactorisation du code : passage à `httpx` comme client HTTP unique et restructuration du module de configuration.
    - Correction de bruits de logs sous ASGI et résolution de problèmes de démarrage de l'environnement de développement (Vite).

### Autres changements
- **Internationalisation** : Mise à jour des chaînes de traduction ([#717](https://github.com/suitenumerique/conversations/pull/717), [#711](https://github.com/suitenumerique/conversations/pull/711)).
- **Documentation** : Refonte de la procédure de release et documentation des paramètres de limitation de débit de l'API.
