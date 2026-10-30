## Changelog : maestro (30 derniers jours, au 29 octobre 2026)

### Résumé
Ce mois-ci, le développement s'est concentré sur un enrichissement majeur des capacités de configuration (paramétrage) et de planification (programmation). Les utilisateurs disposent désormais de fonctionnalités plus fines pour gérer les plans, les sous-plans, les matrices et les modalités d'échantillonnage. Des améliorations ont également été apportées à l'expérience utilisateur, notamment sur mobile et pour la recherche, ainsi qu'à la gestion des notifications.

### Évolutions fonctionnelles

**Paramétrage et Gestion métier**
- Extension des capacités de configuration : ajout de la gestion des sous-plans [#1681], des matrices [#1582], des substances [#1629] et des modalités d'échantillonnage [#1641].
- Amélioration de la flexibilité : possibilité de renommer des domaines [#1665], de modifier les titres de plans [#1583] et de spécifier des contextes d'intervention (SIGAL) [#1754].
- Sécurisation des données : blocage de la modification de certains champs après le lancement d'un plan [#1710] et révision des droits de création/suppression [#1725].
- Gestion des règles métier : remplacement de certaines colonnes par des règles métier automatisées [#1669].

**Programmation et Prélèvements**
- Programmation : gestion au niveau départemental [#1751], bouton d'initiation de nouvelle saison [#1716] et ouverture des droits d'import aux coordinateurs régionaux et départementaux [#1578].
- Prélèvements : possibilité de prélever plusieurs matrices simultanément [#1603], sélection d'ateliers [#1680] et correction des filtres par sous-plan [#1695].
- Prescriptions : génération automatique des prescriptions lors de la création d'un sous-plan [#1713].

**Interface et Expérience utilisateur**
- Recherche : amélioration de la recherche textuelle qui ignore désormais les accents [#1724].
- Affichage : optimisation de la largeur des tableaux sur mobile [#1709] et gestion de l'affichage des boutons pendant la sauvegarde [#1734].
- Notifications : ajustement des alertes Tchap (affichage HTML des releases et suppression des notifications pour les interprétations) [#1752, #1753] et ciblage des alertes support lors de l'ajout de préleveurs [#1742].

### Évolutions techniques

**Architecture et Base de données**
- Migration des matrices vers la base de données [#1706].
- Refactorisation des schémas de données pour les substances [#1608] et les prescriptions [#1577].
- Mise à jour de l'infrastructure PostgreSQL [#1632].
- Mise en place de l'anonymisation des données pour Metabase [#1628].

**CI/CD et DevOps**
- Optimisation des pipelines de tests : limitation du déclenchement des jobs [#1750, #1741] et utilisation d'images Docker pour l'installation de Playwright [#1743].

**Refactoring et Code**
- Remplacement de la bibliothèque d'internationalisation (i18n) par une solution interne [#1661].

### Autres changements
- Nettoyage du projet : suppression de plusieurs dépendances inutilisées (`uuid` [#1633], `dotenv` [#1627], `compose-middleware` [#1626]).
- Mise à jour des outils de développement (Storybook, Knip).
