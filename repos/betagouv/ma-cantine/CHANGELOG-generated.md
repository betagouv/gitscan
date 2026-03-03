## Changelog : ma-cantine (30 derniers jours)

### Résumé
Les dernières mises à jour de ma-cantine apportent des améliorations significatives à l'import de données, notamment pour les cantines et les bilans, ainsi qu'à l'export des données. Des corrections de bugs ont été implémentées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant les télédéclarations et le tableau de bord. Des optimisations techniques ont également été réalisées, incluant la mise à jour de Django et des améliorations des performances de l'API.

### Évolutions fonctionnelles
- Ajout d'un tableur xlsx pour le suivi des achats ([#6426](https://github.com/betagouv/ma-cantine/issues/6426)).
- Ajout d'un message d'alerte dans l'observatoire pour signaler des incohérences de chiffres ([#6446](https://github.com/betagouv/ma-cantine/issues/6446)).
- Possibilité d'importer des bilans via l'ID de la cantine ([#6393](https://github.com/betagouv/ma-cantine/issues/6393)).
- Nouvelle page dédiée à l'import de bilans détaillés avec un schéma compatible Validata ([#6394](https://github.com/betagouv/ma-cantine/issues/6394), [#6397](https://github.com/betagouv/ma-cantine/issues/6397)).
- Ajout de supports webinaires sur la gestion concédée et les résultats des sondages ([#6350](https://github.com/betagouv/ma-cantine/issues/6350), [#6355](https://github.com/betagouv/ma-cantine/issues/6355)).
- Ajout d'une modale d'export sur le tableau de bord ([#6368](https://github.com/betagouv/ma-cantine/issues/6368)).
- Possibilité d'exporter uniquement les cantines enregistrées via SIREN ([#6409](https://github.com/betagouv/ma-cantine/issues/6409)).
- Ajout de fichiers dédiés pour la création et la modification des cantines lors de l'import ([#6395](https://github.com/betagouv/ma-cantine/issues/6395), [#6407](https://github.com/betagouv/ma-cantine/issues/6407), [#6408](https://github.com/betagouv/ma-cantine/issues/6408)).
- Suppression du bandeau rappel conso dans l'en-tête ([#6384](https://github.com/betagouv/ma-cantine/issues/6384)).
- Mise à jour des textes de la page tampon pour l'import ([#6411](https://github.com/betagouv/ma-cantine/issues/6411)).

### Évolutions techniques
- Mise à jour de Django de 5.1.15 à 5.2.11, incluant DRF et Wagtail ([#6390](https://github.com/betagouv/ma-cantine/issues/6390)).
- Amélioration des performances de l'API 'liste' des achats ([#6364](https://github.com/betagouv/ma-cantine/issues/6364)).
- Refactor de l'export des achats pour utiliser un endpoint dédié ([#6373](https://github.com/betagouv/ma-cantine/issues/6373)).
- Amélioration de la gestion des données géographiques lors de la création des cantines.
- Utilisation de services dédiés pour Postgres et Redis dans les tests.
- Ajout de nouveaux champs (siret_inconnu, siret_ferme) pour gérer l'état du SIRET des cantines.
- Stockage du nombre de bilans à télédéclarer chaque nuit.
- Ajout d'un champ `invalid_reason_list` pour les télédéclarations.
- Suppression des snapshots lors de l'annulation d'une télédéclaration.
- Amélioration de la gestion des événements pour n'afficher que ceux en cours et à venir.
- Refactor du code pour l'export des données Open Data.
- Suppression des emails de rappels 'pas de diagnostics' et bascule sur Brevo.
- Stockage des données des bilans dans le champ 'data' pour Brevo.
- Mise à jour des informations cantines plus tôt dans la nuit.

### Autres changements
- Ajout d'instructions pour Claude et Github Copilot dans la documentation ([#6419](https://github.com/betagouv/ma-cantine/issues/6419)).
- Ajout d'informations dans le tableau des versions de la télédéclaration ([#6401](https://github.com/betagouv/ma-cantine/issues/6401)).
- Ajout de tests et de fichiers pour les schémas d'import.
- Corrections de bugs mineurs et améliorations de la documentation.
- Suppression de l'import admin pour les cantines ([#6387](https://github.com/betagouv/ma-cantine/issues/6387)).
- Correction d'une erreur bloquante sur le tableau de bord si une cantine n'a pas de mode de production ([#6410](https://github.com/betagouv/ma-cantine/issues/6410)).
- Correction d'une erreur sur les prix lors de l'import des achats ([#6389](https://github.com/betagouv/ma-cantine/issues/6389)).
- Correction de la vérification des champs de cantine lors de sa revendication ([#6388](https://github.com/betagouv/ma-cantine/issues/6388)).
- Correction du lien vers le fichier d'exemple des bilans détaillés ([#6404](https://github.com/betagouv/ma-cantine/issues/6404)).
- Ajout d'erreurs Sentry à ignorer pour les nouveaux imports cantines ([#6412](https://github.com/betagouv/ma-cantine/issues/6412)).
- Amélioration du verbose_name de certains champs dans le diagnostic ([#6402](https://github.com/betagouv/ma-cantine/issues/6402)).
- Correction d'un bug dans le calcul des totaux EGalim ([#6362](https://github.com/betagouv/ma-cantine/issues/6362)).
- Correction d'un test suite aux modifications géographiques récentes ([#6385](https://github.com/betagouv/ma-cantine/issues/6385)).
- Amélioration de l'export des colonnes pat_list & pat_lib_list ([#6322](https://github.com/betagouv/ma-cantine/issues/6322)).
- Amélioration de l'utilisation des données du satellite pour les télédéclarations ([#6324](https://github.com/betagouv/ma-cantine/issues/6324), [#6325](https://github.com/betagouv/ma-cantine/issues/6325)).
- Correction d'un bug dans le calcul des TD, excluant les TD groupes ([#6399](https://github.com/betagouv/ma-cantine/issues/6399)).
