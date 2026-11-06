## Changelog : hyyypertool (30 derniers jours, au 05 novembre 2026)

### Résumé
Ce mois a été marqué par un renforcement significatif de la traçabilité et de la visibilité pour les modérateurs. L'introduction de nouveaux journaux d'activité (globaux et par utilisateur) et l'amélioration du suivi des décisions concernant les domaines permettent une gestion plus fine et transparente des processus de modération.

### Évolutions fonctionnelles
- **Journal d'activité et traçabilité** :
    - Création d'une page de journal d'activité global [#1969](https://github.com/proconnect-gouv/hyyypertool/issues/1969) et affichage de l'historique spécifique à chaque utilisateur sur sa fiche [#1967](https://github.com/proconnect-gouv/hyyypertool/issues/1967).
    - Ajout d'un filtre par date dans le journal d'activité [#1976](https://github.com/proconnect-gouv/hyyypertool/issues/1976).
    - Amélioration de l'affichage des acteurs dans les logs (liens vers les profils et affichage par email) [#1971](https://github.com/proconnect-gouv/hyyypertool/issues/1971), [#1972](https://github.com/proconnect-gouv/hyyypertool/issues/1972).
    - Optimisation de l'interface du journal avec un nouveau mode d'affichage en flux [#1978](https://github.com/proconnect-gouv/hyyypertool/issues/1978) et correction de la pagination [#1974](https://github.com/proconnect-gouv/hyyypertool/issues/1974), [#1977](https://github.com/proconnect-gouv/hyyypertool/issues/1977).
- **Gestion des domaines et organisations** :
    - Ajout de l'historique des domaines directement sur la page des organisations [#1958](https://github.com/proconnect-gouv/hyyypertool/issues/1958).
    - Journalisation des décisions de modération et des suppressions de domaines [#1957](https://github.com/proconnect-gouv/hyyypertool/issues/1957), [#1960](https://github.com/proconnect-gouv/hyyypertool/issues/1960).
    - Affichage des membres promus sous leurs décisions de domaine respectives [#1959](https://github.com/proconnect-gouv/hyyypertool/issues/1959).
- **Interface utilisateur et support** :
    - Affichage du statut des demandes d'autorisation sur les pages utilisateurs [#1928](https://github.com/proconnect-gouv/hyyypertool/issues/1928).
    - Augmentation de la densité d'affichage (20 modérations par page) [#1908](https://github.com/proconnect-gouv/hyyypertool/issues/1908).
    - Ajout de l'adresse email de support via Crisp lors des actions d'assistance [#1846](https://github.com/proconnect-gouv/hyyypertool/issues/1846).
    - Correction de liens erronés vers l'annuaire des dirigeants [#1847](https://github.com/proconnect-gouv/hyyypertool/issues/1847) et des erreurs sur les documents des dirigeants [#1949](https://github.com/proconnect-gouv/hyyypertool/issues/1949).

### Évolutions techniques
- **Tests et Qualité** :
    - Migration massive des tests de fonctionnalités vers le framework Buncept (ex: [#1865](https://github.com/proconnect-gouv/hyyypertool/issues/1865), [#1866](https://github.com/proconnect-gouv/hyyypertool/issues/1866), [#1867](https://github.com/proconnect-gouv/hyyypertool/issues/1867), etc.).
    - Optimisation du temps d'exécution des tests via le partitionnement (sharding) sur plusieurs runners [#1881](https://github.com/proconnect-gouv/hyyypertool/issues/1881), [#1894](https://github.com/proconnect-gouv/hyyypertool/issues/1894), [#1939](https://github.com/proconnect-gouv/hyyypertool/issues/1939).
- **Refactoring et Architecture** :
    - Harmonisation du nommage du code (modules, requêtes, cas d'utilisation) en `snake_case` pour plus de cohérence [#1962](https://github.com/proconnect-gouv/hyyypertool/issues/1962), [#1963](https://github.com/proconnect-gouv/hyyypertool/issues/1963), [#1964](https://github.com/proconnect-gouv/hyyypertool/issues/1964), [#1965](https://github.com/proconnect-gouv/hyyypertool/issues/1965), [#1966](https://github.com/proconnect-gouv/hyyypertool/issues/1966).
    - Nettoyage du code : suppression de clients API obsolètes [#1895](https://github.com/proconnect-gouv/hyyypertool/issues/1895) et simplification de la vérification des domaines [#1956](https://github.com/proconnect-gouv/hyyypertool/issues/1956).
- **Infrastructure et CI/CD** :
    - Mise à jour des environnements d'exécution : Node.js [#cd14ba8], PostgreSQL [#1922] et Bun [#1936].
    - Migration de la gestion des dépendances de Dependabot vers une configuration Renovate partagée [#1994](https://github.com/proconnect-gouv/hyyypertool/issues/1994).
    - Mise en place d'un nouveau workflow de release automatisé via `release-action` [#1857](https://github.com/proconnect-gouv/hyyypertool/issues/1857), [#1862](https://github.com/proconnect-gouv/hyyypertool/issues/1862).
    - Amélioration de l'expérience de développement avec le seed automatique des bases de données en local [#1950](https://github.com/proconnect-gouv/hyyypertool/issues/1950).

### Autres changements
- Gestion des versions : Ajout et mise à jour de nombreux fichiers de changements (changesets) pour automatiser les notes de version [#1979](https://github.com/proconnect-gouv/hyyypertool/issues/1979), [#1952](https://github.com/proconnect-gouv/hyyypertool/issues/1952), [#1860](https://github.com/proconnect-gouv/hyyypertool/issues/1860).
