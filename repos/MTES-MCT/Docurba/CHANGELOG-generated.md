## Changelog : Docurba (30 derniers jours, au 09/10/2026)

### Résumé
Ce mois-ci, Docurba a connu des évolutions majeures axées sur la gestion des utilisateurs et la traçabilité des données. Les outils d'administration ont été enrichis pour offrir un meilleur contrôle sur les procédures et les partages de projets, tandis que la sécurité et la stabilité de la plateforme ont été renforcées par une meilleure gestion des sessions et des accès.

### Évolutions fonctionnelles
- **Gestion des utilisateurs** : Réactivation de la création de comptes, mise en place de l'envoi d'e-mails de vérification et possibilité pour l'administrateur de désactiver les inscriptions.
- **Traçabilité et édition** : Amélioration de la visibilité dans les trames avec l'affichage de l'auteur de la dernière modification, du créateur de section et des détails d'édition. La conservation de l'auteur national est désormais assurée lors de la copie de sections vers un département.
- **Gestion des procédures** : Ajout du champ "complément de nom", affichage des dates d'approbation des procédures parentes dans les formulaires secondaires et application de règles de validation strictes (blocage de la création de procédures sans commune ou sans contexte EPCI).
- **Administration (Backoffice)** : 
    - Ajout de filtres par type de procédure.
    - Amélioration de la gestion des partages de projets (affichage et suppression facilités).
    - Transition d'un mode de suppression vers un mode d'archivage pour les événements afin de préserver l'historique.

### Évolutions techniques
- **Sécurité et infrastructure** : 
    - Renforcement de la limitation de débit (rate limiting) via Nginx et Django pour prévenir les abus.
    - Sécurisation des permissions de base de données (RLS) et suppression des sessions utilisateur à durée infinie.
    - Mise en place d'un système de sauvegarde pour Metabase.
- **Intégration et API** : 
    - Création d'un client Pipedrive pour automatiser la synchronisation lors de la vérification des profils utilisateurs.
    - Nettoyage de l'API Nuxt avec la suppression de nombreux endpoints inutilisés (geo, pipedrive, pdf, data, slack, urba).
- **Architecture et Refactoring** : 
    - Réorganisation de la structure des applications API et interne vers un nouveau dossier dédié.
    - Suppression des composants Nuxt3 obsolètes.
    - Optimisation de la gestion des erreurs et des tentatives de reconnexion (utilisation de Tenacity).

### Autres changements
- **Sécurité** : Ajout d'un fichier `security.txt` pour faciliter le signalement de vulnérabilités.
- **Qualité logicielle** : Amélioration de la couverture de tests (ajout de factories pour les profils et les partages de projets) et nettoyage du code mort.
