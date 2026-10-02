## Changelog : hubee (30 derniers jours, au 30 septembre 2026)

### Résumé
Ce mois a été marqué par une refonte majeure de la gestion des fichiers et du suivi des dossiers sur le portail, rendant l'expérience utilisateur plus fluide et explicite. Parallèlement, une mise à niveau profonde de la sécurité a été déployée, renforçant l'authentification (notamment via le multi-facteur) et la traçabilité des accès.

### Évolutions fonctionnelles
- **Gestion documentaire améliorée** : 
    - Possibilité de télécharger les pièces jointes reçues ([#163](https://github.com/datagouv/hubee/issues/163)).
    - Meilleure visibilité sur les fichiers : affichage des types de pièces, regroupement des fichiers sous un titre unique et accès à une archive des pièces reçues.
    - Messages d'aide contextuels pour expliquer pourquoi une pièce est requise ou pourquoi un téléchargement est impossible.
- **Pilotage des télédossiers** : 
    - Transition terminologique : les "démarches" sont désormais appelées "télédossiers".
    - Nouvelles actions disponibles : accuser réception d'un nouveau dossier, faire avancer un dossier directement depuis sa page de détail et répondre à un dossier par l'envoi d'une pièce.
    - Amélioration du suivi : intégration des actions de récupération de pièces dans l'historique du dossier.
- **Recherche et navigation** : 
    - Recherche facilitée par numéro de dossier (partiel ou complet).
    - Amélioration des filtres : possibilité de filtrer la liste des dossiers sur plusieurs flux simultanément et maintien du tri lors de l'application de filtres.

### Évolutions techniques
- **Sécurité et Authentification** : 
    - Refonte complète du système d'authentification avec intégration de l'OpenID Connect (OIDC) via ProConnect.
    - Renforcement de la sécurité pour les comptes à privilèges via l'exigence d'une authentification multi-facteur (MFA).
    - Mise en place d'un système de décision d'accès robuste : enregistrement en base des décisions, traçabilité des fournisseurs d'identité et gestion de la rétention des accès.
- **Architecture et API** : 
    - Implémentation du socle OAuth2 (client credentials) et protection des endpoints par jetons.
    - Refonte structurelle du portail pour isoler les règles d'accès et améliorer la maintenance (utilisation d'organizers et de politiques Pundit plus strictes).
    - Mise à jour majeure de l'intégration avec `hub-api-v1`.
- **Infrastructure et CI/CD** : 
    - Sécurisation de l'image de runtime Docker via l'utilisation d'une base "distroless".
    - Mise en place de "review apps" pour tester les modifications directement sur les Pull Requests ([#134](https://github.com/datagouv/hubee/issues/134)).
- **Qualité et Tests** : 
    - Augmentation significative de la couverture de tests, notamment sur les parcours d'authentification et les tests de bout en bout (E2E) en navigateur réel.

### Autres changements
- **Documentation** : Rédaction de nouveaux guides, incluant la description de la lecture des dossiers par le portail et un runbook pour les opérations liées à l'API.
- **Nettoyage** : Refactoring important pour améliorer la lisibilité du code et l'isolation des composants.
