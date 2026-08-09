## Changelog : nosgestesclimat-app (30 derniers jours, au 07 août 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec le déploiement et l'internationalisation du catalogue d'actions. L'expérience utilisateur a été affinée avec de nouvelles fonctionnalités visuelles et des corrections de bugs, tandis que l'infrastructure a été optimisée pour offrir une navigation plus rapide et une meilleure stabilité globale.

### Évolutions fonctionnelles
- Déploiement et internationalisation du catalogue d'actions ([#1964](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1964), [#1938](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1938))
- Prise en charge étendue des régions pour les actions ([#1961](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1961))
- Réactivation des actions liées aux services sociétaux ([#1955](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1955))
- Mise à disposition publique du catalogue d'actions ([#1845](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1845))
- Améliorations de l'interface : ajout d'un bouton de fermeture sur les bannières ([#1912](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1912)), affichage des icônes de grille uniquement sur desktop ([#1960](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1960)) et remplacement des notifications IA par des anecdotes ("funfacts") ([#1970](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1970))
- Corrections de bugs : liens externes dans les iframes ([#1962](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1962)), processus de confirmation de newsletter ([#1931](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1931)), erreurs d'authentification ([#1959](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1959)), déconnexion avec les anciennes sessions ([#1926](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1926)) et migration des simulations de login ([#1930](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1930))
- Harmonisation de la terminologie (utilisation de "consommation" au lieu de "divers") ([#1904](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1904))

### Évolutions techniques
- Optimisation de l'infrastructure : mise en place d'un système de cache via Nginx pour améliorer la rapidité (page d'accueil, tutoriels) et gestion du débit (rate limiting) ([#1941](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1941), [#1946](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1946)) et proxying des assets S3 ([#1949](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1949))
- Refonte du flux d'authentification : passage à une machine à états et gestion typée des erreurs pour une meilleure fiabilité ([#1934](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1934), [#1942](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1942))
- Gestion des modèles : mise à jour de la version du modèle ([#1965](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1965)) et ajout d'un script d'automatisation des releases de modèles ([#1980](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1980))
- Stabilité et tests : résolution de fuites de mémoire lors des simulations de groupe ([#1923](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1923)), correction d'erreurs de mémoire (OOM) sur les workers ([#1940](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1940)) et amélioration de la stabilité des tests E2E ([#1977](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1977))
- SEO : refonte du sitemap ([#1944](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1944)) et correction des URLs canoniques du tutoriel ([#1935](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1935))

### Autres changements
- Nettoyage de la base de données après la fusion de l'internationalisation des actions ([#1943](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1943))
- Amélioration du suivi analytique (Posthog et stockage local des IDs de tracking) ([#1956](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1956), [#1957](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1957))
