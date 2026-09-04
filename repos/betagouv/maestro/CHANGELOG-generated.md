## Changelog : maestro (30 derniers jours, au 03 septembre 2026)

### Résumé
Ce mois-ci, Maestro a franchi une étape importante dans la gestion des domaines et la configuration du système. L'expérience utilisateur a été enrichie par l'introduction de nouveaux rôles et une gestion plus fine des utilisateurs, ainsi que par l'amélioration des processus de notification et d'importation de données. Plusieurs correctifs ont également permis de stabiliser les tableaux de bord et les processus de sauvegarde.

### Évolutions fonctionnelles

**Gestion des domaines et paramétrage**
- Création et consultation de domaines, incluant l'ajout de l'année dans leurs informations [#1343](https://github.com/betagouv/maestro/issues/1343), [#1342](https://github.com/betagouv/maestro/issues/1342), [#1372](https://github.com/betagouv/maestro/issues/1372), [#1349](https://github.com/betagouv/maestro/issues/1349).
- Amélioration de la configuration via une nouvelle page dédiée pour les champs spécifiques et les sous-plans [#1400](https://github.com/betagouv/maestro/issues/1400), [#1399](https://github.com/betagouv/maestro/issues/1399), [#1365](https://github.com/betagouv/maestro/issues/1365).
- Intégration des informations de domaine directement dans la cartographie [#1344](https://github.com/betagouv/maestro/issues/1344).
- Ajout d'un fil d'ariane et de nouvelles actions dans l'interface de paramétrage [#1351](https://github.com/betagouv/maestro/issues/1351).
- Simplification de l'assignation des domaines aux plans via une gestion native [#1387](https://github.com/betagouv/maestro/issues/1387).

**Gestion des utilisateurs et accès**
- Introduction de nouveaux rôles, notamment pour les administrateurs BGIR [#1337](https://github.com/betagouv/maestro/issues/1337).
- Capacité pour les coordinateurs de gérer leurs propres utilisateurs [#1280](https://github.com/betagouv/maestro/issues/1280).
- Affichage du laboratoire dans la liste des utilisateurs [#1366](https://github.com/betagouv/maestro/issues/1366) et gestion de l'accès conditionnée à la formation pour les préleveurs [#1335](https://github.com/betagouv/maestro/issues/1335).
- Optimisation de la recherche d'utilisateurs (gestion des majuscules et des plans à plusieurs stades) [#1324](https://github.com/betagouv/maestro/issues/1324), [#1411](https://github.com/betagouv/maestro/issues/1411), [#1311](https://github.com/betagouv/maestro/issues/1311).
- Optimisation de la récupération des données utilisateurs pour plus de légèreté [#1336](https://github.com/betagouv/maestro/issues/1336).

**Notifications et données**
- Ajout d'une boîte email institutionnelle pour les notifications de détection [#1388](https://github.com/betagouv/maestro/issues/1388).
- Réponse automatique aux laboratoires en cas d'adresse email incorrecte [#1305](https://github.com/betagouv/maestro/issues/1305).
- Lecture des rapports PDF des LNR [#1304](https://github.com/betagouv/maestro/issues/1304).
- Gestion du fichier déclencheur lors de l'envoi d'une DAI via SFTP [#1289](https://github.com/betagouv/maestro/issues/1289).

**Corrections**
- Correction de la localisation lors de l'étape 4 des prélèvements [#1414](https://github.com/betagouv/maestro/issues/1414).
- Fiabilisation de l'importation de fichiers (Cereco, Inovalys, Girpa) [#1306](https://github.com/betagouv/maestro/issues/1306), [#1276](https://github.com/betagouv/maestro/issues/1276), [#1275](https://github.com/betagouv/maestro/issues/1275).
- Correction des statistiques sur le tableau de bord (prélèvements non conformes et détails par région) [#1384](https://github.com/betagouv/maestro/issues/1384), [#1288](https://github.com/betagouv/maestro/issues/1288).
- Mise à jour automatique du laboratoire destinataire lors du changement de matrice [#1274](https://github.com/betagouv/maestro/issues/1274).

### Évolutions techniques
- Migration des domaines vers une gestion en base de données [#1342](https://github.com/betagouv/maestro/issues/1342).
- Amélioration de la robustesse du script de sauvegarde (arrêt immédiat en cas d'erreur) [#1386](https://github.com/betagouv/maestro/issues/1386).
- Initialisation automatique des départements sur les environnements de revue (review apps) [#1367](https://github.com/betagouv/maestro/issues/1367).
- Suppression de la version "cartes" de la programmation pour simplifier le code [#1325](https://github.com/betagouv/maestro/issues/1325).

### Autres changements
- Mise à jour de PostCSS [#1310](https://github.com/betagouv/maestro/issues/1310).
