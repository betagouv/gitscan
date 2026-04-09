## Changelog : grist-core (30 derniers jours, au 2026-04-08)

### Résumé
Les dernières semaines ont été marquées par des améliorations de la stabilité et de la fiabilité du logiciel, notamment en corrigeant des problèmes de tests aléatoires et en améliorant la gestion des imports depuis Airtable. Des efforts ont également été déployés pour améliorer l'expérience utilisateur, notamment dans les formulaires et l'interface d'administration, ainsi que pour la traduction dans plusieurs langues. Enfin, des fondations pour de nouvelles fonctionnalités, comme les automatisations et l'authentification, ont été posées.

### Évolutions fonctionnelles
- **Import Airtable :** Amélioration de l'importation depuis Airtable, avec la prise en charge des couleurs des choix et la conversion des références de champs en colonnes de type "Ref" (#2199, #2201). Possibilité de mettre à jour les lignes existantes lors de l'importation (#2216).
- **Formulaires :** Amélioration de l'accessibilité des champs "select" pour les lecteurs d'écran (#2164).
- **Automatisations :** Ajout d'une nouvelle interface utilisateur pour les déclencheurs de documents dans le cadre des automatisations (#2205).
- **Authentification :** Ajout d'une page de configuration initiale et d'une connexion via clé d'amorçage (#2250).
- **Suggestions :** Amélioration de l'affichage des différences dans le mode suggestion (#2140).
- **SCIM :** Accélération de la recherche d'utilisateurs dans le protocole SCIM (#2070).
- **Gestion des abonnements :** Ajout de bannières d'abonnement et mise en lecture seule du site en cas de problème d'abonnement.

### Évolutions techniques
- **Tests :** Correction de plusieurs tests aléatoires (flakiness) dans différents modules (DocTutorial, PageWidgetPicker, AccessRules2, Search2, UserManager, GranularAccess, CursorSaving) (#2244, #2247, #2248, #2250, #2224, #2232).
- **Infrastructure :** Mise à jour de plusieurs dépendances, notamment `axios`, `mocha-webdriver`, `@gristlabs/sqlite3` et `handlebars`.
- **Docker :** Amélioration des builds Docker et utilisation de `gristlabs/gvisor-unprivileged`.
- **Architecture :** Refonte de la gestion des liens ancrés dans les commentaires pour utiliser des URL relatives.
- **Storybook :** Ajout de Storybook pour documenter les composants de l'interface utilisateur.
- **Vercel/NFT :** Remplacement de Browserify par Vercel/NFT pour la gestion des fichiers.
- **Logging :** Réduction du niveau de détail des logs pour l'API.

### Autres changements
- **Traduction :** Ajout et mise à jour de traductions dans plusieurs langues (français, allemand, suédois, catalan, portugais brésilien, hongrois, grec, basque, tamoul, indonésien).
- **Documentation :** Mise à jour de la documentation sur le format des données Grist et ajout d'informations sur les valeurs de référence.
- **README :** Mise à jour de la liste des fonctionnalités dans le fichier README.md.
- **CLA :** Signature du CLA par plusieurs contributeurs.
- **Nettoyage de code :** Diverses corrections de typos et améliorations de la lisibilité du code.
