## Changelog : monlogementetudiant (30 derniers jours, au 25 septembre 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'expérience utilisateur, tant pour les étudiants que pour les gestionnaires. L'ajout d'un espace étudiant dédié, de nouvelles fonctionnalités de recherche géolocalisée et d'outils d'export de données pour les propriétaires renforce l'utilité de la plateforme. Parallèlement, un travail de fond important a été réalisé pour renforcer la sécurité des données et optimiser la gestion des archives et de la base de données.

### Évolutions fonctionnelles
- **Expérience Étudiant** :
    - Création d'un nouvel espace étudiant permettant de sauvegarder les calculs de budget et de les exporter en PDF.
    - Amélioration de la gestion des favoris avec la possibilité de paramétrer les préférences de notifications.
    - Gestion plus fluide des résidences : les résidences non publiées sont conservées dans les favoris mais redirigent l'utilisateur vers la recherche de la ville concernée.
- **Recherche et Cartographie** :
    - Introduction de la recherche de ville par géolocalisation et stabilisation de la carte des résultats.
    - Amélioration de la précision des recherches par département et de la redirection des slugs de ville.
- **Outils Gestionnaires et Propriétaires** :
    - Nouveaux outils d'exportation de données (CSV) pour le suivi des contacts et les statistiques des résidences.
    - Amélioration du pilotage : affichage de la date de dernière mise à jour des disponibilités et monitoring des connexions des gestionnaires.
    - Gestion plus fine des droits : possibilité pour certains gestionnaires de gérer les contacts de manière spécifique par résidence.
- **Gestion des candidatures et alertes** :
    - Mise en place de la possibilité de suspendre les candidatures et l'envoi de mails.
    - Ajout d'alertes d'expiration pour les processus en cours.

### Évolutions techniques
- **Sécurité et Protection des données** :
    - Renforcement de la politique de sécurité (CSP basé sur les nonces) et sécurisation des liens de connexion (tokens hachés).
    - Protection accrue de la vie privée : masquage des emails étudiants dans les logs et restriction des accès aux endpoints sensibles.
    - Sécurisation des interactions : sandboxing des iframes pour les visites virtuelles et protection contre les injections via tRPC.
- **Gestion des données et Performance** :
    - Mise en place d'une politique de rétention et d'archivage automatique sur S3 pour les données de suivi (tracking) et les tables d'historique.
    - Optimisation de la base de données via l'ajout d'index et la gestion des connexions inactives.
    - Amélioration des performances via la mise en cache des images.
- **Architecture et Refactoring** :
    - Migration de la gestion des dates vers `dayjs` pour plus de fiabilité.
    - Remplacement de la bibliothèque SheetJS par `read-excel-file` pour les imports de fichiers Excel.
    - Optimisation des tâches de fond (cron) pour éviter les dépassements de limites d'infrastructure.

### Autres changements
- **Documentation** : Mise à jour de la politique de confidentialité et ajout de notes techniques concernant la gestion des archives S3.
- **Maintenance du code** : Nettoyage important du code (suppression de commentaires obsolètes, de code mort et de références à d'anciennes méthodes d'authentification) et harmonisation du formatage avec Biome.
