## Changelog : dora (30 derniers jours, au 07/08/2026)

### Résumé
Ce mois-ci, Dora a bénéficié d'améliorations visant à fluidifier la recherche et l'expérience utilisateur, notamment par une meilleure gestion des résultats et des erreurs. Des travaux importants ont également été menés sur la fiabilité des données, la synchronisation des informations liées aux orientations et la mise en conformité (accessibilité et CGU).

### Évolutions fonctionnelles
- **Recherche et navigation** :
    - Limitation du nombre de résultats de recherche pour améliorer la lisibilité [#1245].
    - Activation de la recherche via la touche "Entrée" [#1230].
    - Amélioration de la pertinence de la recherche sémantique en excluant systématiquement les doublons [#1228].
    - Annulation du test A/B concernant la recherche textuelle [#1246].
- **Expérience utilisateur (UX)** :
    - Allègement du tableau des structures dans le tableau de bord des gestionnaires de territoire [#1229].
    - Amélioration de la gestion des erreurs : affichage d'une erreur 404 pour un service inaccessible au lieu d'une redirection vers la page de connexion [#1224].
    - Filtrage du balisage Markdown dans les descriptions courtes des services [#1221].
- **Données et exports** :
    - Exclusion de certaines sources de données du formulaire Dora [#1225].
    - Ajout d'une fonctionnalité d'export des orientations "Les Emplois" [#1209].
- **Conformité et légal** :
    - Mise à jour de la déclaration d'accessibilité [#1202].
    - Mise à jour des Conditions Générales d'Utilisation (CGU) [#1182].

### Évolutions techniques
- **Gestion des données et base de données** :
    - Migration du champ `kinds` de M2M vers `ArrayField` pour les recherches sauvegardées et les vues de recherche [#1247].
    - Garantie de l'unicité de tous les critères d'admission [#1243].
    - Ajout d'une commande pour supprimer les anciennes structures orphelines [#1219].
    - Stockage du code de la zone géographique (commune, département ou région) dans les statistiques [#1216].
    - Amélioration de la synchronisation des statuts des orientations "Les Emplois" (nouveau endpoint et ajout du champ `processing_date`) [#1169, #1212, #1190].
- **Refactoring et optimisation** :
    - Retrait de la recherche DORA de la recherche de services [#1201].
    - Nettoyage du code : suppression de la méthode `_map_dora_kinds_to_di` [#1199] et optimisation du traitement des résultats de services [#1176, #1175].
    - Passage des vues d'administration en lecture seule pour les statistiques [#1179].
- **Infrastructure et maintenance** :
    - Mise à jour majeure de la bibliothèque de cartographie `maplibe-gl` [#1231].
    - Remplacement de la bibliothèque de génération de fichiers Excel [#1191].
    - Protection contre la suppression en cascade d'objets [#1220].
    - Optimisation du reporting d'erreurs vers Sentry pour éviter les doublons [#1203].
    - Augmentation de la couverture de tests sur les critères d'orientabilité des services [#1227].

### Autres changements
- Correction du tri des imports dans certains fichiers Python [#1200].
- Amélioration du client de données fictives (`FakeDataInclusionClient`) pour les tests [#1198].
