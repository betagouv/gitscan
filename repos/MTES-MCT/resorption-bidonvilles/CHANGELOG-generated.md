## Changelog : resorption-bidonvilles (30 derniers jours, au 2026-04-17)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'export des données, notamment des actions, avec une granularité accrue des permissions et la prise en compte de la territorialité. Des corrections et améliorations ont également été apportées à l'interface utilisateur et à la gestion des données, ainsi qu'à la robustesse de l'application.

### Évolutions fonctionnelles
- **Export des actions :**
    - Ajout de la possibilité d'exporter les actions par les correspondants et administrateurs locaux, avec des permissions spécifiques. [#1437](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1437)
    - Gestion du filtrage territorial pour l'export des actions, en fonction des zones d'intervention de l'utilisateur.
    - Possibilité de sélectionner l'année par défaut lors de l'exportation.
    - Prise en compte des données financières dans l'export (avec possibilité de les exclure).
- **Permissions :**
    - Ajout de la permission `access_action_finances` pour les acteurs nationaux.
    - Gestion réactive des options pour les autorisations utilisateur.
- **Interface utilisateur :**
    - Amélioration de l'affichage des badges de statistiques (taux de mise à jour des sites et des populations).
    - Correction de l'affichage du département dans l'onglet 'tous'.
    - Correction du comportement lors des modifications d'action.
    - Correction d'un bug empêchant le rechargement de la page lors du clic sur un élément de liste.
- **Notifications & Alertes:**
    - Affichage des indicateurs de mise à jour de population dans l'email récapitulatif hebdomadaire.
    - Ajout des indicateurs de mise à jour de population sur 3 mois.

### Évolutions techniques
- **Refactoring :**
    - Utilisation de `refreshViewCascade` et `refreshView` pour une meilleure gestion des vues interdépendantes.
    - Remplacement de `parseInt` par `Number.parseInt` et de `reverse` par `toReversed` pour une meilleure conformité aux standards.
    - Suppression de dépendances circulaires dans le routeur.
- **Infrastructure & CI/CD :**
    - Mise à jour des fichiers générés et exemple de preview.
    - Correction du build pour inclure les fichiers JSON des seeders.
- **Tests :**
    - Ajout de tests unitaires pour les nouvelles fonctionnalités.
    - Correction de tests unitaires existants.
- **Code qualité :**
    - Corrections pour satisfaire les règles de SonarQube.
    - Suppression de code inutile et amélioration de la clarté du code.
    - Utilisation de Lodash pour certaines opérations.

### Autres changements
- Mise à jour de la documentation.
- Correction de la gestion du click.
- Correction de la date de MAJ de population.
- Amélioration de la hauteur de la popup.
- Ajout de la popup d'export des actions.
- Correction de l'expiration du jeton d'activation (passée de 10 minutes à 168 heures).
- Correction d'erreurs de linting.
- Suppression d'un log inutile.
- DSFRisation de l'affichage des erreurs d'export.
- Ajout de la data dans l'historisation du site.
- Ajout du champ `dihalFinancingYear` au type Action et affichage de l'année dans le badge 'Financement DIHAL'.
- Correction de la formulation des taux de mises à jour.
- Ajout de l'adresse de messagerie du demandeur d'accès.
- Correction du lien de demande d'info en demande d'accès.
- Ajout de la gestion des erreurs si l'API est inaccessible.
- Ajout d'un bloc pour gérer l'affichage d'erreur si l'API est inaccessible.
- Correction du nom de migration et peuplement des données.
- Ajout de la date de modification des habitants.
- Correction de l'appel à la `fakeAction`.
- Simplification de l'appel à la `fakeAction`.
- Amélioration du test unitaire.
- Correction de l'affichage du département dans l'onglet 'tous'.
- Ajout de la popup d'export des actions.
- Ajout de la gestion des erreurs si l'API est inaccessible.
- Correction de l'expiration du jeton d'activation.
- Correction de la gestion du click.
- Correction du comportement lors des modifications d'action.
- Correction du rechargement de la page lors du clic sur un élément de liste.
- Correction des erreurs "Argument of type 'null' is not assignable to parameter of type 'number[] | undefined'".
- Ajout de `dihalFinancingYear` à la factory action.
- Affichage de l'année dans le badge 'Financement DIHAL'.
- Filtrage des actions par année de financement DIHAL.
- Ajout de tests unitaires pour `mergeFinance`.
- Calcul de l'année la plus récente pour laquelle existe un financement Dihal dans `mergeFinances`.
- Changement du label du filtre Financement et suppression des options statiques.
- Génération dynamique des options du filtre Financement DIHAL.
- Nommage de la fonction fléchée.
- Correction du nom de la fonction et de certains blocs de code.
- Initialisation de `dihalFinancingYear` dans `hashActions`.
- Ajout du champ `dihalFinancingYear` au type Action.
- Ajout de l'adresse de messagerie du demandeur d'accès.
- Correction du lien de demande d'info en demande d'accès.
- Correction de l'expiration du jeton d'activation.
- Correction de l'action utilisée pour les tests, empêchant le build API.
- Correction du yarn.lock avec lodash.
- Correction de l'affichage du département dans l'onglet 'tous'.
- Amélioration du score du code.
- DSFRisation de l'affichage de l'erreur d'export.
- Sécurisation et transmission des datas pour le header des actions.
- Intégration du header des Actions avec taux calculé.
- Correction de l'expiration du jeton d'activation.
- Correction de l'erreur lors de la modification d'action.
- Correction du comportement lors des modifications d'action.
- Correction de l'erreur "Argument of type 'null' is not assignable to parameter of type 'number[] | undefined'".
- Ajout de `dihalFinancingYear` à la factory action.
- Affichage de l'année dans le badge 'Financement DIHAL'.
- Filtrage des actions par année de financement DIHAL.
- Ajout de tests unitaires pour `mergeFinance`.
- Calcul de l'année la plus récente pour laquelle existe un financement Dihal dans `mergeFinances`.
- Changement du label du filtre Financement et suppression des options statiques.
