## Changelog : plusfraisautravail (30 derniers jours, au 29/09/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'enrichissement du système de gestion de contenu (CMS) pour permettre la création de nouveaux formats de pages (FAQ, questions/réponses) et une meilleure gestion des contenus. Parallèlement, l'infrastructure a été renforcée pour améliorer la performance, la sécurité et la fiabilité des services, notamment pour le formulaire de contact et la recherche climatique.

### Évolutions fonctionnelles
- **Nouveaux formats de contenus :** Ajout de pages FAQ [#26] et de blocs de questions/réponses avec aperçu DSFR [#24] dans le CMS.
- **Navigation et recherche :** 
    - Rétablissement des filtres par tags pour la section solutions [#31].
    - Correction de la recherche Climadiag pour éviter les erreurs de l'API (nécessite désormais un minimum de 3 caractères).
- **Améliorations de l'expérience :** 
    - Correction du formulaire de contact pour résoudre les erreurs d'envoi d'e-mails.
    - Traduction du pied de page en français.

### Évolutions techniques
- **Optimisation du CMS (Wagtail) :** 
    - Amélioration de la structure hiérarchique avec l'ajout de `wagtail-treebeard` [#29].
    - Optimisation de la gestion des médias (support du format WebP et mise en cache longue durée).
    - Optimisation des déploiements en évitant les migrations de modèles de pages inutiles [#28].
- **Infrastructure et Performance :** 
    - Augmentation des ressources allouées aux conteneurs (CPU et RAM).
    - Sécurisation de la base de données via un réseau privé et mise en place de redirections (301) vers le domaine canonique.
    - Optimisation de la diffusion via un proxy de production.
- **Outils et CI/CD :** 
    - Intégration de l'outil d'analyse PostHog via un proxy interne.
    - Amélioration de la fiabilité des tests CI en utilisant PostgreSQL au lieu de SQLite.
    - Synchronisation du formulaire de contact avec Notion via l'intégration d'un token dédié.
