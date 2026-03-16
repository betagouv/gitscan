## Changelog : portail-rse (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions du portail RSE se concentrent sur l'amélioration de l'intégration avec Proconnect, la gestion des utilisateurs et des entreprises, ainsi que sur l'ajout de nouveaux indicateurs et l'amélioration de l'export de données. Des corrections de bugs et des refactorisations ont également été apportées pour améliorer la stabilité et la maintenabilité du code.

### Évolutions fonctionnelles
- **Proconnect :** Amélioration de l'intégration avec Proconnect pour gérer les invitations et l'association des utilisateurs aux entreprises, notamment en empêchant un utilisateur d'être rattaché à une entreprise déjà existante [#767bace](https://github.com/betagouv/portail-rse/commit/767bace).
- **Gestion des utilisateurs :**
    - Possibilité pour un utilisateur de changer sa fonction RSE.
    - Affichage de l'état "Conseiller RSE" dans l'administration et le menu utilisateur.
    - Amélioration du formulaire de modification de compte pour la compatibilité CORS.
    - Simplification de la cinématique d'invitation et enregistrement du choix utilisateur (membre ou conseiller).
- **Entreprises :**
    - Prise en compte des noms d'entreprises longs dans le tableau des entreprises accompagnées.
    - Suppression de la colonne "propriétaires" du tableau des entreprises accompagnées.
    - Correction d'un bug empêchant la session de fonctionner après la suppression d'une entreprise [#c2f7859](https://github.com/betagouv/portail-rse/commit/c2f7859).
- **Indicateurs VSME :** Ajout de la date du premier indicateur rempli sur un rapport VSME [#6a3d6ff](https://github.com/betagouv/portail-rse/commit/6a3d6ff).
- **Indicateurs C4 :** Ajout et configuration des indicateurs C4, incluant la gestion de la non-applicabilité et l'export dans les fichiers Excel [#86567b3](https://github.com/betagouv/portail-rse/commit/86567b3), [#7ace305](https://github.com/betagouv/portail-rse/commit/7ace305), [#6e211b6](https://github.com/betagouv/portail-rse/commit/6e211b6), [#4e1753b](https://github.com/betagouv/portail-rse/commit/4e1753b).
- **Invitations :** Acceptation automatique de l'invitation en arrivant sur l'URL d'invitation [#cce9590](https://github.com/betagouv/portail-rse/commit/cce9590).

### Évolutions techniques
- **Refactoring :** Plusieurs refactorisations ont été effectuées pour simplifier le code, améliorer sa lisibilité et sa maintenabilité, notamment dans les tests et la gestion des variables.
- **Tests :** Amélioration et suppression de tests devenus non pertinents.
- **OIDC :** Modifications et corrections liées à l'intégration OIDC, incluant la redirection après connexion et la gestion des tests en CI [#fa1e7b0](https://github.com/betagouv/portail-rse/commit/fa1e7b0), [#d80d175](https://github.com/betagouv/portail-rse/commit/d80d175).
- **Modèles :** Modifications des modèles utilisateur et entreprise pour supporter les nouvelles fonctionnalités.

### Autres changements
- **Documentation :** Précisions sur les e-mails à utiliser en recette avec ProConnect [#07c02a7](https://github.com/betagouv/portail-rse/commit/07c02a7).
- **Suppression de code inutile :** Suppression de templates et de code non utilisés.
- **Script d'export :** Correction et amélioration du script d'export `origine_departement` [#dcc541f](https://github.com/betagouv/portail-rse/commit/dcc541f).
- **Badge Beta :** Suppression du badge "beta" dans l'en-tête des pages [#6331f43](https://github.com/betagouv/portail-rse/commit/6331f43).
- **Mise à jour de dépendance :** Mise à jour de la dépendance `joserfc` de 1.4.2 à 1.6.3 [#c5bedde](https://github.com/betagouv/portail-rse/commit/c5bedde).
