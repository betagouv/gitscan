## Changelog : seves (30 derniers jours, au 16 septembre 2026)

### Résumé
Ce mois-ci, le projet a connu une évolution majeure centrée sur le module de Santé Animale (SA). Les utilisateurs bénéficient de formulaires plus intelligents, de nouveaux blocs d'informations (enquêtes, vétérinaires, mesures) et d'une meilleure gestion du cycle de vie des événements (clôture, publication). La visualisation a également été enrichie avec des cartes plus précises et de nouveaux tableaux de bord de pilotage.

### Évolutions fonctionnelles
*   **Gestion de la Santé Animale (SA) :**
    *   Enrichissement des formulaires avec de nouveaux blocs de saisie : espèces concernées, enquête épidémiologique, vétérinaire, ADIS et mesures.
    *   Amélioration de l'expérience de saisie : utilisation de sélecteurs optimisés (TreeSelect) pour les espèces et les maladies, et pré-remplissage automatique des données de détenteurs via les API SIRENE et BAN.
    *   Nouveaux contrôles de gestion : possibilité de clôturer, publier ou supprimer des événements animaux.
    *   Interface utilisateur : création d'une nouvelle vue détaillée pour la SA incluant l'historique et des filtres [#2220], ajout de bulles d'aide (tooltips) sur le statut des animaux [#2211] et intégration de nouveaux icônes pour la SA [#2214].
*   **Cartographie et Visualisation :**
    *   Amélioration de la cartographie : affichage par défaut en mode satellite, affichage des parcelles agricoles [#2221] et gestion optimisée des marqueurs de localisation.
    *   Pilotage : intégration de nouveaux tableaux de bord Metabase pour le suivi SSA et TIAC.

### Évolutions techniques
*   **Architecture et Données :**
    *   Mise en place d'un domaine dédié à la SA et mise à jour des middlewares associés [#2216].
    *   Refonte de la gestion des méthodes d'analyse et intégration de nouveaux jeux de données.
    *   Optimisation des performances via la création de vues matérialisées pour alimenter les tableaux de bord.
    *   Nettoyage et résolution des conflits de migrations de la base de données.
*   **Sécurité et Infrastructure :**
    *   Renforcement de la sécurité avec l'ajout d'un WAF (Web Application Firewall) et du header X-XSS-Protection.
    *   Ajustement de la version de Go pour garantir la compatibilité avec l'infrastructure de déploiement (scalingo).
*   **Performance :**
    *   Optimisation de la vitesse du composant TreeSelect lors de l'affichage de listes volumineuses.

### Autres changements
*   Corrections de diverses coquilles dans l'interface utilisateur et les tests.
*   Nettoyage des fichiers PDF (suppression du JavaScript) avant numérisation.
