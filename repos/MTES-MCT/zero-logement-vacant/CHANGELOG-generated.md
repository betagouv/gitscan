## Changelog : zero-logement-vacant (30 derniers jours, au 21 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité et la robustesse de l'authentification, avec une migration vers un nouveau système (Better Auth). Des corrections et améliorations ont également été apportées à la gestion des périmètres, à l'affichage des données sur la carte et à la gestion des logements, notamment pour l'export de données et l'édition des propriétaires. Des travaux préparatoires pour un outil de réparation des données ont été entrepris.

### Évolutions fonctionnelles
- **Authentification:** Amélioration significative de la sécurité et de la gestion des utilisateurs avec l'intégration progressive de Better Auth. Cela inclut la gestion des sessions, la synchronisation des utilisateurs Cerema et la gestion des accès.
- **Carte:**
    - Les périmètres sont maintenant affichés avec un contour, permettant de mieux visualiser les zones sélectionnées et de distinguer les périmètres inclus et exclus.
    - Ajout d'un contrôle plein écran pour la carte des logements.
- **Logements:**
    - Correction d'un problème empêchant l'édition des propriétaires dont l'adresse BAN a un score nul.
    - Amélioration de l'export des données des logements avec l'utilisation correcte de la classe DPE (Diagnostic de Performance Énergétique).
    - Correction de l'affichage du filtre "Année de vacance 2023".
- **Utilisateurs:**
    - Amélioration de la gestion des affiliations multi-structures pour les utilisateurs.
    - Affichage correct des périmètres associés à chaque établissement pour les utilisateurs ayant accès à plusieurs structures.

### Évolutions techniques
- **Authentification:**
    - Refonte complète de l'authentification avec l'intégration de Better Auth, incluant la migration des données utilisateurs et la gestion des sessions.
    - Amélioration de la sécurité avec la limitation du taux de tentatives de connexion pour les administrateurs.
    - Mise en place d'un système de synchronisation des utilisateurs Cerema.
- **Infrastructure:**
    - Mise en place d'un nouveau processus de déploiement avec Terraform pour le frontend.
    - Configuration de l'environnement de test avec Playwright pour les tests d'authentification.
- **Outils:**
    - Développement d'un outil de réparation des données (ZLV repair harness) avec une interface en ligne de commande (CLI) et des tests unitaires.
- **Divers:**
    - Mise à jour des dépendances npm et yarn.
    - Amélioration de la documentation pour le déploiement et l'authentification.
    - Refactoring du code pour améliorer la lisibilité et la maintenabilité.
    - Ajout de tests unitaires et d'intégration.

### Autres changements
- Documentation : Ajout de la méthodologie RGAA complète pour l'accessibilité.
- Documentation : Mise à jour de la documentation concernant l'utilisation de Clever Cloud pour les tâches cron.
- Divers : Corrections de style et de formatage du code.
- Divers : Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Divers : Correction de problèmes de performance mineurs.
