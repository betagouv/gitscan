## Changelog : docs (30 derniers jours, au 28 septembre 2026)

### Résumé
Ce mois a été marqué par une transition technologique majeure avec le passage du serveur de collaboration vers YHub, renforçant la robustesse de la synchronisation. L'expérience utilisateur a été enrichie par l'arrivée de nouveaux blocs de contenu (mathématiques, diagrammes), un meilleur support du mode hors-ligne et des améliorations significatives sur l'exportation et l'accessibilité.

### Évolutions fonctionnelles
- **Nouvelles capacités d'édition** : Ajout de blocs de mathématiques et de diagrammes dans l'éditeur, et possibilité de télécharger les documents au format Markdown.
- **Amélioration de l'exportation** : Support de l'exportation des présentations en PDF (avec filigrane du logo) et maintien du ratio d'aspect des images dans les colonnes PDF.
- **Expérience utilisateur (UX)** : 
    - Support du mode hors-ligne pour l'arborescence et le contenu.
    - Transformation automatique des liens de documents collés en liens internes (interlinking).
    - Ouverture des résultats de recherche dans un nouvel onglet via Ctrl/Cmd+clic.
    - Amélioration de la gestion de l'historique des versions (granularité configurable et affichage progressif des données migrées).
- **Interface & Accessibilité** : 
    - Refonte des pages d'erreur (404, 403) et de la page de confirmation d'email.
    - Amélioration de l'accessibilité (gestion du focus, masquage des emojis décoratifs pour les lecteurs d'écran).
    - Ajout d'indications de raccourcis clavier dans les menus.

### Évolutions techniques
- **Migration de la collaboration** : Transition complète du serveur de collaboration de Hocuspocus vers YHub, incluant la migration logicielle des documents et de l'historique des versions depuis S3.
- **Architecture Backend** : 
    - Refonte de la gestion du contenu des documents via le service YHub.
    - Implémentation de nouveaux endpoints de gestion (reset de connexion, restauration, création de documents).
    - Optimisation des performances via l'amélioration des requêtes SQL et de la gestion du cache Redis.
- **Sécurité & Authentification** : Renforcement de la sécurité par l'utilisation systématique de tokens JWT pour les services de conversion et le fournisseur de collaboration.
- **Infrastructure & DevOps** : 
    - Mise à jour des déploiements Helm (version 6.0.0-alpha.1).
    - Remplacement de Minio par Silo/S3 pour le stockage.
    - Mise en place d'un monitoring avancé avec Prometheus et Grafana, et ajout de tests de charge (k6) incluant des "canaries" de navigateur pour mesurer la perception utilisateur sous charge.
- **Tests** : Extension significative de la couverture E2E et stabilisation des tests pour réduire la volatilité (flakiness).

### Autres changements
- **Documentation** : Mise à jour complète de la documentation technique (architecture, installation et guides de migration vers YHub).
- **Internationalisation** : Mise à jour des chaînes de caractères traduites (i18n).
- **Maintenance** : Nettoyage du code, suppression de dépendances obsolètes (whitenoise) et optimisation des processus de développement (Docker, Tilt).
