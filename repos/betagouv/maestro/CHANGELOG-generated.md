## Changelog : maestro (30 derniers jours, au 01/09/2026)

### Résumé
Ce mois-ci, Maestro a franchi une étape majeure avec l'intégration complète de la gestion des domaines dans la base de données. La plateforme a également été enrichie par de nouvelles capacités de gestion des utilisateurs et des permissions, ainsi que par une amélioration significative de l'automatisation et de la fiabilité des imports de données (LNR, Cereco, Girpa, SFTP).

### Évolutions fonctionnelles
- **Gestion des domaines** : Mise en place complète du cycle de vie des domaines (ajout, consultation, cartographie des informations et liaison avec les plans) [#1343, #1344, #1349, #1372, #1373, #1387].
- **Paramétrage et navigation** : Gestion des sous-plans, ajout d'un fil d'ariane et nouvelle interface de configuration des champs spécifiques [#1351, #1365, #1399, #1400].
- **Utilisateurs et accès** : 
    - Introduction du nouveau rôle d'administrateur BGIR et possibilité pour les coordinateurs de gérer leurs propres utilisateurs [#1280, #1337].
    - Mise en place de l'obligation de formation pour les préleveurs [#1335].
    - Améliorations de l'interface utilisateur : affichage des laboratoires dans la liste, gestion optimisée des stades de prélèvement et correction de la recherche [#1311, #1324, #1350, #1366].
- **Traitement des données et imports** : 
    - Lecture des rapports PDF des LNR [#1304] et gestion des fichiers déclencheurs SFTP pour les envois de DAI [#1289].
    - Corrections et améliorations sur les imports Cereco, Girpa, Inovalys et le nettoyage des références de données [#1263, #1264, #1265, #1275, #1276, #1306].
- **Notifications et tableau de bord** : 
    - Ajout de notifications par email institutionnel pour les détections [#1388] et réponse automatique en cas d'email incorrect [#1305].
    - Corrections des statistiques de conformité et de l'affichage des détails dans le tableau de bord [#1262, #1288, #1384].
- **Référentiel** : Ajout de la substance active cyprosulfamide [#1246].
- **Interface** : Suppression de la version "cartes" de la programmation [#1325].

### Évolutions techniques
- **Architecture et performance** : 
    - Migration de la gestion des domaines vers la base de données [#1342].
    - Refactorisation du code d'extraction des références laboratoires pour une meilleure maintenance [#1247].
    - Optimisation de la consommation de mémoire lors de la mise à jour des départements [#1260].
- **Fiabilité et DevOps** : 
    - Amélioration de la robustesse du script de sauvegarde en cas d'erreur [#1386].
    - Initialisation automatique des départements sur les environnements de revue (review apps) [#1367].
