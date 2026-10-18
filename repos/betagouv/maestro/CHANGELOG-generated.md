## Changelog : maestro (30 derniers jours, au 15 octobre 2026)

### Résumé
Ce mois a été marqué par une extension majeure des capacités de paramétrage de la plateforme. L'introduction de la notion de sous-plans et une gestion plus fine des matrices et des substances permettent une configuration beaucoup plus granulaire des programmes. Parallèlement, des efforts importants ont été portés sur l'anonymisation des données et l'optimisation des droits d'accès pour les différents profils de coordination.

### Évolutions fonctionnelles

**Configuration et paramétrage du système**
- Extension de la hiérarchie avec l'ajout de sous-plans [#1681] et la possibilité de dupliquer des domaines, plans ou sous-plans [#1550].
- Amélioration de la gestion des plans : création de nouveaux plans [#1667], modification des titres [#1583] et renommage des domaines [#1665].
- Paramétrage avancé des prélèvements : gestion des substances dans les sous-plans [#1629], définition des modalités d'échantillonnage [#1641], gestion des analytes par échantillon [#1513] et configuration des clés de répartition et des notes [#1625].
- Évolution du modèle de données métier : remplacement de certaines colonnes par des règles métier plus flexibles [#1669] et introduction d'un nouveau mode de programmation [#1670].
- Gestion optimisée des matrices : possibilité de les sélectionner [#1568], de les gérer au niveau du plan [#1590] et de réaliser des prélèvements sur plusieurs matrices simultanément [#1603].

**Programmation et gestion des prélèvements**
- Automatisation du calcul des échantillons et de leurs exemplaires via le paramétrage [#1524].
- Ouverture des droits d'import de la programmation aux coordinateurs régionaux et départementaux [#1578].
- Corrections diverses : correction du nombre de prélèvements à effectuer en cas de non-conformité [#1682], correction de l'affichage des tableaux de programmation [#1630], tri automatique des sous-plans [#1537] et correction des étiquettes PPV [#1607].

**Utilisateurs et administration**
- Gestion des droits : accès en lecture seule au dictionnaire des descripteurs pour les coordinateurs nationaux [#1536] et correction des accès à la programmation pour les prélèveurs [#1502].
- Amélioration des outils de support pour les utilisateurs [#1538].

### Évolutions techniques

**Architecture et refactoring**
- Refonte structurelle : séparation des PPV en sous-plans [#1512], déplacement des matrices de prescription vers les sous-plans [#1580] et refonte de la gestion des substances (passage d'un type "Any" à une distinction Mono/Multi) [#1608].
- Optimisation du code : suppression du code de gestion du mode offline [#1523], nettoyage du code mort [#1522] et remplacement de la bibliothèque `i18n` par une solution interne [#1661].

**Données et sécurité**
- Renforcement de la protection des données via l'anonymisation des données dans Metabase [#1628] et corrections liées à l'anonymisation des tables.
- Maintenance de l'infrastructure : mise à jour de PostgreSQL [#1632] et nettoyage des colonnes obsolètes dans les tables de plans et de prescriptions [#1666, #1577].

**Qualité et maintenance**
- Amélioration de la fiabilité des tests (gestion du seed des départements [#1631] et correction de tests instables [#1606]).
- Amélioration de la traçabilité via des logs plus précis pour les routes inconnues [#1663].
