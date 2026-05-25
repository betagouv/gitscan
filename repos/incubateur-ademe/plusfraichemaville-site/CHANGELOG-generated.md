## Changelog : plusfraichemaville-site (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'outil ClimaDiag, avec des ajustements pour les collectivités d'outre-mer et une meilleure gestion des données. Des améliorations ont également été apportées à l'onglet "Financement" pour faciliter la création de projets et l'accès aux aides, ainsi qu'une redirection vers la page de connexion pour l'accès au statut personnalisé.

### Évolutions fonctionnelles
- **ClimaDiag :** Amélioration de la recherche en supprimant les caractères spéciaux qui pouvaient perturber les résultats [#497](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/497).
- **ClimaDiag :** Adaptation des métriques utilisées pour les collectivités d'outre-mer afin d'assurer une meilleure pertinence des données [#493](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/493).
- **ClimaDiag :** Correction de l'affichage concernant la disponibilité de ClimaDiag dans les territoires d'outre-mer [#494](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/494).
- **Onglet Financement :** Ajout d'un incitatif "Espace Projet" dans l'onglet financement pour faciliter la création de projets [#492](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/492).
- **Onglet Financement :** Correction d'un problème de redirection lors de la création d'un projet depuis l'onglet financement [#492](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/492).
- **Statut Personnalisé :** Redirection vers la page de connexion si l'utilisateur n'est pas authentifié lors de l'accès à la page de statut personnalisé [#491](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/491).
- **Canaux d'acquisition :** Modification des canaux d'acquisition [#498](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/498).

### Évolutions techniques
- Mise à jour des dépendances du projet [#496](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/496).
- Mise à jour de la version de pnpm [#491](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/491).
- Utilisation du seuil ClimaDiag de manière cohérente dans tout le code [#493](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/493).
- Suppression de l'attribut `lien_aides_territoires` [#492](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/492).
- Amélioration du script d'importation des données ClimaDiag.
- Correction de l'utilisation de `is_live` pour filtrer les aides territoriales [#495](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/495).

### Autres changements
- Correction de problèmes de formatage avec Prettier [#493](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/493).
- Mise à jour de la version de l'action `actions/setup-node` à la version 6.4.0 [#491](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/491).
