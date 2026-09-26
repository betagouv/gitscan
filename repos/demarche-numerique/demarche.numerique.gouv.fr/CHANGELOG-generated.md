## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 25 septembre 2026)

### Résumé
Les évolutions de ce mois se concentrent sur la résilience du système face aux défaillances des services externes (comme les API SIRET ou RNA) grâce à l'introduction d'un mode "dégradé" qui évite de bloquer les usagers. La sécurité a été renforcée, notamment par la généralisation de l'authentification ProConnect pour les administrateurs et la mise en place de bac à sable (sandbox) pour le traitement des fichiers. Enfin, une importante phase de modernisation technique a été menée, incluant la migration de vues et l'optimisation des performances de recherche.

### Évolutions fonctionnelles
- **Résilience des données externes** : Mise en place d'un mode "dégradé" pour les champs dépendants d'API externes (SIRET, RNA). En cas d'indisponibilité ou d'erreur de l'API, le système permet de poursuivre la saisie tout en signalant l'état de la donnée à l'instructeur. [#14058](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14058), [#14072](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14072).
- **Sécurité et accès** : Renforcement de l'usage de ProConnect pour les administrateurs et gestionnaires, avec de nouveaux flux d'invitation et une gestion plus stricte des accès. [#13996](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13996).
- **Gestion des comptes** : Automatisation de la purge des comptes inactifs et amélioration de la traçabilité des sessions pour les super-administrateurs. [#14051](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14051).
- **Expérience utilisateur et Accessibilité** :
    - Amélioration des composants de sélection (combobox/select) pour une navigation plus fluide.
    - Corrections d'accessibilité sur les titres de pages, les menus d'aide et les badges de notification. [#14086](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14086), [#14088](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14088).
    - Amélioration de l'export des données de l'annuaire éducation. [#14038](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14038).
    - Mise à jour et corrections typographiques de la FAQ.

### Évolutions techniques
- **Sécurité** : 
    - Durcissement de la validation des URLs pour rejeter les hôtes locaux ou internes. [#14093](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14093).
    - Implémentation d'un bac à sable (sandbox) pour isoler le traitement des fichiers et des données non sécurisées.
    - Sécurisation des requêtes GraphQL pour empêcher la divulgation de procédures en brouillon.
- **Performance** : 
    - Optimisation des temps de réponse via le préchargement de données (dossiers, pièces jointes, annotations).
    - Résolution de plusieurs problèmes de requêtes N+1 dans les vues de gestion.
    - Refonte du moteur de recherche utilisant les index `tsvector` de PostgreSQL. [#14089](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/14089).
- **Architecture et Refactoring** :
    - Migration massive des templates de vues de HAML vers ERB.
    - Refonte de la logique de gestion des "champs" et de l'historique des révisions de dossiers.
- **Infrastructure et CI/CD** :
    - Mise à jour de l'environnement de production (passage à Ubuntu 24.04).
    - Montée de version vers Sidekiq 8. [#13926](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13926).

### Autres changements
- **Documentation** : Amélioration de la documentation des variables d'environnement et des guides pour les agents.
- **Maintenance** : Nettoyage du code (suppression de vues obsolètes, de dépendances inutilisées et de drapeaux de fonctionnalités supprimées).
