## Changelog : hyyypertool (30 derniers jours, au 31 octobre 2026)

### Résumé
Ce mois a été marqué par un renforcement majeur de la traçabilité et de la visibilité des données pour les modérateurs, notamment grâce à l'ajout de journaux d'activité détaillés et d'historiques de domaines. Parallèlement, le projet a bénéficié d'une importante phase de nettoyage technique et d'optimisation de la suite de tests pour améliorer la stabilité et la rapidité des déploiements.

### Évolutions fonctionnelles
- **Traçabilité et audit**
  - Ajout d'une page de journal d'activité globale ([#1969](https://github.com/proconnect-gouv/hyyypertool/issues/1969)).
  - Affichage de l'historique d'activité spécifique à chaque utilisateur sur sa fiche dédiée ([#1967](https://github.com/proconnect-gouv/hyyypertool/issues/1967)).
  - Amélioration de la clarté des logs : liaison des acteurs à leurs pages et affichage de leur adresse email ([#1972](https://github.com/proconnect-gouv/hyyypertool/issues/1972), [#1971](https://github.com/proconnect-gouv/hyyypertool/issues/1971)).
  - Journalisation des décisions de modération et des suppressions de domaines ([#1960](https://github.com/proconnect-gouv/hyyypertool/issues/1960), [#1957](https://github.com/proconnect-gouv/hyyypertool/issues/1957)).
- **Interface et expérience utilisateur**
  - Visualisation de l'historique des domaines directement sur la page de l'organisation ([#1958](https://github.com/proconnect-gouv/hyyypertool/issues/1958)).
  - Affichage du statut des demandes d'autorisation sur la fiche utilisateur ([#1928](https://github.com/proconnect-gouv/hyyypertool/issues/1928)).
  - Affichage des membres promus sous leur décision de domaine ([#1959](https://github.com/proconnect-gouv/hyyypertool/issues/1959)).
  - Optimisation de la pagination (20 modérations par page) ([#1908](https://github.com/proconnect-gouv/hyyypertool/issues/1908)).
  - Ajout d'un lien de contact (email Crisp) lors des actions de support ([#1846](https://github.com/proconnect-gouv/hyyypertool/issues/1846)).
- **Corrections**
  - Correction de l'affichage de la liste des dirigeants pour les associations ([#1847](https://github.com/proconnect-gouv/hyyypertool/issues/1847), [#1949](https://github.com/proconnect-gouv/hyyypertool/issues/1949)).
  - Suppression d'une signature codée en dur ([#1891](https://github.com/proconnect-gouv/hyyypertool/issues/1891)).

### Évolutions techniques
- **Refactoring et architecture**
  - Harmonisation du nommage (passage en `snake_case`) des modules, helpers, cas d'utilisation (use cases) et requêtes ([#1965](https://github.com/proconnect-gouv/hyyypertool/issues/1965), [#1966](https://github.com/proconnect-gouv/hyyypertool/issues/1966), [#1963](https://github.com/proconnect-gouv/hyyypertool/issues/1963), [#1964](https://github.com/proconnect-gouv/hyyypertool/issues/1964), [#1962](https://github.com/proconnect-gouv/hyyypertool/issues/1962)).
  - Optimisation de la vérification des domaines en supprimant l'usage du gestionnaire legacy ([#1956](https://github.com/proconnect-gouv/hyyypertool/issues/1956)).
  - Suppression d'un client API obsolète pour l'administration d'Identité ([#1895](https://github.com/proconnect-gouv/hyyypertool/issues/1895)).
- **Infrastructure et dépendances**
  - Mise à jour majeure de l'infrastructure : Node.js (v24.22.1) et PostgreSQL (v18.6) ([#1922](https://github.com/proconnect-gouv/hyyypertool/issues/1922)).
  - Montée de version de la bibliothèque cœur `proconnect.identite` ([#1970](https://github.com/proconnect-gouv/hyyypertool/issues/1970), [#1955](https://github.com/proconnect-gouv/hyyypertool/issues/1955), [#1906](https://github.com/proconnect-gouv/hyyypertool/issues/1906)).
- **Tests et CI/CD**
  - Migration massive des tests de fonctionnalités vers le framework `buncept` ([#1866](https://github.com/proconnect-gouv/hyyypertool/issues/1866), [#1870](https://github.com/proconnect-gouv/hyyypertool/issues/1870), [#1871](https://github.com/proconnect-gouv/hyyypertool/issues/1871), [#1872](https://github.com/proconnect-gouv/hyyypertool/issues/1872), [#1873](https://github.com/proconnect-gouv/hyyypertool/issues/1873), [#1874](https://github.com/proconnect-gouv/hyyypertool/issues/1874), [#1877](https://github.com/proconnect-gouv/hyyypertool/issues/1877), [#1878](https://github.com/proconnect-gouv/hyyypertool/issues/1878), [#1879](https://github.com/proconnect-gouv/hyyypertool/issues/1879), [#1883](https://github.com/proconnect-gouv/hyyypertool/issues/1883), [#1884](https://github.com/proconnect-gouv/hyyypertool/issues/1884), [#1885](https://github.com/proconnect-gouv/hyyypertool/issues/1885), [#1886](https://github.com/proconnect-gouv/hyyypertool/issues/1886), [#1887](https://github.com/proconnect-gouv/hyyypertool/issues/1887)).
  - Optimisation de la CI par le partitionnement (sharding) des tests de fonctionnalités pour réduire les temps d'exécution ([#1939](https://github.com/proconnect-gouv/hyyypertool/issues/1939), [#1894](https://github.com/proconnect-gouv/hyyypertool/issues/1894)).

### Autres changements
- **Expérience de développement**
  - Automatisation de l'initialisation (seed) des bases de données lors du démarrage en environnement de développement ([#1950](https://github.com/proconnect-gouv/hyyypertool/issues/1950)).
