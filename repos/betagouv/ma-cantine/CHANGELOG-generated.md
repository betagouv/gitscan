## Changelog : ma-cantine (30 derniers jours)

### Résumé
Les dernières mises à jour de ma-cantine apportent des améliorations significatives à l'import de données, à l'observatoire, aux ressources disponibles pour les utilisateurs et à la gestion des cantines. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de supports pour les webinaires "grandes collectivités" et "acteurs de terrain" dans la section Ressources. ([#6470](https://github.com/betagouv/ma-cantine/issues/6470), [#6355](https://github.com/betagouv/ma-cantine/issues/6355))
- Amélioration des filtres de recherche dans l'observatoire. ([#6465](https://github.com/betagouv/ma-cantine/issues/6465))
- Ajout d'un message d'alerte dans l'observatoire pour signaler les incohérences de données. ([#6446](https://github.com/betagouv/ma-cantine/issues/6446))
- Ajout d'un tableur XLSX pour le suivi des achats dans la section Ressources. ([#6426](https://github.com/betagouv/ma-cantine/issues/6426))
- Ajout de la possibilité d'exporter la liste des cantines au format XLSX. ([#6369](https://github.com/betagouv/ma-cantine/issues/6369))
- Ajout d'une modale d'export dans le tableau de bord. ([#6368](https://github.com/betagouv/ma-cantine/issues/6368))
- Ajout de la possibilité d'exporter les cantines enregistrées via SIREN. ([#6409](https://github.com/betagouv/ma-cantine/issues/6409))
- Ajout d'un nouvel import de bilans via l'ID de la cantine. ([#6393](https://github.com/betagouv/ma-cantine/issues/6393))
- Ajout d'une nouvelle page dédiée aux imports de bilans détaillés. ([#6397](https://github.com/betagouv/ma-cantine/issues/6397))
- Suppression de l'import admin pour les cantines. ([#6387](https://github.com/betagouv/ma-cantine/issues/6387))
- Ajout d'un fichier dédié à la création de cantines pour les gestionnaires. ([#6383](https://github.com/betagouv/ma-cantine/issues/6383))
- Remplacement du badge dans le header par un bandeau d'information indiquant l'environnement. ([#6358](https://github.com/betagouv/ma-cantine/issues/6358))

### Évolutions techniques
- Mise à jour de Django de 5.1.15 à 5.2.11 (et des dépendances associées). ([#6390](https://github.com/betagouv/ma-cantine/issues/6390))
- Refactor de l'API des exports achats pour améliorer la performance. ([#6373](https://github.com/betagouv/ma-cantine/issues/6373))
- Amélioration des performances de la réponse de l'API "liste" des achats. ([#6364](https://github.com/betagouv/ma-cantine/issues/6364))
- Refactor du code pour la gestion des données géographiques des cantines. ([#6374](https://github.com/betagouv/ma-cantine/issues/6374))
- Utilisation de services dédiés pour Postgres et Redis dans les tests. ([#6380](https://github.com/betagouv/ma-cantine/issues/6380))
- Suppression des emails de rappels "pas de diagnostics" et bascule sur Brevo. ([#6282](https://github.com/betagouv/ma-cantine/issues/6282))
- Stockage des données de bilan dans le champ 'data' pour Brevo. ([#6367](https://github.com/betagouv/ma-cantine/issues/6367))
- Mise à jour des informations des cantines plus tôt dans la nuit pour Brevo. ([#6366](https://github.com/betagouv/ma-cantine/issues/6366))
- Simplification de l'export Open Data. ([#6354](https://github.com/betagouv/ma-cantine/issues/6354))
- Suppression de fonctions inutilisées dans Metabase. ([#6353](https://github.com/betagouv/ma-cantine/issues/6353))

### Corrections
- Correction d'un bug d'arrondi des décimales dans le gaspillage alimentaire. ([#6449](https://github.com/betagouv/ma-cantine/issues/6449))
- Correction d'une erreur bloquante dans le tableau de bord si une cantine n'a pas de mode de production. ([#6410](https://github.com/betagouv/ma-cantine/issues/6410))
- Correction de l'affichage de la modale de succès lors d'un import échoué. ([#6448](https://github.com/betagouv/ma-cantine/issues/6448))
- Correction d'un bug empêchant la revendication d'une cantine si des champs étaient vérifiés. ([#6388](https://github.com/betagouv/ma-cantine/issues/6388))
- Correction d'une erreur sur les prix lors de l'import des achats. ([#6389](https://github.com/betagouv/ma-cantine/issues/6389))
- Correction de deux tests flaky. ([#6457](https://github.com/betagouv/ma-cantine/issues/6457))
- Correction du lien vers le fichier d'exemple des bilans détaillés. ([#6404](https://github.com/betagouv/ma-cantine/issues/6404))
- Correction du calcul des totaux EGalim. ([#6362](https://github.com/betagouv/ma-cantine/issues/6362))
- Correction du filtrage des événements pour n'afficher que ceux en cours et à venir. ([#6361](https://github.com/betagouv/ma-cantine/issues/6361))
