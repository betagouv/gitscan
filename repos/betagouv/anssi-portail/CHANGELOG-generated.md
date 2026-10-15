## Changelog : anssi-portail (30 derniers jours, au 14 octobre 2026)

### Résumé
Ce mois-ci, le portail a franchi une étape majeure avec le déploiement de la simulation interactive "Réflexes Cyber" et la mise en place d'un nouveau système de blog. L'expérience utilisateur est renforcée par une meilleure visibilité des parcours de sécurisation sur l'ensemble du site et l'ajout de nouveaux outils pratiques, comme le comparateur de financements et des modèles d'annuaire de crise.

### Évolutions fonctionnelles
- **Simulation "Réflexes Cyber"** : Lancement complet de l'outil de simulation incluant le choix de rôles et de scénarios, des animations interactives, la gestion du son, ainsi que l'affichage du score final et des résultats.
- **Nouveau système de Blog** : Mise en place d'une gestion complète des articles (affichage, récupération par slug, mise en cache) et intégration d'un mécanisme de retours utilisateurs.
- **Outils de financement** : Ajout d'un comparateur de financements permettant de générer des rapports de différences au format Markdown.
- **Boîte à outils** : 
    - Intégration de nouvelles procédures (notamment la procédure de CRISE.8).
    - Ajout d'un outil permettant de télécharger un modèle d'annuaire de crise au format XLSX.
- **Parcours de sécurisation** : Intégration visuelle accrue du parcours dans le menu, le héros de la page d'accueil, les résultats des tests et le pied de page.
- **Mini-tests** : Amélioration des tests de maturité et d'exposition avec un mode autonome, des statistiques de résultats et des corrections d'affichage.
- **Contacts** : Amélioration de la gestion des contacts régionaux et passage à un affichage côté serveur.

### Évolutions techniques
- **Refonte de l'architecture API** : Réorganisation majeure de la gestion des routes (API, statiques, authentification, financements) et des middlewares pour une meilleure maintenabilité.
- **Optimisation des performances** : Mise en place de mécanismes de cache pour les articles du blog et les résumés afin d'accélérer le chargement.
- **Modernisation de la Toolchain** : 
    - Migration vers pnpm 12.
    - Optimisation de la gestion des dépendances par la suppression de nombreux "overrides" obsolètes.
    - Mise à jour des runners GitHub Actions.
- **Qualité et Tests** : 
    - Amélioration de la structure des tests et passage aux spies Vitest.
    - Automatisation du déploiement des composants de mini-tests.

### Autres changements
- **SEO & Visibilité** : Mise à jour massive des métadonnées (titres, descriptions, liens réseaux sociaux) et ajout des articles du blog au sitemap.
- **Nettoyage** : Suppression des fichiers Jekyll obsolètes, des anciens services Crisp et nettoyage de commentaires ou de variables inutiles.
- **Conformité** : Mise à jour des mentions dans la politique de confidentialité.
