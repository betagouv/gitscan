## Changelog : Docurba (30 derniers jours, au 15 octobre 2026)

### Résumé
Ce mois-ci, Docurba a franchi une étape importante dans la précision de la gestion documentaire et la traçabilité des actions. Les utilisateurs bénéficient d'une meilleure visibilité sur l'origine des modifications (auteurs des sections) et d'une gestion plus fine des procédures (nouveaux types, calcul automatique des noms). L'administration a également été renforcée pour offrir un meilleur contrôle sur les comptes utilisateurs et le partage de projets.

### Évolutions fonctionnelles
- **Gestion des procédures** : 
    - Ajout du champ "complément de nom" et automatisation du calcul du nom de la procédure.
    - Introduction de nouveaux types de procédures (ex: Révision) et amélioration de la gestion des types de documents.
    - Meilleure visibilité des données clés : affichage des dates d'approbation des procédures parentes et inclusion des communes déléguées dans le calcul des zones.
    - Mise en place d'un système d'archivage pour les événements au lieu d'une suppression pure et simple.
- **Expérience utilisateur (Interface Nuxt)** :
    - Amélioration de la traçabilité : affichage de l'auteur de la dernière modification et de l'auteur de la création des sections.
    - Optimisation de l'édition : meilleure gestion de l'ouverture des sections et de la continuité des auteurs lors de la copie de sections entre départements.
    - Contrôle de saisie : blocage de la création de procédures dans certains contextes géographiques (absence de commune ou configuration EPCI spécifique).
- **Administration et Utilisateurs** :
    - Réactivation de la création de comptes utilisateurs et automatisation de l'envoi d'emails de vérification.
    - Amélioration de l'interface d'administration pour la gestion du partage de projets et la vérification des profils.
    - Possibilité de désactiver l'inscription des nouveaux utilisateurs.

### Évolutions techniques
- **Architecture Backend (Django)** :
    - Refactorisation majeure des énumérations (enums) pour une meilleure structure du code.
    - Optimisation des API internes pour le listage et le filtrage des procédures.
    - Amélioration de la robustesse via l'implémentation de mécanismes de tentatives automatiques (Tenacity) en cas d'échec.
- **Infrastructure et DevOps** :
    - Optimisation des "Review Apps" (gestion dynamique des ressources et mise à jour du nommage).
    - Mise en place de sauvegardes pour l'outil Metabase.
    - Nettoyage des endpoints API inutilisés côté Nuxt.
- **Base de données et Tests** :
    - Mise à jour et résolution de conflits dans les migrations de base de données.
    - Renforcement de l'intégrité des données (contraintes de non-nullité sur les rôles de partage).
    - Amélioration de la qualité des tests : correction de tests instables ("flaky tests"), nettoyage des snapshots et ajout de nouvelles usines de test (Factories).

### Autres changements
- Suppression de Nuxt3 et nettoyage du code mort.
- Augmentation des limites de débit (rate limiting) pour la sécurité.
