## Changelog : ma-cantine (30 derniers jours, au 13 juillet 2026)

### Résumé
Les dernières mises à jour de ma-cantine améliorent l'expérience utilisateur pour les achats, notamment avec une meilleure présentation des informations et la correction de bugs liés aux imports et à l'envoi de formulaires. Des améliorations techniques ont été apportées à l'API et à l'historisation des données, ainsi qu'à la gestion des commandes et des logs.

### Évolutions fonctionnelles
- Ajout d'un bandeau de service réduit pour le contact ([#6889](https://github.com/betagouv/ma-cantine/issues/6889)).
- Amélioration de la présentation des libellés et des valeurs dans les formulaires d'achats ([#6885](https://github.com/betagouv/ma-cantine/issues/6885)).
- Remontée du bloc de facture dans les achats ([#6888](https://github.com/betagouv/ma-cantine/issues/6888)).
- Correction du bug d'envoi du formulaire "Acteurs de l'écosystème" ([#6895](https://github.com/betagouv/ma-cantine/issues/6895)).
- Correction de la colonne "definition_local_km" dans les nouveaux imports d'achats ([#6896](https://github.com/betagouv/ma-cantine/issues/6896)).
- Correction du lien vers l'ancienne page d'import des achats SIRET ([#6884](https://github.com/betagouv/ma-cantine/issues/6884)).
- Renommage de la catégorie 'Boulangerie / Pâtisserie fraîches' pour enlever 'et surgelées' ([#6890](https://github.com/betagouv/ma-cantine/issues/6890)).
- Ajout des nouveaux guides du CNRC dans la section "Ressources" ([#6835](https://github.com/betagouv/ma-cantine/issues/6835)).
- Ajout d'un sélecteur de cantine lors de la duplication d'un achat ([#6823](https://github.com/betagouv/ma-cantine/issues/6823)).

### Évolutions techniques
- Amélioration de l'API : regroupement des endpoints par lot fonctionnel ([#6886](https://github.com/betagouv/ma-cantine/issues/6886)).
- Correction des warnings affichés dans la console Swagger de l'API ([#6891](https://github.com/betagouv/ma-cantine/issues/6891)).
- Ajout de champs `creation_user` et `creation_source` pour suivre l'origine de la création des données (cantines, bilans, achats, évaluations de gaspillage) ([#6831](https://github.com/betagouv/ma-cantine/issues/6831)).
- Refactor de l'historisation des données : ajout d'un nouveau champ `history_source_api_oauth2_application` pour identifier l'application OAuth2 ayant modifié un objet ([#6869](https://github.com/betagouv/ma-cantine/issues/6869)).
- Refactor de l'historisation : déplacement des signals dans le modèle ([#6865](https://github.com/betagouv/ma-cantine/issues/6865)).
- Ajout d'une nouvelle classe `MaCantineBaseCommand` pour gérer le loggage des résultats des commandes de gestion ([#6838](https://github.com/betagouv/ma-cantine/issues/6838)).
- Ajout d'une table `CommandLog` pour stocker les résultats des commandes de gestion ([#6837](https://github.com/betagouv/ma-cantine/issues/6837)).
- Restriction de l'accès aux achats via l'API pour les éditeurs à leurs propres achats ([#6858](https://github.com/betagouv/ma-cantine/issues/6858)).
- Ouverture de l'accès aux achats via l'API pour les éditeurs (OAuth2) ([#6857](https://github.com/betagouv/ma-cantine/issues/6857)).
- Nouvel endpoint API pour la création d'achats avec des caractéristiques divisées en 4 parties ([#6855](https://github.com/betagouv/ma-cantine/issues/6855)).
- Nouvel endpoint API pour la récupération, la modification et la suppression d'achats avec des caractéristiques divisées en 4 parties ([#6810](https://github.com/betagouv/ma-cantine/issues/6810)).
- Nouvel endpoint API dédié à l'upload et la suppression de factures ([#6840](https://github.com/betagouv/ma-cantine/issues/6840)).

### Autres changements
- Documentation de l'API : masquage du champ `creation_source` dans Swagger ([#6864](https://github.com/betagouv/ma-cantine/issues/6864), [#6863](https://github.com/betagouv/ma-cantine/issues/6863)).
- Documentation de l'API : remplissage du `help_text` des champs avec leur `verbose_name` ([#6862](https://github.com/betagouv/ma-cantine/issues/6862)).
- Refactor : remplacement de `authentication_method` par `history_source` dans l'historisation ([#6866](https://github.com/betagouv/ma-cantine/issues/6866)).
- Refactor : ajout de `history_source` à d'autres modèles (Canteen, Diagnostic, WasteMeasurement, ResourceAction) ([#6868](https://github.com/betagouv/ma-cantine/issues/6868)).
- Ajout des nouvelles propriétés `categories_egalim`, `origine`, `est_local` et `est_circuit_court` aux achats ([#6807](https://github.com/betagouv/ma-cantine/issues/6807)).
- Refonte de la définition de "local" avec l'ajout d'un nouveau champ `definition_local_km` et des modifications des choix ([#6845](https://github.com/betagouv/ma-cantine/issues/6845)).
- Amélioration de l'organisation de la page d'imports ([#6846](https://github.com/betagouv/ma-cantine/issues/6846)).
- Correction d'un revert sur le fichier achats.json (fix du pre-commit) ([#6848](https://github.com/betagouv/ma-cantine/issues/6848)).
- Ajout du champ `groupe_snapshot` au modèle `Diagnostic` et affichage dans l'admin ([#6799](https://github.com/betagouv/ma-cantine/issues/6799)).
- Remplissage du champ `groupe_snapshot` pour les TD générées ([#6818](https://github.com/betagouv/ma-cantine/issues/6818)).
