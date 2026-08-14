## Changelog : les-emplois (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois a été marqué par l'intégration majeure du module d'orientation (Insertion), permettant une synchronisation fluide avec l'outil Dora. Nous avons également renforcé la sécurité des accès via une refonte de la double authentification (MFA) et amélioré l'expérience utilisateur grâce à de nouveaux filtres de recherche et une interface plus intuitive pour le suivi des candidats et des entreprises.

### Évolutions fonctionnelles
- **Module d'Orientation (Insertion) :** 
    - Ajout d'un menu dédié et d'une vue détaillée pour les orientations.
    - Mise en place de filtres avancés dans les listes (par bénéficiaire, structure, statut ou expéditeur).
    - Synchronisation automatique des statuts d'orientation depuis Dora.
- **Gestion des Candidats :** 
    - Amélioration de la visibilité des informations de contact des accompagnateurs.
    - Ajout d'alertes informatives lors de la mise à jour de profils avec une identité certifiée.
    - Clarification des champs en lecture seule pour les utilisateurs.
- **Entreprises & GEIQ :** 
    - Nouvelles contraintes de saisie sur les dates de contrat pour plus de cohérence.
    - Automatisation du transfert des évaluations GEIQ et des données d'évaluation lors des changements d'entreprise.
- **Interface & Navigation :** 
    - Mise à jour du thème visuel et amélioration de l'affichage des résultats de recherche.
    - Ajout de propriétés d'affichage pour les types de membres au sein des organisations.

### Évolutions techniques
- **Sécurité & Authentification :** 
    - Refonte complète de la gestion du MFA (TOTP) : ajout d'exemples d'applications d'authentification, amélioration des messages d'erreur et gestion plus robuste des codes de secours.
    - Renommage complet du module de connexion (passage de `PoleEmploiConnect` à `FTConnect`) pour une meilleure cohérence sémantique.
    - Amélioration du flux de déconnexion FranceConnect.
- **Performance & Optimisation :** 
    - Optimisation des requêtes SQL (réduction des problèmes de type 1+N) sur les listes de candidats.
    - Amélioration des performances de recherche et de l'affichage des listes.
- **Architecture & Données :** 
    - Mise en place de la suppression logique (*soft-delete*) pour les services et les structures.
    - Amélioration de la gestion des logs de transition pour les statuts d'orientation.
    - Refactorisation des vues de détails pour une meilleure maintenabilité.

### Autres changements
- **Nettoyage :** Suppression de templates, de tests et de méthodes inutilisés.
- **Documentation & Code :** Passage des commentaires techniques du module d'insertion en anglais et mise à jour de la documentation interne.
- **Maintenance :** Mise à jour du thème (v3.5.0) et optimisation des processus de nettoyage des fichiers.
