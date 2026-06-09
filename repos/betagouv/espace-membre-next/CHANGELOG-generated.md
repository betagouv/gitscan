## Changelog : espace-membre-next (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs, l'amélioration de l'accessibilité et l'ajout de nouvelles fonctionnalités liées à la gestion des comptes Matrix et des phases de projets. Des ajustements ont également été apportés pour une meilleure cohérence avec beta.gouv.fr et pour renforcer la sécurité.

### Évolutions fonctionnelles
- Modification du formulaire pour la saisie des jours travaillés par semaine. [#1395](https://github.com/betagouv/espace-membre-next/issues/1395)
- Ajout d'une table `matrix_accounts` et d'un script de synchronisation pour la gestion des comptes Matrix. [#1373](https://github.com/betagouv/espace-membre-next/issues/1373)
- Renommage de "perennisation" en "consolidation" dans la gestion des phases de projets. [#1392](https://github.com/betagouv/espace-membre-next/issues/1392)
- Correction des noms des événements dans la section startups. [#1385](https://github.com/betagouv/espace-membre-next/issues/1385)
- Alignement des labels des phases avec ceux utilisés sur beta.gouv.fr. [#1384](https://github.com/betagouv/espace-membre-next/issues/1384)

### Évolutions techniques
- Amélioration de la détection de Tchap pour éviter des traitements inutiles. [#1393](https://github.com/betagouv/espace-membre-next/issues/1393)
- Mise à jour des contraintes de nom des phases pour une meilleure cohérence des données. [#1356](https://github.com/betagouv/espace-membre-next/issues/1356)
- Renforcement de la sécurité en vérifiant l'authentification lors de la mise à jour des événements. [#1357](https://github.com/betagouv/espace-membre-next/issues/1357)
- Augmentation du timeout pour la synchronisation des emails (dimail-sync). [#1372](https://github.com/betagouv/espace-membre-next/issues/1372)
- Nettoyage du code lié aux anciens systèmes d'envoi d'emails. [#1375](https://github.com/betagouv/espace-membre-next/issues/1375)
- Renommage et documentation de la tâche de rappel des phases. [#1374](https://github.com/betagouv/espace-membre-next/issues/1374)
- Suppression de code environnemental obsolète. [#1383](https://github.com/betagouv/espace-membre-next/issues/1383)

### Évolutions d'accessibilité
- Ajout de l'attribut `lang` à la balise `<html>` pour améliorer l'accessibilité (RGAA 8.3). [#1361](https://github.com/betagouv/espace-membre-next/issues/1361)
- Remplacement des labels orphelins par des éléments `fr-label` pour les éditeurs personnalisés (RGAA 11.1). [#1363](https://github.com/betagouv/espace-membre-next/issues/1363)
- Rendre les éléments `onClick` statiques accessibles au clavier (RGAA 7.1 / 7.3). [#1364](https://github.com/betagouv/espace-membre-next/issues/1364)
- Finalisation de la baseline jsx-a11y (RGAA). [#1365](https://github.com/betagouv/espace-membre-next/issues/1365)
