## Changelog : drive (30 derniers jours, au 15 octobre 2026)

### Résumé
Cette période a été marquée par une amélioration significative de la gestion du stockage pour les administrateurs et une optimisation majeure des performances pour les utilisateurs manipulant de gros volumes de données. La fiabilité des téléchargements et la sécurité des accès ont également été renforcées.

### Évolutions fonctionnelles
- **Gestion du stockage (Admin) :**
  - Amélioration de la visibilité sur les quotas utilisateurs (affichage du quota total et des fichiers les plus volumineux).
  - Possibilité de définir des limites de stockage en Go directement depuis l'interface d'administration.
  - Nouvelle gestion des exclusions de quota, permettant d'exclure certains éléments ou dossiers entiers du calcul de l'espace utilisé.
- **Expérience de téléchargement :**
  - Amélioration de la fiabilité des uploads grâce à une réservation préalable de l'espace disque.
  - Uniformisation de l'affichage des tailles de fichiers entre l'interface utilisateur et l'administration.
- **Sécurité et accès :**
  - Restriction de la création de nouveaux éléments pour les utilisateurs n'ayant pas les droits de téléchargement nécessaires.
  - Mise en place de limites de débit (rate limiting) sur les points d'entrée de création d'éléments.

### Évolutions techniques
- **Optimisations de performance :**
  - Refonte des requêtes pour l'affichage des listes de fichiers, des favoris et des éléments récents afin d'éviter les scans complets de tables et d'accélérer le traitement sur les bases de données volumineuses.
  - Optimisation de la recherche des ancêtres et de la résolution des rôles utilisateurs via les chemins de fichiers.
- **Observabilité et monitoring :**
  - Intégration de PostHog pour le suivi des événements clés (création via modèle, conversion, export de dossier, suppression et édition de documents via WOPI).
  - Ajout de commandes pour profiler les principaux points d'entrée de l'API.
- **Infrastructure et déploiement :**
  - Migration du stockage objet local en environnement Docker vers RustFS.
  - Optimisation de la gestion des connexions PostgreSQL via l'activation du pooling (psycopg_pool).
  - Ajustements des configurations Helm pour la flexibilité des variables d'environnement et la robustesse des sondes de disponibilité (readiness probes).
- **Tests et Qualité :**
  - Amélioration de la couverture des tests de bout en bout (e2e) sur les processus de téléchargement et de suppression.
  - Ajout d'une commande pour générer des jeux de données de taille "production" pour les tests de charge.

### Autres changements
- **Documentation :** Ajout de documentation technique sur la stratégie de mise à l'échelle (scaling) des requêtes d'items.
- **Nettoyage :** Suppression de valeurs codées en dur et mise à jour de la terminologie concernant le stockage objet.
