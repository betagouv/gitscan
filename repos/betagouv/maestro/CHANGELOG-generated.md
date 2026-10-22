## Changelog : maestro (30 derniers jours, au 21 octobre 2026)

### Résumé
Ce mois a été marqué par une montée en puissance du module de paramétrage, offrant désormais une gestion beaucoup plus fine et granulaire des plans, des sous-plans et des modalités d'échantillonnage. La plateforme gagne également en automatisation avec la génération des prescriptions et une meilleure gestion des droits pour les différents profils de coordinateurs.

### Évolutions fonctionnelles
- **Paramétrage avancé** : Gestion étendue des plans et sous-plans (création [#1681], duplication [#1550], renommage de domaine [#1665], modification du code NAT [#1715]), des matrices [#1582], des substances [#1629], des modalités d'échantillonnage [#1641] et des analytes par échantillon [#1513].
- **Programmation et prélèvements** : Automatisation de la génération des prescriptions lors de la création de sous-plans [#1713], introduction d'un nouveau mode de programmation [#1670] et calcul automatisé des échantillons basé sur les règles de paramétrage [#1524].
- **Interface et expérience utilisateur** : Optimisation de l'affichage des tableaux sur mobile [#1709], correction des filtres de recherche [#1695], amélioration de la navigation (bouton haut de page [#1539], tri des sous-plans [#1537]) et corrections sur le tableau de bord [#1694, #1682].
- **Gestion des droits et accès** : Ouverture des droits d'import de programmation aux coordinateurs régionaux et départementaux [#1578], accès en lecture seule au dictionnaire pour les coordinateurs nationaux [#1536] et correction des accès pour les prélèveurs [#1502].

### Évolutions techniques
- **Architecture et données** : Migration des matrices vers la base de données [#1706], séparation des PPV en sous-plans [#1512], refonte de la gestion des substances (passage de "Any" à Mono/Multi) [#1608] et suppression de colonnes obsolètes dans les tables de plans [#1666, #1669].
- **Qualité et maintenance du code** : Nettoyage du code (suppression du code mort et de la gestion du mode offline [#1523, #1522]), remplacement de la bibliothèque d'internationalisation par une solution interne [#1661] et mise en place de l'anonymisation des données pour Metabase [#1628].
- **Infrastructure et tests** : Amélioration de la gestion des sauvegardes sur Scalingo [#1693], mise à jour de PostgreSQL [#1632] et stabilisation des tests automatisés [#424d1e3].

### Autres changements
- Nettoyage des dépendances (suppression de `uuid` [#1633], `dotenv` [#1627] et `compose-middleware` [#1626]).
