## Changelog : cartographie (30 derniers jours, au 10 avril 2026)

### Résumé
Cette version apporte des améliorations significatives en termes de performance, notamment au niveau du chargement des données et de l'optimisation des requêtes. Des corrections de bugs ont été implémentées pour améliorer la stabilité et la fiabilité de l'application, notamment concernant la gestion des exports CSV, des robots.txt et de la compatibilité avec les versions de Node.js.  De nouvelles fonctionnalités ont été ajoutées pour améliorer l'expérience utilisateur, comme la gestion des erreurs et l'ajout de pages légales.

### Évolutions fonctionnelles
- Ajout de pages légales avec MDX.
- Ajout de redirections pour les anciennes routes Angular.
- Pré-remplissage des informations du lieu dans le formulaire de signalement d'erreur.
- Ajout d'un point de terminaison de vérification de l'état de santé pour le conteneur Scaleway.
- Configuration du `robots.txt` avec l'URL du site correct et blocage des robots d'IA.
- Publication du `robots.txt` et du `sitemap` dans le dossier `public/` pour le déploiement Docker.

### Évolutions techniques
- Mise à jour de Node.js de la version 20 à la version 22 pour une meilleure compatibilité avec les Web Streams.
- Optimisation des ressources du conteneur (1120 mVCPU / 2048 MB).
- Refactorisation des routes et des middlewares pour une meilleure organisation du code.
- Migration des gestionnaires de routes vers une API basée sur des pipes.
- Utilisation de middlewares pour la gestion du cache HTTP et côté serveur.
- Amélioration de la gestion des requêtes vers l'API, notamment avec l'utilisation de `curried collectivite parameter`.
- Ajout de tests E2E pour les endpoints de l'API stats.
- Ajout de configuration de la carte basée sur l'URL pour l'application Next.js.
- Implémentation d'un cache LRU pour les chunks de carte.
- Utilisation de `Suspense` pour les états de chargement des routes principales.
- Optimisation du rendu React pour les marqueurs de carte et les éléments de liste.
- Stream des exports CSV via `ReadableStream`.
- Ajout de timeouts avec `AbortSignal` pour les appels API.
- Ajout de sources de données Cockpit Grafana pour la synchronisation.

### Autres changements
- Mise à jour des dépendances.
- Correction de typos dans la configuration.
- Mise à jour de l'URL de La Coop.
- Amélioration de la stabilité des tests E2E.
- Ajout de variables d'environnement Matomo.
- Mise à jour de la documentation pour refléter l'URL de cartographie.
- Suppression des fichiers `robots.txt` et `sitemap` générés du suivi Git.
- Stabilisation du calcul des heures d'ouverture.
- Correction d'un bug lié à la préservation des filtres `code_insee`.
- Correction d'un bug lié à l'affichage des cases à cocher.
- Correction d'un bug lié au nom des lieux dans les réponses de l'API web component.
