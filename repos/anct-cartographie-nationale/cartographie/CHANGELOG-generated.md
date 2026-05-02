## Changelog : cartographie (30 derniers jours, au 30 avril 2026)

### Résumé
Cette version apporte des améliorations significatives en termes de performance et de sécurité. L'équipe a notamment optimisé le temps de chargement des pages, renforcé la protection contre les bots malveillants et amélioré la gestion du cache. Des corrections de bugs et des améliorations de l'accessibilité ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un bouton pour intégrer la carte sur d'autres sites web, avec suivi via Matomo.
- Correction de la navigation arrière depuis la page de détail d'un lieu pour utiliser l'historique du navigateur.
- Amélioration de la gestion des erreurs avec une page d'erreur plus conviviale.

### Évolutions techniques
- **Performance :**
    - Mise en cache des exports CSV avec des tags pour une récupération plus rapide.
    - Utilisation de `next/dynamic` pour charger MapLibre de manière paresseuse, améliorant le temps de chargement initial.
    - Optimisation du rendu React pour les marqueurs de carte et les éléments de liste.
    - Extraction du contenu LCP (Largest Contentful Paint) vers des composants serveur pour un affichage plus rapide.
    - Mise en place d'un cache HTTP et côté serveur pour les routes API.
    - Utilisation de `ReadableStream` pour les exports CSV afin d'améliorer l'efficacité.
    - Réduction de la taille de l'image Docker de 42%.
- **Sécurité :**
    - Ajout de limitations de débit (rate limiting) pour protéger contre les attaques et les abus.
    - Blocage des bots malveillants sur les exports et configuration du pare-feu Nginx.
    - Ajout d'un pare-feu géographique (geo-blocking) pour restreindre l'accès en fonction de la localisation.
    - Intégration de CrowdSec pour la détection collaborative des menaces.
- **Infrastructure :**
    - Amélioration de la configuration des ressources conteneur Scaleway.
    - Ajout d'un endpoint de vérification de l'état de santé pour Scaleway.
- **Autres :**
    - Mise à jour des dépendances.
    - Amélioration de la configuration de l'environnement Node.js.
    - Refactorisation de la configuration Nginx et ajout de tests associés.
    - Ajout de tests E2E pour les API de statistiques.

### Autres changements
- Ajout de logs d'accès Nginx avec l'adresse IP du client et le statut du cache.
- Amélioration des tests E2E pour une meilleure couverture et stabilité.
- Correction de problèmes liés à l'affichage des heures d'ouverture.
- Mise à jour de la configuration robots.txt et sitemap.
- Suppression de code inutilisé et amélioration de la lisibilité du code.
