## Changelog : Docurba (30 derniers jours, au 15 octobre 2026)

### Résumé
Ce mois-ci, Docurba a franchi une étape importante dans la traçabilité et la fiabilité des données. Les utilisateurs bénéficient d'une meilleure visibilité sur l'origine des modifications (qui a créé ou modifié quoi) et d'un contrôle plus strict lors de la création de procédures. La plateforme est également plus robuste grâce à une gestion optimisée des comptes utilisateurs et une amélioration des processus d'archivage.

### Évolutions fonctionnelles
- **Amélioration de la traçabilité** : Affichage systématique de l'auteur des dernières modifications et de l'auteur de la création des sections dans les trames.
- **Gestion des procédures** : 
    - Automatisation du calcul des noms de procédures pour plus de cohérence.
    - Ajout de nouveaux champs (complément de nom) et affichage des dates d'approbation des procédures parentes.
    - Mise en place de règles de validation pour empêcher la création de procédures sans commune ou dans des contextes EPCI non conformes.
- **Administration et utilisateurs** :
    - Amélioration du filtrage par type de procédure dans l'interface d'administration.
    - Activation de la vérification des comptes utilisateurs par email.
    - Meilleure gestion du partage de projets avec une interface de suppression et d'affichage améliorée.
    - Intégration de Pipedrive pour automatiser la vérification des profils utilisateurs.

### Évolutions techniques
- **Optimisation de l'API** : Nettoyage important des points de terminaison (endpoints) inutilisés et refactorisation des énumérations (enums) pour une structure de code plus propre.
- **Gestion des données et fiabilité** :
    - Transition d'un système de suppression vers un système d'archivage pour les événements.
    - Mise en place de mécanismes de tentatives automatiques (retries) pour gérer les échecs temporaires.
    - Correction de tests instables et mise à jour des migrations de base de données.
- **Infrastructure et CI/CD** :
    - Optimisation des "Review Apps" pour une meilleure gestion des ressources.
    - Mise en place de sauvegardes pour l'outil de BI Metabase.
    - Augmentation des limites de débit (rate limiting) pour améliorer la stabilité du service.

### Autres changements
- **Nettoyage** : Suppression de code mort, de snapshots orphelins et de variables d'environnement inutilisées.
- **Documentation** : Mise à jour des snapshots de l'API d'export.
