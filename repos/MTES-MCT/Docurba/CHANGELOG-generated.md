## Changelog : Docurba (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, Docurba a bénéficié d'améliorations significatives sur l'interface utilisateur, notamment une refonte du menu utilisateur et une meilleure gestion des filtres de recherche. Des efforts importants ont également été consacrés à la gestion des données, en particulier pour la conformité avec la loi Huwart, avec des corrections et des ajouts pour assurer la précision et l'intégrité des informations. Enfin, des optimisations techniques ont été apportées à l'infrastructure et aux tests.

### Évolutions fonctionnelles
- **Interface utilisateur :** Le menu utilisateur a été amélioré avec un menu déroulant plus clair et intuitif, incluant un bouton dédié pour accéder au tableau de bord. [#1868](https://github.com/MTES-MCT/Docurba/issues/1868)
- **Navigation :** Le département sélectionné est maintenant conservé lors de la navigation, améliorant l'expérience utilisateur.
- **Recherche :** Les champs de recherche sont maintenant synchronisés avec les paramètres de l'URL, permettant de conserver les filtres appliqués.
- **Gestion des PLU/PLUi :** Mise à jour en masse du type de document des procédures de PLU vers PLUi.
- **Accès aux données :** Exposition des thématiques des procédures dans les APIs SCoT et communes.
- **Page PAC :** La page de lecture des PAC est désormais accessible au public.

### Évolutions techniques
- **Architecture :** L'application `internal_api` a été déplacée dans le répertoire `docurba` pour une meilleure organisation.
- **Tests :**
    - Intégration de FactoryBoy pour la création d'objets de test plus robustes et maintenables.
    - Ajout de factories pour les objets User, Profile, Procedure et CommuneProcedure.
    - Amélioration des tests de l'API SCoT.
    - Correction de tests instables.
- **Infrastructure :**
    - Mise à jour de Django (6.0.4 -> 6.0.5).
    - Mise à jour de djangorestframework (3.16.1 -> 3.17.1).
    - Mise à jour de urllib3 (2.6.3 -> 2.7.0).
    - Mise à jour de pre-commit (4.5.1 -> 4.6.0).
    - Mise à jour de ruff (0.15.10 -> 0.15.11 et 0.15.11 -> 0.15.12).
    - Augmentation de la taille du disque et du plan Supabase pour les environnements de revue.
- **Base de données :**
    - Ajout d'une colonne `started_before_huwart_law` dans la table `Procedure` pour indiquer si une procédure a débuté avant la loi Huwart.
    - Ajout d'un index personnalisé `OversizedIndex` pour améliorer les performances.
    - La colonne `commune_id` de la table `CommuneProcedure` est maintenant générée automatiquement.
    - Suppression des événements de fin d'échéance pour se conformer à la loi Huwart.

### Autres changements
- **Documentation :** Ajout de documentation pour les thématiques des procédures dans les APIs communes et SCoT.
- **Code :** Simplification de la commande de gestion `fill_started_before_huwart_law`.
- **Configuration :** Correction de conflits de migration Django.
- **Nettoyage :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Makefile:** Mise à jour et simplification du Makefile.
