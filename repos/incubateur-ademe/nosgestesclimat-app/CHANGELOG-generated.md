## Changelog : nosgestesclimat-app (30 derniers jours, au 4 août 2026)

### Résumé
Ce mois-ci, l'application a franchi une étape majeure avec le déploiement du nouveau catalogue d'actions et l'amélioration de leur internationalisation. Le modèle de calcul de l'empreinte carbone a également été mis à jour pour plus de précision. Parallèlement, des optimisations techniques importantes ont été réalisées pour améliorer la rapidité de l'application et renforcer sa sécurité.

### Évolutions fonctionnelles
- **Nouveautés liées aux actions** : Déploiement du catalogue public des actions ([#1845](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1845)), réactivation des actions liées aux services sociétaux ([#1955](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1955)) et déploiement global du système d'actions ([#1964](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1964)).
- **Internationalisation** : Support de toutes les régions (actuelles et précédentes) pour les actions ([#1961](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1961)) et mise en place de l'i18n pour le catalogue d'actions ([#1938](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1938)).
- **Mise à jour du modèle** : Montée de version du modèle de calcul de l'empreinte carbone ([#1965](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1965), [#1917](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1917)).
- **Expérience utilisateur et Interface** : 
    - Mise à jour de l'affichage des graphiques de distribution de l'empreinte ([#1898](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1898)).
    - Remplacement des notifications IA par des anecdotes ("funfacts") ([#1970](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1970)).
    - Amélioration de la clarté terminologique (remplacement de "divers" par "consommation") ([#1904](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1904)).
    - Ajustements visuels : icônes de grille sur desktop uniquement ([#1960](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1960)), ajout d'un bouton de fermeture sur les bannières ([#1912](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1912)) et correction de l'affichage des bannières de kit de communication ([#1928](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1928)).
    - Optimisation de l'affichage : masquage du bloc d'actions sur la page des résultats d'eau ([#1913](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1913)) et restriction d'accès aux blocs de communication pour les non-administrateurs ([#1919](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1919)).
- **Corrections de bugs** : Résolution de liens brisés dans les iframes ([#1962](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1962)), correction de l'origine de confirmation de la newsletter ([#1931](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1931)) et correction des erreurs de déconnexion avec les sessions héritées ([#1926](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1926)).

### Évolutions techniques
- **Performance et Infrastructure** : 
    - Mise en place d'un système de cache via Nginx (reverse proxy) avec limitation de débit pour remplacer un CDN ([#1941](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1941)).
    - Mise en cache de la page d'accueil et des tutoriels pour les utilisateurs anonymes ([#1946](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1946)).
    - Optimisation de la distribution des assets S3 via Nginx ([#1949](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1949)).
- **Sécurité et Authentification** : 
    - Correction de vulnérabilités d'autorisation et de fuites de données lors des simulations de groupe ([#1885](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1885), [#1923](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1923)).
    - Refactorisation complète du flux de connexion via une machine à états et typage des erreurs ([#1934](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1934), [#1942](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1942)).
- **Stabilité et Refactoring** : 
    - Résolution de problèmes de consommation mémoire (OOM kill) sur les workers de l'application de revue ([#1940](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1940)).
    - Migration vers un nouveau système de gestion de cache pour les composants ([#1945](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1945)).

### Autres changements
- **SEO** : Refonte du sitemap ([#1944](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1944)) et correction des URLs canoniques pour les tutoriels ([#1935](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1935)).
- **Qualité logicielle** : Correction de tests instables ([#1954](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1954)) et amélioration des composants de données de test ([#1882](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1882)).
- **Nettoyage** : Nettoyage de la base de données suite à la fusion de l'i18n des actions ([#1943](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1943)).
