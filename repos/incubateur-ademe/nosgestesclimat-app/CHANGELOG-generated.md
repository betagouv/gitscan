## Changelog : nosgestesclimat-app (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec le déploiement du catalogue d'actions concrètes pour réduire son empreinte climat. L'expérience utilisateur a été enrichie par de nouveaux éléments d'accompagnement et une interface plus fluide, tandis que l'infrastructure a été optimisée pour garantir une navigation plus rapide et une meilleure stabilité du système.

### Évolutions fonctionnelles
- **Déploiement des actions :** Mise en ligne du catalogue public d'actions [#1845](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1845), support de l'internationalisation [#1938](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1938) et extension de la compatibilité des actions aux différentes régions du modèle climatique [#1961](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1961).
- **Amélioration de l'expérience utilisateur (UX) :** 
    - Ajout d'une section explicative sur la page des résultats de tests collectifs [#1969](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1969).
    - Remplacement des notifications par des "fun facts" pour un ton plus engageant [#1970](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1970).
    - Ajout d'un bouton de fermeture sur les bannières [#1912](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1912).
- **Authentification et sécurité :** Ajout de la confirmation par email [#1929](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1929) et correction des erreurs liées aux codes d'authentification invalides [#1959](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1959).
- **Corrections d'interface :** Ajustement du style des champs de saisie [#1992](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1992) et résolution de liens brisés dans les iframes [#1962](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1962).

### Évolutions techniques
- **Optimisation des performances et infrastructure :** 
    - Mise en place d'un système de cache via Nginx (remplaçant un CDN) pour accélérer l'accès à la page d'accueil et aux tutoriels [#1941](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1941), [#1946](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1946).
    - Proxyification des assets S3 via Nginx pour une meilleure gestion des contenus statiques [#1949](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1949).
- **Fiabilisation du code et des tests :** 
    - Travail important sur la stabilité des tests de bout en bout (E2E) pour réduire les échecs aléatoires en environnement de CI et de préproduction [#1993](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1993), [#1990](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1990), [#1981](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1981).
    - Refactorisation du flux de connexion via une machine à états pour une gestion plus robuste des erreurs [#1934](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1934).
- **Maintenance du modèle et des données :** 
    - Mise à jour de la version du modèle climatique [#1965](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1965).
    - Ajout de vues anonymes pour les groupes dans le schéma de base de données [#1989](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1989).

### Autres changements
- Refonte du sitemap pour optimiser le référencement [#1944](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1944).
- Nettoyage de la base de données suite à la fusion des traductions des actions [#1943](https://github.com/incubateur-ademe/nosgestesclimat-app/pull/1943).
