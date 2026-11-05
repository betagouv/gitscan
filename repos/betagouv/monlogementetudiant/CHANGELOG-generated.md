## Changelog : monlogementetudiant (30 derniers jours, au 4 novembre 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'expérience de recherche et de navigation grâce à une carte plus interactive et une barre de recherche repensée. L'outil de budget étudiant est devenu plus complet avec la possibilité d'exporter un récapitulatif en PDF. Par ailleurs, la plateforme renforce sa fiabilité et sa sécurité avec l'implémentation d'un système de tickets de support et une couverture de tests automatisés beaucoup plus large.

### Évolutions fonctionnelles
- **Recherche et Cartographie** :
    - Refonte de la barre de recherche avec l'utilisation de tags et d'un curseur de prix stable.
    - Amélioration de la carte : ajout du zoom, passage aux fonds de carte IGN (labels en français), et colorisation intelligente des clusters de marqueurs.
    - Optimisation de l'affichage des résultats : prévisualisation via popups et meilleure gestion du clustering.
    - Amélioration de la géolocalisation dans la barre de recherche.
- **Espace Étudiant** :
    - Nouveau système d'export du budget étudiant en format PDF, incluant un graphique de répartition des dépenses.
    - Ajout d'un formulaire de signalement de problème pour les utilisateurs.
    - Amélioration de l'ergonomie mobile (espacements, empilement des cartes d'aide et menus).
    - Ajout d'objectifs personnalisés dans le plan d'action étudiant.
- **Gestion et Administration** :
    - Mise en place d'un système complet de tickets de support (création, suivi, notifications et gestion par les administrateurs).
    - Nouveaux outils pour les gestionnaires : gestion des candidatures via un tableau de bord et export CSV des suivis de contact.
    - Possibilité pour les bailleurs d'afficher leur numéro de téléphone sur la page de la résidence.
    - Ajout de métriques sur les candidatures des résidences suspendues.

### Évolutions techniques
- **Sécurité** :
    - Mise à jour critique de `better-auth` pour répondre à une faille de sécurité.
    - Renforcement de la protection des données : hachage des tokens de liens magiques, masquage des erreurs SQL en production et durcissement de la politique de sécurité du contenu (CSP).
    - Nettoyage des sessions expirées et des tentatives de connexion obsolètes.
- **Tests et Qualité** :
    - Déploiement massif de tests de bout en bout (E2E) avec Playwright couvrant les parcours critiques : recherche, favoris, espace étudiant, création de résidence et gestion des disponibilités.
    - Mise en place de rapports de couverture de tests.
- **Performance et Infrastructure** :
    - Optimisation du chargement des pages de résidence via le streaming des établissements à proximité.
    - Réduction de la taille des images de déploiement Scalingo en excluant les caches de build.
    - Amélioration de la gestion des imports de données (CSV) pour les loyers et les équipements.
- **Refactoring** :
    - Modernisation de la gestion des formulaires avec `react-hook-form`.
    - Suppression de dépendances obsolètes (notamment `dayjs`) et nettoyage du code (suppression des commentaires redondants et des anciens credentials).

### Autres changements
- **Documentation** : Mise à jour de la documentation concernant les redirections vers les pages WordPress.
- **Configuration** : Redirection des mentions légales vers le site WordPress et mise à jour de la version de Node.js.
