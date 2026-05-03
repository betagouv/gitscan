## Changelog : api-engagement (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la performance de l'API, notamment en optimisant les recherches et en améliorant la gestion des données. L'interface utilisateur du back office a également été améliorée en termes d'accessibilité et de convivialité, avec des corrections de mise en page et des améliorations de la gestion des utilisateurs. Des corrections de bugs ont été apportées pour assurer la stabilité et la fiabilité de l'application.

### Évolutions fonctionnelles
- Correction de l'affichage des filtres de modération et résolution d'un problème de débordement des onglets dans l'application back office. [#975](https://github.com/betagouv/api-engagement/issues/975)
- Amélioration de la mise en page du sélecteur de plage de dates pour une meilleure expérience utilisateur. [#976](https://github.com/betagouv/api-engagement/issues/976)
- Ajout de scripts pour les missions SDIS (Service Départemental d'Incendie et de Secours). [#942](https://github.com/betagouv/api-engagement/issues/942)
- Amélioration de la gestion des utilisateurs et de la liste des utilisateurs dans l'application back office, notamment en termes d'accessibilité. [#922](https://github.com/betagouv/api-engagement/issues/922)
- Correction du blocage de la sélection du jour courant dans le sélecteur de plage de dates. [#924](https://github.com/betagouv/api-engagement/issues/924)
- Correction d'un bug empêchant la déconnexion en cas d'erreur réseau. [#930](https://github.com/betagouv/api-engagement/issues/930)
- Amélioration de l'accessibilité du sélecteur de plage de dates. [#928](https://github.com/betagouv/api-engagement/issues/928)
- Correction d'un problème d'affichage de la page des organisations désactivées. [#930](https://github.com/betagouv/api-engagement/issues/930)
- Correction d'un problème de redirection après la création d'une mission. [#926](https://github.com/betagouv/api-engagement/issues/926)
- Amélioration du formulaire d'édition du widget. [#925](https://github.com/betagouv/api-engagement/issues/925)

### Évolutions techniques
- Refactorisation de l'API pour exécuter l'agrégation des widgets séquentiellement, améliorant ainsi la performance. [#966](https://github.com/betagouv/api-engagement/issues/966)
- Refactorisation de l'API pour gérer les missions en excluant les organisations publiantes. [#965](https://github.com/betagouv/api-engagement/issues/965)
- Suppression du magasin partagé de limitation de débit (rate limit). [#959](https://github.com/betagouv/api-engagement/issues/959)
- Utilisation de `tsvector` pour la recherche d'organisations, améliorant la performance des recherches textuelles. [#950](https://github.com/betagouv/api-engagement/issues/950)
- Ajout de tâches de sauvegarde de la base de données RDB. [#955](https://github.com/betagouv/api-engagement/issues/955)
- Ajout de limiteurs de débit pour les requêtes de l'API (par éditeur et par adresse IP). [#932](https://github.com/betagouv/api-engagement/issues/932)
- Suppression d'une colonne inutile dans la base de données. [#935](https://github.com/betagouv/api-engagement/issues/935)
- Suppression de la clé étrangère `mission` dans la table `stat_events`. [#933](https://github.com/betagouv/api-engagement/issues/933)
- Suppression des champs dénormalisés de mission de la table `stat_event`. [#921](https://github.com/betagouv/api-engagement/issues/921)
- Amélioration des règles CLAUDE pour la modération. [#957](https://github.com/betagouv/api-engagement/issues/957)
- Mise à l'échelle de l'API (scaling) pour une meilleure performance. [#949](https://github.com/betagouv/api-engagement/issues/949)
- Ajout d'une politique de sécurité. [#920](https://github.com/betagouv/api-engagement/issues/920)

### Autres changements
- Publication des versions v1.4.0 et v1.4.1.
- Mise à jour des dépendances (anthropics/claude-code-action, dorny/paths-filter, actions/setup-node, vite).
- Amélioration du script de vérification des champs orphelins de mission dans `stat_event`.
