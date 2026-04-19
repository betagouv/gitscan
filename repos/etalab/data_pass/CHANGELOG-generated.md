## Changelog : data_pass (30 derniers jours, au 18 avril 2026)

### Résumé
Ce mois-ci, les évolutions de data_pass se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de fonctionnalités de bannissement d'utilisateurs, l'amélioration des formulaires et des emails, et l'optimisation des performances. Des corrections de bugs et des améliorations de la documentation ont également été apportées.

### Évolutions fonctionnelles
- **Bannissement d'utilisateurs :** Ajout d'une interface d'administration pour bannir des utilisateurs, bloquant leur accès à la plateforme et aux sessions actives. [#1508](https://github.com/etalab/data_pass/pull/1508)
- **Formulaires Extenso :** Amélioration du formulaire Extenso avec l'ajout de la possibilité de spécifier un cas d'utilisation, l'édition des champs de contenu et la suppression de certains scopes pré-remplis. [#1472](https://github.com/etalab/data_pass/pull/1472), [#1467](https://github.com/etalab/data_pass/pull/1467), [#1462](https://github.com/etalab/data_pass/pull/1462)
- **Emails :** Amélioration de l'envoi d'emails pour les approbations DGFIP, avec envoi à des personnes spécifiques. Les URLs dans les emails sont désormais cliquables. [#1511](https://github.com/etalab/data_pass/pull/1511), [#1505](https://github.com/etalab/data_pass/pull/1505)
- **API Particulier :** Ajout du scope `men_regime_pensionnat` pour le formulaire Solis. Les scopes `cnaf_adresse` et `cnaf_enfants` sont désormais cochables. [#1495](https://github.com/etalab/data_pass/pull/1495)
- **Documentation :** Mise à jour de la documentation concernant les rôles et les webhooks. [#1507](https://github.com/etalab/data_pass/pull/1507), [#1502](https://github.com/etalab/data_pass/pull/1502)
- **Amélioration de l'habilitation :** Correction d'un bug empêchant la consultation d'une habilitation avec une organisation non vérifiée. [#1478](https://github.com/etalab/data_pass/pull/1478)

### Évolutions techniques
- **Optimisation des tests :** Optimisation significative de la suite de tests, notamment en parallélisant les tests Cucumber et RSpec, et en réduisant le temps d'exécution global. [#1503](https://github.com/etalab/data_pass/pull/1503)
- **Refactoring :** Refactorisation de la suppression des HabilitationType pour utiliser un interactor. [#1462](https://github.com/etalab/data_pass/pull/1462)
- **Mise à jour Rails :** Mise à jour de Rails vers la version 8.1.2.1. [#1460](https://github.com/etalab/data_pass/pull/1460)
- **Webhooks :** Ajout d'un service MarkdownRenderer et documentation du format du payload de test des webhooks. [#1512](https://github.com/etalab/data_pass/pull/1512), [#1502](https://github.com/etalab/data_pass/pull/1502)
- **ID des habilitations :** Utilisation de l'ID numérique des autorisations dans les URLs pour une meilleure performance. [#1498](https://github.com/etalab/data_pass/pull/1498)

### Autres changements
- **Correction de typos :** Correction de typos dans les sujets des emails. [#1506](https://github.com/etalab/data_pass/pull/1506)
- **Amélioration de la gestion des erreurs :** Correction d'une erreur silencieuse lors de la soumission d'une demande d'autorisation depuis la page de résumé. [#1510](https://github.com/etalab/data_pass/pull/1510)
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances (zlib, rack-session, rubocop, action_text-trix, etc.).
- **Intégration CLAUDE :** Introduction de CLAUDE pour la co-authorisation des commits. [#1504](https://github.com/etalab/data_pass/pull/1504)
- **Correction d'une boucle de redirection :** Correction d'une boucle de redirection sur les dates d'homologation identiques. [#1469](https://github.com/etalab/data_pass/pull/1469)
