## Changelog : dora (30 derniers jours, au 05/08/2026)

### Résumé
Ce mois-ci, la plateforme Dora a bénéficié d'améliorations significatives de son interface utilisateur pour faciliter la navigation et la recherche. Les capacités de synchronisation de données avec des partenaires externes (notamment "Les Emplois") ont été renforcées, tandis que des travaux importants de nettoyage technique et de mise à jour des outils ont été réalisés pour garantir la stabilité et la performance du système.

### Évolutions fonctionnelles
- **Amélioration de l'interface et de l'ergonomie** :
    - Allègement du tableau des structures dans le tableau de bord des gestionnaires de territoire [#1229].
    - Activation de la recherche via la touche "Entrée" [#1230].
    - Amélioration du bouton de suppression des options dans les menus déroulants [#1156].
    - Filtrage du balisage Markdown dans les descriptions courtes des services [#1221].
    - Affichage de la source de l'orientation directement sur la page dédiée [#1155].
- **Expérience utilisateur et recherche** :
    - Gestion des doublons dans la recherche sémantique pour des résultats plus précis [#1228].
    - Affichage d'une erreur 404 explicite pour les services inaccessibles au lieu d'une redirection vers la connexion [#1224].
    - Exclusion des sources "data·inclusion" du formulaire Dora [#1225].
- **Nouvelles fonctionnalités et statistiques** :
    - Ajout d'une commande d'export des orientations pour "Les Emplois" [#1209].
    - Stockage des codes de zones géographiques (commune, département, région) pour enrichir les statistiques [#1216].
    - Passage des vues administratives en mode lecture seule pour les statistiques [#1179].

### Évolutions techniques
- **Synchronisation et gestion des données** :
    - Renforcement de la synchronisation des orientations avec "Les Emplois" via l'ajout d'identifiants uniques (UUID) [#1157], de dates de traitement [#1212] et d'un nouvel endpoint dédié [#1169].
    - Synchronisation de la table des données d'orientation des emplois [#1190].
    - Mise en place d'une commande de suppression des anciennes structures orphelines [#1219].
- **Maintenance et refactoring** :
    - Nettoyage du code suite à la mise en place de la recherche unifiée [#1095].
    - Suppression de méthodes, filtres et listes intermédiaires devenus obsolètes [#1199, #1176, #1201, #1175].
    - Protection contre les suppressions d'objets en cascade [#1220].
- **Infrastructure et outils** :
    - Mise à jour majeure de la bibliothèque cartographique MapLibre-GL [#1231].
    - Remplacement de la bibliothèque de génération de fichiers Excel [#1191].
    - Optimisation de la remontée d'erreurs vers Sentry (correction des faux positifs sur Safari et les doublons) [#1203, #1164, #1160].
    - Amélioration des outils de test et de la couverture sur les critères d'orientabilité [#1227, #1198].
    - Ajustements de l'environnement de build (NPM, constantes API BAN) [#1166, #1167, #1168].

### Autres changements
- **Conformité et légal** : Mise à jour de la déclaration d'accessibilité [#1202] et des Conditions Générales d'Utilisation (CGU) [#1182].
- **Nettoyage** : Suppression des données de l'application Admin Express [#1154] et corrections diverses (typos, tri des imports) [#1181, #1200].
