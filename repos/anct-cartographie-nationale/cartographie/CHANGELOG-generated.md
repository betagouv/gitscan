## Changelog : cartographie (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la performance et la stabilité de la plateforme. Des optimisations significatives ont été apportées au caching, à la gestion des requêtes API et à l'infrastructure, notamment avec l'ajout d'un reverse proxy Nginx et de mesures de sécurité renforcées. Des corrections de bugs ont également été implémentées pour améliorer l'expérience utilisateur et la fiabilité du système.

### Évolutions fonctionnelles
- Ajout d'un endpoint `/api/cache/reset` pour invalider manuellement le cache.
- Pré-remplissage des informations du lieu dans le formulaire de signalement d'erreur.
- Ajout de pages légales avec du contenu en MDX.
- Redirections pour les anciennes routes Angular.
- Amélioration de la gestion du thème (passage automatique au thème système).

### Évolutions techniques
- Implémentation d'un cache en mémoire (BFF) pour remplacer les appels directs à l'API PostgREST, améliorant significativement les performances.
- Ajout d'un reverse proxy Nginx avec caching (TTL de 6h), compression gzip, et configuration de sécurité (limitation de débit, page d'erreur personnalisée 403, timeouts).
- Intégration de CrowdSec pour la détection collaborative de menaces.
- Optimisation de la taille de l'image Docker (réduction de 42%).
- Amélioration de la gestion des erreurs et ajout de logs plus détaillés.
- Mise à jour de Node.js vers la version 22 pour une meilleure compatibilité avec les Web Streams.
- Amélioration de la configuration et des ressources des conteneurs Scaleway.
- Ajout de tests d'infrastructure pour la restriction géographique et le cache.
- Refactorisation de la configuration Nginx et des tests associés.
- Ajout de tests e2e pour les endpoints de statistiques.

### Autres changements
- Mise à jour des variables d'environnement Matomo.
- Mise à jour de l'URL de La Coop.
- Mise à jour des dépendances.
- Amélioration de la configuration de lint-staged.
- Ajout de sources de données Cockpit Grafana.
- Correction de la configuration robots.txt et sitemap.
- Ajout de health check pour Scaleway container.
- Suppression de code et de dépendances inutilisées.
- Amélioration de la configuration des workflows GitHub Actions.
- Correction de bugs divers liés à l'extraction d'IP, la gestion des filtres, et la configuration de l'environnement.
