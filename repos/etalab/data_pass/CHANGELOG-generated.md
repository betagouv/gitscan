## Changelog : data_pass (30 derniers jours, au 10 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées à data_pass au cours des 30 derniers jours. Les évolutions concernent principalement des corrections de bugs, des améliorations de l'expérience utilisateur (notamment dans les emails et les formulaires pré-remplis), des mises à jour de l'API et des ajustements de sécurité. Des efforts ont également été faits pour améliorer la qualité du code et la documentation.

### Évolutions fonctionnelles
- Amélioration des emails FranceConnect : reformulation du texte d'approbation. [#1603](https://github.com/etalab/data_pass/pull/1603)
- Ajout d'un lien de gestion des notifications dans les emails d'instruction. [#1585](https://github.com/etalab/data_pass/pull/1585)
- Possibilité pour les administrateurs de s'auto-éditer leurs propres droits d'accès. [#1573](https://github.com/etalab/data_pass/pull/1573)
- Ajout du formulaire pré-rempli MGDIS Aides facultatives départementales. [#1578](https://github.com/etalab/data_pass/pull/1578)
- Ajout du formulaire pré-rempli Andyvie (Recreo). [#1577](https://github.com/etalab/data_pass/pull/1577)
- Activation des brouillons pour les instructeurs FranceConnect. [#1597](https://github.com/etalab/data_pass/pull/1597)
- Mise à jour des CGU Prosante Connect. [#1596](https://github.com/etalab/data_pass/pull/1596)
- Mise à jour des CGU TDAE. [#1585](https://github.com/etalab/data_pass/pull/1585)
- Limitation de la taille des fichiers uploadés. [#1554](https://github.com/etalab/data_pass/pull/1554)
- Amélioration de la recherche d'instructeurs : acceptation du formatted_id (D/H). [#1575](https://github.com/etalab/data_pass/pull/1575)
- Possibilité de trier les résultats des endpoints de l'API par date de création. [#1593](https://github.com/etalab/data_pass/pull/1593)

### Évolutions techniques
- Correction de races conditionnelles dans les tests Cucumber, améliorant leur fiabilité. [#1608](https://github.com/etalab/data_pass/pull/1608)
- Correction des liens vers la documentation dans l'interface Swagger. [#1623](https://github.com/etalab/data_pass/pull/1623)
- Mise à jour de Ruby à la dernière version. [#1285](https://github.com/etalab/data_pass/pull/1285)
- Refactorisation du code pour utiliser `params.expect` pour les strong parameters, améliorant la sécurité et la lisibilité.
- Suppression d'une redirection inutile lors d'une recherche par ID. [#1602](https://github.com/etalab/data_pass/pull/1602)
- Suppression du champ `recurrence` du bloc `cnous_data_extraction_criteria`. [#1621](https://github.com/etalab/data_pass/pull/1621)
- Ajout de mapping des codes INSEE pour la catégorie légale des organisations. [#1582](https://github.com/etalab/data_pass/pull/1582)
- Correction de bugs et améliorations dans les tests Cucumber. [#1612](https://github.com/etalab/data_pass/pull/1612), [#1591](https://github.com/etalab/data_pass/pull/1591)

### Autres changements
- Mise à jour de la documentation pour clarifier le format des scopes en réponse API.
- Mise à jour des liens CGU des services CISIRH. [#1620](https://github.com/etalab/data_pass/pull/1620)
- Mise à jour de la documentation et suppression de TODOs. [#1594](https://github.com/etalab/data_pass/pull/1594)
- Corrections de linting et amélioration de la qualité du code. [#1611](https://github.com/etalab/data_pass/pull/1611), [#1613](https://github.com/etalab/data_pass/pull/1613)
- Mises à jour de dépendances (Faraday, JWT, Rubocop, etc.).
