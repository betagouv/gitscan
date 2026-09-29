## Changelog : conversations (30 derniers jours, au 28 septembre 2026)

### Résumé
Ce mois-ci, Conversations s'enrichit de nouveaux outils puissants (recherche web, génération de présentations, connecteur data.gouv) et améliore significativement la fluidité de l'interface de chat. Le projet renforce également sa robustesse technique via une mise à jour majeure de son SDK d'IA et l'implémentation de nouveaux cadres d'évaluation pour garantir la qualité des réponses.

### Évolutions fonctionnelles
- **Nouveaux outils IA** : ajout de la recherche web via Staan, de la génération de présentations (slide decks) et d'un connecteur pour data.gouv.
- **Amélioration de l'interface (UI/UX)** : remplacement des actions d'entrée par un menu déroulant "+", affichage de la taille des conversations dans l'administration, et meilleure gestion visuelle du streaming des réponses.
- **Fiabilité du chat** : corrections sur la gestion de l'historique, la prévention des doubles envois et la reprise après échec de connexion.
- **Gestion de l'usage** : introduction de limitations de débit (throttling) pour la création de projets et de conversations, avec des messages d'information pour l'utilisateur en cas de limite atteinte.

### Évolutions techniques
- **Mise à jour majeure** : migration vers le SDK Vercel AI v5 et adaptation du format de stockage des messages.
- **Tests et évaluation** : déploiement d'un nouveau framework d'évaluation comportementale pour mesurer la qualité des réponses de l'IA.
- **Infrastructure et CI/CD** : remplacement de MinIO par RustFS pour le développement local et la CI, optimisation des images de conteneurs et audit de sécurité des workflows GitHub Actions.
- **Optimisations backend** : refactorisation du module de configuration et amélioration de la stabilité des requêtes de listes.

### Autres changements
- **Documentation** : révision de la procédure de publication des versions (release).
- **Internationalisation** : mises à jour des traductions ([#717](https://github.com/suitenumerique/conversations/pull/717), [#711](https://github.com/suitenumerique/conversations/pull/711)).
