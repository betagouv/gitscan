## Changelog : bhasile (30 derniers jours, au 14 septembre 2026)

### Résumé
Cette période est marquée par un enrichissement important des capacités d'extraction de données, avec l'ajout de nouveaux formats d'export (PDF et Excel). L'application bénéficie également d'une amélioration de son accessibilité et de performances accrues grâce à une optimisation de la manière dont les données sont récupérées et affichées.

### Évolutions fonctionnelles
- **Exportation de données** : Ajout de l'export PDF pour les statistiques [#1643](https://github.com/betagouv/bhasile/issues/1643) (incluant une nouvelle interface modale [#1632](https://github.com/betagouv/bhasile/issues/1632)), de l'export Excel [#1640](https://github.com/betagouv/bhasile/issues/1640), ainsi que de nouveaux téléchargements de feuilles de calcul [#1625](https://github.com/betagouv/bhasile/issues/1625) et des types de lieux [#1614](https://github.com/betagouv/bhasile/issues/1614).
- **Interface et Accessibilité** : Création d'une page dédiée à l'accessibilité [#1649](https://github.com/betagouv/bhasile/issues/1649), amélioration de la bannière de statistiques (texte et alignement) [#1653](https://github.com/betagouv/bhasile/issues/1653), [#1655](https://github.com/betagouv/bhasile/issues/1655) et correction visuelle des accordéons [#1636](https://github.com/betagouv/bhasile/issues/1636).
- **Expérience utilisateur et corrections** : Mémorisation des paramètres de recherche dans la liste des opérateurs pour faciliter la navigation [#1613](https://github.com/betagouv/bhasile/issues/1613) et correction de la récupération du code DNA pour les structures [#1628](https://github.com/betagouv/bhasile/issues/1628).

### Évolutions techniques
- **Optimisation des performances** : Migration de plusieurs composants clés (listes et fiches de structures, CPOM) vers le mode *React Server Components* (RSC) pour accélérer la récupération des données [#1633](https://github.com/betagouv/bhasile/issues/1633), [#1629](https://github.com/betagouv/bhasile/issues/1629), [#1626](https://github.com/betagouv/bhasile/issues/1626).
- **Refactorisation et maintenance** : Optimisation de la gestion des paramètres de recherche [#1615](https://github.com/betagouv/bhasile/issues/1615), clarification de l'usage des départements pour les structures [#1601](https://github.com/betagouv/bhasile/issues/1601), renommage de classes d'erreurs [#1627](https://github.com/betagouv/bhasile/issues/1627) et correction du middleware CPOM [#1654](https://github.com/betagouv/bhasile/issues/1654).
- **Nettoyage et suivi** : Suppression de composants obsolètes (prahdas [#1645](https://github.com/betagouv/bhasile/issues/1645)), remplacement de Matomo par un nouveau système de suivi [#1618](https://github.com/betagouv/bhasile/issues/1618) et mise en place du suivi des exports [#1630](https://github.com/betagouv/bhasile/issues/1630).

### Autres changements
- **Documentation** : Simplification du fichier README en retirant les instructions opérateurs [#1638](https://github.com/betagouv/bhasile/issues/1638).
