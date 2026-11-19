## Changelog : ma-cantine (30 derniers jours, au 18 novembre 2026)

### Résumé
Ce mois a été marqué par une préparation intensive de la campagne 2026. Les évolutions majeures concernent l'enrichissement de la télédéclaration avec de nouveaux volets thématiques (gaspillage, plastique, diversification), une refonte profonde du système d'import de données pour plus de robustesse, et une gestion plus fine des groupes de cantines. L'expérience utilisateur a été fluidifiée par une meilleure communication sur l'état d'avancement des diagnostics.

### Évolutions fonctionnelles

**Télédéclaration & Diagnostics**
- Ajout de nouveaux volets thématiques pour la campagne 2026 : substitution plastique ([#7537](https://github.com/betagouv/ma-cantine/issues/7537)), gaspillage ([#7527](https://github.com/betagouv/ma-cantine/issues/7527)), diversification ([#7564](https://github.com/betagouv/ma-cantine/issues/7564)) et information des convives ([#7531](https://github.com/betagouv/ma-cantine/issues/7531)).
- Amélioration de l'interface de télédéclaration : navigation dynamique, icônes d'état mises à jour et messages d'erreur plus explicites ([#7545](https://github.com/betagouv/ma-cantine/issues/7545), [#7620](https://github.com/betagouv/ma-cantine/issues/7620)).
- Mise en place de la gestion des "Couverts Groupe" pour permettre la saisie et l'affichage du nombre de repas annuels au niveau du groupe ([#7638](https://github.com/betagouv/ma-cantine/issues/7638), [#7642](https://github.com/betagouv/ma-cantine/issues/7642)).
- Introduction du statut "Petite structure" pour adapter les obligations de saisie ([#7584](https://github.com/betagouv/ma-cantine/issues/7584), [#7587](https://github.com/betagouv/ma-cantine/issues/7587)).
- Optimisation du module de justificatifs : nouvelle version 2026 et meilleure organisation par année ([#7634](https://github.com/betagouv/ma-cantine/issues/7634), [#7633](https://github.com/betagouv/ma-cantine/issues/7633)).

**Gestion des Groupes**
- Possibilité pour une cantine de se détacher d'un groupe ([#7689](https://github.com/betagouv/ma-cantine/issues/7689), [#7687](https://github.com/betagouv/ma-cantine/issues/7687)).
- Synchronisation automatique du nombre de repas des satellites lors de l'ajout ou de la suppression d'une cantine dans un groupe ([#7651](https://github.com/betagouv/ma-cantine/issues/7651), [#7622](https://github.com/betagouv/ma-cantine/issues/7622)).

**Imports & Données**
- Nouveau système d'import pour 2026 supportant l'import par SIRET ou par ID ([#7493](https://github.com/betagouv/ma-cantine/issues/7493), [#7467](https://github.com/betagouv/ma-cantine/issues/7467)).
- Amélioration de la tolérance aux erreurs de formatage Excel (gestion des SIRET, séparateurs décimaux point/virgule) ([#7615](https://github.com/betagouv/ma-cantine/issues/7615), [#7613](https://github.com/betagouv/ma-cantine/issues/7613)).

**Sécurité**
- Correction de failles de type XSS (injection de code) dans les formulaires et l'administration ([#7398](https://github.com/betagouv/ma-cantine/issues/7398), [#7397](https://github.com/betagouv/ma-cantine/issues/7397)).
- Renforcement de la confidentialité lors de l'envoi des emails de confirmation ([#7395](https://github.com/betagouv/ma-cantine/issues/7395), [#7393](https://github.com/betagouv/ma-cantine/issues/7393)).

### Évolutions techniques

**Architecture & Refactoring**
- Refonte majeure du modèle `Diagnostics` : découpage par mixins pour isoler les différents volets thématiques et faciliter la maintenance ([#7442](https://github.com/betagouv/ma-cantine/issues/7442), [#7444](https://github.com/betagouv/ma-cantine/issues/7444)).
- Création d'une application dédiée `imports` pour centraliser et structurer la logique d'importation ([#7450](https://github.com/betagouv/ma-cantine/issues/7450)).
- Implémentation d'un nouveau système de journalisation des événements (`EventLog`) pour tracer les actions de la plateforme ([#7421](https://github.com/betagouv/ma-cantine/issues/7421), [#7424](https://github.com/betagouv/ma-cantine/issues/7424)).
- Refactorisation des tâches asynchrones (Celery) pour rendre les commandes plus autonomes ([#7419](https://github.com/betagouv/ma-cantine/issues/7419)).

**API**
- Déploiement de l'API v2 pour les bilans et les diagnostics, incluant le support OAuth2 pour les éditeurs ([#7577](https://github.com/betagouv/ma-cantine/issues/7577), [#7510](https://github.com/betagouv/ma-cantine/issues/7510)).
- Nouveaux endpoints pour la gestion fine des données de groupes via API ([#7626](https://github.com/betagouv/ma-cantine/issues/7626), [#7623](https://github.com/betagouv/ma-cantine/issues/7623)).

**Data & Pipeline**
- Amélioration des modèles de données dbt pour le pilotage des "Petites structures" et l'analyse des logs d'événements ([#7588](https://github.com/betagouv/ma-cantine/issues/7588), [#7383](https://github.com/betagouv/ma-cantine/issues/7383)).

### Autres changements
- Ajout du fichier `SECURITY.md` pour définir la politique de signalement de vulnérabilités ([#7413](https://github.com/betagouv/ma-cantine/issues/7413)).
- Optimisation des temps d'exécution (timeouts) des jobs CI/CD ([#7429](https://github.com/betagouv/ma-cantine/issues/7429)).
