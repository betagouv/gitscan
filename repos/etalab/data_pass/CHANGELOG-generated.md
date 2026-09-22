## Changelog : data_pass (30 derniers jours, au 21 septembre 2026)

### Résumé
Cette période est marquée par l'enrichissement des cas d'usage de l'API Particulier et une amélioration de la fiabilité des formulaires. Les efforts se sont concentrés sur la fluidification du parcours utilisateur (gestion des brouillons et validation des étapes) et sur le renforcement de la sécurité, notamment via une meilleure gestion des accès locaux et des scopes OAuth.

### Évolutions fonctionnelles
- **Nouveaux cas d'usage** : Ajout d'un nouveau cas d'usage pour l'API Particulier incluant un cas d'usage éditeur associé [#1745](https://github.com/etalab/data_pass/issues/1745).
- **Personnalisation juridique** : Adaptation du cadre juridique pour les "Produits DINUM" [#1749](https://github.com/etalab/data_pass/issues/1749).
- **Homogénéisation des données** : Alignement des intitulés de l'API Particulier (notamment EAJE et stationnement résidentiel) avec ceux de Simplifions [#1744](https://github.com/etalab/data_pass/issues/1744).
- **Amélioration du tunnel de saisie** : 
    - Meilleure validation des étapes lors de la progression dans les formulaires [#1730](https://github.com/etalab/data_pass/issues/1730).
    - Amélioration de la reprise des brouillons grâce à une validation de l'étape mémorisée en cookie [#1761](https://github.com/etalab/data_pass/issues/1761).
- **Corrections d'interface** : Résolution de problèmes d'affichage et d'échappement HTML sur la bannière d'accès externe [#1754](https://github.com/etalab/data_pass/issues/1754).

### Évolutions techniques
- **Sécurité et accès** : 
    - Restriction de l'accès `local-sign-in` sur les environnements sensibles [#1693](https://github.com/etalab/data_pass/issues/1693).
    - Automatisation du scope `read_webhooks` pour les nouvelles applications et mise en conformité des applications OAuth existantes [#1753](https://github.com/etalab/data_pass/issues/1753).
- **Fiabilité du système** :
    - Sécurisation du tri des dossiers dans le tableau de bord d'instruction [#1729](https://github.com/etalab/data_pass/issues/1729).
    - Correction d'un bug de réinitialisation des cas d'utilisation DGFIP [#1760](https://github.com/etalab/data_pass/issues/1760).
    - Stabilisation de l'outil de test Ferrum pour éviter les régressions de contexte de navigation.

### Autres changements
- **Documentation** : Ajout de la documentation concernant le mode opératoire des tokens `local-sign-in`.
- **Qualité des données** : Normalisation des apostrophes typographiques dans les jeux de données de test.
