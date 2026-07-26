## Changelog : monstagedeseconde (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur des entreprises et des étudiants, avec des mises à jour des pages partenaires, de la page étudiant et du formulaire de création d'offres. Des corrections de sécurité importantes ont également été apportées, ainsi que des refactorisations techniques pour améliorer la qualité du code et la maintenance de la plateforme.

### Évolutions fonctionnelles
- **Pages Partenaires :** Ajout d'un carrousel de logos de partenaires sur les pages dédiées. [#944](https://github.com/betagouv/monstagedeseconde/pull/944)
- **Page Étudiant :** Mise à jour de la page étudiant avec des améliorations non précisées. [#941](https://github.com/betagouv/monstagedeseconde/pull/941)
- **Formulaire Offres :** Amélioration de la visualisation des erreurs lors de la création d'une offre. [#937](https://github.com/betagouv/monstagedeseconde/pull/937)
- **Statut des offres :** Modification des libellés des états des candidatures dans les tableaux de bord pour plus de clarté. [#936](https://github.com/betagouv/monstagedeseconde/pull/936)
- **Suppression FAQ :** Suppression de la FAQ de la page d'accueil. [#921](https://github.com/betagouv/monstagedeseconde/pull/921)
- **Limitation description offre :** Limitation de la longueur de la description des offres via l'API. [#922](https://github.com/betagouv/monstagedeseconde/pull/922)

### Évolutions techniques
- **Refactorisation du code :** Mutualisation de code pour la vérification SIRET et la création de signatures.
- **Refactorisation des états de candidature :** Refactorisation des libellés des états des candidatures. [#936](https://github.com/betagouv/monstagedeseconde/pull/936)
- **Sécurité :** Correction d'une vulnérabilité potentielle de détournement de compte par un élève. [#932](https://github.com/betagouv/monstagedeseconde/pull/932)
- **Sécurité :** Correction d'une vulnérabilité XSS dans le rendu du contenu Prismic. [#933](https://github.com/betagouv/monstagedeseconde/pull/933)
- **Archivage des offres :** Amélioration de la tâche d'archivage automatique des offres d'entreprises.
- **Maintenance :** Mise à jour pour la maintenance estivale. [#943](https://github.com/betagouv/monstagedeseconde/pull/943)
- **Refactorisation :** Suppression d'instanciation inutile de l'objet `signature_builder`.
- **Refactorisation :** Mutualisation de `before_action :authenticate_user!` dans les contrôleurs du tableau de bord.

### Autres changements
- Mise à jour des dépendances : `websocket-driver` (0.8.0 -> 0.8.1), `view_component` (4.9.0 -> 4.12.0), `js-yaml` (3.14.2 -> 3.15.0).
- Correction de tests unitaires et système.
- Amélioration de la gestion des erreurs.
- Suppression de code obsolète.
