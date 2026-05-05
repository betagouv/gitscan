## Changelog : drive (30 derniers jours, au 4 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées à Drive au cours du dernier mois. Les principales évolutions concernent l'expérience de visualisation et de manipulation des fichiers (notamment les PDF), l'ajout de fonctionnalités de gestion des droits et d'informations sur l'utilisation, ainsi que des corrections de bugs et des optimisations de performance. Des améliorations de sécurité ont également été intégrées.

### Évolutions fonctionnelles
- Ajout d'un visualiseur PDF avec barre latérale de vignettes, zoom et navigation par page.
- Possibilité de dupliquer des fichiers avec un retour visuel et une gestion de l'état.
- Ajout d'un modal d'avertissement concernant les conditions d'utilisation (entitlement disclaimer).
- Amélioration de l'affichage des fichiers : l'extension est maintenant affichée à la place du type.
- Ajout de la possibilité de trier les éléments par nom complet du créateur.
- Amélioration de la gestion des téléchargements avec affichage de la progression, des erreurs et possibilité d'annulation.
- Ajout d'un menu d'actions sur mobile pour la page "Mes fichiers".
- Possibilité de configurer la durée de validité des invitations via une variable d'environnement.
- Amélioration de la gestion des fichiers dans la corbeille : affichage d'un modal lors du clic sur un fichier et correction du rafraîchissement après suppression définitive.
- Ajout de la possibilité de configurer PKCE pour l'authentification SSO.
- Ajout d'informations sur l'utilisation de l'organisation via l'API.

### Évolutions techniques
- Refactorisation des entitlements dans un package backend dédié.
- Amélioration de la gestion des transactions lors de la duplication de fichiers.
- Mise à jour des dépendances : Django, pytest, vite et next.js (incluant des correctifs de sécurité).
- Optimisation du cache des navigateurs Playwright pour les tests E2E.
- Mise en place d'un système de shard pour les tests E2E afin d'améliorer la performance.
- Utilisation de Nginx pour servir le frontend pré-construit, améliorant ainsi les performances.
- Restriction des droits du token GitHub Actions pour le workflow frontend.
- Suppression de la fonctionnalité de mirroring.
- Amélioration de la gestion des erreurs et des états dans les tests E2E.
- Refactorisation des viewers de preview pour une meilleure maintenabilité.
- Ajout de la configuration dynamique de PostgreSQL via des variables d'environnement.
- Correction de la gestion des URL JWKS lors de l'utilisation de OIDC.
- Mise à jour de Pillow (librairie Python) pour corriger une vulnérabilité de sécurité.

### Autres changements
- Ajout d'une commande pour purger les éléments supprimés.
- Configuration d'une tâche cron quotidienne pour purger les éléments supprimés.
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et corrections.
- Corrections de style et de typographie dans l'interface utilisateur.
- Ajout d'événements PostHog pour le suivi des colonnes personnalisées et de la duplication d'éléments.
- Amélioration des tests E2E pour couvrir les nouvelles fonctionnalités et corriger les tests existants.
- Suppression de code inutilisé.
- Ajout de traductions pour les nouveaux messages et fonctionnalités.
- Mise à jour des notes de version.
