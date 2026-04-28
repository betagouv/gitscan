## Changelog : cartographie (30 derniers jours, au 26 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'optimisation des performances du site, notamment en améliorant la vitesse de chargement des pages et en réduisant la charge sur le serveur. Des améliorations de sécurité ont également été apportées avec l'ajout de limitations de débit et la protection contre les bots malveillants. Enfin, des corrections d'accessibilité et des améliorations de l'expérience utilisateur ont été implémentées.

### Évolutions fonctionnelles
- Ajout d'un point de terminaison `/api/cache/reset` pour invalider le cache à la demande. [#80781fc](https://github.com/anct-cartographie-nationale/cartographie/commit/80781fc)
- Amélioration de la gestion des erreurs avec une page d'erreur plus conviviale pour les échecs d'API. [#f462ef5](https://github.com/anct-cartographie-nationale/cartographie/commit/f462ef5)
- Correction de l'affichage des heures d'ouverture. [#a8da3b8](https://github.com/anct-cartographie-nationale/cartographie/commit/a8da3b8)
- Correction du comportement des filtres pour conserver les filtres `code_insee` spécifiques. [#f5d08c1](https://github.com/anct-cartographie-nationale/cartographie/commit/f5d08c1)
- Correction de l'affichage du thème sombre, qui utilise maintenant les préférences du système. [#b8448bd](https://github.com/anct-cartographie-nationale/cartographie/commit/b8448bd)

### Évolutions techniques
- Optimisation significative des performances :
    - Mise en cache du CSV export avec des tags et augmentation du timeout Nginx.
    - Utilisation de `next/dynamic` pour le chargement différé de MapLibre.
    - Extraction du contenu LCP (Largest Contentful Paint) vers des composants serveur pour un rendu plus rapide.
    - Mise en cache HTTP et côté serveur pour les routes API.
    - Utilisation de ReadableStream pour les exports CSV.
    - Optimisation du rendu React pour les marqueurs de carte et les éléments de liste.
    - Ajout de preconnect hints pour les assets statiques S3.
- Amélioration de la sécurité :
    - Ajout de limitations de débit (rate limiting) et blocage des bots malveillants.
    - Intégration de CrowdSec pour la détection collaborative des menaces.
    - Ajout d'un reverse proxy Nginx avec cache, compression gzip, et configuration améliorée.
    - Ajout d'un geo-whitelist pour autoriser l'accès depuis certains pays (notamment les crawlers de moteurs de recherche).
- Infrastructure :
    - Mise à jour de Node.js vers la version 22 pour la compatibilité avec Web Streams.
    - Réduction de la taille de l'image Docker.
    - Amélioration de la configuration des ressources conteneur Scaleway.
- Tests :
    - Ajout de tests E2E pour les endpoints de statistiques.
    - Amélioration des tests E2E existants.

### Autres changements
- Mise à jour des dépendances.
- Correction de la configuration de `lint-staged`.
- Mise à jour de l'URL de la cartographie dans la documentation.
- Ajout de variables d'environnement Matomo.
- Amélioration de la configuration de GitHub Actions.
- Ajout d'un health check endpoint pour Scaleway.
- Ajout de logs d'accès Nginx avec country et status du cache.
- Suppression de code inutile et nettoyage général du code.
