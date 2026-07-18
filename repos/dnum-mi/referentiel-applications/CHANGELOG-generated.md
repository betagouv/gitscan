## Changelog : referentiel-applications (30 derniers jours, au 18 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives en termes d'accessibilité (RGAA), de recherche, de gestion des droits et d'importation de données. Des corrections de bugs et des optimisations de performance ont également été implémentées pour améliorer l'expérience utilisateur et la stabilité de l'application. La fonctionnalité de gestion des licences a été supprimée.

### Évolutions fonctionnelles
- **Recherche :** Amélioration de la recherche globale avec préfixe et fiabilisation complète.
- **Droits :** Les administrateurs d'application ont désormais les droits complets (lecture et écriture) sur leurs applications.
- **Importation :**
    - Ajout de l'importation d'acteurs depuis un fichier Excel.
    - Ajout de l'importation d'applications et d'hébergements depuis un fichier Excel.
    - Ajout de l'importation générique Excel avec la feuille Conformités.
- **MDIT :** Ajout de la gestion des millésimes MDIT avec campagnes dette IT, sélecteur de temps et accès administrateur.
- **Impersonation :** Possibilité pour un administrateur d'impersonner un utilisateur.
- **RGAA :** Amélioration de l'accessibilité (RGAA) avec plusieurs lots de corrections (couleurs, contrastes, formulaires, messages d'état, etc.).
- **Tri :** Possibilité de trier les types d'acteur.
- **Modification historique :** Traçabilité des modifications de la matrice des droits dans l'historique.
- **Statut :** Affichage du libellé de statut même sans date.
- **Tags :** Ajout de tags et de sélections.

### Évolutions techniques
- **CI/CD :** Fiabilisation du démarrage de la base de données et du backend en CI pour éviter les tests aléatoires.
- **Performance :** Optimisation de la recherche d'applications.
- **Sécurité :** Correction des alertes de sécurité Dependabot pour le backend et le frontend.
- **Docker :** Correction des permissions sur l'image frontend Docker pour une meilleure compatibilité avec OpenShift.
- **Refactoring :** Correction de code smells TypeScript détectés par SonarQube.
- **Tests :** Ajout de couverture de tests E2E pour de nouveaux domaines.
- **Documentation :** Ajout de documentation récapitulative du RefApp et des ADR (Architecture Decision Records).

### Autres changements
- Suppression de la fonctionnalité de gestion des licences (modèle, API, UI, tests).
- Ajout de documentation pour les ADR 0001 et 0002 (shared foundation).
- Correction de bugs mineurs et améliorations diverses de l'interface utilisateur.
