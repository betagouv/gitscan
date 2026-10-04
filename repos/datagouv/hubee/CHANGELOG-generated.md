## Changelog : hubee (30 derniers jours, au 02 octobre 2026)

### Résumé
Cette période a été marquée par une amélioration majeure de l'expérience utilisateur sur le portail, notamment pour la gestion des pièces jointes et le suivi des dossiers. La sécurité a également été considérablement renforcée par l'introduction de l'authentification multi-facteur (MFA) et une gestion plus robuste des accès et des jetons de connexion.

### Évolutions fonctionnelles
- **Gestion des dossiers (Portail) :**
    - Amélioration de la recherche et du filtrage : possibilité de rechercher un dossier par son numéro, de filtrer par plusieurs flux simultanément et de trier les listes.
    - Consultation simplifiée : les agents peuvent désormais consulter les dossiers liés à leur organisation ([#128](https://github.com/datagouv/hubee/issues/128)).
    - Pilotage des dossiers : possibilité d'accuser réception d'un nouveau dossier et de faire avancer son état directement depuis la page de détail.
- **Gestion documentaire :**
    - Téléchargement des pièces jointes : les agents peuvent désormais télécharger les pièces reçues ([#163](https://github.com/datagouv/hubee/issues/163)) et obtenir le contenu des pièces via la bibliothèque interne ([#162](https://github.com/datagouv/hubee/issues/162)).
    - Meilleure visibilité : regroupement des pièces par dossier, affichage explicite des formats de fichiers et gestion plus claire des erreurs de téléchargement.
- **Sécurité et accès :**
    - Introduction de l'authentification multi-facteur (MFA) pour les comptes à privilèges.
    - Meilleure traçabilité : enregistrement systématique des décisions d'accès et des fournisseurs d'identité en base de données.

### Évolutions techniques
- **Sécurité et API :**
    - Mise en place du socle OAuth2 en mode `client_credentials`.
    - Renforcement de la sécurité des endpoints par l'utilisation de jetons (tokens) avec attribution systématique des appels.
    - Automatisation de la maintenance de sécurité via une purge quotidienne des jetons obsolètes.
- **Infrastructure et Base de données :**
    - Optimisation des performances et de la stabilité PostgreSQL : limitation du temps de connexion (5s) et restriction des connexions au nœud primaire uniquement.
    - Sécurisation de l'environnement d'exécution via l'utilisation d'images Docker "distroless".
- **Architecture :**
    - Refonte de la logique métier du portail (utilisation d'organizers) pour une meilleure séparation des responsabilités.
    - Migration de la gestion de l'authentification ProConnect pour une meilleure intégration avec les standards OIDC.

### Autres changements
- **Documentation :** Mise à jour de la documentation de l'API, des procédures d'authentification et des guides d'utilisation des gestes clients.
- **Tests :** Augmentation significative de la couverture de tests, notamment via des tests de bout en bout (E2E) simulant des parcours utilisateurs réels dans le navigateur.
