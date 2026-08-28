## Changelog : maestro (30 derniers jours, au 25 août 2026)

### Résumé
Ce mois-ci, Maestro a franchi des étapes importantes dans la gestion des domaines (création, consultation et cartographie) et le renforcement de la gestion des utilisateurs (nouveaux rôles et droits de gestion). La fiabilité du traitement des données a également été améliorée grâce à de nombreuses corrections sur les processus d'importation (Cereco, Girpa, Inovalys) et une meilleure gestion des flux SFTP.

### Évolutions fonctionnelles

**Gestion des domaines et planification**
- Mise en place complète du cycle de vie des domaines : création de nouveaux domaines [#1343](https://github.com/betagouv/maestro/issues/1343), consultation via une page dédiée [#1349](https://github.com/betagouv/maestro/issues/1349) et intégration des informations sur la carte [#1344](https://github.com/betagouv/maestro/issues/1344).
- Ajout de la notion d'année pour les domaines [#1372](https://github.com/betagouv/maestro/issues/1372) et interface temporaire pour l'assignation des domaines aux plans [#1373](https://github.com/betagouv/maestro/issues/1373).
- Ajout de la liste des sous-plans dans le paramétrage [#1365](https://github.com/betagouv/maestro/issues/1365).

**Utilisateurs et accès**
- Évolution des rôles : création du rôle administrateur BGIR [#1337](https://github.com/betagouv/maestro/issues/1337) et possibilité pour les coordinateurs de gérer leurs propres utilisateurs [#1280](https://github.com/betagouv/maestro/issues/1280).
- Renforcement de la sécurité : l'accès pour les préleveurs est désormais conditionné par une formation [#1335](https://github.com/betagouv/maestro/issues/1335).
- Améliorations de l'interface utilisateur : affichage du laboratoire dans la liste des utilisateurs [#1366](https://github.com/betagouv/maestro/issues/1366), optimisation de l'affichage des stades [#1350](https://github.com/betagouv/maestro/issues/1350) et correction de la recherche (sensibilité à la casse) [#1324](https://github.com/betagouv/maestro/issues/1324).

**Traitement des données et imports**
- Amélioration de la lecture des rapports PDF des LNR [#1304](https://github.com/betagouv/maestro/issues/1304).
- Fiabilisation des imports de données : corrections sur les fichiers Cereco (feuilles multiples, complexité chimique), Girpa (lignes de forfait, méthodes d'analyse) et Inovalys (récupération des références) [#1306](https://github.com/betagouv/maestro/issues/1306), [#1264](https://github.com/betagouv/maestro/issues/1264), [#1275](https://github.com/betagouv/maestro/issues/1275), [#1265](https://github.com/betagouv/maestro/issues/1265), [#1276](https://github.com/betagouv/maestro/issues/1276).
- Automatisation : réponse automatique aux laboratoires en cas d'adresse email incorrecte [#1305](https://github.com/betagouv/maestro/issues/1305) et gestion du fichier déclencheur lors de l'envoi d'une DAI via SFTP [#1289](https://github.com/betagouv/maestro/issues/1289).
- Mise à jour du référentiel avec l'ajout de la substance active cyprosulfamide [#1246](https://github.com/betagouv/maestro/issues/1246).

**Interface et expérience utilisateur**
- Ajout d'un fil d'ariane et de nouvelles actions dans le paramétrage [#1351](https://github.com/betagouv/maestro/issues/1351).
- Corrections sur le tableau de bord concernant la visibilité des détails de prélèvements et la récupération des conformités [#1288](https://github.com/betagouv/maestro/issues/1288), [#1262](https://github.com/betagouv/maestro/issues/1262).

### Évolutions techniques

**Optimisation et architecture**
- Migration de la gestion des domaines vers la base de données pour une meilleure persistance [#1342](https://github.com/betagouv/maestro/issues/1342).
- Optimisation des performances : réduction de l'empreinte mémoire lors de la mise à jour des départements [#1260](https://github.com/betagouv/maestro/issues/1260) et optimisation de la récupération des données utilisateurs [#1336](https://github.com/betagouv/maestro/issues/1336).
- Refactoring du code pour la gestion des références laboratoires [#1247](https://github.com/betagouv/maestro/issues/1247).

**Infrastructure et environnement**
- Initialisation automatique des départements sur les environnements de revue (review apps) [#1367](https://github.com/betagouv/maestro/issues/1367).

### Autres changements
- Mises à jour de l'outillage de développement et de build (PostCSS, Vite, etc.) [#1310](https://github.com/betagouv/maestro/issues/1310), [#1261](https://github.com/betagouv/maestro/issues/1261).
