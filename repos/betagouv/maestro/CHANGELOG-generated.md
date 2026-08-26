## Changelog : maestro (30 derniers jours, au 25 août 2026)

### Résumé
Ce mois a été marqué par un développement majeur autour de la gestion des domaines, qui sont désormais intégrés à la base de données avec de nouvelles capacités de consultation et d'assignation. La gestion des utilisateurs a également été renforcée par l'introduction de nouveaux rôles et de nouvelles règles d'accès. Enfin, plusieurs améliorations ont été apportées à l'automatisation des échanges de données (email, SFTP) et à la précision des rapports et tableaux de bord.

### Évolutions fonctionnelles
- **Gestion des domaines** : 
    - Possibilité de créer de nouveaux domaines [#1343].
    - Création d'une page dédiée pour la consultation des domaines [#1349] et affichage de leurs informations sur une carte [#1344].
    - Ajout de la notion d'année pour les domaines [#1372] et mise en place d'une interface pour l'assignation des domaines aux plans [#1373].
- **Gestion des utilisateurs et accès** : 
    - Création du rôle d'administrateur BGIR [#1337].
    - Autorisation donnée aux coordinateurs pour gérer leurs propres utilisateurs [#1280].
    - Mise en place d'une condition d'accès pour les préleveurs (nécessité d'être formé) [#1335].
    - Améliorations de l'interface : affichage du laboratoire dans la liste des utilisateurs [#1366], recherche insensible à la casse [#1324] et affichage conditionnel des stades [#1350].
- **Traitement des données et rapports** : 
    - Lecture des rapports PDF des LNR [#1304].
    - Ajout de la substance active cyprosulfamide dans le référentiel [#1246].
    - Ajout d'un filtre sur la date d'envoi des DAI [#1231].
- **Automatisation et flux** : 
    - Gestion du fichier déclencheur lors des envois SFTP de DAI [#1289].
    - Réponse automatique par email au laboratoire en cas d'adresse incorrecte [#1305].
    - Mise à jour automatique du laboratoire destinataire lors d'un changement de matrice de prélèvement [#1274].
- **Corrections et interface** : 
    - Corrections sur les flux de données spécifiques (Cereco, Girpa, Inovalys) pour améliorer la fiabilité des analyses [#1306, #1275, #1276, #1265, #1264].
    - Améliorations de l'ergonomie : ajout d'un fil d'ariane [#1351], gestion des sous-plans [#1365] et corrections d'affichage sur les tableaux de bord et les listes de documents [#1288, #1262, #1232, #1230, #1229].

### Évolutions techniques
- **Architecture et données** : Migration de la gestion des domaines vers la base de données [#1342].
- **Optimisation des performances** : 
    - Réduction de la consommation de mémoire vive (RAM) lors de la mise à jour des départements [#1260].
    - Optimisation de la récupération des informations utilisateurs pour plus de légèreté [#1336].
- **Maintenance du code** : Refactorisation du code d'extraction des références Maestro pour mutualiser les processus [#1247].
