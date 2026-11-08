## Changelog : maestro (30 derniers jours, au 05/11/2026)

### Résumé
Ce mois-ci, Maestro a franchi une étape importante dans la finesse de son paramétrage, notamment grâce à l'introduction de la gestion des sous-plans et de nouvelles modalités d'échantillonnage. L'expérience utilisateur a été enrichie par l'intégration de cartes IGN, une meilleure gestion de la recherche et une interface mobile optimisée, tandis que la plateforme gagne en robustesse grâce à des améliorations de l'infrastructure et de la sécurité.

### Évolutions fonctionnelles

**Paramétrage et gestion des plans**
- Introduction de la gestion des sous-plans : création, modification du code NAT et génération automatique des prescriptions [#1681](https://github.com/betagouv/maestro/issues/1681), [#1715](https://github.com/betagouv/maestro/issues/1715), [#1713](https://github.com/betagouv/maestro/issues/1713).
- Amélioration de la gestion des plans : possibilité d'ajouter de nouveaux plans [#1667](https://github.com/betagouv/maestro/issues/1667), de les renommer [#1665](https://github.com/betagouv/maestro/issues/1665) et de gérer la programmation au niveau départemental [#1751](https://github.com/betagouv/maestro/issues/1751).
- Évolution des modalités d'échantillonnage : ajout de la quantité maximale et paramétrage complet des modalités [#1641](https://github.com/betagouv/maestro/issues/1641), [#1787](https://github.com/betagouv/maestro/issues/1787).
- Nouvelles fonctionnalités métier : ajout de la notion de délégation [#1804](https://github.com/betagouv/maestro/issues/1804) et nouveau mode de programmation [#1670](https://github.com/betagouv/maestro/issues/1670).
- Renforcement du contrôle : blocage de la modification de certains champs après le lancement [#1710](https://github.com/betagouv/maestro/issues/1710) et révision des droits de création/suppression [#1725](https://github.com/betagouv/maestro/issues/1725).

**Utilisateurs et Sécurité**
- Amélioration de la gestion des utilisateurs : ajout des abattoirs sur les fiches et possibilité de se sélectionner soi-même dans la liste [#1797](https://github.com/betagouv/maestro/issues/1797), [#1796](https://github.com/betagouv/maestro/issues/1796).
- Activation de l'accès pour les coordinateurs nationaux [#1778](https://github.com/betagouv/maestro/issues/1778).
- Mise en place d'une nouvelle politique de sécurité [#1785](https://github.com/betagouv/maestro/issues/1785).

**Données et Descripteurs**
- Enrichissement des descripteurs : support des listes à choix multiples et des valeurs numériques décimales [#1755](https://github.com/betagouv/maestro/issues/1755), [#1756](https://github.com/betagouv/maestro/issues/1756).
- Utilisation du référentiel Sigal pour l'alimentation des descripteurs DAI [#1767](https://github.com/betagouv/maestro/issues/1767).

**Interface et Expérience Utilisateur (UX)**
- Cartographie : remplacement de MapTiler par des cartes IGN [#1792](https://github.com/betagouv/maestro/issues/1792).
- Optimisation mobile : correction de l'affichage des tableaux en largeur sur mobile [#1709](https://github.com/betagouv/maestro/issues/1709).
- Améliorations diverses : support du Markdown dans les messages du tableau de bord [#1805](https://github.com/betagouv/maestro/issues/1805), recherche insensible aux accents [#1724](https://github.com/betagouv/maestro/issues/1724) et nouveau composant de sélection multiple [#1790](https://github.com/betagouv/maestro/issues/1790).

**Notifications et Communication**
- Optimisation Tchap : affichage des releases en HTML et suppression des notifications d'interprétation non pertinentes [#1753](https://github.com/betagouv/maestro/issues/1753), [#1752](https://github.com/betagouv/maestro/issues/1752).
- Ajustement des alertes de support lors de l'ajout de nouveaux préleveurs [#1742](https://github.com/betagouv/maestro/issues/1742).

**Corrections (Fixes)**
- Correction de l'export de la programmation [#1664](https://github.com/betagouv/maestro/issues/1664).
- Correction de l'affichage des étiquettes et des noms de plans [#1788](https://github.com/betagouv/maestro/issues/1788).
- Correction du filtre par sous-plan dans la gestion des prélèvements [#1695](https://github.com/betagouv/maestro/issues/1695).
- Correction du comptage des prélèvements à faire sur le tableau de bord [#1682](https://github.com/betagouv/maestro/issues/1682).

### Évolutions techniques

**Architecture et Données**
- Migration des matrices vers la base de données pour une meilleure persistance [#1706](https://github.com/betagouv/maestro/issues/1706).
- Refactoring : suppression du code obsolète concernant les enquêtes laboratoires [#1791](https://github.com/betagouv/maestro/issues/1791) et remplacement de la bibliothèque i18n par une solution interne [#1661](https://github.com/betagouv/maestro/issues/1661).

**Infrastructure et CI/CD**
- Optimisation de la performance : gestion de la mise à jour groupée de la programmation pour réduire la consommation réseau [#1779](https://github.com/betagouv/maestro/issues/1779).
- Mise à jour de l'environnement : passage à la dernière version LTS de Node.js [#1774](https://github.com/betagouv/maestro/issues/1774).
- Amélioration de la CI : limitation du nombre de jobs de tests [#1750](https://github.com/betagouv/maestro/issues/1750) et utilisation d'images Docker pour Playwright [#1743](https://github.com/betagouv/maestro/issues/1743).
- Maintenance infrastructure : tentatives de correction des backups sur Scalingo [#1693](https://github.com/betagouv/maestro/issues/1693).

### Autres changements
- Nettoyage de la base de données : suppression de colonnes obsolètes dans les plans [#1666](https://github.com/betagouv/maestro/issues/1666).
