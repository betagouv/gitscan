## Changelog : maestro (30 derniers jours, au 14 octobre 2026)

### Résumé
Ce mois-ci, Maestro a franchi une étape importante dans la flexibilité de son moteur de paramétrage. Les utilisateurs peuvent désormais configurer de manière beaucoup plus fine les plans, les échantillons et les substances. Parallèlement, des efforts significatifs ont été déployés pour renforcer l'anonymisation des données et affiner les droits d'accès selon les différents rôles administratifs.

### Évolutions fonctionnelles
- **Paramétrage avancé** : ajout de nouveaux modes de programmation [#1670], possibilité de créer, renommer ou modifier des plans [#1667, #1665, #1583], gestion des contextes au niveau du plan [#1609] et fonction de duplication d'éléments (domaine, plan ou sous-plan) [#1550].
- **Gestion des prélèvements et échantillons** : configuration fine des modalités d'échantillonnage [#1641], des substances [#1629], des analytes [#1476, #1513] et des matrices [#1568, #1582, #1590, #1603]. Le calcul des échantillons et de leurs exemplaires est désormais automatisé via le paramétrage [#1524].
- **Programmation et suivi** : ajout d'un système de suivi de la programmation [#1221], détermination automatique du nom des sous-plans [#1591] et correction de l'affichage des tableaux de programmation pour certains profils [#1630].
- **Droits et accès** : gestion affinée des rôles avec un accès en lecture seule au dictionnaire pour les coordinateurs nationaux [#1536], ouverture de l'import de programmation aux coordinateurs régionaux et départementaux [#1578] et correction des accès pour les prélèveurs [#1502].
- **Sécurité et conformité** : renforcement de l'anonymisation des données, notamment pour les outils de visualisation comme Metabase [#1628].
- **Corrections diverses** : correction des étiquettes PPV [#1607], de l'émetteur des emails automatiques [#1567] et de la méthode d'analyse GIRPA [#1565].

### Évolutions techniques
- **Architecture et Refactoring** : remplacement de la bibliothèque i18n par une solution interne [#1661], refactorisation de la gestion des substances (passage de "Any" à Mono/Multi) [#1608] et séparation des PPV en sous-plans [#1512].
- **Base de données** : mise à jour de PostgreSQL [#1632] et renforcement de l'intégrité des données via l'ajout de contraintes sur la table des prescriptions [#1577].
- **Maintenance et optimisation** : suppression de code mort [#1522], de la gestion du mode hors-ligne [#1523] et de plusieurs dépendances NPM (uuid, dotenv, compose-middleware, etc.). Amélioration de la précision des logs pour les routes inconnues [#1663].

### Autres changements
- Passage du projet sous licence MIT [#1489].
