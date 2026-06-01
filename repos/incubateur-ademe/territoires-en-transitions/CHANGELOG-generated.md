## Changelog : territoires-en-transitions (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la plateforme en termes de performance, de sécurité et d'expérience utilisateur. Des corrections ont été apportées pour résoudre des problèmes de sécurité, notamment une injection SQL potentielle. De nombreuses améliorations concernent la gestion des référentiels, l'édition des actions, et la personnalisation de l'interface. Des refactorings importants ont également été réalisés pour préparer le terrain à de futures évolutions et améliorer la maintenabilité du code.

### Évolutions fonctionnelles

*   **Collectivités :** Correction d'un problème de filtre par niveau de labellisation TE. Ajout de la structure "sans statut juridique" pour les collectivités.
*   **Référentiels :**
    *   Amélioration de la gestion des archives de preuves d'audit, avec génération asynchrone côté backend.
    *   Possibilité de demander un audit directement depuis l'interface.
    *   Correction de l'affichage du graphique de comparaison d'audit.
    *   Amélioration de l'affichage des actions dans le tableau de bord EDL.
*   **Actions :**
    *   Rendre le tableau des actions éditable, avec des options de suppression et de modification.
    *   Ajout d'un bouton pour ouvrir une action directement depuis le tableau, avec gestion des permissions.
    *   Amélioration de la gestion des sous-actions et de leur affichage.
*   **Interface utilisateur :**
    *   Amélioration de l'accessibilité et du design de plusieurs composants (badges, sélecteurs, tables).
    *   Nouvelle page "Plateforme numérique" sur le site web, avec FAQ et informations actualisées.
    *   Amélioration de la gestion des erreurs et des retours d'information à l'utilisateur.
*   **Import de plans :** Amélioration de la robustesse et de la performance de l'import de plans, avec gestion des erreurs et des utilisateurs/tags.
*   **Suivi des indicateurs :** Amélioration de la gestion du compteur d'indicateurs et de la stabilité des tests associés.

### Évolutions techniques

*   **Sécurité :** Correction d'une vulnérabilité d'injection SQL dans la recherche de collectivités [#6499ceb](https://github.com/incubateur-ademe/territoires-en-transitions/commit/6499ceb).
*   **Architecture :**
    *   Migration de plusieurs fonctionnalités vers tRPC pour améliorer la performance et la sécurité (ressources partagées, historique des référentiels, ajout de documents).
    *   Refactoring du code pour améliorer la modularité et la maintenabilité.
    *   Suppression de code obsolète et de dépendances inutilisées.
*   **Tests :**
    *   Migration des tests Storybook vers Vitest.
    *   Amélioration de la couverture et de la robustesse des tests (e2e, unitaires).
    *   Correction de problèmes de synchronisation et de timeouts dans les tests.
*   **CI/CD :**
    *   Optimisation de la configuration du workflow CI/CD pour améliorer la performance et la fiabilité.
    *   Restriction des permissions du token GITHUB_TOKEN pour renforcer la sécurité.
*   **Dépendances :** Mise à jour de certaines dépendances pour bénéficier des dernières corrections et améliorations.
*   **Backend :** Génération des PDF côté backend via tRPC.

### Autres changements

*   **Documentation :** Documentation de la création de client\_id/client\_secret via curl.
*   **Nettoyage de code :** Suppression de fichiers inutilisés, de commentaires obsolètes et de code dupliqué.
*   **Configuration :** Mise à jour de la configuration de l'environnement de développement et de production.
*   **Monitoring :** Ajout d'événements PostHog pour suivre l'utilisation de certaines fonctionnalités.
*   **Design System :** Utilisation accrue des composants du Design System (DS) pour uniformiser l'interface utilisateur.
*   **Refactor labels :** Migration des labels JSX vers un catalogue centralisé pour une meilleure cohérence et maintenabilité.
*   **Amélioration des logs :** Ajout de logs pour faciliter le débogage et le suivi des erreurs.
*   **Correction de typos :** Correction de fautes de frappe et d'erreurs de syntaxe.
*   **Mise à jour des types :** Amélioration du typage pour une meilleure sécurité et une meilleure expérience de développement.
*   **Suppression de code déprécié :** Suppression de composants et de fonctionnalités dépréciées.
*   **Amélioration de la synchronisation Calendly Airtable.**
*   **Remplacement de Stonly par une bannière gérée en propre.**
*   **Modification pour remplacer les stats d'usage par des stats d'impacts et de résultats.**
*   **Ajout d'une page "mesure désactivée".**
*   **Amélioration de la gestion des timeouts dans les tests liés à la personnalisation.**
*   **Amélioration de la stabilité des tests.**
*   **Ajout d'une option pour filtrer les mesures désactivées par la personnalisation.**
*   **Utilisation du backend pour le filtrage des mesures désactivées par la personnalisation.**
*   **Amélioration de la gestion des annexes d'une fiche.**
*   **Ajout du point trpc pour compter les documents associés aux mesures et leurs descendants.**
*   **Ajout du point trpc d'ajout d'un document à une fiche action.**
*   **Amélioration de la synchronisation Calendly Airtable.**
*   **Ajout d'event posthog au niveau des imports de plan.**
*   **Suppression de endpoints trpc dans l'app panier.**
*   **Correction d'une typo.**
*   **Ajout d'une page "mesure désactivée".**
*   **Amélioration de la gestion des timeouts dans les tests liés à la personnalisation.**
*   **Amélioration de la stabilité des tests.**
*   **Ajout d'une option pour filter les mesures désactivées par la personnalisation.**
*   **Utilisation du backend pour le filtrage des mesures désactivées par la personnalisation.**
*   **Amélioration de la gestion des annexes d'une fiche.**
*   **Ajout du point trpc d'ajout d'un document à une fiche action.**
*   **Amélioration de la synchronisation Calendly Airtable.**
*   **Ajout d'event posthog au niveau des imports de plan.**
*   **Suppression de endpoints trpc dans l'app panier.**
*   **Correction d'une typo.**
*   **Ajout d'une page "mesure désactivée".**
*   **Amélioration de la gestion des timeouts dans les tests liés à la personnalisation.**
*   **Amélioration de la stabilité des tests.**
*   **Ajout d'une option pour filter les mesures désactivées par la personnalisation.**
*   **Utilisation du backend pour le filtrage des mesures désactivées par la personnalisation.**
*   **Amélioration de la gestion des annexes d'une fiche.**
*   **Ajout du point trpc d'ajout d'un document à une fiche action.**
*   **Amélioration de la synchronisation Calendly Airtable.**
*   **Ajout d'event posthog au niveau des imports de plan.**
*   **Suppression de endpoints trpc dans l'app panier.**
*   **Correction d'une typo.**
*   **Ajout d'une page "mesure désactivée".**
*   **Amélioration de la gestion des timeouts dans les tests liés à la personnalisation.**
*   **Amélioration de la stabilité des tests.**
*   **Ajout d'une option pour filter les mesures désactivées par la personnalisation.**
*   **Utilisation du backend pour le filtrage des mesures désactivées par la personnalisation.**
*   **Amélioration de la gestion des annexes d'une fiche.**
*   **Ajout du point trpc d'ajout d'un document à une fiche action.**
*   **Amélioration de la synchronisation Calendly Airtable.**
*   **Ajout d'event posthog au niveau des imports de plan.**
*   **Suppression de endpoints trpc dans l'app panier.**
