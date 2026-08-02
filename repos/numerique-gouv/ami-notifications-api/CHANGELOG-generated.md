## Changelog : ami-notifications-api (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur, notamment sur l'écran d'accueil et les pages de suivi. De nouvelles fonctionnalités liées aux services ont été implémentées, permettant d'intégrer et de gérer des services externes via l'application. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'API.

### Évolutions fonctionnelles
- **Écran d'accueil amélioré :** Refonte de l'écran d'accueil avec amélioration de la présentation des informations FranceConnect, ajustement de la taille des icônes, et recentrage du contenu.  Ajout d'un titre à l'écran d'accueil. [#1098]
- **Gestion des suivis (Followups) :** Ajout de pages de détails pour les suivis, avec affichage des informations pertinentes et gestion de l'archivage.  Amélioration de l'affichage des suivis archivés. [#266]
- **Intégration des services :** Ajout d'une nouvelle section "Services" dans le menu principal, permettant d'accéder à une liste de services externes.  Possibilité d'intégrer des services avec une authentification silencieuse si activée.  Affichage des paramètres et descriptions des services. [#943]
- **Bannières :** Ajout de bannières sur les pages d'édition. [#769]
- **Correction d'un bug :** Correction d'un bug empêchant l'affichage correct des dates. [#1076]
- **Correction d'un bug :** Correction d'un problème lié à l'affichage du bouton "Retour" dans l'en-tête. [#950]
- **Gestion des feature flags :** Ajout d'un mécanisme pour activer/désactiver certaines fonctionnalités via des *feature flags*, notamment pour l'intégration des services. [#1081]

### Évolutions techniques
- **Refactoring de la navigation :** Refactorisation de la navigation principale avec correction des styles et amélioration de l'accessibilité (RGAA). [#1037]
- **Correction de la sérialisation OTVJWTTokenSerializer :** Correction d'un problème dans la sérialisation des tokens OTVJWT. [#1070]
- **Mise à jour des dépendances :**
    - Django mis à jour de la version 6.0.5 à 6.0.6.
    - Daphne mis à jour de la version 4.2.1 à 4.2.2.
    - Soupsieve mis à jour de la version 2.8.3 à 2.8.4.
    - ws mis à jour de la version 8.20.1 à 8.21.0.

### Autres changements
- **Suppression de code inutilisé :** Suppression de code non utilisé dans la gestion des suivis. [#266]
- **Amélioration de la compatibilité WebView Android :** Correction pour assurer que l'application utilise la pleine hauteur de la fenêtre sur les WebView Android. [#1013]
- **Documentation :** Amélioration de la documentation interne.
