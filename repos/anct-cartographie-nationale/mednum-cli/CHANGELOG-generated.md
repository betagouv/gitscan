## Changelog : mednum-cli (30 derniers jours, au 16 septembre 2026)

### Résumé
Ce mois-ci, l'outil a bénéficié d'un enrichissement de ses sources de données et d'une meilleure précision dans la gestion des horaires et des adresses. Parallèlement, une refonte de l'architecture interne et une sécurisation des processus de publication renforcent la fiabilité et la maintenabilité du projet.

### Évolutions fonctionnelles
- **Enrichissement des données** : Ajout de la source de données pour la Manche [#361](https://github.com/anct-cartographie-nationale/mednum-cli/pull/361).
- **Gestion des horaires** : Possibilité d'ajouter des commentaires pour les horaires d'ouverture liés à des occurrences mensuelles spécifiques [#362](https://github.com/anct-cartographie-nationale/mednum-cli/pull/362).
- **Règles de gestion des adresses** : Mise en place d'une fonctionnalité pour exclure les adresses vérifiées [#368](https://github.com/anct-cartographie-nationale/mednum-cli/pull/368).
- **Correction de données** : Exclusion de certains lieux spécifiques (Dora et Les Landes) pour garantir la conformité des données [#366](https://github.com/anct-cartographie-nationale/mednum-cli/pull/366).

### Évolutions techniques
- **Architecture** : Refonte de l'architecture des capacités de fonctionnalités (*feature ability architecture*) [#367](https://github.com/anct-cartographie-nationale/mednum-cli/pull/367).
- **Qualité des données** : Optimisation de la détection des doublons grâce à l'application d'une règle de déduplication partagée [#364](https://github.com/anct-cartographie-nationale/mednum-cli/pull/364).
- **CI/CD et Tooling** : 
    - Migration vers Biome pour le linting et le formatage du code [#365](https://github.com/anct-cartographie-nationale/mednum-cli/pull/365).
    - Sécurisation des processus de publication via le *trusted publishing* [#365](https://github.com/anct-cartographie-nationale/mednum-cli/pull/365).
- **Maintenance** : Correction du mécanisme de réinitialisation du cache des adresses pour éviter les données obsolètes [#363](https://github.com/anct-cartographie-nationale/mednum-cli/pull/363).
