## Changelog : mon-service-securise (30 derniers jours, au 27 août 2026)

### Résumé
Ce mois-ci, le service a franchi une étape importante avec la refonte complète de son parcours d'accompagnement (visite guidée) et l'ajout d'outils de pilotage puissants via une nouvelle interface de statistiques pour les administrateurs et superviseurs. L'expérience utilisateur est également enrichie par un nouveau système de notifications et une gestion simplifiée des préférences personnelles et des consentements.

### Évolutions fonctionnelles
- **Système de notifications** : Mise en place d'un nouveau système de notifications incluant les mentions, les nouveautés et les tâches à faire. Les notifications sont désormais regroupées par date et affichées avec des badges (ex: "Non lu") pour une meilleure lisibilité.
- **Tableau de bord statistiques** : Création d'une nouvelle page de statistiques pour les administrateurs et superviseurs. Elle permet de visualiser l'évolution du nombre de services, les taux de complétude des mesures, les indices cyber moyens et la répartition des statuts, avec des options de filtrage et d'impression.
- **Visite guidée** : Refonte majeure de la visite guidée pour offrir un parcours plus fluide et interactif (nouvelles modales, ciblage précis des éléments, mode avancé et meilleure gestion du défilement).
- **Gestion des préférences** : Ajout d'une page dédiée permettant aux utilisateurs de gérer leurs consentements et leurs préférences de communication.
- **Améliorations de l'interface** : 
    - Déploiement d'une nouvelle page d'accueil (landing page).
    - Mise à jour visuelle des niveaux de risque (couleurs) sur l'interface et dans les exports PDF.
    - Affichage de nouvelles informations contextuelles (département de l'entité, SIRET, version des référentiels).
- **Sécurité** : Amélioration de la gestion du MFA (Multi-Factor Authentication) et de la validation via ProConnect.

### Évolutions techniques
- **Architecture des données** : 
    - Implémentation d'un nouvel adaptateur de statistiques basé sur PostgreSQL.
    - Mise en place de la persistance des notifications en base de données.
    - Refactorisation de plusieurs adaptateurs en classes pour une meilleure structure.
- **Optimisation de la visite guidée** : Utilisation de `ResizeObserver` pour une détection plus précise des éléments à mettre en avant et optimisation du calcul du scroll.
- **Gestion des assets** : Mise en place d'une politique de cache et d'un système de versionnage pour les fichiers statiques.
- **Refactoring et nettoyage** : 
    - Suppression massive de code obsolète (anciens services, variables d'environnement, méthodes de visite guidée v1 et proxies inutiles).
    - Extraction de composants utilitaires (ex: `PieChart`, gestion des risques).
    - Optimisation des appels API et de la gestion des événements.

### Autres changements
- **UI Kit** : Mises à jour régulières des composants pour s'aligner sur le Design System (DSFR).
- **Qualité de code** : Corrections de règles ESLint et de types TypeScript.
- **Contenu** : Ajustements de la rédaction (wording) pour les modules de risques et les formations.
