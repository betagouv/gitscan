## Changelog : data_pass (30 derniers jours, au 31/08/2026)

### Résumé
Ce mois-ci, data_pass a enrichi son catalogue de formulaires et de cadres juridiques, notamment avec l'intégration de nouveaux services comme Ianord et Nexys. L'outil a également bénéficié d'une meilleure cohérence de ses intitulés avec d'autres services de l'État (Simplifions) et d'un renforcement de la sécurité sur les tableaux de bord d'instruction.

### Évolutions fonctionnelles
- **Nouveaux formulaires et cas d'usage** : intégration de l'éditeur Ianord avec ses formulaires pour les cantines (lycées/collèges) [#1710](https://github.com/etalab/data_pass/issues/1710), ajout du formulaire API Entreprise Nexys (MGDIS) [#1731](https://github.com/etalab/data_pass/issues/1731) et création d'un nouveau cas d'usage pour un cadre juridique [#1745](https://github.com/etalab/data_pass/issues/1745).
- **Extension des données et scopes** : ajout du scope INE [#1722](https://github.com/etalab/data_pass/issues/1722) et affichage des scopes AEEH et régime pensionnat sur les formulaires CapDemat [#1709](https://github.com/etalab/data_pass/issues/1709).
- **Améliorations de l'interface et cohérence** : renommage du champ « Nom de naissance » en « Nom de famille » [#1738](https://github.com/etalab/data_pass/issues/1738) et harmonisation des intitulés (EAJE, stationnement résidentiel, noms de cas d'usage) pour correspondre à ceux de Simplifions [#1744](https://github.com/etalab/data_pass/issues/1744).

### Évolutions techniques
- **Sécurité** : protection du tri du tableau de bord d'instruction contre les injections SQL [#1729](https://github.com/etalab/data_pass/issues/1729).
- **Authentification** : correction du scope OAuth pour HubEE afin d'utiliser le scope `DATAPASS` au lieu de `ADMIN` [#1723](https://github.com/etalab/data_pass/issues/1723).
- **Corrections techniques** : résolution d'un problème d'import relatif en TypeScript [#1732](https://github.com/etalab/data_pass/issues/1732) et gestion des erreurs (404) sur les étapes de tunnel inexistantes.

### Autres changements
- **Documentation** : mise à jour de la documentation sur la politique de retry des webhooks [#1728](https://github.com/etalab/data_pass/issues/1728) et actualisation des informations relatives aux cadres juridiques (Ianord, Socle général) [#1736](https://github.com/etalab/data_pass/issues/1736).
- **Nettoyage** : simplification et renommage du champ de statut de bourse [#1721](https://github.com/etalab/data_pass/issues/1721).
