## Changelog : maestro (30 derniers jours, au 22 octobre 2026)

### Résumé
Ce mois-ci, Maestro a connu une évolution majeure de son module de paramétrage, offrant une gestion beaucoup plus fine des plans, des sous-plans et des matrices. Les fonctionnalités de programmation ont été enrichies pour faciliter le travail des coordinateurs, tandis que des efforts importants ont été portés sur la confidentialité des données (anonymisation) et l'amélioration de l'expérience utilisateur, notamment via une recherche plus intuitive et un affichage mobile optimisé.

### Évolutions fonctionnelles

**Paramétrage et Configuration**
- Introduction de la gestion par sous-plans, permettant une organisation plus granulaire ([#1681](https://github.com/betagouv/maestro/issues/1681), [#1512](https://github.com/betagouv/maestro/issues/1512)).
- Possibilité de dupliquer des domaines, des plans ou des sous-plans pour gagner du temps ([#1550](https://github.com/betagouv/maestro/issues/1550)).
- Gestion avancée des matrices : sélection possible ([#1568](https://github.com/betagouv/maestro/issues/1568)), paramétrage au niveau du plan ([#1590](https://github.com/betagouv/maestro/issues/1590)) et migration vers les sous-plans ([#1580](https://github.com/betagouv/maestro/issues/1580)).
- Amélioration du contrôle métier : modification du code NAT des sous-plans ([#1715](https://github.com/betagouv/maestro/issues/1715)), paramétrage des substances ([#1629](https://github.com/betagouv/maestro/issues/1629)) et des modalités d'échantillonnage ([#1641](https://github.com/betagouv/maestro/issues/1641)).
- Nouvelles options de gestion : renommage de domaines ([#1665](https://github.com/betagouv/maestro/issues/1665)), ajout de l'IT directement sur le plan ([#1541](https://github.com/betagouv/maestro/issues/1541)) et nouveau mode de programmation ([#1670](https://github.com/betagouv/maestro/issues/1670)).

**Programmation et Prélèvements**
- Automatisation : génération des prescriptions lors de la création d'un sous-plan ([#1713](https://github.com/betagouv/maestro/issues/1713)).
- Accessibilité : ouverture de l'import de la programmation aux coordinateurs régionaux et départementaux ([#1578](https://github.com/betagouv/maestro/issues/1578)).
- Améliorations de saisie : ajout d'un bouton pour initier une nouvelle saison ([#1716](https://github.com/betagouv/maestro/issues/1716)) et sélection de l'atelier lors des prélèvements ([#1680](https://github.com/betagouv/maestro/issues/1680)).
- Corrections : filtrage par sous-plan dans la liste des prélèvements ([#1695](https://github.com/betagouv/maestro/issues/1695)) et gestion des erreurs de type de plan ([#1708](https://github.com/betagouv/maestro/issues/1708)).

**Interface et Recherche**
- Recherche textuelle améliorée qui ignore désormais les accents ([#1724](https://github.com/betagouv/maestro/issues/1724)).
- Optimisation de l'affichage mobile pour les tableaux ([#1709](https://github.com/betagouv/maestro/issues/1709)).
- Corrections diverses sur le tableau de bord (URLs trop longues [#1694](https://github.com/betagouv/maestro/issues/1694), calcul des prélèvements en cas de non-conformité [#1682](https://github.com/betagouv/maestro/issues/1682)) et l'affichage des tableaux de programmation ([#1630](https://github.com/betagouv/maestro/issues/1630)).

### Évolutions techniques

**Architecture et Données**
- Migration des matrices vers la base de données pour une meilleure persistance ([#1706](https://github.com/betagouv/maestro/issues/1706)).
- Refactorisation de la gestion des substances (remplacement de "Any" par "Mono" + "Multi") ([#1608](https://github.com/betagouv/maestro/issues/1608)).
- Mise en œuvre de l'anonymisation des données, notamment pour Metabase ([#1628](https://github.com/betagouv/maestro/issues/1628)).
- Nettoyage de la base de données par la suppression de colonnes obsolètes (contexts [#1666](https://github.com/betagouv/maestro/issues/1666), programming_plan_id [#1577](https://github.com/betagouv/maestro/issues/1577)).

**Infrastructure et Maintenance**
- Amélioration de la gestion des sauvegardes sur Scalingo ([#1693](https://github.com/betagouv/maestro/issues/1693)).
- Remplacement de la bibliothèque d'internationalisation par une solution interne ([#1661](https://github.com/betagouv/maestro/issues/1661)).
- Amélioration des logs d'erreur pour les routes inconnues ([#1663](https://github.com/betagouv/maestro/issues/1663)).
- Mise à jour de PostgreSQL ([#1632](https://github.com/betagouv/maestro/issues/1632)).

### Autres changements
- Nettoyage des dépendances npm (suppression de `uuid`, `dotenv`, `compose-middleware`, etc.).
- Amélioration de la stabilité de la suite de tests (correction de tests instables).
