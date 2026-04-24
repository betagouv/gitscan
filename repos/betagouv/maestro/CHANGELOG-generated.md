## Changelog : maestro (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les évolutions de Maestro se concentrent sur l'amélioration de la gestion des prélèvements, des analyses et des plans de surveillance. Plusieurs corrections de bugs ont été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment concernant l'affichage des informations, la gestion des droits et l'export des données. Des améliorations significatives ont également été apportées à l'envoi des données via Sacha, avec l'ajout de la gestion des erreurs et de l'envoi par SFTP.

### Évolutions fonctionnelles
- Ajout d'une table pour l'envoi des DAI ([#789](https://github.com/betagouv/maestro/issues/789)).
- Possibilité d'éditer les descripteurs des prélèvements ([#652](https://github.com/betagouv/maestro/issues/652)).
- Affichage des consignes de répartition et des notes lors de l'export des programmations ([#796](https://github.com/betagouv/maestro/issues/796)).
- Affichage des analyses sur les étiquettes, procès verbaux et documents vierges ([#791](https://github.com/betagouv/maestro/issues/791)).
- Possibilité de supprimer le département d'un utilisateur ([#790](https://github.com/betagouv/maestro/issues/790)).
- Affichage d'un message si aucun échantillon n'est saisissable en raison d'une programmation incomplète ([#784](https://github.com/betagouv/maestro/issues/784)).
- Affichage de la note additionnelle sur les échantillons dans le suivi du prélèvement ([#780](https://github.com/betagouv/maestro/issues/780)).
- Correction du lien de retour à la liste des prélèvements ([#779](https://github.com/betagouv/maestro/issues/779)).
- Déblocage des DAI pour les LNR ([#714](https://github.com/betagouv/maestro/issues/714)).
- Ajout d'un tableau de bord pour la consultation des plans fermés ([#696](https://github.com/betagouv/maestro/issues/696)).
- Possibilité de filtrer les plans par administrateur ([#697](https://github.com/betagouv/maestro/issues/697)).
- Gestion des compétences analytiques des laboratoires (en cours de développement) ([#491](https://github.com/betagouv/maestro/issues/491)).
- Correction de l'affichage des décalages horaires ([#710](https://github.com/betagouv/maestro/issues/710)).
- Correction de l'affichage des notifications pour les documents ajoutés ([#709](https://github.com/betagouv/maestro/issues/709)).
- Correction de l'affichage du filtre par entreprise ([#7551fd](https://github.com/betagouv/maestro/commit/f7551fd)).
- Correction de la récupération de l'utilisateur dans le local storage ([#819b19b](https://github.com/betagouv/maestro/commit/819b19b)).

### Évolutions techniques
- Ajout de Sentry pour la gestion des erreurs côté frontend ([#768](https://github.com/betagouv/maestro/issues/768)).
- Refactorisation du frontend pour typer les requêtes via les définitions des routes dans `shared` ([#693](https://github.com/betagouv/maestro/issues/693)).
- Préparation à la migration vers PostgreSQL 17 ([#708](https://github.com/betagouv/maestro/issues/708)).
- Remplacement de ESLint et Prettier par BiomeJS pour le linting et le formattage du code ([#672](https://github.com/betagouv/maestro/issues/672)).
- Mise à jour de nombreuses dépendances (voir les commits pour la liste complète).

### Autres changements
- Correction de la référence dans les DAI ([#783](https://github.com/betagouv/maestro/issues/783)).
- Correction de l'attribution des laboratoires au niveau régional pour la PPV ([#782](https://github.com/betagouv/maestro/issues/782)).
- Ajout d'un schéma pour les échanges hors EDI Sacha ([#711](https://github.com/betagouv/maestro/issues/711)).
- Correction de l'affichage du champ saisie pour DAOA.
- Correction du préleveur dans les DAI ([#744](https://github.com/betagouv/maestro/issues/744)).
- Correction de l'export des prélèvements ([#763](https://github.com/betagouv/maestro/issues/763)).
- Ajout d'une année et de plans aux ressources ([#671](https://github.com/betagouv/maestro/issues/671)).
- Correction de l'historique de la programmation ([#668](https://github.com/betagouv/maestro/issues/668)).
- Correction du message d'erreur pour la programmation non disponible ([#669](https://github.com/betagouv/maestro/issues/669)).
- Masquage de l'impression des étiquettes en l'absence de type de plan ([#797](https://github.com/betagouv/maestro/issues/797)).
- Correction de la regression sur l'initialisation du laboratoire ([#795](https://github.com/betagouv/maestro/issues/795)).
