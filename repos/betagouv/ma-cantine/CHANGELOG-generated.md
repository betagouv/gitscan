## Changelog : ma-cantine (30 derniers jours, au 6 novembre 2026)

### Résumé
Ce mois a été marqué par une préparation intensive pour la campagne 2026. Les évolutions majeures concernent l'enrichissement des outils de télédéclaration avec de nouveaux volets thématiques (gaspillage, plastique, menu végétarien), la mise à jour des formats d'import de données et une refonte profonde de la traçabilité des actions via un nouveau système de journaux d'événements (EventLog).

### Évolutions fonctionnelles
- **Télédéclaration** : 
    - Ajout de nouveaux volets thématiques : substitution plastique [#7537](https://github.com/betagouv/ma-cantine/issues/7537), information convives [#7531](https://github.com/betagouv/ma-cantine/issues/7531), gaspillage alimentaire [#7527](https://github.com/betagouv/ma-cantine/issues/7527) et menu végétarien [#7473](https://github.com/betagouv/ma-cantine/issues/7473).
    - Amélioration de l'expérience de saisie : navigation optimisée par volets [#7543](https://github.com/betagouv/ma-cantine/issues/7543), fonctionnalités de remplissage automatique [#7384](https://github.com/betagouv/ma-cantine/issues/7384) et suivi de la progression du tunnel [#7323](https://github.com/betagouv/ma-cantine/issues/7323).
    - Possibilité de modifier une télédéclaration déjà soumise [#7275](https://github.com/betagouv/ma-cantine/issues/7275).
- **Diagnostics & Bilans** : 
    - Mise à jour des champs pour la campagne 2026 (volets information et plastique) [#7520](https://github.com/betagouv/ma-cantine/issues/7520), [#7521](https://github.com/betagouv/ma-cantine/issues/7521).
    - Enrichissement des indicateurs : nouveaux calculs automatiques pour les objectifs EGalim, les circuits courts et les origines des produits [#7361](https://github.com/betagouv/ma-cantine/issues/7361), [#7364](https://github.com/betagouv/ma-cantine/issues/7364).
    - Amélioration de l'API pour une récupération plus exhaustive des données de tous les volets [#7509](https://github.com/betagouv/ma-cantine/issues/7509).
- **Gestion des imports** : 
    - Introduction de nouveaux formats d'import pour 2026, notamment par ID ou par SIRET [#7493](https://github.com/betagouv/ma-cantine/issues/7493), [#7467](https://github.com/betagouv/ma-cantine/issues/7467).
    - Sécurisation des imports : restriction de l'accès aux pages d'import uniquement durant les périodes de campagne ouvertes [#7472](https://github.com/betagouv/ma-cantine/issues/7472), [#7490](https://github.com/betagouv/ma-cantine/issues/7490).
- **Expérience utilisateur** : 
    - Simplification du profil utilisateur par la suppression du champ "username" [#7228](https://github.com/betagouv/ma-cantine/issues/7228).
    - Amélioration de la visibilité des informations relatives aux établissements et à leurs groupes rattachés [#7522](https://github.com/betagouv/ma-cantine/issues/7522).

### Évolutions techniques
- **Traçabilité & Data** : 
    - Implémentation d'un nouveau système de journalisation (`EventLog`) pour tracer l'ensemble des événements critiques (appels API, imports, tâches asynchrones) [#7421](https://github.com/betagouv/ma-cantine/issues/7421), [#7311](https://github.com/betagouv/ma-cantine/issues/7311).
    - Migration des données historiques vers ce nouveau système de logs [#7387](https://github.com/betagouv/ma-cantine/issues/7387), [#7334](https://github.com/betagouv/ma-cantine/issues/7334).
    - Intégration des nouveaux logs dans le pipeline de données dbt pour l'analyse [#7383](https://github.com/betagouv/ma-cantine/issues/7383).
- **Architecture & Refactoring** : 
    - Refonte majeure du module de Diagnostics via l'utilisation de mixins pour segmenter la logique par volet [#7442](https://github.com/betagouv/ma-cantine/issues/7442), [#7443](https://github.com/betagouv/ma-cantine/issues/7443).
    - Restructuration du module d'Imports dans une application dédiée avec une gestion par schémas plus robuste [#7450](https://github.com/betagouv/ma-cantine/issues/7450), [#7451](https://github.com/betagouv/ma-cantine/issues/7451).
    - Optimisation des commandes de tâches asynchrones (export, nettoyage, dbt) [#7419](https://github.com/betagouv/ma-cantine/issues/7419), [#7417](https://github.com/betagouv/ma-cantine/issues/7417).
- **Sécurité** : 
    - Correction de plusieurs vulnérabilités de type XSS (Cross-Site Scripting) sur les formulaires publics, l'administration et l'affichage des cantines [#7398](https://github.com/betagouv/ma-cantine/issues/7398), [#7397](https://github.com/betagouv/ma-cantine/issues/7397), [#7396](https://github.com/betagouv/ma-cantine/issues/7396).
    - Correction de failles liées au processus de confirmation par email et à l'authentification [#7395](https://github.com/betagouv/ma-cantine/issues/7395), [#7393](https://github.com/betagouv/ma-cantine/issues/7393).
- **Infrastructure & CI/CD** : 
    - Optimisation des temps d'exécution des jobs de tests (ajout de timeouts) [#7429](https://github.com/betagouv/ma-cantine/issues/7429).
    - Nettoyage et regroupement (squash) des migrations de base de données pour alléger le projet [#7431](https://github.com/betagouv/ma-cantine/issues/7431), [#7402](https://github.com/betagouv/ma-cantine/issues/7402).

### Autres changements
- Ajout du fichier `SECURITY.md` pour définir la politique de signalement de vulnérabilités [#7413](https://github.com/betagouv/ma-cantine/issues/7413).
- Mise à jour de la documentation de l'API concernant les nouveaux champs de diagnostics [#7302](https://github.com/betagouv/ma-cantine/issues/7302).
