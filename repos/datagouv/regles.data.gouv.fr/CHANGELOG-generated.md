## Changelog : regles.data.gouv.fr (30 derniers jours, au 16 octobre 2026)

### Résumé
Le projet est passé d'une phase de configuration initiale à une version capable de présenter un catalogue de règles structuré. L'interface utilisateur s'est alignée sur les standards de l'État (DSFR) et le système de gestion des données a été renforcé pour assurer la fiabilité et l'intégrité des informations publiées.

### Évolutions fonctionnelles
- Publication d'un catalogue de règles sous forme de pages statiques pour une consultation simplifiée [#26](https://github.com/datagouv/regles.data.gouv.fr/pull/26).
- Mise en conformité visuelle avec le Design System de l'État (DSFR) et ajout d'un mode "marque blanche" pour l'interface web [#29](https://github.com/datagouv/regles.data.gouv.fr/pull/29).

### Évolutions techniques
- Amélioration du moteur (core) : construction automatique du registre à partir des fichiers de règles et gestion automatique des doublons [#25](https://github.com/datagouv/regles.data.gouv.fr/pull/25).
- Automatisation de la génération des types de données à partir des schémas de contrat [#23](https://github.com/datagouv/regles.data.gouv.fr/pull/23).
- Mise en place d'un schéma de validation pour les contrats [#20](https://github.com/datagouv/regles.data.gouv.fr/pull/20).
- Optimisation de la chaîne de production (CI/CD) : déploiement de prévisualisations sur GitHub Pages [#30](https://github.com/datagouv/regles.data.gouv.fr/pull/30), automatisation des tests et du linting via `mise` [#22](https://github.com/datagouv/regles.data.gouv.fr/pull/22) et amélioration de l'intégration des nouvelles entrées [#21](https://github.com/datagouv/regles.data.gouv.fr/pull/21).
- Initialisation de l'outillage de développement et de la structure du projet [#7](https://github.com/datagouv/regles.data.gouv.fr/pull/7).

### Autres changements
- Documentation technique : ajout de documents de décision d'architecture (ADR) concernant la validation des données [#18](https://github.com/datagouv/regles.data.gouv.fr/pull/18) et la configuration du dépôt [#16](https://github.com/datagouv/regles.data.gouv.fr/pull/16).
