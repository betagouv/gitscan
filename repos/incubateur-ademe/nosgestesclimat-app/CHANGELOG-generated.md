## Changelog : nosgestesclimat-app (30 derniers jours, au 11 août 2026)

### Résumé
Ce mois a été marqué par le déploiement majeur du catalogue d'actions environnementales, permettant aux utilisateurs de découvrir et d'appliquer des solutions concrètes. Parallèlement, l'application a bénéficié d'une optimisation importante de ses performances et de sa stabilité grâce à une refonte de la gestion du cache et de l'infrastructure serveur. L'expérience utilisateur a également été fluidifiée par des améliorations de l'interface et une sécurisation du processus d'authentification.

### Évolutions fonctionnelles
**Nouvelles fonctionnalités**
- Déploiement du catalogue public des actions ([#1845](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1845), [#1964](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1964)) et support des différentes régions pour les actions ([#1961](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1961)).
- Réactivation des actions liées aux services sociétaux ([#1955](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1955)).
- Mise en place de la confirmation par email pour les utilisateurs ([#1929](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1929)).

**Améliorations de l'expérience utilisateur**
- Ajout d'une section explicative sur la page des résultats de tests collectifs ([#1969](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1969)).
- Amélioration de l'engagement avec le remplacement des notifications IA par des "fun facts" ([#1970](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1970)).
- Mise à jour de la terminologie pour plus de clarté (remplacement de "divers" par "consommation") ([#1904](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1904)).
- Optimisations de l'interface : ajout d'un bouton de fermeture sur les bannières ([#1912](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1912)), correction des styles d'input ([#1992](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1992)) et affichage adaptatif des icônes sur desktop ([#1960](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1960)).

**Corrections**
- Résolution de problèmes liés à l'authentification et à la déconnexion ([#1959](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1959), [#1930](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1930), [#1926](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1926)).
- Correction de liens externes brisés dans les iframes ([#1962](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1962)) et des URLs du tutoriel ([#1935](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1935)).
- Correction du processus de confirmation de la newsletter ([#1931](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1931)).

### Évolutions techniques
**Infrastructure et Performance**
- Mise en place de Nginx comme alternative à un CDN, incluant la gestion du cache, le rate limiting et le proxying des assets S3 ([#1941](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1941), [#1949](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1949)).
- Optimisation du cache pour la page d'accueil et le tutoriel pour les utilisateurs anonymes ([#1946](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1946)).
- Amélioration de la stabilité des workers pour éviter les erreurs de type "Out of Memory" ([#1940](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1940)).

**Architecture et Refactoring**
- Refonte complète du flux de connexion avec une machine à états et une gestion typée des erreurs ([#1934](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1934), [#1942](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1942)).
- Migration des composants de cache vers une nouvelle méthode interne ([#1945](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1945)).
- Amélioration de la base de données avec l'ajout de vues anonymes pour les groupes ([#1989](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1989)).

**Données et Tests**
- Mise à jour et gestion des versions des modèles de calcul ([#1965](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1965), [#1972](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1972)).
- Amélioration de la fiabilité des tests E2E et correction de tests instables ([#1977](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1977), [#1954](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1954)).

### Autres changements
- Refonte du sitemap pour un meilleur référencement ([#1944](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1944)).
- Amélioration du suivi analytique (tracking ID et referrers) ([#1957](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1957), [#1956](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1956)).
