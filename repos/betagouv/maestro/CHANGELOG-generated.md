## Changelog : maestro (30 derniers jours, au 23 septembre 2026)

### Résumé
Ce mois-ci, les évolutions de Maestro se sont concentrées sur l'enrichissement des capacités de paramétrage et la gestion des données métier. Les outils de configuration des échantillons et des plans ont été considérablement étendus, tandis que les droits d'accès et la visibilité des informations ont été affinés pour les coordinateurs nationaux et régionaux. L'expérience utilisateur a également été améliorée par des corrections de navigation et de recherche.

### Évolutions fonctionnelles

**Configuration et Paramétrage**
- Extension des capacités de paramétrage : gestion des sous-plans [#1399], notion de surcharge entre plans et sous-plans [#1412], et ajout d'un statut "Terminer" [#1441].
- Gestion avancée des échantillons : possibilité de configurer les analytes (plusieurs analytes par échantillon [#1513], [#1476]), gestion des propriétaires [#1453], et calcul automatique des exemplaires via le paramétrage [#1524].
- Évolution des domaines et ressources : ajout de la notion d'année pour les domaines [#1372], possibilité de rendre l'année optionnelle pour les ressources [#1540], et simplification de l'interface d'assignation des domaines [#1373], [#1387].
- Amélioration de la gestion des données : possibilité de supprimer les domaines, plans et sous-plans non terminés [#1475] et déplacement de la configuration des champs spécifiques [#1400].

**Gestion des utilisateurs et des droits**
- Renforcement des droits des coordinateurs nationaux : accès en lecture seule au dictionnaire des descripteurs [#1536], visibilité sur l'ensemble des domaines [#1462] et correction de l'importation [#1535].
- Amélioration du support et de la visibilité : ajout de fonctionnalités pour le support utilisateur [#1538] et visibilité accrue des commentaires de la coordination nationale pour les coordinateurs régionaux [#1452].
- Corrections d'accès : correction de l'accès à la programmation pour les prélèveurs [#1502].

**Programmation et Prélèvements**
- Nouvelles fonctionnalités : ajout du suivi de la programmation [#1221] et ajout d'un type "date" pour les descripteurs [#1491].
- Améliorations de l'expérience utilisateur : ajout d'un bouton "haut de page" [#1539], tri des sous-plans par numéro [#1537], et possibilité de modifier la localisation à l'étape 4 du prélèvement [#1414].
- Corrections : correction de la recherche d'entreprises [#1473], de la recherche pour les plans multi-étapes [#1411] et de la suppression d'un prélèvement à envoyer [#1454].

**Notifications et Statistiques**
- Migration des notifications vers l'outil Tchap [#1430].
- Ajout d'une boîte email institutionnelle pour les notifications de détection [#1388].
- Correction des statistiques de prélèvements non conformes sur le tableau de bord [#1384].

### Évolutions techniques

**Maintenance et Infrastructure**
- Refactoring : suppression du code de gestion du mode hors-ligne pour les prélèvements [#1523] et nettoyage du code mort dans la partie programmation [#1522].
- Fiabilité et Build : amélioration de la gestion des erreurs du script de sauvegarde (backup) [#1386], correction des types de routes lors du build et initialisation des départements sur les environnements de test (review apps) [#1367].

### Autres changements
- Passage du projet sous licence MIT [#1489].
