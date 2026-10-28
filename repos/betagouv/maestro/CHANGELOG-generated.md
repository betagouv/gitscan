## Changelog : maestro (30 derniers jours, au 27 octobre 2026)

### Résumé
Ce mois-ci, Maestro a franchi une étape importante dans la granularité de son paramétrage, notamment grâce à l'introduction de la gestion par sous-plans et une flexibilité accrue pour les matrices et les substances. La programmation devient plus précise avec une gestion possible au niveau départemental. Enfin, l'expérience utilisateur a été affinée par des corrections sur mobile, une recherche plus intuitive et une optimisation des notifications.

### Évolutions fonctionnelles
- **Gestion et paramétrage :**
  - Introduction de la notion de sous-plans pour une organisation plus fine ([#1681](https://github.com/betagouv/maestro/issues/1681), [#1512](https://github.com/betagouv/maestro/issues/1512)).
  - Amélioration de la gestion des matrices (sélection, paramétrage et gestion au niveau du plan) ([#1582](https://github.com/betagouv/maestro/issues/1582), [#1590](https://github.com/betagouv/maestro/issues/1590), [#1706](https://github.com/betagouv/maestro/issues/1706)).
  - Possibilité de paramétrer les substances au sein des sous-plans ([#1629](https://github.com/betagouv/maestro/issues/1629)) et de gérer les modalités d'échantillonnage ([#1641](https://github.com/betagouv/maestro/issues/1641)).
  - Flexibilité accrue pour les administrateurs : modification des titres de plans, des codes NAT et des contextes d'intervention ([#1723](https://github.com/betagouv/maestro/issues/1723), [#1715](https://github.com/betagouv/maestro/issues/1715), [#1754](https://github.com/betagouv/maestro/issues/1754)).
  - Ajout de listes à choix multiples pour les descripteurs ([#1755](https://github.com/betagouv/maestro/issues/1755)).
- **Programmation :**
  - Gestion de la programmation au niveau départemental ([#1751](https://github.com/betagouv/maestro/issues/1751)).
  - Nouveau mode de programmation disponible ([#1670](https://github.com/betagouv/maestro/issues/1670)) et bouton pour initier une nouvelle saison ([#1716](https://github.com/betagouv/maestro/issues/1716)).
  - Ouverture des droits d'import de la programmation aux coordinateurs régionaux et départementaux ([#1578](https://github.com/betagouv/maestro/issues/1578)).
- **Prélèvements et prescriptions :**
  - Possibilité de prélever plusieurs matrices simultanément ([#1603](https://github.com/betagouv/maestro/issues/1603)).
  - Génération automatique des prescriptions lors de la création d'un sous-plan ([#1713](https://github.com/betagouv/maestro/issues/1713)).
  - Correction de la sélection d'ateliers ([#1680](https://github.com/betagouv/maestro/issues/1680)) et des filtres par sous-plan ([#1695](https://github.com/betagouv/maestro/issues/1695)).
- **Expérience utilisateur et notifications :**
  - Amélioration de la recherche textuelle (prise en compte des accents [#1724](https://github.com/betagouv/maestro/issues/1724)).
  - Optimisation de l'affichage mobile pour les tableaux ([#1709](https://github.com/betagouv/maestro/issues/1709)).
  - Ajustements des notifications Tchap (affichage HTML des releases [#1753](https://github.com/betagouv/maestro/issues/1753) et réduction du bruit pour les interprétations [#1752](https://github.com/betagouv/maestro/issues/1752)).

### Évolutions techniques
- **Architecture et données :**
  - Migration de la gestion des matrices vers la base de données ([#1706](https://github.com/betagouv/maestro/issues/1706)).
  - Refonte de la structure des substances (passage de "Any" à un modèle Mono/Multi) ([#1608](https://github.com/betagouv/maestro/issues/1608)).
  - Refactorisation de la gestion des PPV via la séparation en sous-plans ([#1512](https://github.com/betagouv/maestro/issues/1512)).
  - Remplacement de la bibliothèque d'internationalisation par une solution interne ([#1661](https://github.com/betagouv/maestro/issues/1661)).
- **Infrastructure et CI/CD :**
  - Optimisation des pipelines de tests en limitant le nombre de jobs déclenchés ([#1750](https://github.com/betagouv/maestro/issues/1750), [#1741](https://github.com/betagouv/maestro/issues/1741)).
  - Utilisation d'images Docker pour l'installation de Playwright dans la CI ([#1743](https://github.com/betagouv/maestro/issues/1743)).
  - Mise à jour de l'infrastructure PostgreSQL ([#1632](https://github.com/betagouv/maestro/issues/1632)).

### Autres changements
- **Nettoyage du code :** Suppression de plusieurs dépendances inutilisées telles que `uuid` ([#1633](https://github.com/betagouv/maestro/issues/1633)), `dotenv` ([#1627](https://github.com/betagouv/maestro/issues/1627)) et `compose-middleware` ([#1626](https://github.com/betagouv/maestro/issues/1626)).
- **Confidentialité :** Amélioration de l'anonymisation des données pour l'outil Metabase ([#1628](https://github.com/betagouv/maestro/issues/1628)).
