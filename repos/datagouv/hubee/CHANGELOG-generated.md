## Changelog : hubee (30 derniers jours, au 08 octobre 2026)

### Résumé
Ce mois-ci, hubee a franchi une étape importante avec la transition vers le concept de "télédossiers" et une amélioration majeure de la gestion documentaire. Les utilisateurs bénéficient désormais d'une meilleure capacité à télécharger les pièces reçues, à consulter des archives de documents et à suivre plus précisément l'avancement des dossiers grâce à des messages et des indicateurs d'état plus explicites.

### Évolutions fonctionnelles
- **Gestion documentaire et pièces jointes** :
    - Possibilité de télécharger les pièces jointes reçues ([#163](https://github.com/datagouv/hubee/issues/163), [#162](https://github.com/datagouv/hubee/issues/162)).
    - Mise en place d'une archive des pièces reçues pour faciliter la consultation historique.
    - Amélioration de la visibilité des fichiers : affichage des formats, des types de pièces et regroupement des documents sous un titre unique.
    - Meilleure gestion des erreurs de téléchargement avec des explications claires pour l'utilisateur.
- **Pilotage des télédossiers** :
    - Transition de la terminologie "démarches" vers "télédossiers".
    - Amélioration du cycle de vie des dossiers : accusé de réception, gestion des décisions (acceptation/refus) et passage de l'état "en cours" après lecture.
    - Affichage détaillé des raisons nécessitant une action (ex: pourquoi une décision attend une pièce jointe).
- **Recherche et navigation** :
    - Recherche facilitée par numéro de dossier (partiel ou complet).
    - Amélioration des filtres : possibilité de filtrer par plusieurs flux simultanément et maintien du tri lors de l'application des filtres.
- **Interface utilisateur (UI)** :
    - Ajout d'un bandeau pour orienter les utilisateurs vers le support de la version bêta.
    - Nettoyage visuel : correction de la typographie, alignement des cellules de récapitulatif et des filtres, et amélioration de la lisibilité des messages d'état.

### Évolutions techniques
- **Infrastructure et CI/CD** :
    - Sécurisation de l'image de production via l'utilisation d'une base Docker "distroless".
    - Optimisation des *review apps* : intégration des erreurs dans Sentry, gestion de Solid Queue dans Puma et résolution des problèmes de limitation de débit Let's Encrypt.
- **Base de données et Performance** :
    - Optimisation des connexions PostgreSQL : limitation du temps de connexion (5s) et configuration pour ne se connecter qu'au nœud primaire.
    - Amélioration des performances via la mise en cache des abonnements.
- **Architecture et API** :
    - Montée de version progressive de l'intégration avec `hub-api-v1`.
    - Refactorisation de la gestion des flux et des habilitations pour une meilleure cohérence.
    - Exposition de l'état des télédossiers en tant que sous-ressource API.
- **Qualité logicielle** :
    - Renforcement significatif de la suite de tests de bout en bout (E2E) sur les processus critiques : téléchargement, archivage des pièces et changements d'état des dossiers.

### Autres changements
- **Documentation** : Mise à jour des documents techniques concernant l'authentification des agents et le fonctionnement interne de la recherche de pièces jointes.
