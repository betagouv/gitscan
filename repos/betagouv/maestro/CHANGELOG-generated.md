## Changelog : maestro (30 derniers jours, au 15 septembre 2026)

### Résumé
Ce mois-ci, Maestro a connu une évolution majeure de son module de paramétrage, offrant une plus grande flexibilité dans la gestion des plans, des sous-plans et des analytes. La gestion des utilisateurs et des droits d'accès a été renforcée pour mieux coller aux réalités métier, tandis que la gestion des domaines et des prélèvements a été fluidifiée. Ces changements visent à offrir un outil plus précis et mieux adapté aux processus de coordination nationale et régionale.

### Évolutions fonctionnelles

**Gestion du paramétrage**
- Possibilité de paramétrer les analytes [#1476], les sous-plans [#1399, #1365] et de gérer la notion de "Terminer" [#1441].
- Introduction de nouvelles notions métier : gestion des propriétaires [#1453] et gestion de la surcharge entre un plan et ses sous-plans [#1412].
- Amélioration de l'interface de configuration : ajout d'un fil d'ariane et de nouvelles actions [#1351], et réorganisation de la page de configuration des champs spécifiques [#1400].
- Possibilité de supprimer les domaines, plans et sous-plans lorsqu'ils ne sont pas terminés [#1475].
- Suppression de la version "cartes" dans le module de programmation [#1325].

**Domaines et Cartographie**
- Amélioration de la gestion des domaines : ajout de nouveaux domaines [#1343], consultation via une page dédiée [#1349] et intégration des informations directement dans la carte du domaine [#1344].
- Ajout de la notion d'année pour les domaines [#1372].
- Suppression de l'interface temporaire d'assignation des domaines aux plans au profit d'un système intégré [#1387].

**Utilisateurs et Permissions**
- Évolution des rôles et accès : création du rôle administrateur BGIR [#1337], obligation de formation pour les préleveurs [#1335], et extension des droits des coordinateurs nationaux pour voir tous les domaines [#1462].
- Amélioration de la visibilité : les coordinateurs régionaux peuvent désormais voir les commentaires de la coordination nationale [#1452].
- Optimisation de l'affichage et de la recherche : affichage des laboratoires dans la liste des utilisateurs [#1366], gestion de l'affichage des stades uniquement si nécessaire [#1350], et corrections de la recherche (sensibilité à la casse [#1324], gestion des plans multi-stages [#1411]).

**Prélèvements, Alertes et Statistiques**
- Amélioration du suivi des prélèvements : possibilité de modifier la localisation à l'étape 4 [#1414] et correction d'un bug lors de la suppression d'un prélèvement à envoyer [#1454].
- Optimisation des alertes de correction en PPV [#1474] et correction des statistiques de prélèvements non conformes sur le tableau de bord [#1384].

**Notifications**
- Intégration d'une boîte email institutionnelle pour la notification des détections [#1388].

**Autres corrections**
- Correction du moteur de recherche pour les entreprises [#1473].

### Évolutions techniques

**Architecture et Données**
- Migration de la gestion des domaines vers la base de données [#1342].
- Migration de l'outil de communication de Mattermost vers Tchap [#1430].

**Infrastructure et Tests**
- Amélioration de la fiabilité du script de sauvegarde (backup) en cas d'erreur [#1386].
- Initialisation automatique des départements sur les environnements de test (review apps) [#1367].
- Stabilisation des tests automatisés concernant l'ouverture des fenêtres modales [#1451].
