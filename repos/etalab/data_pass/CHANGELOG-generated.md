## Changelog : data_pass (30 derniers jours, au 2026-05-21)

### Résumé
Ce mois-ci, les évolutions de DataPass se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des droits et des demandes, ainsi que sur des corrections de bugs et des optimisations techniques. Des améliorations de la documentation et de l'accessibilité ont également été apportées.

### Évolutions fonctionnelles
- Les administrateurs peuvent désormais s'auto-éditer leurs propres droits d'accès. [#1573](https://github.com/etalab/data_pass/pull/1573)
- Amélioration de la recherche d'instructeurs dans le tableau de bord d'instruction, acceptant désormais l'ID formaté (D/H). [#1575](https://github.com/etalab/data_pass/pull/1575)
- Possibilité de pré-remplir une demande via des paramètres d'URL. [#1566](https://github.com/etalab/data_pass/pull/1566)
- Mise à jour de l'interface pour permettre la gestion de l'état actuel des demandes. [#1521](https://github.com/etalab/data_pass/pull/1521)
- Ajout d'un bouton "Précédent" manquant dans l'étape de traitement des données personnelles. [#1539](https://github.com/etalab/data_pass/pull/1539)
- Affichage du statut d'une demande comme "revendiqué" ou "non revendiqué". [#1537](https://github.com/etalab/data_pass/pull/1537)
- Suppression du compteur de longlet "Demandes" pour les instructeurs. [#1538](https://github.com/etalab/data_pass/pull/1538)
- Mise à jour du texte de l'accusé de réception de dépôt de demande. [#1536](https://github.com/etalab/data_pass/pull/1536)
- Ajout d'informations sur les services CISIRH et mise à jour des scopes associés. [#1543](https://github.com/etalab/data_pass/pull/1543), [#1545](https://github.com/etalab/data_pass/pull/1545), [#1547](https://github.com/etalab/data_pass/pull/1547)
- Ajout d'un encart de connexion rapide hors production. [#1565](https://github.com/etalab/data_pass/pull/1565)
- Limitation du nombre de fichiers uploadés à 6 par champ document. [#1554](https://github.com/etalab/data_pass/pull/1554)

### Évolutions techniques
- Refactorisation de l'alerte. [#1567](https://github.com/etalab/data_pass/pull/1567)
- Mise à jour de plusieurs dépendances (Faraday, JWT, Rubocop, View Component, etc.).
- Amélioration de la gestion des tests (correction de tests aléatoires, ajout de tests parallèles). [#1562](https://github.com/etalab/data_pass/pull/1562)
- Mise à jour de Rails Pulse et migration des tables associées. [#1534](https://github.com/etalab/data_pass/pull/1534)
- Amélioration de l'accessibilité en forçant la définition du titre de chaque vue. [#1525](https://github.com/etalab/data_pass/pull/1525)
- Correction d'un problème bloquant l'authentification en cas d'ID SIRET invalide. [#1528](https://github.com/etalab/data_pass/pull/1528)
- Utilisation de `formatted_id` au lieu de `id` dans les emails. [#1535](https://github.com/etalab/data_pass/pull/1535)

### Autres changements
- Réorganisation du dossier de documentation en sous-dossiers (technique, métier, API particulier). [#1549](https://github.com/etalab/data_pass/pull/1549)
- Ajout de la documentation du système HabilitationType dynamique. [#1548](https://github.com/etalab/data_pass/pull/1548)
- Clarification du format des scopes en réponse API dans la documentation du tutoriel. [#1569](https://github.com/etalab/data_pass/pull/1569)
- Amélioration de l'affichage des erreurs. [#1515](https://github.com/etalab/data_pass/pull/1515)
- Correction de fautes de français dans la documentation. [#1533](https://github.com/etalab/data_pass/pull/1533)
