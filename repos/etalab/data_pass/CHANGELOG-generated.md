## Changelog : data_pass (30 derniers jours, au 12 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment dans la gestion des données géographiques, l'intégration avec FranceConnect et la simplification de l'interface administrative. Des corrections de bugs et des mises à jour de sécurité ont également été apportées pour garantir la stabilité et la fiabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité de trier les résultats des endpoints de l'API par date de création (descendant par défaut) [#1583](https://github.com/etalab/data_pass/pull/1583).
- Amélioration de la recherche par ID : les demandes validées sont désormais incluses dans les résultats [#1584](https://github.com/etalab/data_pass/pull/1584).
- Intégration du formulaire pré-rempli Andyvie (Recreo) dans l'API particulier [#1577](https://github.com/etalab/data_pass/pull/1577).
- Ajout d'un lien de gestion des notifications dans les emails d'instruction [#1575](https://github.com/etalab/data_pass/pull/1575).
- Mise à jour des CGU pour Prosante Connect [#1596](https://github.com/etalab/data_pass/pull/1596).
- Mise à jour des CGU pour TDAE [#1585](https://github.com/etalab/data_pass/pull/1585).
- Amélioration des emails FranceConnect : ajout d'un lien pour ne plus recevoir ces emails [#1603](https://github.com/etalab/data_pass/pull/1603).
- Ajout du formulaire pré-rempli MGDIS Aides facultatives départementales [#1501](https://github.com/etalab/data_pass/pull/1501).
- Les administrateurs peuvent désormais s'auto-éditer leurs propres droits [#1573](https://github.com/etalab/data_pass/pull/1573).
- Activation des brouillons d'instructeurs pour FranceConnect [#1597](https://github.com/etalab/data_pass/pull/1597).

### Évolutions techniques
- Refactor de la gestion des données CNous : amélioration de la performance et de la lisibilité du code [#1582](https://github.com/etalab/data_pass/pull/1582).
- Implémentation d'une nouvelle méthode pour récupérer les données de périmètre géographique de CNous, affichées côté client [#1581](https://github.com/etalab/data_pass/pull/1581).
- Correction de problèmes de concurrence dans les tests Cucumber [#1608](https://github.com/etalab/data_pass/pull/1608).
- Mise à jour de la documentation concernant l'authentification ProConnect [#1622](https://github.com/etalab/data_pass/pull/1622).
- Amélioration de la gestion des liens dans la documentation Swagger [#1623](https://github.com/etalab/data_pass/pull/1623).
- Mise à jour des dépendances : Ruby, puma, jwt, faraday, rubocop, actions/checkout.

### Autres changements
- Mise à jour du lien CGU pour les services CISIRH [#1621](https://github.com/etalab/data_pass/pull/1621).
- Correction de l'introduction des TD CESU [#1617](https://github.com/etalab/data_pass/pull/1617) et [#1616](https://github.com/etalab/data_pass/pull/1616).
- Suppression de la redirection vers la demande lors d'une recherche par ID [#1602](https://github.com/etalab/data_pass/pull/1602).
- Amélioration de la documentation du tutoriel de lecture de l'API [#1569](https://github.com/etalab/data_pass/pull/1569).
- Suppression d'un scope obsolète (DHTOUR) pour l'hébergement touristique [#1574](https://github.com/etalab/data_pass/pull/1574).
- Ajout d'une limite de taille pour l'upload de documents [#1554](https://github.com/etalab/data_pass/pull/1554).
- Correction de bugs et améliorations diverses de l'interface utilisateur.
