## Changelog : ma-cantine (30 derniers jours, au 2 juin 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations de la traçabilité de la création des données (cantines, achats, diagnostics) grâce à l'ajout de champs "creation_user". Des optimisations ont également été apportées aux diagnostics, notamment au niveau du calcul des indicateurs et du remplissage des champs, ainsi qu'à la gestion des données géographiques. Enfin, des corrections et améliorations ont été apportées au formulaire d'achats et à l'export des données.

### Évolutions fonctionnelles
- Ajout d'un champ "creation_user" pour suivre l'utilisateur ayant créé une cantine.
- Ajout d'un champ "creation_user" pour suivre l'utilisateur ayant créé un achat.
- Ajout d'un champ "creation_user" pour suivre l'utilisateur ayant créé un diagnostic.
- Amélioration du formulaire d'achats avec une division des caractéristiques en 4 sections pour une meilleure organisation et expérience utilisateur [#6740](https://github.com/betagouv/ma-cantine/issues/6740).
- Ajout de la définition "PAT" comme produit local dans le formulaire d'achats [#6741](https://github.com/betagouv/ma-cantine/issues/6741).
- Remplacement de la vidéo explicative sur le formulaire d'achats par un lien vers la documentation [#6742](https://github.com/betagouv/ma-cantine/issues/6742).
- Ajout des livrables GT sanitaire et médico-social dans la section Ressources [#6733](https://github.com/betagouv/ma-cantine/issues/6733).
- Mise à jour du fichier de référence PAT (Produits d'Agriculture et de Transformation) [#6693](https://github.com/betagouv/ma-cantine/issues/6693).

### Évolutions techniques
- Refactor de l'API cantines pour ne plus appeler l'API Adresse lors de la création d'une cantine, corrigeant un problème de formulaire [#6766](https://github.com/betagouv/ma-cantine/issues/6766).
- Amélioration des tests API suite aux changements récents [#6757](https://github.com/betagouv/ma-cantine/issues/6757).
- Ajout d'un nouveau champ `cout_repas` dans les diagnostics pour stocker l'information au lieu de la recalculer à chaque fois [#6753](https://github.com/betagouv/ma-cantine/issues/6753).
- Amélioration du calcul des champs agrégés et des pourcentages dans les diagnostics, calculés à chaque sauvegarde [#6752](https://github.com/betagouv/ma-cantine/issues/6752).
- Ajout de nouveaux querysets pour faciliter le filtrage des raisons d'alerte dans les diagnostics [#6758](https://github.com/betagouv/ma-cantine/issues/6758), [#6736](https://github.com/betagouv/ma-cantine/issues/6736), [#6735](https://github.com/betagouv/ma-cantine/issues/6735).
- Ajout d'un nouveau champ `warning_reason_list` pour stocker des informations non bloquantes dans les diagnostics [#6732](https://github.com/betagouv/ma-cantine/issues/6732).
- Amélioration des scripts de remplissage des champs calculés dans les diagnostics [#6754](https://github.com/betagouv/ma-cantine/issues/6754), [#6747](https://github.com/betagouv/ma-cantine/issues/6747), [#6748](https://github.com/betagouv/ma-cantine/issues/6748).
- Suppression des tâches asynchrones liées à la récupération des données géographiques, et suppression du code associé.
- Optimisation des statistiques d'agrégation dans les achats avec l'ajout de querysets dédiés [#6706](https://github.com/betagouv/ma-cantine/issues/6706).
- Refactor de l'API de recherche d'entreprises pour ne pas utiliser de camelCase dans les résultats [#6710](https://github.com/betagouv/ma-cantine/issues/6710).
- Correction de la sécurité en sanitizant le paramètre 'next' [#6709](https://github.com/betagouv/ma-cantine/issues/6709).

### Autres changements
- Ajout d'une page de documentation expliquant les commandes liées à une campagne de télédéclaration [#6738](https://github.com/betagouv/ma-cantine/issues/6738).
- Correction du nom de la dernière migration pour éviter un conflit [#6741](https://github.com/betagouv/ma-cantine/issues/6741).
- Correction de l'URL vers les CGU dans le frontend [#6701](https://github.com/betagouv/ma-cantine/issues/6701).
- Mise à jour des dépendances Wagtail et Django.
- Réparation des tests suite aux ajouts de règles métiers récents et à la fin de la campagne de télédéclaration [#6677](https://github.com/betagouv/ma-cantine/issues/6677).
- Suppression d'un script inutilisé (field_gen.py).
- Amélioration de l'export des données vers Open Data et Metabase.
- Correction de l'export Open Data.
- Ajout de la possibilité d'exporter les mesures de gaspillage dans les exports bruts (dbt).
