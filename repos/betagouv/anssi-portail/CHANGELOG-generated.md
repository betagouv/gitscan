## Changelog : anssi-portail (30 derniers jours, au 22/09/2026)

### Résumé
Ce mois a été marqué par une montée en puissance des outils interactifs avec le déploiement de la simulation "Réflexe Cyber" et d'une nouvelle série de "Mini-tests" (notamment un quiz Vrai/Faux). Parallèlement, le projet a franchi une étape technique majeure avec la migration de l'interface vers Svelte 5 et une modernisation complète de la suite de tests.

### Évolutions fonctionnelles
- **Réflexe Cyber** : Déploiement complet du parcours de simulation, incluant le choix des rôles et scénarios, le suivi du score en temps réel, un minuteur animé et l'envoi des résultats vers Mattermost.
- **Mini-tests** : Lancement d'un nouveau format de quiz (Vrai/Faux) avec affichage des scores, statistiques de réussite, estimation du temps de complétion et possibilité de partage social.
- **Test d'Exposition** : Amélioration de l'expérience utilisateur avec l'ajout d'une carte interactive, de résumés contextuels, de badges de progression et d'un système de collecte d'avis.
- **Comparateur de financements** : Ajout d'un nouvel outil permettant de comparer les aides disponibles et de générer des rapports de différences en Markdown.
- **Accessibilité & UX** : 
    - Suppression des animations non essentielles (confettis, animations de héros) pour améliorer l'accessibilité.
    - Optimisation de la navigation mobile et uniformisation des fils d'Ariane sur l'ensemble du site.
    - Amélioration de la visibilité des focus et des contrastes.
- **Sécurité** : Renforcement des processus d'authentification avec l'exigence du MFA (authentification multi-facteurs) et ajout de limites de débit (rate limiting) sur les routes de connexion.

### Évolutions techniques
- **Migration Svelte 5** : Refonte massive de la bibliothèque de composants pour migrer vers Svelte 5 et activation du mode "Runes" pour une meilleure gestion de la réactivité.
- **Modernisation des tests** : Migration complète de la suite de tests (backend, frontend et intégration) vers Vitest, incluant l'utilisation de mocks et d'assertions plus performantes.
- **Optimisation CI/CD & Infrastructure** : 
    - Amélioration des workflows GitHub Actions avec mise en cache des tests.
    - Stabilisation des déploiements sur CleverCloud via une gestion native de pnpm.
- **Refactoring & Performance** : 
    - Nettoyage approfondi du projet (suppression de composants, styles CSS, images et variables inutilisés).
    - Optimisation de la gestion des types avec Zod (passage de `z.infer` à `z.output`).
    - Restructuration des adaptateurs de recherche et de gestion des données.
- **IA & Outillage** : Intégration de nouveaux outils de développement basés sur le protocole MCP (Model Context Protocol) et mise à jour des outils de test Playwright.

### Autres changements
- **SEO** : Optimisation des URLs par la suppression des extensions `.html` et ajout de dates de modification pour les contenus (contacts, services, ressources).
- **Documentation** : Ajout d'un fichier `llms.txt` pour faciliter l'indexation par les modèles de langage.
- **Qualité de code** : Durcissement des règles de linting pour interdire l'usage de styles en ligne dans les composants Svelte.
