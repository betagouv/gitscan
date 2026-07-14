## Changelog : referentiel-applications (30 derniers jours, au 13 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives en termes d'accessibilité (RGAA), de performance de recherche, et de fonctionnalités pour l'importation de données et la gestion des droits. Des corrections de bugs et des améliorations de la sécurité ont également été implémentées.

### Évolutions fonctionnelles
- Ajout de la gestion des licences et des stacks techniques sur la fiche d'application.
- Implémentation de filtres de conformité.
- Possibilité de trier les types d'acteurs.
- Importation d'acteurs depuis un fichier Excel.
- Importation d'applications et d'hébergements depuis Excel.
- Ajout de la gestion des campagnes MDIT et de l'impersonation d'utilisateurs par les administrateurs.
- Amélioration de la recherche d'applications (plus rapide).
- Ajout de tags et de sélections.
- Affichage du libellé de statut même sans date.
- Ajout de permissions d'écriture pour la modification des données des applications.

### Évolutions techniques
- Amélioration de la fiabilité du démarrage de la base de données et du backend en CI.
- Correction de problèmes de "flakiness" dans les tests E2E (attente de la disponibilité du backend, correction de locators).
- Correction de code smells identifiés par SonarQube (TypeScript).
- Résolution des alertes de sécurité CodeQL.
- Amélioration de la gestion des erreurs 401 (déconnexion de l'utilisateur).
- Mise à jour de l'image Docker frontend pour corriger des problèmes de permissions.
- Documentation récapitulative du RefApp et des ADR.
- Correction de problèmes de contraste de couleurs et d'éléments graphiques pour l'accessibilité (RGAA).
- Implémentation de plusieurs lots d'améliorations RGAA (formulaires, étiquettes, messages de statut, etc.).
- Correction de problèmes de focus et de gestion du clavier pour l'accessibilité (RGAA).

### Autres changements
- Mise à jour de la version à 1.82.0.
- Correction de bugs mineurs et améliorations de la stabilité.
- Ajout de tests non-régression pour plusieurs domaines.
- Mise à jour des URLs Swagger OIDC.
- Refactorisation de l'interface FooterLink.
